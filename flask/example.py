from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.get('/users')
def users_get():
    return 'GET /users'

@app.post('/users')
def users_post():
    return 'POST /users'

app.run(host='0.0.0.0', port=8000)
