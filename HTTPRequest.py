#coding=utf-8

import urllib.request
import urllib.parse

class HttpRequest(object):
        def __init__(self, url):
            self.url = url

        def get(self, param):
            params = urllib.parse.urlencode(param)
            url = self.url + '?%s' %params
            with urllib.request.urlopen(url) as response:
                result = response.read().decode('utf-8')
            return result

        def post(self, param):
            data = urllib.parse.urlencode(param)
            data = data.encode()
            with urllib.request.urlopen(self.url, data) as response:
                result = response.read().decode('utf-8')
            return result

if __name__ == '__main__':
    request = HttpRequest('https://www.baidu.com/')
    s = request.post('')
    print (s)