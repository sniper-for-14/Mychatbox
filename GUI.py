#coding=utf8
from tkinter import *
from tkinter import scrolledtext 
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
import os
from PIL import Image, ImageTk  
from tkinter.messagebox import *
import requests
import re
import csv
from translate import get_translate
from weather import *
from music_id import *
import threading
from movie import *
from chat.turn_data import *
from recommend_all import *
import time

T1 = None
T2 = None
x = 400
y = 120
x0 = 400
y0 = 120
button_for = 0
test_button = 0

# 第二个
bt2_right=None
bt2_left=None
Lb2_2_3=None
Lb2_2_2=None
Lb2_2_1=None
frm1s2k=None
have_a_img=None
have_bg_img=None
music_button=0

# 第三个
T3_2_music_s=None
Loading=None
frm1s3 = None
T3_1=None
LB3_1 = None
LB3_2 = None
LB3_3 = None
T3_1 = None   # 获取搜索内容
L3_2_2 = None  # 音乐播放按钮
res_for_music=None  #歌曲单
lac_sings=None   # 歌曲名目
songs=None
T3_2_music=None
frm1_1=None
L3_2_100=None
tp = 0
tb = 0
music_lab=0
pause_sing=0
pygame.mixer.init()  # 音频初始化

movie_img=None

# 第四个
frm1s4=None
T1 = None
comboxlist = None
comvalue =None
but_for_translate =None
translate_lab =None

# 主程序
root = Tk()
root.config(bg='white')
root.title('Hello')
root.resizable(width=False, height=False)

root.wm_attributes("-topmost", 1)
root.geometry('524x452+{0}+{1}'.format(x0,y0))
root.iconbitmap('gen.ico')

## 图片
frm0_img = ImageTk.PhotoImage(Image.open('img/frm0.jpg'))
frm1_img = ImageTk.PhotoImage(Image.open('img/frm1.jpg'))
frm1_2img = ImageTk.PhotoImage(Image.open('img/frm2_3.jpg'))

bt2_music_bg = ImageTk.PhotoImage(Image.open('img/B2_music_bg.jpg').resize((380,500)))
bt2_movie_bg = ImageTk.PhotoImage(Image.open('img/bt2_movie_bg.jpg').resize((380,500)))

music2_img = ImageTk.PhotoImage(Image.open('img/music2.jpg'))
music3_img = ImageTk.PhotoImage(Image.open('img/music3.jpg'))
music_bg = ImageTk.PhotoImage(Image.open('img/music_bg.jpg'))
music_bg2 = ImageTk.PhotoImage(Image.open('img/music_bg2.jpg'))

trans_img = ImageTk.PhotoImage(Image.open('img/trans.jpg'))
trans_result_img = ImageTk.PhotoImage(Image.open('img/trans_result.jpg'))
frm2_3_1_img = ImageTk.PhotoImage(Image.open('img/frm2_3_1.jpg'))
frm2_3_2_img = ImageTk.PhotoImage(Image.open('img/back.jpg'))
L3_2_2_img = ImageTk.PhotoImage(Image.open('img/play-pause.jpg'))
L3_2_3_img = ImageTk.PhotoImage(Image.open('img/pause.jpg'))

left_feet0 = ImageTk.PhotoImage(Image.open('img/left0.jpg').resize((20,20)))
left_feet1 = ImageTk.PhotoImage(Image.open('img/left1.jpg').resize((20,20)))
right_feet0 = ImageTk.PhotoImage(Image.open('img/right0.jpg').resize((20,20)))
right_feet1 = ImageTk.PhotoImage(Image.open('img/right1.jpg').resize((20,20)))

to_chat_img = ImageTk.PhotoImage(Image.open('img/to_chat.jpg'))
to_img = ImageTk.PhotoImage(Image.open('img/to.jpg').resize((150,50)))

button1_img = ImageTk.PhotoImage(Image.open('img/button1.jpg'))
button2_img = ImageTk.PhotoImage(Image.open('img/button2.jpg'))
button3_img = ImageTk.PhotoImage(Image.open('img/button3.jpg'))
button4_img = ImageTk.PhotoImage(Image.open('img/button4.jpg'))

