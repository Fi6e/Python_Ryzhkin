import datetime
import json
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

class HttpGetHandler(BaseHTTPRequestHandler):
    name = ''

    def do_POST(self):
        result = ""
        self.send_response(200)
        self.send_header("Content-type", "text")

        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        post_data_str = post_body.decode('utf-8')
        post_data_dict = json.loads(post_data_str)

        if post_data_dict.get("name") != "":
            self.name = post_data_dict.get("name")
        elif self.name == "":
            result = "Будь ласка, скажіть мені ваше ім'я. "

        if post_data_dict.get("text") and self.name != "":
            text = post_data_dict.get("text")
            if text == "Яке моє ім'я?":
                if self.name == "":
                    result = "Я не знаю."
                else:
                    result = self.name
            elif text == "Який сьогодні день?":
                result = str(datetime.date.today())
            elif text == "Який зараз час?":
                result = str(datetime.datetime.now().strftime("%H:%M"))
            elif text == "Яка сьогодні погода?":
                result = "Дуже тепла"
            elif text == "Тобі подобаються останні пісні SadSvit?":
                result = "Дуже!"

        self.end_headers()
        self.wfile.write(result.encode())

server_address = ('', 80)
httpd = HTTPServer(server_address, HttpGetHandler)
print('Python HTTP сервер очікує на з/єднання')
httpd.serve_forever()
