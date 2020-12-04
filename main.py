
import pyttsx3
import speech_recognition as sr
from speech_recognition import Microphone
from pyttsx3 import engine
import webbrowser
from time import ctime
import wikipedia 
import pyjokes
from googletrans import Translator
from tkinter import *
import os
from datetime import datetime
import pywhatkit

import wolframalpha
# win=Tk()

# win.geometry('500x500')

app_id='HAKJQ3-KP28H6TLT6'
r=sr.Recognizer()
r1=sr.Recognizer()

engine=pyttsx3.init()
client=wolframalpha.Client(app_id)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def value():
    a=input()
    return a


def respond(voice_data):
    try:
        if 'Hey assistant' in voice_data:
            print('listening')

            engine.say('yes tell me')
            engine.runAndWait()
        #     with Microphone() as source1:
        #         r1.adjust_for_ambient_noise(source1,duration=0.2)
        #         audio2=r1.listen(source1,phrase_time_limit=4)
        #         respond(audio2)
        if 'what is your name' in voice_data:
            
            engine.say('My name is assistant')
            engine.runAndWait()
        if 'search for' in voice_data:
            s_data=voice_data.split('for')
            r_data=s_data[-1]
            engine.runAndWait()
            search=record_audio()
            url='https://google.com/search?q= ' + r_data
            webbrowser.get().open(url)
            engine.say("Here is what I found about" +r_data )
            engine.runAndWait()
            try:
                page=wikipedia.summary(r_data,sentences=2)
                engine.say(page)
                engine.runAndWait()
            except:
                print('Nothing to say')
            print("Here is what I found " + search)
        if 'what is the time' in voice_data:
            print(ctime())
            
            engine.say(ctime())
            engine.runAndWait()
        if 'find location' in voice_data:
            l_data=voice_data.split('location')
            f_data=l_data[-1]
            url='https://google.nl/maps/place/' +f_data+ '/&amp;'
            webbrowser.get().open(url)
            engine.say('Here is the location '+ f_data)
            engine.runAndWait()
        if 'YouTube' in voice_data:
            
            engine.say('opening youtube')
            engine.runAndWait()
            print('opening youtube')
            url='https://www.youtube.com/'
            webbrowser.get().open(url)
        if 'play' in voice_data:
            p_data=voice_data.split('play')
            pl_data=p_data[-1]
            try:
                pywhatkit.playonyt(pl_data)
                
                engine.say('playing')
                engine.runAndWait()
                print('playing')
            except:
                print('An error occured')
        if 'app' in voice_data:
            try:
                engine.say('opening whatsapp')
                engine.runAndWait()
                url=('https://web.whatsapp.com/')
                webbrowser.get().open(url)
            except:
                engine.say('could not open')
                print('could not open')
        if 'Lpu Live' in voice_data:
            engine.say('opening lpulive')
            engine.runAndWait()
            url='https://lpulive.lpu.in/lpu-demo1/messages/1408548'
            webbrowser.get().open(url)
        if 'tell me a joke' in voice_data:
            joke1=pyjokes.get_joke(language='en', category= 'all')
            print(joke1)
            
            engine.say(joke1)
            engine.runAndWait()
        if 'translate' in voice_data:
            engine.say('What do you want to translate')
            engine.runAndWait()
            tran=record_audio()
            try:
                p=Translator()
                k=p.translate(tran,dest='hi')
                translated=k.pronunciation
                newVoiceRate = 145
                engine.setProperty('rate',newVoiceRate)
                engine.say(translated)
                engine.runAndWait()
                print(translated)
            except:
                engine.say('Sorry I could not translate')
                engine.runAndWait()
        if 'insta' in voice_data:
            engine.say('opening insta')
            engine.runAndWait()
            url='https://www.instagram.com/'
            webbrowser.get().open(url)
        if 'notepad' in voice_data:
            engine.say('What do you want to write')
            engine.runAndWait()
            write_to_file=record_audio()
            file_f="hello"+'-note.txt'
            with open(file_f,'w') as myFile:
                    myFile.write(write_to_file)
                    os.startfile(file_f)
                    engine.runAndWait()
        if "today's temperature" in voice_data:
            v_data=voice_data.split(" ")
            vo_data=v_data[-1]
            url='https://www.google.com/search?q=%20today%27s%20temperature%20in%20'+vo_data
            webbrowser.get().open(url)
            engine.say(vo_data)
            engine.runAndWait()
        if 'who is' in voice_data:
            try:
                
                i_data=voice_data.split('who is')
                r_data=i_data[-1]
                res=client.query(r_data)
                engine.say(next(res.results).text)
                engine.runAndWait()
            except:
                pass
        if 'what is the' in voice_data:
            try:
                s_data=voice_data.split('what is the')
                is_data=s_data[-1]
                res=client.query(is_data)
                engine.say(next(res.results).text)
                engine.runAndWait()
            except:
                pass

        if 'calculate' in voice_data:
            try:
                c_data=voice_data.split('calculate')
                cr_data=c_data[-1]
                engine.say(cr_data)
                engine.runAndWait()
            except:
                pass
                
    except:
        pass  
    


def record_audio():
        with Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=0.2)
            audio=r.listen(source,phrase_time_limit=4)
            voice_data=' '
            try:
                voice_data=r.recognize_google(audio)
            except sr.UnknownValueError:
                # voices = engine.getProperty('voices')
                # engine.setProperty('voice', voices[1].id)
                # engine.say('Sorry I did not get that')
                # print('Sorry I did not get that')
                # engine.runAndWait()
                pass
            except sr.RequestError:
                # engine.say('my service is down now')
                pass
            return voice_data




while (1):
    voice_data=record_audio()      
    if 'exit' in voice_data:
        engine.say('Closing')
        engine.runAndWait()
        break
    respond(voice_data)
    




# b1=Button(win,text='start',command=record_audio)
# b1.grid(row=5,column=5)



# print('How can I help you')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# engine.say('How can I help you')
# engine.runAndWait()




# win.mainloop()



    


    




  