button1__img = ImageTk.PhotoImage(Image.open('img/button1__.jpg'))
button2__img = ImageTk.PhotoImage(Image.open('img/button2__.jpg'))
button3__img = ImageTk.PhotoImage(Image.open('img/button3__.jpg'))
button4__img = ImageTk.PhotoImage(Image.open('img/button4_.jpg'))


frm0 = Frame(root,width=88,height=452,bg='white')
frm0.place(x=0,y=0)
frm1 = Frame(root,width=428,height=450,bg='white')
frm1.place(x=90,y=0)
LB1 = Label(frm0,image=frm0_img,bg='white')
LB1.place(x=3,y=3)
LB2 = Label(frm1,image=frm1_img,bg='white')
LB2.place(x=0,y=0)

see_bt2_l = 0
ids_movie=None
frm1s2m=None
L2_songs=None
L2_songs_pause=None
def turn_pause(event):
	global lac_sings,pause_sing,L3_2_2,L2_songs_pause
	if pause_sing == 0:
		try:
			L3_2_2.config(image=L3_2_2_img)
		except:
			L2_songs_pause.config(image=L3_2_2_img)
		pygame.mixer.music.pause()
		pause_sing = 1
	else:
		try:
			L3_2_2.config(image=L3_2_3_img)
		except:
			L2_songs_pause.config(image=L3_2_3_img)
		pygame.mixer.music.unpause()
		pause_sing = 0 

def take_Chorme(event):
	global ids_movie
	webbrowser.open_new_tab('https://maoyan.com/cinemas?movieId={0}'.format(ids_movie))

def handler(event, a):
	global frm1s2m,L2_songs_pause,music_button
	music_button=2
	L2_songs = Label(frm1s2m,text='Loading......',bg='white')
	L2_songs.place(x=20,y=30)
	frm1s2m.update()
	if not os.path.exists('music/{0}.mp3'.format(a)):
		sings = get_music(a)
		download_mp3(sings,a)
		
	lac_sings = pygame.mixer.music.load('music/{0}.mp3'.format(a))
	L2_songs.destroy()
	frm1s2m.update()
	pygame.mixer.music.play()
	L2_songs_pause.config(image=L3_2_3_img)
	
	

def handlerAdaptor(fun, **kwds):

	return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)

	
def reco_music():
	global Lb2_2_3,Lb2_2_2,Lb2_2_1,frm1s2k,have_a_img,frm1s2,ids_movie,frm1s2m,L2_songs_pause
	re_music=[]
	for i in csv.reader(open('recommend/music.csv','r',encoding='utf-8')):
		try:
			re_music+=[[i[0],i[1]]]
		except:
			continue
	try:
		frm1s2k.place(x=500,y=0)
	except:
		pass
	frm1s2m = Frame(frm1s2,width=360,height=390,bg='red')
	frm1s2m.place(x=35,y=20)
	Lb2_2_bg_img = Label(frm1s2m,image=bt2_music_bg)
	Lb2_2_bg_img.place(x=0,y=0)
	Lb2_2_0 = Label(frm1s2m,text=re_music[0][1],compound='center',image=music_bg2,font=('楷体',11))
	Lb2_2_0.bind('<Double-Button-1>',handlerAdaptor(handler,a=re_music[0][0]))
	Lb2_2_0.place(x=160,y=120)
	Lb2_2_1 = Label(frm1s2m,text=re_music[1][1],compound='center',image=music_bg2,font=('楷体',11))
	Lb2_2_1.bind('<Double-Button-1>',handlerAdaptor(handler,a=re_music[1][0]))
	Lb2_2_1.place(x=0,y=180)
	Lb2_2_2 = Label(frm1s2m,text=re_music[2][1],compound='center',image=music_bg2,font=('楷体',11))
	Lb2_2_2.bind('<Double-Button-1>',handlerAdaptor(handler,a=re_music[2][0]))
	Lb2_2_2.place(x=160,y=240)
	Lb2_2_3 = Label(frm1s2m,text=re_music[3][1],compound='center',image=music_bg2,font=('楷体',11))
	Lb2_2_3.bind('<Double-Button-1>',handlerAdaptor(handler,a=re_music[3][0]))
	Lb2_2_3.place(x=0,y=290)
	Lb2_2_4 = Label(frm1s2m,text=re_music[4][1],compound='center',image=music_bg2,font=('楷体',11))
	Lb2_2_4.bind('<Double-Button-1>',handlerAdaptor(handler,a=re_music[4][0]))
	Lb2_2_4.place(x=160,y=340)
	
	L2_songs_pause = Label(frm1s2m,image=L3_2_2_img)
	L2_songs_pause.bind('<ButtonPress-1>',turn_pause)
	L2_songs_pause.place(x=300,y=30)
	
