from wsgiref.simple_server import make_server
from example import app

def server(wsgi_app):
    serverd = make_server('', 8000, wsgi_app)
    print("Server started on :8000...")
    serverd.serve_forever()


if __name__ == '__main__':
    server(app)
