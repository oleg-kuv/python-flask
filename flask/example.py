from flask import Flask,request,make_response,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    print(request.headers)
    return 'Hello from Flask!'

@app.route('/courses/')
def courses_handler():
    courses = ['course1', 'course2', 'course3']

    return render_template(
        'courses/show.html',
        courses=courses
    )


@app.get('/users')
def users_get():
    print(request.headers)
    return 'GET /users'

@app.post('/users')
def users_post():
    print(request.headers)
    return 'POST /users'

@app.route('/json/')
def json():
    return {'json': 42}

@app.route('/members')
def members():
    response = make_response('members')
    response.headers['location']='/users'
    response.status_code = 302

    return response

app.run(host='0.0.0.0', port=8000)