def reco_movie():
	global Lb2_2_3,Lb2_2_2,Lb2_2_1,frm1s2k,have_a_img,frm1s2,ids_movie,frm1s2m
	re_movies=[]
	recommand_movie()
	for i in csv.reader(open('recommend/movie.csv','r')):
		re_movies+=[i]
	with open('recommend/reco_movie.jpg','wb') as f:
		f.write(requests.get(re_movies[0][0]).content)
	try:
		frm1s2m.place(x=500,y=0)
	except:
		pass
	
	
	frm1s2k = Frame(frm1s2,width=360,height=380,bg='white')
	frm1s2k.place(x=35,y=20)
	ids_movie = re_movies[0][-2]
	have_a_img = ImageTk.PhotoImage(Image.open('recommend/reco_movie.jpg'))
	Lb2_bg_1 = Label(frm1s2k,image=bt2_movie_bg)
	Lb2_bg_1.place(x=0,y=0)
	Lb2_1_img = Label(frm1s2k,image=have_a_img)
	Lb2_1_img.place(x=17,y=14)
	Lb2_1_1 = Label(frm1s2k,text=re_movies[0][1],bg='#CC6600',font=('楷体', 17))
	Lb2_1_1.place(x=210,y=14)
	Lb2_1_2 = Label(frm1s2k,text=re_movies[0][2],font=('楷体', 10),bg='#CC6600')
	Lb2_1_2.place(x=185,y=90)
	Lb2_1_3 = Label(frm1s2k,text=re_movies[0][3],font=('楷体', 10),bg='#CC6600')
	Lb2_1_3.place(x=185,y=150)
	Bb2_1_4 = Button(frm1s2k,text='Buy Ticket',font=('楷体', 10),bg='#CC6600')
	Bb2_1_4.bind('<ButtonPress-1>',take_Chorme)
	Bb2_1_4.place(x=260,y=200)
	
	T2_1_5 = Text(frm1s2k,font=('楷体',12),width=44,height=7,bg='#993300',bd=0)
	T2_1_5.insert(END,recommend_intro_movie(ids_movie))
	
	T2_1_5.place(x=4,y=265)
	
def bt2_left__(event):
	global bt2_right,bt2_left,see_bt2_l
	if see_bt2_l==0:
		bt2_right.config(image=right_feet1)
		bt2_left.config(image=left_feet0)
		see_bt2_l=1
		reco_movie()
	else:
		see_bt2_l=0
		

def bt2_right__(event):
	global bt2_right,bt2_left,see_bt2_l
	if see_bt2_l==1:
		bt2_right.config(image=right_feet0)
		bt2_left.config(image=left_feet1)
		see_bt2_l=0
		reco_music()
	else:
		see_bt2_l=1
		

