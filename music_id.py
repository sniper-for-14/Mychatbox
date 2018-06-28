import base64
import json
import random
import requests
import pygame
from Crypto.Cipher import AES
from string import ascii_letters, digits
import re
import time

_charset = ascii_letters + digits

def music_lyric(id=387718):
	url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(id) + '&lv=1&kv=1&tv=-1'
	j = json.loads(requests.get(url).text)
	try:
		text = re.sub(re.compile(r'\[.*\]'),"", j['lrc']['lyric']).strip()
	except:
		text='没有歌词'
	
	return text

def rand_char(num=16):
    return ''.join(random.choice(_charset) for _ in range(num))


def aes_encrypt(msg, key, iv='0102030405060708'):
    def padded(msg):
        try:
            msg=str(msg,encoding='utf-8')
        except:
            pass
        pad = 16 - len(msg) % 16
        return msg + pad * chr(pad)

    msg = padded(msg)
    cryptor = AES.new(key, IV=iv, mode=AES.MODE_CBC)
    text = cryptor.encrypt(msg)
    text = base64.b64encode(text)
    return text


def gen_params(d, i):
    text = aes_encrypt(d, '0CoJUm6Qyw8W8jud')
    text = aes_encrypt(text, i)
    return text
modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
pubKey = '010001'

def rsa_encrypt(msg):
    msg = msg[::-1]
    rs = int(msg.encode('utf-8').hex(),16)**int(pubKey, 16)%int(modulus, 16)
    return format(rs, 'x').zfill(256)


def encrypt(query):
    query = json.dumps(query)
    rand_i = rand_char(16)
    params = gen_params(query, rand_i)
    enc_sec_key = rsa_encrypt(rand_i)
    data = {
        'params': params,
        'encSecKey': enc_sec_key
    }
    return data

def get_id(name_music):

    url = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'music.163.com',
        'Origin': 'http://music.163.com',
        'Referer': 'http://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }
    query = {
	"hlpretag":"<span class=\"s-fc7\">",
	"hlposttag":"</span>",
	"s":'{0}'.format(name_music),
	"type":"1",
	"offset":"0",
	"total":"true",
	"limit":"30",
	"csrf_token":""
	}
    data = encrypt(query)

    r = requests.post(url, data=data, headers=headers)
    results = r.json()
    lists_music={}
    count_num = 0
    count_num = 0
    for i in results['result']['songs']:
        if i['ar'][0]['name'] in lists_music.keys():
            lists_music.update({i['ar'][0]['name']+str(count_num):i['id']})
            count_num+=1
            continue
        else:
            lists_music.update({i['ar'][0]['name']:i['id']})
        
		
    return lists_music
	
def get_music(ids=186240):

    url = 'http://music.163.com/weapi/song/enhance/player/url?csrf_token='
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'music.163.com',
        'Origin': 'http://music.163.com',
        'Referer': 'http://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    query = {
    'ids':'[{0}]'.format(ids),
	'br':320000,
	'csrf_token':'',
	}
    data = encrypt(query)
    r = requests.post(url, data=data, headers=headers)
    return r.json()['data'][0]['url']
'''
def start(name):
	ids = get_id(name)
	file= get_music()
	
	pygame.mixer.init()
	track = pygame.mixer.music.load(file)
	pygame.mixer.music.play()
	time.sleep(10)
	pygame.mixer.music.stop()
'''

def download_mp3(l_songs,name):
	req = requests.get(l_songs)    
	with open('music/{0}.mp3'.format(name), 'wb') as code:    
		code.write(req.content)
'''	
pygame.init() 进行全部模块的初始化， 
pygame.mixer.init() 或者只初始化音频部分 
pygame.mixer.music.load(‘xx.mp3’) 使用文件名作为参数载入音乐 ,音乐可以是ogg、mp3等格式。载入的音乐不会全部放到内容中，而是以流的形式播放的，即在播放的时候才会一点点从文件中读取。 
pygame.mixer.music.play()播放载入的音乐。该函数立即返回，音乐播放在后台进行。 
play方法还可以使用两个参数 
pygame.mixer.music.play(loops=0, start=0.0) loops和start分别代表重复的次数和开始播放的位置。 
pygame.mixer.music.stop() 停止播放， 
pygame.mixer.music.pause() 暂停播放。 
pygame.mixer.music.unpause() 取消暂停。 
pygame.mixer.music.fadeout(time) 用来进行淡出，在time毫秒的时间内音量由初始值渐变为0，最后停止播放。 
pygame.mixer.music.set_volume(value) 来设置播放的音量，音量value的范围为0.0到1.0。 
pygame.mixer.music.get_busy() 判断是否在播放音乐,返回1为正在播放。 
pygame.mixer.music.set_endevent(pygame.USEREVENT + 1) 在音乐播放完成时，用事件的方式通知用户程序，设置当音乐播放完成时发送pygame.USEREVENT+1事件给用户程序。 pygame.mixer.music.queue(filename) 使用指定下一个要播放的音乐文件，当前的音乐播放完成后自动开始播放指定的下一个。一次只能指定一个等待播放的音乐文件。
'''