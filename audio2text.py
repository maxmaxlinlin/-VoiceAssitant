import urllib.request
import urllib
import json
import base64
api_key = "mUG5koXhdqPRtiHmLNXRoB3m"
api_secert = "37b2duGIoMay2SMjTSLhsNCopMXwGDEr"

class BaiduRest:
    def __init__(self, cu_id, api_key, api_secert):
        self.token_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
        self.getvoice_url = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"
        self.upvoice_url = 'http://vop.baidu.com/server_api'
        self.cu_id = cu_id
        self.getToken(api_key, api_secert)
        return

    def getToken(self, api_key, api_secert):
        token_url = self.token_url % (api_key,api_secert)

        r_str = urllib.request.urlopen(token_url).read().decode('utf-8')
        token_data = json.loads(r_str)
        self.token_str = token_data['access_token']
        pass

    def getVoice(self, text, filename):
        get_url = self.getvoice_url % (urllib.parse.quote(text), self.cu_id, self.token_str)

        voice_data = urllib.request.urlopen(get_url).read()
        voice_fp = open(filename,'wb+')
        voice_fp.write(voice_data)
        voice_fp.close()
        pass

    def getText(self, filename):
        data = {}
        data['format'] = 'wav'
        data['rate'] = 16000
        data['channel'] = 1
        data['cuid'] = self.cu_id
        data['token'] = self.token_str
        wav_fp = open(filename,'rb')
        voice_data = wav_fp.read()
        data['len'] = len(voice_data)
        data['speech'] = base64.b64encode(voice_data).decode('utf-8')
        post_data = json.dumps(data)
        r_data = urllib.request.urlopen(self.upvoice_url,data=bytes(post_data,encoding="utf-8"))
        r_data2=r_data.read().decode('utf-8')
        print(r_data2)
        return json.loads(r_data2)['result'][0]
def getData():
    word=input("enter what you want to hear")
    bdr.getVoice(word, "out.mp3")
    value=(bdr.getText("16k.wav"))[0]
    print(value)
    print(1)
    return value

if __name__ == "__main__":
    
    bdr = BaiduRest("test_python", api_key, api_secert)
    val1=bdr.getText("temp.wav")
    #txt  = (open(val1[0], "r"))
    #print(val1)
    #bdr.getVoice(val1, "out.mp3")
    #sudo arecord -t wav -c 1 -r 16000 -D "plughw:1,0" -d 5 -f S16_LE temp.wav
    #omxplayer -o local temp.wav