frm1s2 = None
make_button_recommend = 0
def recommend(event):
	global bt1,bt2,bt3,bt4,test_button,frm1,LB3_1,LB3_2,LB3_3,T3_1,frm1s1,frm1s2,frm1s3,frm1s4,L3_2_2,songs,T3_2_music_s,bt2_right,bt2_left,Lb2_2_3,Lb2_2_2,Lb2_2_1,frm1s2k,make_button_recommend
	make_button_recommend+=1
	try:
		frm1s1.place(x=500,y=0)
	except:
		pass
	try:
		frm1s3.place(x=500,y=0)
	except:
		pass
	try:
		frm1s4.place(x=1000,y=0)
	except:
		pass
	try:
		frm1s2.place(x=0,y=0)
	except:
		pass
	
	bt2.config(image=button2__img)
	bt1.config(image=button1_img)
	bt3.config(image=button3_img)
	bt4.config(image=button4_img)
	
	if not frm1s2 or make_button_recommend%2==0:

		frm1s2 = Frame(frm1,width=428,height=450,bg='white')
		frm1s2.place(x=0,y=0)
		LB2 = Label(frm1s2,image=frm1_img,bg='white')
		LB2.place(x=0,y=0)
	
		bt1.config(image=button1_img)
		bt3.config(image=button3_img)
		bt4.config(image=button4_img)
		bt2.config(image=button2__img)
	
		bt2_left = Label(frm1s2,image=left_feet0)
		bt2_left.bind('<ButtonPress-1>',bt2_left__)
		bt2_left.place(x=10,y=110)
		bt2_right = Label(frm1s2,image=right_feet1)
		bt2_right.bind('<ButtonPress-1>',bt2_right__)
		bt2_right.place(x=395,y=110)
		reco_movie()
	else:
		
		frm1s2.place(x=0,y=0)
	
	
	

def class_search_1(event):
	global LB3_1,LB3_2,LB3_3,tp,tb
	if tp==1 and tb!=1:
		LB3_1.config(bg='green')
		tb = 1
	else:
		LB3_1.config(bg='red')
	LB3_2.config(bg='yellow')
	LB3_3.config(bg='blue')
	tp=1
def class_search_2(event):
	global LB3_1,LB3_2,LB3_3,tp,tb
	if tp==2 and tb!=2:
		LB3_2.config(bg='yellow')
		tb=2
	else:
		LB3_2.config(bg='red')
	LB3_1.config(bg='green')
	LB3_3.config(bg='blue')
	tp=2
def class_search_3(event):
	global LB3_1,LB3_2,LB3_3,tp,tb
	
	if tp==3 and tb!=3: 
		LB3_3.config(bg='blue')
		tb=3
	else:
		LB3_3.config(bg='red')
	LB3_1.config(bg='green')
	LB3_2.config(bg='yellow')
	tp=3


search_music_word=None
def sing_song_0(event):
	global res_for_music,frm1_1,T3_2_music,lac_sings,songs,search_music_word,music_button
	music_button=3
	music_song=None
	Loading=Label(frm1_1,text='Loading......',width='10',height='1',bg='white')
	Loading.place(x=30,y=10)
	frm1_1.update()
	_lyric=music_lyric(list(res_for_music.values())[0])
	T3_2_music.insert(END,_lyric)
	songs=_lyric
	frm1_1.update()
	if not os.path.exists('music/{0}.mp3'.format(list(res_for_music.keys())[0]+'_'+search_music_word[:-1])):
		sings = get_music(list(res_for_music.values())[0])
		download_mp3(sings,list(res_for_music.keys())[0]+'_'+search_music_word[:-1])
		
	lac_sings = pygame.mixer.music.load('music/{0}.mp3'.format(list(res_for_music.keys())[0]+'_'+search_music_word[:-1]))
	Loading.destroy()
	frm1_1.update()
	pygame.mixer.music.play()
	L3_2_2.config(image=L3_2_3_img)

def sing_song_1(event):
	global res_for_music,frm1_1,T3_2_music,lac_sings,songs,search_music_word,music_button
	music_button=3
	music_song=None
	Loading=Label(frm1_1,text='Loading......',width='10',height='1',bg='white')
	Loading.place(x=30,y=10)
	frm1_1.update()
	_lyric=music_lyric(list(res_for_music.values())[1])
	T3_2_music.insert(END,_lyric)
	songs=_lyric
	frm1_1.update()
	if not os.path.exists('music/{0}.mp3'.format(list(res_for_music.keys())[1]+'_'+search_music_word[:-1])):
		sings = get_music(list(res_for_music.values())[1])
		download_mp3(sings,list(res_for_music.keys())[1]+'_'+search_music_word[:-1])
	lac_sings = pygame.mixer.music.load('music/{0}.mp3'.format(list(res_for_music.keys())[1]+'_'+search_music_word[:-1]))
	Loading.destroy()
	frm1_1.update()
	pygame.mixer.music.play()
	L3_2_2.config(image=L3_2_3_img)

