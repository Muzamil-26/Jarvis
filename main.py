import speech_recognition as sr
import webbrowser
import pyttsx3
import song
import google.generativeai as genai
# import client as api

# from openai import OpenAI

recognizer= sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def gemini(c):
            genai.configure(api_key="AIzaSyD83IDGQUTyMmjcUym_FhAM0ED3-xTZbr4")
            model = genai.GenerativeModel('gemini-1.5-flash')

            response = model.generate_content(c)
            return response.text

# def openai(c):
#                 from openai import OpenAI

# # client = OpenAI()
# # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# # if you saved the key under a different environment variable name, you can do something like:
#                 client = OpenAI(
#                 api_key="APY_KEY",
#                 )

#                 completion = client.chat.completions.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {"role": "system", "content": "You are a virtual assistant jarvis skilled in general task like alexa and google clouds"},
#                     {"role": "user", "content": c}
#                 ]
#                 )
#                 return completion.choices[0].message.content

def processcommand(c):
    if "open google" in c.lower():
        print(c.lower())
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        print(c.lower())
        webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play") or c.lower().startswith("open"):
                                    songs = c.lower().split(' ')[1]
                                    print(songs)
                                    link= song.songs[songs]
                                    print(link)
                                    webbrowser.open(link)
    elif "open instagram" in c.lower():
          webbrowser.open("https://www.instagram.com")
    elif "open gitub" in c.lower():
           webbrowser.open("https://github.com/")

    else:
          output= gemini(c)
          print(output)
          speak(str(output)) 
                 
          


if __name__=="__main__":
    speak("Intializing Jarvis...")
    while True:
        r=sr.Recognizer()
        
       

        try:
            with sr.Microphone() as source:
                print("listening..")
                audio=r.listen(source, timeout=2,phrase_time_limit=2)
                word=r.recognize_google(audio)
                print(word)
            
            if(word.lower()=="jarvis"):
                speak("Yes sir!")
                with sr.Microphone() as source:
                    print("Active jarvis..")
                    audio=r.listen(source,phrase_time_limit=4)
                    command=r.recognize_google(audio)       
                    processcommand(command)
                 
        except Exception as e:
            print(f"Error is:{e}")
