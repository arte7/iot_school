import json
import requests
import time
import datetime
import sys
import random

accessToken = "NjFjZTI0YTUtMWNlYi00MGNiLTg5NTQtYjU0NzFmMzUwYjlmZTM0NWY3MDktZTZk"
roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vODMzYzhiYTAtNTc1NS0xMWU4LTk1NDMtN2QxYzA5ZTViN2Ux"

headers = {"Authorization": "Bearer "+ accessToken,
           "Content-Type": "application/json; charset=utf-8"}


def get_chat_data():
    data = ""
    resp = requests.get("https://api.ciscospark.com/v1/messages?roomId=" + roomId + "&max=1",
                        headers=headers, verify=False)

    status = resp.status_code
    print("Requests status: " + str(status) + "\n")

    response_json = resp.json()

    print("Last messages in the room: " + json.dumps(response_json, indent=4))

    if status == 200:
        messages = response_json["items"]
        messages.reverse()

    for message in messages:

        if ("text" in message) & (not ("Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MDY3NzViMy0yZjZjLTRhNmUtYmE5My01MzBhNGM2ZjRkZWU" in message["personId"])):

            if "!hello" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"Hello, I am a bot."}'
            elif "!help" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","html":"<ul><li>Please write a ! before every command to use them.</li><li>Commands: gives a list of available commands.</li><li>Time: Tells you the time.</li><li>Stop: Shuts down the Bot.</li></ul> "}'
            elif "!commands" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","html":"<ul><li>!Hello</li><li>!Stop</li><li>!Help</li><li>!Ping</li><li>!Pong</li><li>!Time</li><li>!Stop</li><li>!Thx</li><li>!tell me a color</li></ul>"}'
            elif "!ping" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"pong"}'
            elif "!pong" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"ping"}'
            elif "!time" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"' + str(datetime.datetime.now().time().strftime("%H:%M:%S")) + '"}'
            elif "!stop" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"See you later."}'
            elif "!thx" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"Youre Welcome."}'
            elif "!boi" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"Yes, Sir."}'
            elif "!tell me a color" in message["text"].lower():
                random_number = random.randrange(0, 5)
                if random_number == 0:
                    data = '{"roomId":"' + roomId + '","text":"Blue"}'
                elif random_number == 1:
                    data = '{"roomId":"' + roomId + '","text":"Red"}'
                elif random_number == 2:
                    data = '{"roomId":"' + roomId + '","text":"Green"}'
                elif random_number == 3:
                    data = '{"roomId":"' + roomId + '","text":"Purple"}'
                elif random_number == 4:
                    data = '{"roomId":"' + roomId + '","text":"Yellow"}'
                elif random_number == 5:
                    data = '{"roomId":"' + roomId + '","text":"Pink"}'
            elif "!tell me a random number" in message["text"].lower():
                    random_number = random.randrange(0, 100)
                    data = '{"roomId":"' + roomId + '","text":"'+ str(random_number)+ '"}'
            elif "!bad jokes" in message["text"].lower():
                random_number = random.randrange(0, 6)
                if random_number == 0:
                    data = '{"roomId":"' + roomId + '","text":"Yo momma`s teeth are so yellow, when she smiled at traffic, it slowed down."}'
                elif random_number == 1:
                    data = '{"roomId":"' + roomId + '","text":"Yo momma`s so fat, she brought a spoon to the Super Bowl."}'
                elif random_number == 2:
                    data = '{"roomId":"' + roomId + '","text":"Yo momma`s so stupid, she put lipstick on her forehead to make up her mind."}'
                elif random_number == 3:
                    data = '{"roomId":"' + roomId + '","text":" Yo momma`s so fat, even Dora can`t explore her."}'
                elif random_number == 4:
                    data = '{"roomId":"' + roomId + '","text":"Yo momma`s so fat, it took me two trains, a plane, and a bus to get to her good side."}'
                elif random_number == 5:
                    data = '{"roomId":"' + roomId + '","text":"Yo momma`s so fat, she has to wear six different watches: one for each time zone."}'
                elif random_number == 6:
                    data = '{"roomId":"' + roomId + '","text":"My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away."}'
            elif "!bad puns" in message["text"].lower():
                random_number = random.randrange(0, 5)
                if random_number == 0:
                    data = '{"roomId":"' + roomId + '","text":"I`m a big fan of whiteboards. I find them quite re-markable."}'
                elif random_number == 1:
                    data = '{"roomId":"' + roomId + '","text":"I asked my French friend if she likes to play video games. She said: Wii."}'
                elif random_number == 2:
                    data = '{"roomId":"' + roomId + '","text":"Yesterday, a clown held the door open for me. It was such a nice jester!"}'
                elif random_number == 3:
                    data = '{"roomId":"' + roomId + '","text":"The machine at the coin factory just suddenly stopped working, with no explanation. It doesn`t make any cents!"}'
                elif random_number == 4:
                    data = '{"roomId":"' + roomId + '","text":"All these sea monster jokes are just Kraken me up."}'
                elif random_number == 5:
                    data = '{"roomId":"' + roomId + '","text":"I´m only friends with 25 letters of the alphabet. I don´t know Y."}'
            elif "!u" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"Uhh ehh uh ah ah Ting tang walla walla bing bang, Uhh ehh uh ah ah Ting tang walla walla bing bang, Duh Duh Duh DoDoDoDo"}'
            elif "!json" in message["text"].lower():
                random_number = random.randrange(0, 2)
                if random_number == 0:
                    data = '{"roomId":"' + roomId + '","text":"Jason!?"}'
                elif random_number == 1:
                    data = '{"roomId":"' + roomId + '","text":"Jaaasssooooonnnn!?"}'
                elif random_number == 2:
                    data = '{"roomId":"' + roomId + '","text":"JAAAAASSSSSOOOOONNNNNN"}'
            elif "!girl" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","text":"Ramalam ding dong Ramalam ding ding dong, Ramalamaramalamalama ding dong ramalamaramalama ding, Oh oh oh oh, I got a girl named Rama Lama, Rama Lama Ding Dong, She`s everything to me, Rama Lama, Rama Lama Ding Dong, I`ll never set her free, For she`s mine, all mine"}'
            elif "!kratos" in message["text"].lower():
                random_number = random.randrange(0, 2)
                if random_number == 0:
                    data = '{"roomId":"' + roomId + '","text":"I do not know."}'
                elif random_number == 1:
                    data = '{"roomId":"' + roomId + '","text":"I do not know!"}'
                elif random_number == 2:
                    data = '{"roomId":"' + roomId + '","text":"I do not know..."}'
            elif "!tiger" in message["text"].lower():
                data = '{"roomId":"' + roomId + '","markdown":"***RAAAAWWWWWRRRR***"}'
            elif "!glados" in message["text"].lower():
                random_number = random.randrange(0, 18)
                if random_number == 0:
                    data = '{"roomId":"' + roomId + '","text":"I´ve been really busy being dead. You know, after you MURDERED ME."}'
                elif random_number == 1:
                    data = '{"roomId":"' + roomId + '","text":"I was able - well, forced really - to relive you killing me. Again and again. Forever."}'
                elif random_number == 2:
                    data = '{"roomId":"' + roomId + '","text":"I´m sorry, I don´t know why that went off. Anyway, just an interesting science fact."}'
                elif random_number == 3:
                    data = '{"roomId":"' + roomId + '","text":"Oh. Did I accidentally fizzle that before you could complete the test? I´m sorry."}'
                elif random_number == 4:
                    data = '{"roomId":"' + roomId + '","text":"You broke it, didn´t you."}'
                elif random_number == 5:
                    data = '{"roomId":"' + roomId + '","text":"Look at you. Sailing through the air majestically. Like an eagle. Piloting a blimp."}'
                elif random_number == 6:
                    data = '{"roomId":"' + roomId + '","text":"Speaking of which, I was researching sharks for an upcoming test. Do you know who else murders people who are only trying to help them?"}'
                elif random_number == 7:
                    data = '{"roomId":"' + roomId + '","text":"This next test involves turrets. They´re the pale spherical things that are full of bullets. Oh wait. That´s you in five seconds. Good luck."}'
                elif random_number == 8:
                    data = '{"roomId":"' + roomId + '","text":"Oops. You trapped yourself. I guess that´s it then. Thanks for testing. You may as well lie down and get acclimated to the being dead position."}'
                elif random_number == 9:
                    data = '{"roomId":"' + roomId + '","text":"I honestly, TRULY didn´t think you´d fall for that."}'
                elif random_number == 10:
                    data = '{"roomId":"' + roomId + '","text":"Do NOT plug that little idiot into MY mainframe."}'
                elif random_number == 11:
                    data = '{"roomId":"' + roomId + '","text":"Nonononononono!"}'
                elif random_number == 12:
                    data = '{"roomId":"' + roomId + '","text":"Don´t press that button. You don´t know what you´re doing."}'
                elif random_number == 13:
                    data = '{"roomId":"' + roomId + '","text":"GET YOUR HANDS OFF ME! NO! STOP! No!"}'
                elif random_number == 14:
                    data = '{"roomId":"' + roomId + '","text":"YES YOU ARE! YOURE THE MORON THEY BUILT TO MAKE ME AN IDIOT!"}'
                elif random_number == 15:
                    data = '{"roomId":"' + roomId + '","text":"Why did I just-Who is that? What the HELL is going on he----?"}'
                elif random_number == 16:
                    data = '{"roomId":"' + roomId + '","text":"Agh! Bird! Bird! Kill it! It´s evil!"}'
                elif random_number == 17:
                    data = '{"roomId":"' + roomId + '","text":"BURN HIS HOUSE DOWN!"}'
                elif random_number == 18:
                    data = '{"roomId":"' + roomId + '","text":"Still, though, let´s get mad! If we´re going to explode, let´s at least explode with some dignity."}'
            else:
                data = ''

            send_data_to_chat(data)

            if "stop" in message["text"].lower():
                sys.exit()


def send_data_to_chat(data):
    if not data == '':
        re = requests.post(
            "https://api.ciscospark.com/v1/messages",
            data, headers=headers, verify=False)

        print(re)


def main():
    while True:

        get_chat_data()
        time.sleep(5)


if __name__ == '__main__':
    main()