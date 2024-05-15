import pyautogui as pygui
import time as t
import os as system
import screen_brightness_control as sbc
import pyttsx3 as pyt
import speech_recognition as sr
sp=pyt.init()
def speak(text):#this is speak function which will gives a speech output for a text input
    rate=sp.setProperty('rate',150)
    sp.say(text)
    sp.runAndWait()


engine=pyt.init()
engine.setProperty('rate',125)
engine.say("enter the key")
engine.runAndWait()
# physicss=input("enter the key")
def audioinput():
    
    t.sleep(8)
    global b

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold=1000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening.....')
        audio=r.listen(source)
    try:
        print("identifying........")
        text=r.recognize_google(audio)
        return text
    except Exception as e:#this exception will be executed if any errors occurs in finding audio into text
        print(e)
        speak('unable to recognize due to some error')
        print('unable to recognize')
        b=b+1
        speak('can you please enter it in text:')
        text=input('can you please enter it in text:')
        return text

    return text




physicss=audioinput

if  "physics" in physicss:
     print("activated")
     engine.say("Activated")
     engine.runAndWait()

     
     while True:
          engine.say("Enter the commond")
          engine.runAndWait()

     
          phy=audioinput().lower()
          

          if "shutdown" in phy:
               engine.say("shutting down the pc")
               engine.runAndWait()

               system.system("shutdown /r /t 1")
          elif "open notepad" in phy:
               engine.say("opening the notepad")
               engine.runAndWait()

               pygui.click(x=818, y=1051)
               pygui.typewrite('notepad',0.01)
               
               pygui.press('enter')
          elif "open command prompt" in phy:
               engine.say("opening the command prompt")
               engine.runAndWait()

               pygui.click(x=818, y=1051)
               pygui.typewrite('command prompt',0.01)
               pygui.press('enter')
          elif "open idle" in phy:
               engine.say("opening idle")
               engine.runAndWait()

               pygui.hotkey('win','s')
               t.sleep(2)
               pygui.typewrite('idle',0.01)
               pygui.press('enter')
          elif "open chrome"in phy:
               engine.say("opening chrome")
               engine.runAndWait()
               pygui.click(x=818, y=1051)
               pygui.typewrite('chrome',0.01)
               pygui.press('enter')
          elif "chatbox" in phy:
               engine.say("opening your chatbox")
               engine.runAndWait()
               import AI as Ai
               Ai
          if "increase screen brightness" in phy:
               bright=sbc.get_brightness()
               print(sbc.get_brightness())
     
               while True:
                 if "increase" in phy:
                     bright[0]=bright[0]+5
                     sbc.fade_brightness(bright[0],interval=0.01)
                     print(sbc.get_brightness())
                     engine.say("is in it enough or not")
                     engine.runAndWait()
                     v=input("is in it enough or not")
                     
                     if v=="enough":
                         break
                     elif v=="not":
                         if bright[0]<100:
                              bright[0]=bright[0]+5
                              sbc.fade_brightness(bright[0],interval=0.01)
                     else:
                         engine.say("it has already maximum value")
                         engine.runAndWait()
                         print("it has already maximum value")
                         
                         break
          elif "decrease screen brightness" in phy:
                   bright=sbc.get_brightness()
                   print(sbc.get_brightness())
                   while True:
                      if "decrease" in phy:
                          bright[0]=bright[0]-10
                          sbc.fade_brightness(bright[0],interval=0.01)
                          print(sbc.get_brightness())
                          engine.say("is in it enough or not")
                          engine.runAndWait()
                          v=input("is in it enough or not")
                          
                          if v=="enough":
                              break
                          elif v=="not":
                              if bright[0]>1:
                                   bright[0]=bright[0]-10
                                   sbc.fade_brightness(bright[0],interval=0.01)
                              else:
                                   engine.say("it has already minimum value")
                         
                                   engine.runAndWait()

                                   print("it has already minimum value")
                                   break
          else:
               print("enter the valid input")

elif "close"  in physicss:
     print("closing")
     
else:
     "physics" not in physicss
     print("I am not",physicss)
