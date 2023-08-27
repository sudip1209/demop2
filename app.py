# from flask import Flask, request, jsonify, render_template
# from gtts import gTTS
# import os
# import speech_recognition as sr
# import pyttsx3
# import webbrowser
# import openai
# import datetime
# import random
# import numpy as np
# from selenium import webdriver
# import wikipedia

# app = Flask(__name__)
# chatStr = ""
# # https://youtu.be/Z3ZAJoi4x6Q
# def chat(query):
#     global chatStr
#     global retStr
#     retStr="Issue Detected at OpenAI"
#     try:
#         #print(chatStr)
#         openai.api_key = "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"
#         chatStr += f"Uday: {query}\n Apna AI: "
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt= chatStr,
#             temperature=0.7,
#             max_tokens=256,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0
#         )
#         print(jsonify(response))
#         print("TEST",response["choices"][0]["text"])
#         #todo: Wrap this inside of a  try catch block
#         #say(response["choices"][0]["text"])
#         chatStr += f"{response['choices'][0]['text']}\n"
#         #retStr = response["choices"][0]["text"]
#         #webdriver.Chrome().get("about:blank")
#         #webdriver.Chrome().execute_script(f"window.localStorage.setItem('chat','{retStr}');")
#         #webdriver.Chrome().quit()
#         # with open("file.txt","a") as f:
#         #     f.seek(0)
#         #     f.write(retStr)
#         #     f.close()
#        # return retStr
#         return response['choices'][0]['text']
#     except:
#         #webdriver.Chrome().get("about:blank")
#         #retStr=webdriver.Chrome().execute_script(f"window.localStorage.setItem('chat');")
#         #webdriver.Chrome().quit()
#         # with open("file.txt","r") as f:
#         #     f.seek(0)
#         #     f.seek(-2,1)
#         #     retStr=f.read(1)
#         #     f.close()
#         #os.remove('file.txt')
#         return retStr
from flask import Flask, request, jsonify, render_template
import openai  # Import the openai package

app = Flask(__name__)
chatStr = ""

def chat(query):
    global chatStr
    retStr = "Issue Detected at OpenAI"
    try:
        openai.api_key = "your_openai_api_key_here"
        chatStr += f"Uday: {query}\n Apna AI: "
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        chatStr += f"{response['choices'][0]['text']}\n"
        return response['choices'][0]['text']
    except Exception as e:
        print("OpenAI API Error:", str(e))
        return retStr

def ai(prompt):
    openai.api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

    
def ai(prompt):
    openai.api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('code ')[1:]).strip() }.txt", "w") as f:
        f.write(text)



def appMain(test):
    while True:
        #print("Listening...")
        query=test
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"],["google", "https://www.google.com"], ["facebook", "https://www.facebook.com"],["instagram", "https://www.instagram.com"],["flikart", "https://www.flikart.com"],["amazon", "https://www.amazon.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                #say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                return "Opening "+site[0]+" sir..."

        # todo: Add a feature to play a specific song
        if "open music".lower() in query.lower():
            musicPath = "C:\\Users\\usutt\\Downloads\\multiverse1.png"
            #say("opening sir")
            os.system(f"start {musicPath}")
            return "opening sir"
	    
        elif "wikipedia".lower() in query.lower():
            if ("about".lower() in query.lower()):
                res=query.lower().split("about")
                text=res[1]
                result=wikipedia.summary(text, sentences=5)

            elif "search".lower() in query.lower():
                res=query.lower().split("search")
                text=res[1]
                result=wikipedia.summary(text, sentences=5)

            elif "write".lower() in query.lower():
                res=query.lower().split("write")
                text=res[1]
                result=wikipedia.summary(text, sentences=5)

            else :
                text=query.lower()
                result=wikipedia.summary(text, sentences=5)
            
            return result
        
        elif "the time".lower() in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            #say(f"Sir time is {hour} bajj  kee {min} minutes sir")
            return "Sir time is "+hour+" hours  and "+min+" minutes sir."

        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")
            return "Working on it"

        elif "open pass".lower() in query.lower():
            os.system(f"open /Applications/Passky.app")
            return "Working on it"

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
            return "AI done it's job."
        elif "write a code ".lower() in query.lower():
            ai(prompt=query)
            return "AI done it's job."

       # elif "alexa Quit".lower() in query.lower():
       #     exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""
            return "Chat cleared"

        else:
            #print("Chatting...")
            data45=chat(query)
            return data45


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-voice', methods=['POST'])
def process_voice():
    data = request.json
    voice_input = data.get('voiceInput')
    chatResp=appMain(voice_input)
    # Generate speech from text
    # print("Test Main",chatResp)
    # tts = gTTS(chatResp)
    # audio_path = 'static/output.mp3'
    # tts.save(audio_path)
    # return jsonify({"audioPath": audio_path})
    return jsonify({"chatResp": chatResp})



if __name__ == '__main__':
    app.run(debug=True)

