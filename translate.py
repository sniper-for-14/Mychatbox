import requests
import re
import json
import hashlib
import random
import time

def get_translate(word, kes=0):
	if kes==1:
		lan = 'ko'
	elif kes==2:
		lan ='ja'
	else:
		lan = 'AUTO'
	url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
	url_cookies = 'http://fanyi.youdao.com/?keyfrom=dict2.index'

	ers = requests.get(url_cookies) 
	ers = ers.cookies.get_dict()
	str_len = ''
	for i in ers:
		str_len+=i+'='+ers[i]+';'
	headers={
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Content-Length': '200',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Cookie': str_len,
	'Host': 'fanyi.youdao.com',
	'Origin': 'http://fanyi.youdao.com',
	'Referer': 'http://fanyi.youdao.com/?keyfrom=dict2.index',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest',
	}
	
	u = 'fanyideskweb'
	d = word
	f = str(int(time.time()*1000) + random.randint(1,10))
	c = 'rY0D^0\'nM0}g5Mm1z%1G4'
	
	sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()
	
	payload={
	'i': word,
	'from': 'AUTO',
	'to': '{0}'.format(lan),
	'smartresult': 'dict',
	'client': 'fanyideskweb',
	'salt': f,
	'sign': sign,
	'doctype': 'json',
	'version': '2.1',
	'keyfrom': 'fanyi.web',
	'action': 'FY_BY_REALTIME',
	'typoResult': 'false',
	}

	response = requests.post(url,data=payload,headers=headers).text
	try:
		results = json.loads(response)['smartResult']['entries']
	except:
		try:
			results = json.loads(response)['translateResult'][0][0]['tgt']
			lp = ''
			for ks in results:
				lp+=ks
			return lp
		except:
			results=['','NotFound(v_v)']
	return list(results[1:])











	

'''

OUTFOX_SEARCH_USER_ID=2144131117@10.168.8.63; 
JSESSIONID=aaaPGX3dsNtfbgnUtC_mw; 
OUTFOX_SEARCH_USER_ID_NCOO=546307947.1267163; 
fanyi-ad-id=43155; 
fanyi-ad-closed=1; 
___rl__test__cookies=1525761005940
'''

if __name__ == '__main__':
	results = get_translate("世界那么大，我想去看看")
	print(results)
# 	if '''\r\n''' in results[0]:
#
# 		for i in results:
# 			if len(i)>25:
# 				end_word = r'''  {0}\n{1}'''.format(i[:25], i[25:])
# 				translate_lab.config(text=end_word)
# 			else:
# 				translate_lab.config(text=results)
# 	else:
# 		print(results)