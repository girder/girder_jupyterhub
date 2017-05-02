import json

from tornado import gen
from traitlets import Unicode
from jupyterhub.auth import Authenticator
from tornado.httpclient import AsyncHTTPClient

class GirderAuthenticator(Authenticator):

    girder_url = Unicode(
        help='The url to the girder server to use for token validation',
        default_value='http://localhost:8080/api/v1',
        config=True
    )

    _girder_token = {}

    @gen.coroutine
    def authenticate(self, handler, data):
        if 'Girder-Token' in data:
            me_url = '%s/user/me' % self.girder_url
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
                    self._girder_token = {
                        login: girder_token
                    }
                    return login

        return None

    def pre_spawn_start(self, user, spawner):
        if user.name in self._girder_token:
            spawner.extra_create_kwargs['command'] += \
                ' --GirderFileManager.token=%s' % self._girder_token[user.name]
            del self._girder_token[user.name]
