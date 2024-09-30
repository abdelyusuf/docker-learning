from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def hello_world():
    return 'Hello, World! Welcome to the Flask-Redis app.'

@app.route('/count')
def count():
    visit_count = r.incr('visit_count')
    return f'Visit count: {visit_count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