def sing_song_2(event):
	global res_for_music,frm1_1,T3_2_music,lac_sings,songs,Loading,search_music_word,music_button
	music_button=3
	music_song=None
	Loading=Label(frm1_1,text='Loading......',width='10',height='1',bg='white')
	Loading.place(x=30,y=10)
	frm1_1.update()
	_lyric=music_lyric(list(res_for_music.values())[2])
	songs=_lyric
	T3_2_music.insert(END,_lyric)
	
	frm1_1.update()
	if not os.path.exists('music/{0}.mp3'.format(list(res_for_music.keys())[2]+'_'+search_music_word[:-1])):
		sings = get_music(list(res_for_music.values())[2])
		download_mp3(sings,list(res_for_music.keys())[2]+'_'+search_music_word[:-1])
	lac_sings = pygame.mixer.music.load('music/{0}.mp3'.format(list(res_for_music.keys())[2]+'_'+search_music_word[:-1]))
	Loading.destroy()
	frm1_1.update()
	pygame.mixer.music.play()
	L3_2_2.config(image=L3_2_3_img)

def new_find_movie(search_word):
	global frm1,tp,L3_2_2,T3_1,res_for_music,frm1_1,T3_2_music,frm1s1,frm1s2,frm1s3,frm1s4,T3_2_music_s,Loading,movie_img,search_music_word
	frm1s3_2 = Frame(frm1,width=428,height=450,bg='white')
	frm1s3_2.place(x=0,y=0)
	# frm1_1.config(bg='white')
	movie_image,movie_name,movie_type,movie_centry,movie_contry,movie_intro = search_movie(search_word)
	movie_img = ImageTk.PhotoImage(Image.open('movie/{0}.jpg'.format(movie_name)).resize((120,170)))
	L3_1_1 = Label(frm1s3_2,image=movie_img)
	L3_1_1.place(x=20,y=22)
	L3_1_2 = Label(frm1s3_2,text=movie_name,font=('楷体', 17),bg='white')
	L3_1_2.place(x=170,y=22)
	L3_1_3 = Label(frm1s3_2,text=movie_type,font=('楷体', 12),bg='white')
	L3_1_3.place(x=170,y=70)
	L3_1_4 = Label(frm1s3_2,text=movie_centry,font=('楷体', 12),bg='white')
	L3_1_4.place(x=170,y=90)
	L3_1_4 = Label(frm1s3_2,text=movie_contry,font=('楷体', 12),bg='white')
	L3_1_4.place(x=170,y=120)
	T3_1_5 = Text(frm1s3_2,font=('楷体',12),width=47,height=12,bg='white',bd=1)
	T3_1_5.insert(END,movie_intro)
	'''
	bar=Scrollbar(frm1s3_2)
	bar.config(command=T3_1_5.yview)
	bar.place(x=380,y=180)
	'''
	T3_1_5.place(x=0,y=220)
	Bt3_1_2_return = Button(frm1s3_2,text='返回',font=('微软雅黑', 10),bg='#CCCCCC')
	Bt3_1_2_return.bind('<ButtonPress-1>',search)
	Bt3_1_2_return.place(x=360,y=30)
	
		
