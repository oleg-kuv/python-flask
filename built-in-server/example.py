from datetime import datetime

def app(environ, start_response):
    time = datetime.now()
    data = bytes(f'Текущее время {time:%H:%M:%S}', 'utf-8')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return [data]
