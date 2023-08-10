import requests
import json
import os
import main

# city = input("Enter the city:\n")
def func(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=17ec83bc6ba14c8f8e9190818230206&q={city}"
    r=requests.get(url)                          # response generate
    # print(r.text)
    wdic = json.loads(r.text)
    print(wdic["current"]["temp_c"])
    main.say(f"the temperature in {city} is")
    main.say(int(wdic["current"]["temp_c"]))
    main.say("degrees celcius and feels like")
    main.say(int(wdic["current"]["feelslike_c"]))
    main.say("degrees celcius")

    # # Robospeaker
    # with open("speech.vbs", "w") as f:
    #     f.write('Set speech = CreateObject("SAPI.SpVoice")\n')
    #     f.write(f'''speech.Speak "{f"the temperature in {city} is",wdic["current"]["temp_c"],"degrees celcius,feels like",wdic["current"]["feelslike_c"],"degrees celcius"}" \n''')
    #     f.write(f'''speech.Speak"{"last updated on",wdic["current"]["last_updated"]}" ''')
    # command = "cscript speech.vbs"
    # os.system(command)