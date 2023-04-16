from kivymd.app import MDApp
import plyer
from kivy import platform
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder 
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.popup import Popup
import cv2
import time
import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import random
import json
import pickle
from keras.models import load_model

class Treatment(MDScreen):
    pass

class command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_size = 17

class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_size = 17

class MyPopup(Popup):
    def display(self,content):
        self.root.ids["text"].text = content
        self.open()

class RightSwitch(IRightBodyTouch, MDSwitch):
    pass

class MainScreen(MDScreen):
    pass

class CameraScreen(MDScreen):
    pass

class ChatBotScreen(MDScreen):
    pass
class SettingsScreen(MDScreen):
    pass
class About(MDScreen):
    pass
class card(MDCard):
    pass

class Kisaan(MDApp):
    def build(self):
        self.class_names= ["anthracnose","blackspots","blight","canker","downy mildew","fusarium wilt","mosaic","powdery mildew","rust","sooty mold","verticillium wilt"]
        self.treats = {"anthrocnose":"1. Remove and destroy any infected plants in your garden. For trees, prune out the dead wood and destroy the infected leaves.\n2. You can try spraying your plants with a copper-based fungicide, though be careful because copper can build up to toxic levels in the soil for earthworms and microbes."
                       ,"blackspots":"To reduce black spot, irrigate and hose off aphids in the morning instead of the evening or night. Do not plant too close together. Prune canopies to increase air circulation. Prune off infected stems during the dormant season and dispose of fallen leaves and stems away from plants."
                       ,"blight":"Remove all affected leaves and burn them or place them in the garbage. Mulch around the base of the plant with straw, wood chips or other natural mulch to prevent fungal spores in the soil from splashing on the plant.\nStep 1: Mix 3 tablespoons baking soda with 1 gallon of water\nStep 2: Mix in 1 tablespoon vegetable oil, or cooking oil of your choice. This helps the spray to stick to the leaves\nStep 3: Mix in 2 drops of dish soap to help emulsify (mix) everything. Use a gentle dish soap since many have harmful chemicals and are not good for soil life.\nStep 4: Spray on tops and bottoms of leaves till dripping"
                       ,"canker":"Cut out all cankered areas, pruning back around 10-15cm (4-6in) beyond the affected parts into healthy wood.Bacterial canker often enters the tree through wounds – including pruning wounds made in autumn and winter.\nFor canker on plums and cherries, treat with a copper fungicide (containing copper oxychloride) 3 times a year: mid-August, mid-September and mid-October."
                       ,"downy mildew":"-> Grow up! Sprawling plants like cucumbers and melons can be grown on trellises to provide airflow and increased leaf drying....\n-> Use a drip line for watering. ...\n-> Reduce watering by mulching. ...\n-> Prune lower leaves. ...\n-> Get rid of infected plants."
                       ,"fusarium wilt":"Fusarium wilt diseases are best controlled by using resistant or tolerant cultivars, not by using soil applied fungicides. Liming soils and using nitrate nitrogen fertilizer have been effective for management of F. oxysporum on chrysanthemum, aster, gladiolus, cucumber, tomato, and watermelon."
                       ,"mosaic":"Once a houseplant is infected, leaves will develop a mosaic-like pattern with bright discolored spots. New growth is likely to be distorted. There is no treatment for the Mosaic Virus, and affected plants must be discarded immediately as it can spread to other plants."
                       ,"powdery mildew":" Mix 1 tablespoon potassium bicarbonate and ½ teaspoon liquid soap (not detergent) in 1 gallon of water. Spray liberally to all affected areas. This mixture may work better than baking soda as a treatment for existing infections. Milk: Mix 1 part milk to 2 to 3 parts water and spray liberally"
                       ,"rust":"A weekly dusting of sulfur can prevent and treat rust fungus. Neem oil, a botanical fungicide and pesticide, also controls rust. Some organic gardeners swear by baking soda to control garden fungus. The efficacy of baking soda spray might be enhanced by mixing it with light horticultural oil"
                       ,"sooty mold":"The best method to remove the mold is to soak affected plants in a water and detergent mixture. Use 1 tablespoon of household liquid detergent per gallon of water and spray it on the plants. Wait 15 minutes, then wash the detergent solution off with a strong stream of water."
                       ,"verticillium wilt":"There is no effective treatment for verticillium wilt. For affected vegetables, remove and dispose of the plant; don't compost it. For landscape plants, prune out affected branches and dispose of them immediately. Do not use infected wood for chips for landscape mulch"}
        self.lemmatizer = WordNetLemmatizer()
        self.intents = json.loads(open("intents.json").read())
        self.words = pickle.load(open("words.pkl","rb"))
        self.classes = pickle.load(open("classes.pkl","rb"))
        self.model = load_model("chatbot.h5")
        self.cam_model = load_model("model.h5")
        self.icon = "k.png"
        Builder.load_file("main.kv")
        self.screen = MDScreenManager()
        self.screen.add_widget(MainScreen(name="main"))
        self.screen.add_widget(CameraScreen(name="Camera"))
        self.screen.add_widget(ChatBotScreen(name="Chatbot"))
        self.screen.add_widget(SettingsScreen(name="settings"))
        self.screen.add_widget(Treatment(name="treat"))
        self.screen.add_widget(About(name="help"))
        Clock.schedule_interval(self.remainder,3600)
        return self.screen
    
    def change_to_main(self):
        self.screen.current = "main"

    def change_to_settings(self):
        self.screen.current = "settings" 

    def change_to_help(self):
        self.screen.current = "help"
    
    def change_to_camera(self):
        self.screen.current = "Camera"

    def remainder(self,check,value,*args):
        Time = int(time.strftime("%H"))
        if value:
            if Time == 9 or Time == 4 :
                plyer.notification.notify(title="KISAAN",message="it's time to water your plant",app_icon="k.ico")
    
    def send(self):
        if self.screen.get_screen("Chatbot").text_input.text != "":
            size = .22
            halign = "center"
            self.text = self.screen.get_screen("Chatbot").text_input.text
            if len(self.text) < 6:
                size = .22
                halign = "center"
            elif len(self.text) < 11:
                size = .32
                halign = "center"
            elif len(self.text) < 16:
                size = .45
                halign = "center"
            elif len(self.text) < 21:
                size = .58
                halign = "center"
            elif len(self.text) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            self.screen.get_screen("Chatbot").chats.add_widget(command(text=self.text,size_hint_x=size,halign=halign))
            self.screen.get_screen("Chatbot").text_input.text = ""
            Clock.schedule_once(self.response,2)

    def response(self,*args):
        ints = self.prediction(self.text)
        bots_reply = self.reply(ints,self.intents)
        self.screen.get_screen("Chatbot").chats.add_widget(Response(text=bots_reply,size_hint_x=.75))
    
    
    def bot(self):
        self.screen.get_screen("Chatbot").chats.add_widget(Response(text="Hi! I am Vriksh\nHow can I help you?",size_hint_x=.75))

    def clean_up(self,sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(word) for word in sentence_words]
        return sentence_words
    
    def bow(self,sentence):
        sentence_words = self.clean_up(sentence)
        bag = [0] * len(self.words)
        for w in sentence_words:
            for i, word in enumerate(self.words):
                if word == w:
                    bag[i] = 1
        return np.array(bag)
    def prediction(self,sentence):
        bow = self.bow(sentence)
        res = self.model.predict(np.array([bow]))[0]
        error = 0.25
        results = [[i,r] for i,r in enumerate(res) if r>error]
        results.sort(key=lambda x:x[1], reverse=True)
        rlist = []
        for r in results:
            rlist.append({"intents":self.classes[r[0]],"probability":str(r[1])})
        return rlist
    def reply(self,intents,intent_file):
        tag = intents[0]["intents"]
        all_intents = intent_file["intents"]
        for i in all_intents:
            if i["tag"] == tag:
                result = random.choice(i["responses"])
                return result
                break
            else:
                return "I don't know. I better start learning soon."
    def camera(self,*args):
        camera = self.screen.get_screen("Camera").camera
        camera.export_to_png("sample.png")
        data = cv2.imread("sample.png")
        data = cv2.resize(data,(200,200))
        res = self.cam_model.predict(np.array([data]))
        result = self.class_names[np.argmax(res)]
        
        for i in self.class_names:
            if result == i:
                # self.screen.get_screen("Camera").bottom_sheet.open()
                # self.screen.get_screen("Camera").bottom_sheet.add_widget(Treatment(text=self.treats[self.class_names.index(i)],size_hint_x=.75))
                content = self.treats[i]       
                break
        self.screen.get_screen("treat").text.text = content
        self.screen.current = "treat"
    
if __name__ == "__main__":
    if platform == 'Android':
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.CAMERA,Permission.WRITE_EXTERNAL_STORAGE,Permission.READ_EXTERNAL_STORAGE])
    Kisaan().run()