def find_result(event):
	global frm1,tp,L3_2_2,T3_1,res_for_music,frm1_1,T3_2_music,frm1s1,frm1s2,frm1s3,frm1s4,T3_2_music_s,Loading,movie_img,search_music_word
	try:
		T3_2_music_s.destroy()
	except:
		pass
	search_word = T3_1.get("1.0",END)
	
	frm1_1 = Frame(frm1s3,width=400,height=240,bg='white')
	frm1_1.place(x=15,y=165)
	if tp == 2:
		search_music_word = search_word
		L3_2_bg = Label(frm1_1,width='400',height='240',bg='#66FFFF')
		L3_2_bg.place(x=0,y=0)
		L3_2_2 = Label(frm1s3,image=L3_2_2_img)
		L3_2_2.bind('<ButtonPress-1>',turn_pause)
		L3_2_2.place(x=325,y=60)
		
		Loading=Label(frm1_1,text='Loading......',width='10',height='1',bg='white')
		Loading.place(x=30,y=10)
		frm1_1.update()
		
		res_for_music = get_id(search_word)
		texts = list(res_for_music.keys())[:3]
		Loading.destroy()
		frm1_1.update()
		T3_2_music = Text(frm1_1,width=33, height=17)
		T3_2_music.place(x=155,y=7)
		L3_2_3 = Label(frm1_1,width='20',height='2',bg='#0099CC',text=texts[0])
		L3_2_3.bind('<Double-Button-1>',sing_song_0)
		L3_2_3.place(x=0,y=90)
		L3_2_4 = Label(frm1_1,width='20',height='2',bg='#0099CC',text=texts[1])
		L3_2_4.bind('<Double-Button-1>',sing_song_1)
		L3_2_4.place(x=0,y=140)
		L3_2_5 = Label(frm1_1,width='20',height='2',bg='#0099CC',text=texts[2])
		L3_2_5.bind('<Double-Button-1>',sing_song_2)
		L3_2_5.place(x=0,y=190)
	if tp == 1:
		new_find_movie(search_word)
	if tp == 3:
		get_book(search_word)

def search(event):
	global bt1,bt2,bt3,bt4,test_button,frm1,LB3_1,LB3_2,LB3_3,T3_1,frm1s1,frm1s2,frm1s3,frm1s4,L3_2_2,songs,T3_2_music_s
	
	try:
		frm1s1.place(x=500,y=0)
	except:
		pass
	try:
		frm1s2.place(x=500,y=0)
	except:
		pass
	try:
		frm1s4.place(x=500,y=0)
	except:
		pass
	try:
		frm1s3.place(x=0,y=0)
	except:
		pass
	

	frm1s3 = Frame(frm1,width=428,height=450,bg='white')
	frm1s3.place(x=0,y=0)
	LB2 = Label(frm1s3,image=frm1_2img,bg='white')
	LB2.place(x=0,y=0)
	LB3_4 = Label(frm1s3,image=frm2_3_1_img,bg='white')
	LB3_4.place(x=333,y=85)
	LB3_4.bind('<ButtonPress-1>',find_result)
	if pygame.mixer.music.get_busy() and music_button==3:
		L3_2_2 = Label(frm1s3,image=L3_2_3_img)
		L3_2_2.bind('<ButtonPress-1>',turn_pause)
		L3_2_2.place(x=325,y=59)
		T3_2_music_s = Text(frm1s3,width=33, height=17,bd='2')
		T3_2_music_s.place(x=185,y=150)
		T3_2_music_s.insert(END,songs)
		frm1s3.update()
	
	bt1.config(image=button1_img)
	bt2.config(image=button2_img)
	bt4.config(image=button4_img)
	bt3.config(image=button3__img)
	T3_1 = Text(frm1s3,width=29,height=1,bg='white',font=('楷体', 14),bd=0)
	T3_1.place(x=40,y=110)
	T3_1.focus()
	
	
	LB3_1 = Label(frm1s3,text='movie',bg='green')
	LB3_1.bind('<ButtonPress-1>',class_search_1)
	LB3_1.place(x=30,y=40)
	LB3_2 = Label(frm1s3,text='music',bg='yellow',width=7,height='1')
	LB3_2.bind('<ButtonPress-1>',class_search_2)
	LB3_2.place(x=250,y=70)
	LB3_3 = Label(frm1s3,text='book',bg='blue',width=7,height='1')
	LB3_3.bind('<ButtonPress-1>',class_search_3)
	LB3_3.place(x=350,y=30)

