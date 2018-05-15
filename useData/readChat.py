import json
import requests
import time
import mysql.connector


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

        if ("temperature" in text) & ("humidity" in text):
            print("temp")

            if oldresp == {}:
                write_to_db(obj)
            elif obj['created'] != oldresp['created']:
                write_to_db(obj)

            oldresp = resp.json()['items'][0]
            print(oldresp)

        time.sleep(10)


def write_to_db(obj):
    print("nothing")
    text = ""
    data = '{"text": "Die Daten '+text+' wurden in die DB geschrieben", "roomId": "'+roomId+'"}'

    # ------------

    connect = mysql.connector.connect(user='root', host='127.0.0.1', database='projekt')
    cursor = connect.cursor()

    add_data = ("INSERT INTO clima_data (humidity,temperature) VALUES (%(humidity)s,%(temperature)s)")

    obj_data = {
        'humidity': "12",
        'temperature': "13"
    }

    cursor.execute(add_data, obj_data)

    emp_no = cursor.lastrowid

    connect.commit()
    cursor.close()
    connect.close()

    # ------------

    print (data)
    iswritten = requests.post(url+"/messages", data=data, headers=headers)

    print (iswritten)
    if iswritten.status_code != 200:
        print("Fail")


def main():
    get_messages()


if __name__ == '__main__':
    main()
