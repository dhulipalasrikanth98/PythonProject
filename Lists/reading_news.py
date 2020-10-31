from win32com.client import Dispatch
import requests
import json
s=Dispatch("SAPI.SpVoice")
def speak(string):
    
    s.Speak(string)
t= requests.get("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=c6b0fe0e89ca47979e2a2d3068bfb044")
json_loads = json.loads(t.text)
for key,value in json_loads.items():
    if key == 'articles':
        l=json_loads[key]
        speak("Welcome to todays news")
     
        for i in l:
            speak(f"newsreader {i['author']} ")
            speak("Headlines are as follows")
            print(i['title'])
            speak(i['title'])
            speak(i['content'])
        

