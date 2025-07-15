import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Запускаем сервер
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print(f"Сервер запущен по адресу: http://localhost:{PORT}/index.html")
    # Открываем страницу в браузере
    webbrowser.open(f"http://localhost:{PORT}/index.html")
    # Запускаем сервер в бесконечном режиме
    httpd.serve_forever()