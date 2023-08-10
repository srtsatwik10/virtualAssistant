import os
import keyboard
import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import pyautogui
import screen_brightness_control as sbc
import newsApi
from keyboard import press,press_and_release
import time


chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = "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"
    chatStr += f"srt:{query}\nChirkoot:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = "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"
    text = f"GPT Response for Prompt- {prompt}:\n*************************************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("GPT Files"):
        os.mkdir("GPT Files")

    with open(f"GPT Files/{''.join(prompt.split('GPT')[1:])}.txt", "w") as f:
        f.write(text)
        say("response saved in folder")
def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(f"{text}")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 200
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said:{query}")
            return query
        except Exception as e:
            # say("some error occured")
            return takeCommand()

if __name__ == '__main__':
    say(" Hello i am chirkoot A.I.")
    while 1:
        print("listening...")
        query = takeCommand()
        # say(query)


        if "Open".lower() in query.lower():
            sites=[["youtube","https://youtube.in"],["google","https://google.com"],["jio cinema","https://jiocinema.com"],["Instagram","https://www.instragram.com"]]
            for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    # say(f"opening {site[0]} sir...")
                    webbrowser.open(site[1])


        elif "Weather".lower() in query.lower():
            cities = ["Bengaluru","New Delhi","Mumbai","Lucknow","Kolkata","chennai"]
            for city in cities:
                if f"weather in {city}".lower() in query.lower():
                    import waetherapp
                    waetherapp.func(f"{city}")


        elif "screenshot".lower() in query.lower():
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'C:\Users\gupta\Pictures\Screenshots\ScrnShot.png')
            say(r"screenshot taken and saved")


        elif "brightness".lower() in query.lower():
            for lvl in range(100):
                if f"brightness to {lvl}".lower() in query.lower():
                    sbc.set_brightness(lvl)


        elif "news".lower() in query.lower():
            newstopics = ["sports","business","science","health","technology"]
            for topic in newstopics:
                if f"{topic} related news".lower() in query.lower():
                    say("here are some top headlines")
                    try:
                        newsApi.headlines(f"{topic}")
                    except:
                        say("some error in fetching news")


        # YOUTUBE AUTOMATION
        elif "automate youtube".lower() in query.lower():
            say("automating..")
        elif "youtube search".lower() in query.lower():
            webbrowser.open(f"https://www.youtube.com/results?search_query={query[15:]}")
            say("here's what i found")
        elif "full screen".lower() in query.lower():
            press('f')
        elif "Resume".lower() in query.lower() or "Pause".lower() in query.lower():
            press('space bar')
        elif "next video".lower() in query.lower():
            press_and_release('SHIFT + n')
        elif "previous video".lower() in query.lower():
            press_and_release('SHIFT + p')
        elif "back".lower() in query.lower():
            press('j')
        elif "skip".lower() in query.lower():
            press('l')
        elif "mute".lower() in query.lower():
            press('m')

        # WINDOWS AUTOMATION
        elif "minimise window".lower() in query.lower():
            press_and_release('windows + m')
        elif "PC settings".lower() in query.lower():
            press_and_release('windows + i')
        elif "search for".lower() in query.lower():
            press_and_release('windows + s')
            time.sleep(2)
            pyautogui.write(query[11:])
            press('ENTER')
        elif "quick settings".lower() in query.lower():
            press_and_release('windows + a')
        elif"close window".lower() in query.lower():
            press_and_release('ALT + F4')
        elif "switch tab".lower() in query.lower():
            press_and_release('ALT + TAB')


        elif "use GPT".lower() in query.lower():
            say("creating response..")
            ai(query)

        elif "exit".lower() in query.lower():
            say("turning off sir..")
            exit()
        else:
            print("chatting...")
            chat(query)


