def congnize(event):
	global T1,button_for,translate_lab,comvalue
	if '自动' in comvalue.get():
		kes=0
	elif '韩' in comvalue.get():
		kes=1
	else:
		kes=2
	button_for=4
	words = T1.get(1.0,END)
	results = get_translate(words,kes)
	lists=[]
	if kes == 0:
		if '\r\n' in results[0]:
			for i in results:
				lists+=[i.split('\r\n')[0]]
		else:
			lists = [results]
		if len(words) > 60:
			texts_trans = ''
		else:
			texts_trans='''{0}\n\n'''.format(words)
		nums = 0
		for j in lists:
			if '\n' in j:
				if len(j)>30:
					texts_trans+='''  {0}\n{1}'''.format(j[:25],j[25:])
				else:
					texts_trans+='''  {0}'''.format(j)
				nums+=1
				if nums>=2:
					break
			else:
				if len(j)>30:	
					for count_lay in range(int(len(j)/48)+1):
						try:
							texts_trans+='''  {0}\n'''.format(j[(45*count_lay):45*(count_lay+1)])
						except:
							texts_trans+='''  {0}\n'''.format(j[(45*count_lay):])
				else:
					texts_trans+='''  {0}\n'''.format(j)
	else:
		texts_trans='''{0}\n   {1}'''.format(words,results)
	translate_lab.config(text=texts_trans)

def translate(event):
	global bt1,bt2,bt3,bt4,test_button,frm1,T1,comvalue,comboxlist,translate_lab,frm1s4,frm1s3,frm1s2,frm1s1,L3_2_2
	try:
		try:
			frm1s1.place(x=500,y=0)
		except:
			pass
		try:
			frm1s2.place(x=500,y=0)
		except:
			pass
		try:
			frm1s3.place(x=500,y=0)
		except:
			pass
		try:
			L3_2_2.destroy()
		except:
			pass
		try:
			frm1s4.place(x=0,y=0)
		except:
			pass
	except:
		pass
	bt1.config(image=button1_img)
	bt2.config(image=button2_img)
	bt3.config(image=button3_img)
	bt4.config(image=button4__img)
	
	frm1s4 = Frame(frm1,width=428,height=450,bg='white')
	frm1s4.place(x=0,y=0)
	LB2 = Label(frm1s4,image=frm1_img,bg='white')
	LB2.place(x=0,y=0)
	T1 = Text(frm1s4, width=40,height=8,font=("",13,'bold'),fg='#006699',bd='2')
	T1.place(x=13,y=23)
	T1.focus()
	
	comvalue=StringVar()#窗体自带的文本，新建一个值  
	comboxlist=ttk.Combobox(frm1s4,textvariable=comvalue) #初始化  
	comboxlist['values']=('自动检测语言','中--->韩','中--->日')  
	comboxlist.place(x=15,y=200)
	comboxlist.current(0)  #选择第一个 
	
	but_for_translate = Label(frm1s4,image=trans_img,bg='white')
	but_for_translate.place(x=310,y=190)
	but_for_translate.bind('<ButtonPress-1>',congnize)
	translate_lab = Label(frm1s4,image=trans_result_img,bg='white',compound='center',font=('楷体',12),fg='black')
	translate_lab.place(x=10,y=240)

T1_text=None

def chat_to(event):
	global frm1s1,T1_text
	from_word = T1_text.get("1.0",END)
	T1_text.delete(0.0, END)
	T1_text.update()
	L2_chat_from = Label(frm1s1,text='{0}'.format(from_word),image=to_img,compound='center',font=('楷体',10))
	L2_chat_from.place(x=250,y=134)
	if '更新音乐' in from_word:
		recommend_music()
		result = '更新完成'
	elif '张进' in from_word:
		result = '张进是一个大帅哥哎'
	elif '推荐' in from_word:
		result = '您可以看看我们的推荐功能'
	else:
		result = chat_with_me(from_word)
	L2_chat_to = Label(frm1s1,image=to_chat_img,text='{0}'.format(result),compound='center',font=('楷体',10))
	L2_chat_to.place(x=5,y=200)

	L2_chat_to.update()
	
