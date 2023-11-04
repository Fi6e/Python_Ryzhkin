import json
import urllib.request

name = ""


def get_mess_data(text):
    data = {'name': name, 'text': text}
    data = json.dumps(data)
    data = str(data)
    return data.encode('utf-8')


def send(text):
    print("я: " + text)
    req = urllib.request.Request("http://localhost/", get_mess_data(text))
    fhand = urllib.request.urlopen(req)
    for line in fhand:
        print("сервер: " + line.decode('utf-8'))



send("Яка сьогодні погода?")
name = "Олександр"
send("Яке моє ім'я?")
send("Який сьогодні день?")
send("Який зараз час?")
send("Яка сьогодні погода?")
send("Тобі подобаються останні пісні SadSvit?")