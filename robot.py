# -*- coding: utf-8 -*-
#python2
import urllib
import json
key = '05ba411481c8cfa61b91124ef7389767'
api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='

def getresponse():
        info=open('conversation.txt','r').readlines()[-1]
        request = api + info
        print(request)
        response = urllib.urlopen(request).read()
        print(response)
        word= json.loads(response)['text']
        info=open('conversation.txt','wb')
        word=word.encode('utf-8')
        print(word)
        info.write(word+"\n")
        info.close()
        return word
 
if __name__ == '__main__':
    getresponse()
       # while True:
          #info = raw_input('我: ')
##        request = api + info
          #response = getresponse(info)
##        dic_json = json.loads(response)
          #print '机器人: '.decode('utf-8') + response