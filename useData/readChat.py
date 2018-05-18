import requests
import time
import thingspeak
import json


accessToken = "TOKEN_USER_1"
dataroomId = "ROOM_ID_ROOM_1"
chatroomId = "ROOM_ID_ROOM_2"
url = "https://api.ciscospark.com/v1"
headers = {"Authorization": "Bearer " + accessToken, "Content-Type": "application/json; charset=utf-8"}
user = "USER_ID_USER_1"
channel_id = "THINGSPEAK_CHANNEL_ID_ALS_INT"
write_key = "THINGSPEAK_WRITE_KEY"
read_key = "THINGSPEAK_READ_KEY"


def get_messages():

    status = 200

    oldresp = {}

    while status == 200:
        resp = requests.get(url + "/messages?roomId=" + dataroomId + "&max=1", headers=headers, verify=False)

        status = resp.status_code
        print("Request status: " + str(status) + "\n")

        response_json = resp.json()

        obj = response_json['items'][0]
        text = obj['text']

        print(text)

        if ("Temperature" in text) & ("Humidity" in text) & (obj['personId'] != user):

            if oldresp == {}:
                write_to_db(obj)
            elif obj['created'] != oldresp['created']:
                write_to_db(obj)

            oldresp = resp.json()['items'][0]

        time.sleep(10)


def write_to_db(obj):

    # holen der daten aus dem String
    text = json.loads(obj['text'])
    data = '{"html": "Die Daten Temperatur: ' + str(text['Temperature']) + ' &deg;C  und Luftfeuchtigkeit: ' \
           + str(text['Humidity']) + '% wurden &uuml;bermittlet", "roomId": "'+chatroomId+'"}'

    channel = thingspeak.Channel(id=channel_id, write_key=write_key, api_key=read_key)
    tsresponse = channel.update({'field1': text['Temperature'], 'field2': text['Humidity']})

    read = channel.get({})
    print("Read: ", read)

    iswritten = requests.post(url+"/messages", data=data, headers=headers)

    if iswritten.status_code != 200:
        print("Fehler beim Update Benachrichtigung senden " + iswritten.status_code + iswritten.text)


def main():
    get_messages()


if __name__ == '__main__':
    main()
