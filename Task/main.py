import json
import os
import requests


class BaseRequestFactory:
    

    def __init__(self, method: str, path: str, headers: json, data: json):
        self.method = method
        self.path = path
        self.headers = headers
        self.data = data
        self.base_url = self.retrieve_base_url()
        self.allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
        self.validate_method()

    def send(self):
        r = requests.request(self.method, self.base_url + self.path, headers=headers, json=data)
        return r.text

    @staticmethod
    def retrieve_base_url(key='BASE_URL'):
        base_url = os.getenv(key)
        return base_url

    def validate_method(self):
        if not self.method in self.allowed_methods:
            raise Exception(f'The method must be one of the {','.join(self.allowed_methods)} methods.')

if __name__ == "__main__":
    method='PUT'
    path='/put'
    headers = {"Content-Type": "application/json"}
    data={"key": "value"}
    post_fact = BaseRequestFactory(method=method,
                                   path=path,
                                   headers=headers,
                                   data=data
                                   )
    print(post_fact.send())

