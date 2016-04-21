#! python2
# encoding:utf-8

import urllib2, json
import requests
def main():
    url = 'http://www.zhihu.com'
    #print help(urllib2)
    #print urllib2.urlopen(url).read()
    print requests.get(url).content

def test_kanzhihu():
    url = 'http://api.kanzhihu.com/'

    result = requests.get(url + 'getposts')

    if result.status_code == 200:
        r = json.loads(result.text)
        #print r
        #for item in r.get('posts'):
        #    print item['date'], item['name']
        #    print item['excerpt']
        posts = r.get('posts')
        item = posts[0]
        print item['excerpt']
        ans = requests.get(url + 'getpostanswers/' + item['date'].replace('-', '') + '/' + item['name'])
        if ans.status_code == 200:
            #print ans.text
            for d in json.loads(ans.text).get('answers'):
                for key, val in d.items():
                    print key, ':', val

if __name__ == '__main__':
    #main()
    test_kanzhihu()
    #print help(json)
    #print help(urllib2)
    #print help(requests)
    #print help(requests.api)