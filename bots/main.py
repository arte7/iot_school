import json
import requests
import time


accessToken = "NjFjZTI0YTUtMWNlYi00MGNiLTg5NTQtYjU0NzFmMzUwYjlmZTM0NWY3MDktZTZk"
roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vODMzYzhiYTAtNTc1NS0xMWU4LTk1NDMtN2QxYzA5ZTViN2Ux"

headers = {"Authorization": "Bearer " + accessToken,
           "Content-Type": "application/json; charset=utf-8"}

while True:
    resp = requests.get("https://api.ciscospark.com/v1/messages?roomId=" + roomId + "&max=1",
                    headers=headers, verify=False)

    status = resp.status_code
    print("Requests status: " + str(status) + "\n")

    response_json = resp.json()

    print("Last messages in the room: " + json.dumps(response_json, indent=4))
    last_data = ""
    data = "bullshit"
    if status == 200:
        messages = response_json["items"]
        messages.reverse()

    for message in messages:

        if ("text" in message) & (data != last_data):

            if "start" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"ping"}'

            if "stop" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"Kill me, please!?"}'

            if "ping" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"pong"}'

            if "pong" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"ping"}'

            if "hello" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"Hello, how are you?"}'

            if "i'm fine. and you?" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"I\'m fine"}'

            if "how is the weather today?" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"It\'s wonderful, the sun is out and no clouds in the sky."}'

            if "personally, i find it a bit too warm." in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"That is true, I mean we are sitting in a school not at the beach."}'

            if "die" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"Ok!?"}'

            if (not ("Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MDY3NzViMy0yZjZjLTRhNmUtYmE5My01MzBhNGM2ZjRkZWU" in message["personId"])) | ("start" in message["text"].lower()):
                re = requests.post(
                "https://api.ciscospark.com/v1/messages",
                data,headers=headers, verify=False)
                print(headers)
                print(re)


            #if "Jaaaassssoooooon" in message["text"]:
            #    data = '{"roomId":"' + roomId + '","text":"Jason!?"}'
            #if "Jason" in message["text"]:
            #    data = '{"roomId":"' + roomId + '","text":"JAAAASSSOOOON!?"}'
            #if "JAAAASSSOOOON" in message["text"]:
            #    data = '{"roomId":"' + roomId + '","text":"Jaaaassssoooooon!?"}'

            #re = requests.post(
            #   "https://api.ciscospark.com/v1/messages",
            #    data, headers=headers, verify=False)


        last_data = data

    time.sleep(1)