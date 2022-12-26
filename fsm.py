from transitions.extensions import GraphMachine
#from utils import send_text_message, send_carousel_message, send_button_message, send_image_message
from utils import send_text_message, send_button_message, send_image_message
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction

from bs4 import BeautifulSoup
import json
import requests

import numpy
import pandas as pd

import time, random




class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        self.meal = []
        self.drink = [
        "https://www.google.com/maps/search/?api=1&query=22.9936692,120.2114866&query_place_id=ChIJJbSf4Ct3bjQRZf6T45S6HFY",
        "https://www.google.com/maps/search/?api=1&query=22.9942322,120.2153096&query_place_id=ChIJ_yXA1kB3bjQRMAe1UH38d_E",
        "https://www.google.com/maps/search/?api=1&query=23.0084086,120.2096287&query_place_id=ChIJSfFOepJ2bjQRLHZy0weKRZg",
        "https://www.google.com/maps/search/?api=1&query=23.0084079,120.2096287&query_place_id=ChIJA_ya5Fl3bjQRYNynb_0J2SU",
        "https://www.google.com/maps/search/?api=1&query=22.9952821,120.2153169&query_place_id=ChIJlVr9XZJ2bjQRDxpgVXzSk2k",
        "https://www.google.com/maps/search/?api=1&query=22.9961839,120.215326&query_place_id=ChIJdUG08pJ2bjQRMZLc2urxMgk",
      
        ]
        self.dessert = [
        "https://www.google.com/maps/search/?api=1&query=22.9955692,120.2153549&query_place_id=ChIJi4lNYJJ2bjQR_skD0gPWcWM",
        "https://www.google.com/maps/search/?api=1&query=22.99458,120.2121828&query_place_id=ChIJNS3lxI12bjQRPf-Uk8lFMuw",
        "https://www.google.com/maps/search/?api=1&query=22.9892849,120.224882&query_place_id=ChIJ79CbWrx2bjQRYld5gxPHgAk",
        "https://www.google.com/maps/search/?api=1&query=22.9892849,120.224882&query_place_id=ChIJC7JyL5Z2bjQR87yUe3CKhXQ",
        "https://www.google.com/maps/search/?api=1&query=22.9902955,120.2149929&query_place_id=ChIJAV70MpB2bjQRtCNvkyhQhEA",
        "https://www.google.com/maps/search/?api=1&query=22.9901345,120.2148934&query_place_id=ChIJhWs9MpB2bjQRNbSxAplcSvE",

        ]

    def is_going_to_menu(self, event):
        text = event.message.text
        if text == '開始':
            return True
        return False
        #return text.lower() == "go to selection"
        '''
        if text == 'selection' or text.lower()=='back':
            return True
        return False
        '''
    def is_go_back(self, event):
        text = event.message.text
        return text == "go back"
    
    def is_going_to_movie(self, event):
        text = event.message.text
        #return text == "看電影" 
        if text == '看電影' or (self.state == 'movie' and text=='開始'):
            return True
        return False
    

    def is_going_to_eat(self, event):
        text = event.message.text
        #return text == "美食"
        if text == '美食' or (self.state == 'eat' and text == '開始'):
            return True
        return False
    
    
    def is_going_to_work_out(self, event):
        text = event.message.text
        #return text == "健身"
        if text == '健身' or (self.state == 'work_out' and text == '開始'):
            return True
        return False

    def is_going_to_show_fsm(self, event):
        text = event.message.text
        #return text == "show fsm"
        if text == 'show fsm' or (self.state == 'show fsm' and text == '開始'):
            return True
        return False

    def on_enter_menu(self, event):
        print("I'm entering menu")
        #title = '您好!\n我是happy bot。\n很高興為您服務!!'
        title = '請選擇您想要的功能'
        text = '看電影/美食/健身/show fsm'
        btn = [
            MessageTemplateAction(
                label = '看電影',
                text ='看電影'
            ),
            MessageTemplateAction(
                label = '美食',
                text = '美食'
            ),
            MessageTemplateAction(
                label = '健身',
                text = '健身'
            ),
            MessageTemplateAction(
                label = 'show fsm',
                text = 'show fsm'
            ),
        ]
        url = 'https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12153852/American-Eskimo-Dog-standing-in-the-grass-in-bright-sunlight-400x267.jpg'
        send_button_message(event.reply_token, title, text, btn, url)


    
    
    def on_enter_movie(self, event):
        response = requests.get('http://www.atmovies.com.tw/movie/new/')
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'lxml')
        content = []
        for i, data in enumerate(soup.select('div.filmTitle a')):
            if i == 5:
                break
            content.append("\U0001F3AC" + data.text + '\n' + 'http://www.atmovies.com.tw' + data['href'])
        
        send_text_message(event.reply_token, text='\n\n'.join(content))
    
    
    def on_enter_eat(self, event):
        print("I'm entering eat")
        title = "想吃點什麼?"
        text = "請選擇現在想吃什麼，正餐/飲料/點心"
        btn = [
            MessageTemplateAction(
                label = "正餐",
                text = "正餐"
            ),
             MessageTemplateAction(
                label = "飲料",
                text = "飲料"
            ),
             MessageTemplateAction(
                label = "點心",
                text = "點心"
            ),
        ]
        
        url = 'https://khh.travel/content/images/static/4-1-food-11.jpg'
        send_button_message(event.reply_token, title, text, btn, url)



    def is_going_to_meal(self, event):
        text = event.message.text
        #return text.lower() == "go to meal"
        #return text == '正餐'
        if text == '正餐' or (self.state == 'meal' and text == '開始') or (self.state == 'meal' and text == '美食'):
            return True
        return False
    
   
    def on_enter_meal(self, event):
        print("I'm entering meal")
        title = "請選擇吃飯地區?"
        text = "台南市/高雄市"
        btn = [
            MessageTemplateAction(
                label = "台南市",
                text = "台南市"
            ),
            MessageTemplateAction(
                label = "高雄市",
                text = "高雄市"
            ),
        ]
        
        url = 'https://www.funtime.com.tw/blog_campaign/images/bg_map_TW_m.png'
        send_button_message(event.reply_token, title, text, btn, url)
       

    def is_going_to_place1(self, event):
        text = event.message.text
        if text == '台南市' or (self.state == 'place1' and text == '開始') or (self.state == 'place1' and text == '美食'):
            return True
        return False

    def is_going_to_place2(self, event):
        text = event.message.text
        if text == '高雄市' or (self.state == 'place2' and text == '開始') or (self.state == 'place2' and text == '美食'):
            return True
        return False

    def on_enter_place1(self, event):
        print("I'm entering place1")

        response = requests.get("https://ifoodie.tw/explore/台南市/list?sortby=popular&opening=true")
        soup = BeautifulSoup(response.content, "html.parser")
        cards = soup.find_all('div', {'class': 'jsx-3292609844 restaurant-item track-impression-ga'}, limit=5)
        content = ""
        for card in cards:
            title = card.find("a", {"class": "jsx-3292609844 title-text"}).getText()
            stars = card.find( "div", {"class": "jsx-1207467136 text"}).getText()
            address = card.find("div", {"class": "jsx-3292609844 address-row"}).getText()
            content += f"\U0001F35C{title} \n\U0001F31F{stars}顆星 \n\U0001F3DA{address} \n\n"
        
        send_text_message(event.reply_token, content)

    def on_enter_place2(self, event):
        print("I'm entering place2")

        response = requests.get("https://ifoodie.tw/explore/高雄市/list?sortby=popular&opening=true")
        soup = BeautifulSoup(response.content, "html.parser")
        cards = soup.find_all('div', {'class': 'jsx-3292609844 restaurant-item track-impression-ga'}, limit=5)
        content = ""
        for card in cards:
            title = card.find("a", {"class": "jsx-3292609844 title-text"}).getText()
            stars = card.find( "div", {"class": "jsx-1207467136 text"}).getText()
            address = card.find("div", {"class": "jsx-3292609844 address-row"}).getText()
            content += f"\U0001F35C{title} \n\U0001F31F{stars}顆星 \n\U0001F3DA{address} \n\n"
        
        send_text_message(event.reply_token, content)
    

    def is_going_to_drink(self, event):
        text = event.message.text
        #return text.lower() == "go to drink"
        if text == '飲料' or (self.state == 'drink' and text == '開始') or (self.state == 'drink' and text == '美食'):
            return True
        return False

    def on_enter_drink(self, event):
        print("I'm entering drink")

        msg = "\U0001F379\U0001F379\U0001F379\U0001F379\U0001F379\U0001F379\U0001F379\U0001F379\U0001F379\U0001F379\U0001F379\U0001F379\n推薦三間成大附近的飲料店給您！\n" + "1. " + self.drink[0] + "\n" + "2. " + self.drink[1] + "\n" + "3. " + self.drink[2] + \
        "\n\n輸入「random drink」，可幫您隨機選一間飲料店!\U0001F60E"
        send_text_message(event.reply_token, msg)  
    

    def is_going_to_random_drink(self, event):
        text = event.message.text
        if text == 'random drink' or (self.state == 'random_drink' and text == '開始') or (self.state == 'random_drink' and text == '美食') or(self.state == 'random_drink' and text == '飲料'):
            return True
        return False
    
    def on_enter_random_drink(self, event):
        print("I'm entering random drink")
        r = random.randrange(6)
        msg = "\U0001F37A\U0001F37A\U0001F37A\U0001F37A\U0001F37A\U0001F37A\U0001F37A\U0001F37A\U0001F37A\U0001F37A\U0001F37A\U0001F37A\n以下為幫您隨機選擇的飲料店家！\n" + self.drink[r] + "\n"
        send_text_message(event.reply_token, msg)

    

    def is_going_to_dessert(self, event):
        text = event.message.text
        #return text.lower() == "go to drink"
        if text == '點心' or (self.state == 'dessert' and text == '開始') or (self.state == 'dessert' and text == '美食'):
            return True
        return False

    def on_enter_dessert(self, event):
        print("I'm entering dessert")
        msg = "\U0001F361\U0001F361\U0001F361\U0001F361\U0001F361\U0001F361\U0001F361\U0001F361\U0001F361\U0001F361\U0001F361\U0001F361\n推薦三間成大附近的點心店給您！\n" + "1. " + self.dessert[0] + "\n" + "2. " + self.dessert[1] + "\n" + "3. " + self.dessert[2] + \
        "\n\n輸入「random dessert」，可以幫您隨機選一間點心店!\U0001F60E"
        send_text_message(event.reply_token, msg) 

    def is_going_to_random_dessert(self, event):
        text = event.message.text
        if text == 'random dessert' or (self.state == 'random_dessert' and text == '開始') or (self.state == 'random_dessert' and text == '美食') or (self.state == 'random_dessert' and text == '點心'):
            return True
        return False
    
    def on_enter_random_dessert(self, event):
        print("I'm entering random dessert")
        r = random.randrange(6)
        msg = "\U0001F36A\U0001F36A\U0001F36A\U0001F36A\U0001F36A\U0001F36A\U0001F36A\U0001F36A\U0001F36A\U0001F36A\U0001F36A\U0001F36A\n以下為幫您隨機選擇的點心店家！\n" + self.dessert[r] + "\n"
        send_text_message(event.reply_token, msg)

    def on_enter_work_out(self, event):
        print("I'm entering work_out")
        title = "選擇想鍛鍊的時長"
        text = "請選擇現在想時長，可以獲取相關訓練影片!"
        btn = [
            MessageTemplateAction(
                label = "15min",
                text = "15min"
            ),
            MessageTemplateAction(
                label = "20min",
                text = "20min"
            ),
           
        ]
        
        url = 'https://photo.16pic.com/00/92/13/16pic_9213659_b.jpg'
        send_button_message(event.reply_token, title, text, btn, url)


    def is_going_to_fifteen(self, event):
        text = event.message.text
        if text == '15min' or (self.state == 'fifteen' and text == '開始') or (self.state == 'fifteen' and text == '健身'):
            return True
        return False

    def is_going_to_twenty(self, event):
        text = event.message.text
        if text == '20min' or (self.state == 'twenty' and text == '開始') or (self.state == 'twenty' and text == '健身'):
            return True
        return False


    def on_enter_fifteen(self, event):
        msg = "推薦兩個15分鐘訊練影片給您！\n\
        初學者:\n\
        https://www.youtube.com/watch?v=F8v9SA4Ptu4\n\
        進階:\n\
        https://www.youtube.com/watch?v=1skBf6h2ksI\n\
        準備開始健身吧!"
        send_text_message(event.reply_token, msg)

    def on_enter_twenty(self, event):
        msg = "推薦兩個20分鐘訊練影片給您！\n\
        初學者:\n\
        https://www.youtube.com/watch?v=IT94xC35u6k\n\
        進階:\n\
        https://www.youtube.com/watch?v=Y2eOW7XYWxc\n\
        準備開始健身吧!"
        send_text_message(event.reply_token, msg)       

    


    
    def on_enter_show_fsm(self,event):
        url = 'https://github.com/YuniceLingling/happy_bot/blob/main/fsm.png?raw=true' 
        send_image_message(event.reply_token, url)

