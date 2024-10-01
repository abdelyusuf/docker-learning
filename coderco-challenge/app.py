from flask import Flask, render_template_string, request
import redis

app = Flask(__name__)

# Connect to Redis (assuming Redis is running in another container called 'myredis')
redis_client = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

# HTML template for the welcome page (embedded in app.py using render_template_string)
welcome_page = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Abdel Yusuf's Website</title>
</head>
<body>
    <h1>Welcome to Abdel Yusuf's Website!</h1>
    <p>Please enter your name below:</p>
    
    <form action="/greet" method="POST">
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
'''

# HTML template for the greeting page (embedded in app.py using render_template_string)
greeting_page = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Greeting</title>
</head>
<body>
    <h1>Hello, {{ name }}! Welcome to Abdel Yusuf's Website!</h1>
    <p>We are currently connected to Redis. Your visit count is: {{ visit_count }}</p>
</body>
</html>
'''

@app.route('/')
def welcome():
    # Welcome page with a form for user input
    return render_template_string(welcome_page)

@app.route('/greet', methods=['POST'])
def greet():
    # Get the user's name from the form
    name = request.form['name']

    # Increment the visit count in Redis
    visit_count = redis_client.incr('visit_count')

    # Render the greeting page with the user's name and visit count from Redis
    return render_template_string(greeting_page, name=name, visit_count=visit_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)


