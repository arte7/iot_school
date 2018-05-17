import thingspeak
import requests
import json
import time


accessToken = "NmFjOWViZWYtMTZjMy00Y2UxLWI3YmMtMTVkMzg2OTNhM2YyZmZiN2NhMGQtZTc2"
dataroomId = "Y2lzY29zcGFyazovL3VzL1JPT00vNGUyNjE1MjAtNTkwNC0xMWU4LWIwYTEtNmI0Y2M0NzNkZDVj"
chatroomId = "Y2lzY29zcGFyazovL3VzL1JPT00vODMzYzhiYTAtNTc1NS0xMWU4LTk1NDMtN2QxYzA5ZTViN2Ux"
url = "https://api.ciscospark.com/v1/messages"
channel_id = 496768
write_key = "PZVVZFO8R5YJY0D7"
read_key = "MO17791BOVEODHFV"
headers = {"Authorization": "Bearer " + accessToken, "Content-Type": "application/json; charset=utf-8"}

def send_average():

    lastchatentry = requests.get(url+"?roomId="+chatroomId+"&max=1", headers=headers)
    entrytext = lastchatentry.json()['items'][0]['text']
    print(entrytext)
    if "Die Daten Temperatur" in entrytext:
        data = get_average()
        send_message(data)
        send_raw_data(data)

    elif entrytext == "!tempt":
        data = get_average()
        send_message(data)
        send_raw_data(data)


def get_average():

    connect = thingspeak.Channel(id=channel_id, write_key=write_key, api_key=read_key)
    temp = connect.get({"average": "daily"})
    data = json.loads(temp)['feeds'][0]
    return data


def send_message(data):
    text = '{"html":"Die Durchschnittstemperatur betr&auml;gt ' \
           + data['field1'] \
           + ' &deg;C und die Durchschnittsluftfeuchtigkeit betr&auml;gt ' \
           + data['field2'] \
           + ' %", "roomId": "'\
           + chatroomId \
           + '"}'

    req = requests.post(url, data=text, headers=headers)

    print(str(req.status_code) + " " + str(req.reason))


def send_raw_data(data):
    data = {
        'roomId': str(dataroomId),
        'accessToken': str(accessToken),
        'text': '{"avgTemperature": ' + data['field1'] + ', "avgHumidity": ' + data['field2'] + '}'
    }
    print(data)

    req = requests.post(url, json=data, headers=headers)
    print(str(req.status_code) + " " + str(req.reason))
    print(req.text)

def main():
    while True:
        send_average()
        time.sleep(1)


if __name__ == '__main__':
    main()
