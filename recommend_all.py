import requests
import re
import csv
from music_id import *
import time
headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
	}

def recommand_movie():
	content = requests.get('https://maoyan.com/board/1',headers=headers).text
	images = re.findall('<img data-src="(.*?)" alt="',content)   # 10张
	titles = re.findall('title="(.*?)" class="image-link" data-act="boarditem-click"',content)   # 10个
	stars =  re.findall('<p class="star">(.*?)</p>',content)
	times = re.findall('<p class="releasetime">(.*?)</p>',content)
	ids = re.findall('data-act="boarditem-click" data-val="{movieId:(.*?)}">',content)
	content_ = requests.get('https://maoyan.com/board/7',headers=headers).text
	images_ = re.findall('<img data-src="(.*?)" alt="',content_)   # 10张
	titles_ = re.findall('title="(.*?)" class="image-link" data-act="boarditem-click"',content_)   # 10个
	stars_ =  re.findall('''<p class="star">
                (.*?)
        </p>''',content_)
	times_ = re.findall('<p class="releasetime">(.*?)</p>',content_)
	ids_ = re.findall('data-act="boarditem-click" data-val="{movieId:(.*?)}">',content_)
	with open('recommend/movie.csv','w') as f:
		writer = csv.writer(f)
		
		for i in range(10):
			try:
				writer.writerow([images[i],titles[i],stars[i],times[i],ids[i*2],0])
			except:
				writer.writerow([images[i],titles[i],'无',times[i],ids[i*2],0])
		for i in range(10):
			try:
				writer.writerow([images_[i],titles_[i],stars_[i],times_[i],ids_[i*2],0])
			except:
				writer.writerow([images_[i],titles_[i],'无',times_[i],ids_[i*2],0])
			
def recommend_music():
		 
	url='http://music.163.com/weapi/v3/playlist/detail?csrf_token='
	data = { "id": 506889042, "offset": 0, "total": True, "limit": 1000, "n": 1000}
	data = encrypt(data)
	j = requests.post(url,data=data,headers=headers)
	music_lists=[]
	for i in j.json()['playlist']['tracks']:
		music_lists +=[[i['id'],i['name']]]
	with open('recommend/music.csv','w',encoding='utf-8') as fp:
		writer = csv.writer(fp)
		for con in music_lists:
			writer.writerow([str(con[0]),con[1]])
		

def recommend_intro_movie(ids):
	url_movie='https://maoyan.com/films/{0}'.format(ids)
	movie_content=requests.get(url_movie,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}).text
	text = re.findall('<span class="dra">(.*?)</span>',movie_content)
	return text
	
'''	
	function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        c = "";
        for (d = 0; a > d; d += 1) e = Math.random() * b.length,
        e = Math.floor(e),
        c += b.charAt(e);
        return c
    }http://s3.music.126.net/web/s/core.js?2d008d1145747aa0f5385c601dc1ecc2
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b),
        d = CryptoJS.enc.Utf8.parse("0102030405060708"),
        e = CryptoJS.enc.Utf8.parse(a),
        f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b, "", c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {},
        i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
    window.ecnonasr = e
	
'''	
	
	
	