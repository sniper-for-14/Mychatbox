#coding: UTF-8
import requests
import re
import webbrowser
# import pygame
# from pygame.locals import *

# pygame.init()

def de_weather(defaults=None):
	url = 'http://weather.sina.com.cn/'
	if defaults:
		url=url+defaults
	else:
		url=url+'shijiazhuang'
	response = requests.get(url)
	response.encoding='utf-8'

	temperature = re.findall('<div class="slider_degree">(.*?)&#8451;</div>',response.text)[0]
	wea_img = re.findall('<img class="slider_whicon png24" src="(.*?)" height="128" width="128"',response.text)[0]
	wea_word = re.findall('height="128" width="128" alt="(.*?)">', response.text)[0]
	pollute_word = re.findall('<p class="slider_warn_val slider_warn_val3">(.*?)</p>',response.text)[0]
	pollute_num = re.findall('''<div class="slider_warn_i_tt">
                                <h6>污染指数</h6>
                                <p>(.*?)</p>
                            </div>''',response.text)[0]
	
	text = u'{0}°C \n {1} \n{2} {3}'.format(temperature,wea_word,pollute_num,pollute_word)

	with open('img/wea_img.jpg','wb') as file:
		file.write(requests.get(wea_img).content)
	return text
							
							
def more_weather():
	webbrowser.open_new('http://weather.sina.com.cn/')
