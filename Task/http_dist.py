import requests

from main import BaseRequestFactory


class GetRequestFactory(BaseRequestFactory):

    def __init__(self, method, path, headers, data):
        super().__init__(method, path, headers, data)

    def send(self):
        r = requests.get(self.base_url+self.path, headers=self.headers, json=self.data)
        return r.text


class PostRequestFactory(BaseRequestFactory):

    def __init__(self, method, path, headers, data):
        super().__init__(method, path, headers, data)

    def send(self):
        r = requests.post(self.base_url + self.path, headers=self.headers, json=self.data)
        return r.text


class PutRequestFactory(BaseRequestFactory):

    def __init__(self, method, path, headers, data):
        super().__init__(method, path, headers, data)

    def send(self):
        r = requests.put(self.base_url+self.path, headers=self.headers, json=self.data)
        return r.text


class DeleteRequestFactory(BaseRequestFactory):

    def __init__(self, method, path, headers, data):
        super().__init__(method, path, headers, data)

    def send(self):
        r = requests.delete(self.base_url+self.path, headers=self.headers, json=self.data)
        return r.text




if __name__ == "__main__":
    input_dict = {'post': {'class': PostRequestFactory,
                           'method':'POST',
                           'path': '/post'},
                  'get': {'class': GetRequestFactory,
                          'method': 'GET',
                          'path': '/get'},
                  'put': {'class': PutRequestFactory,
                          'method': 'PUT',
                          'path': '/put'},
                  'delete': {'class': DeleteRequestFactory,
                             'method': 'DELETE',
                           'path': '/delete'}
                  }
    headers = {"Content-Type": "application/json"}
    data = {"key": "value"}

    method = 'put'
    inputs = input_dict[method]

    request_object = inputs['class'](
        method=inputs['method'],
        path=inputs['path'],
        headers=headers,
        data=data
    )

    print(request_object.send())
