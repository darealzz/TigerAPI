import requests

class Client:

    def __init__(self, cookie):
        self._session = requests.Session()
        self._session.cookies[".ROBLOSECURITY"] = cookie

    def safe_request(self, method, url, **kwargs):
        request = self._session.request(method, url, **kwargs)
        method = method.lower()
        
        if method.lower() in ('post', 'put', 'patch', 'delete'):
            if "X-CSRF-TOKEN" in request.headers:
                self._session.headers["X-CSRF-TOKEN"] = request.headers["X-CSRF-TOKEN"]
                if request.status_code == 403:
                    request = self._session.request(method, url, **kwargs)

        return request

    
    def change_rank(self, group_id, user_id, new_rank):
        print(new_rank)
        r = self.safe_request('patch', f'https://groups.roblox.com/v1/groups/{group_id}/users/{user_id}', data={"roleId": str(new_rank)})
        print(r.status_code)
        return r
        