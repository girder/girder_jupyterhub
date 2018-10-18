import json

from tornado import gen
from traitlets import Unicode, Bool
from jupyterhub.auth import Authenticator
from tornado.httpclient import AsyncHTTPClient

class GirderAuthenticator(Authenticator):

    api_url = Unicode(
        help='The url to the girder server to use for token validation',
        default_value='http://localhost:8080/api/v1',
        config=True
    )

    inject_girder_token = Bool(
        help='If set an environment variable (GIRDER_TOKEN) is injected into the spawned environment.',
        default_value=True,
        config=True
    )

    # This is needed so we can store the Girder-Token in auth state.
    enable_auth_state = True

    @gen.coroutine
    def authenticate(self, handler, data):
        if 'Girder-Token' in data:
            me_url = '%s/user/me' % self.api_url
            girder_token = data['Girder-Token']
            headers = {
                'Girder-Token': girder_token
            }
            http_client = AsyncHTTPClient()
            r = yield http_client.fetch(me_url, headers=headers)
            if r.code == 200:
                response_json = json.loads(r.body.decode('utf8'))
                if response_json is not None:
                    login = response_json['login']
                    return {
                        'name': login,
                        'auth_state': {
                            'girderToken': girder_token,
                        }
                    }

        return None

    @gen.coroutine
    def pre_spawn_start(self, user, spawner):
        auth_state = yield user.get_auth_state()
        if auth_state is not None:
            spawner.extra_create_kwargs['command'] += \
                ' --GirderContentsManager.token=%s' % auth_state['girderToken']

            if self.inject_girder_token:
                spawner.environment['GIRDER_TOKEN'] = auth_state['girderToken']
        else:
            self.log.warning('Unable to find Girder-Token in auth state.')
