import requests
import time
import thingspeak


accessToken = "NmFjOWViZWYtMTZjMy00Y2UxLWI3YmMtMTVkMzg2OTNhM2YyZmZiN2NhMGQtZTc2"
roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vODMzYzhiYTAtNTc1NS0xMWU4LTk1NDMtN2QxYzA5ZTViN2Ux"
url = "https://api.ciscospark.com/v1"
headers = {"Authorization": "Bearer " + accessToken, "Content-Type": "application/json; charset=utf-8"}


def get_messages():

    status = 200

    oldresp = {}

    while status == 200:
        resp = requests.get(url + "/messages?roomId=" + roomId + "&max=1", headers=headers, verify=False)

        status = resp.status_code
        print("Request status: " + str(status) + "\n")

        response_json = resp.json()

        obj = response_json['items'][0]
        text = obj['text']

        print(text)

        if ("Temperature" in text) & ("Humidity" in text) & (obj['personId'] != "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85MWUyNGRjMC0yMjE1LTQ2ZDMtYTE0Yi01MTBmYTgyZDM1NTE"):

            if oldresp == {}:
                write_to_db(obj)
            elif obj['created'] != oldresp['created']:
                write_to_db(obj)

            oldresp = resp.json()['items'][0]

        time.sleep(10)


def write_to_db(obj):

    # holen der daten aus dem String
    text = str(obj['text']).split()

    data = '{"text": "Die Daten '+obj['text']+' wurden übermittlet", "roomId": "'+roomId+'"}'

    channel_id = 496768
    write_key = "PZVVZFO8R5YJY0D7"
    read_key = "MO17791BOVEODHFV"

    channel = thingspeak.Channel(id=channel_id, write_key=write_key, api_key=read_key)
    tsresponse = channel.update({'field1': text[1], 'field2': text[3]})

    read = channel.get({})
    print("Read: ", read)


    iswritten = requests.post(url+"/messages", data=data, headers=headers)

    print(iswritten.status_code)
    if iswritten.status_code != 200:
        print("Fail")


def main():
    get_messages()


if __name__ == '__main__':
    main()
