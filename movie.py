import requests 
import re
import webbrowser
import os
flag = 0
 

get_url = 'https://maoyan.com/board'
headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
	}

def search_movie(name):
	if u'\u4e00'<=name<=u'\u9fff':
		url_zh='https://maoyan.com/query?kw={0}'.format(name)
		content = requests.get(url_zh,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}).text
		label_type= re.findall('      <a href="/films/(.*?)" target="_blank" data-act="movies-click" data-val="',content)
		url_movie='https://maoyan.com/films/{0}'.format(label_type[0])
		movie_content=requests.get(url_movie,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}).text
		movie_type=re.findall(' <li class="ellipsis">(.*?)</li>',movie_content)[0].split(',')
		movie_contry=re.findall(' <li class="ellipsis">(.*?)</li>',movie_content)[1]
		movie_centry=re.findall('''<li class="ellipsis">
        (.*?)
          (.*?)
        </li>''',movie_content)[0]
		movie_centry=movie_centry[0]+movie_centry[1]
		movie_intro = re.findall('''<div class="mod-content">
                    <span class="dra">(.*?)</span>

    </div>''',movie_content)[0]
		movie_image=re.findall('<img class="avatar" src="(.*?)" alt="">',movie_content)[0]
		movie_name=re.findall('<h3 class="name">(.*?)</h3>',movie_content)[0]
		ir=requests.get(movie_image,stream=True)
		
		with open('movie/{0}.jpg'.format(movie_name),'wb') as f:
			for chunk in ir:
				f.write(chunk)
		return movie_image,movie_name,movie_type,movie_centry,movie_contry,movie_intro
	else:
		url_en='https://maoyan.com/ajax/suggest?kw={0}'.format(name)
		
	 

def get_movie():
	responses = requests.get(get_url,headers=headers).text
	img_url = re.findall('<img data-src="(.*?)" alt=',responses)
	# https://maoyan.com/films/341178
	a_url = re.findall('        <p class="name"><a href="(.*?)" title',responses)
	movie_url = []
	for i in a_url:
		movie_url += ['https://maoyan.com'+i]
	intro_url = []
	for j in movie_url:
		resm = requests.get(j,headers=headers)
		intro_url += re.findall('<meta name="description" content="(.*?)>',resm.text)
	return img_url,movie_url,intro_url
	
# print(get_1())

def get_book(name):
	webbrowser.open_new('http://search.dangdang.com/?key={0}&act=input&sort_type=sort_score_desc#J_tab'.format(name))
	global flag
	if flag == 0:
		flag+=1
	else:
		webbrowser.open_new_tab('https://kyfw.12306.cn/otn/leftTicket/init')


def get_train():
	global flag
	if flag == 0:
		flag+=1
	else:
		webbrowser.open_new_tab('https://kyfw.12306.cn/otn/leftTicket/init')

'''
if __name__ == '__main__':
	print(get_movie())
'''