def chat(event):
	global bt1,bt2,bt3,bt4,test_button,frm1,T1,comvalue,comboxlist,translate_lab,frm1s4,frm1s3,frm1s2,frm1s1,L3_2_2,T1_text
	try:
		frm1s4.place(x=500,y=0)
	except:
		pass
	try:
		frm1s2.place(x=500,y=0)
	except:
		pass
	try:
		frm1s3.place(x=500,y=0)
	except:
		pass
	try:
		L3_2_2.destroy()
	except:
		pass
	try:
		frm1s1.place(x=0,y=0)
	except:
		pass

	bt1.config(image=button1__img)
	bt2.config(image=button2_img)
	bt3.config(image=button3_img)
	bt4.config(image=button4_img)
	
	frm1s1 = Frame(frm1,width=428,height=450,bg='white')
	frm1s1.place(x=0,y=0)
	LB2 = Label(frm1s1,image=frm1_img,bg='white')
	LB2.place(x=0,y=0)
	
	T1_text = Text(frm1s1,width=59,height=8,bg='white',font=('楷体',10))
	T1_text.place(x=5,y=300)
	L1_chat_to = Label(frm1s1,image=to_chat_img,text='Hello!我是你的朋友Sun,我有什么可以帮您的呢？',compound='center',font=('楷体',10))
	L1_chat_to.place(x=5,y=30)
	B1_send = Button(frm1s1,text='发送',bg='green')
	B1_send.bind('<ButtonPress-1>',chat_to)
	B1_send.place(x=380,y=370)

	
	
def handler_back(event, a):	
	if a == 'chat':
		chat(event=None)
	if a == 'recommend':
		recommend(event=None)
	if a == 'search':
		search(event=None)
	if a == 'translate':
		translate(event=None)

def mid_function(fun, **kwds):
	return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)

# handlerAdaptor(handler,a=re_music[2][0])
	
bt1 = Label(frm0,width=60,height=66,image=button1_img)
bt1.bind("<ButtonPress-1>",mid_function(handler_back,a='chat'))
bt1.place(x=14,y=36)

bt2 = Label(frm0,width=60,height=66,image=button2_img)
bt2.bind("<ButtonPress-1>",mid_function(handler_back,a='recommend'))
bt2.place(x=14,y=126)

bt3 = Label(frm0,width=60,height=66,image=button3_img)
bt3.bind("<ButtonPress-1>",mid_function(handler_back,a='search'))
bt3.place(x=14,y=226)

bt4 = Label(frm0,width=60,height=66,image=button4_img)
bt4.bind("<ButtonPress-1>",mid_function(handler_back,a='translate'))
bt4.place(x=14,y=316)

is_side = 0

def callback_Left(event):
	global root,is_side
	if is_side == 0:
		root.overrideredirect(1)
		root.geometry('90x452+0+{0}'.format(y0))
	is_side = 1
	
def callback_Right(event):
	global root,is_side
	if is_side == 0:
		root.overrideredirect(1)
		root.geometry('90x452+1280+{0}'.format(y0))
	is_side = 1
	
def callback_Up(event):
	global root
	root.overrideredirect(1)
	root.geometry('90x100+{0}+0'.format(600))
	
def callback_Down(event):
	global root
	root.overrideredirect(1)
	root.geometry('90x80+{0}+650'.format(600))

def callback_look(event):
	global root,is_side
	if is_side == 1:
		root.overrideredirect(0)
		root.geometry('524x452+{0}+{1}'.format(x0,y0))
		is_side =0
	
root.bind('<Control-Left>',callback_Left)
root.bind('<Control-Right>',callback_Right)

root.bind('<Enter>',callback_look)





root.mainloop()




'''
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
'Cookie': 'OUTFOX_SEARCH_USER_ID=2144131117@10.168.8.63; OUTFOX_SEARCH_USER_ID_NCOO=546307947.1267163; _ntes_nnid=1ca2801e1551a41b8165e38ab074aa7b,1525939072022; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcuVe3gDoDiQaCEBaYqw; fanyi-ad-id=46607; fanyi-ad-closed=1; ___rl__test__cookies=1529847375242'}



data={
'i': '与其说孩子需要莎翁名篇的滋养',
'from': 'AUTO'
}
'''
