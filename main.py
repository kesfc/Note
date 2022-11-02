from flask import Flask
from flask import request

app = Flask(__name__)
#post: enables users to send HTML form data to server
#get: to request data from the server.
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username']=='kevin' and request.form['password']=='kevin00':
        return '<h3>Hello, kevin!</h3>'
    elif request.form['username']!='kevin':
        return '<h3>Username incorrect<h3>'
    else:
        return '<h3>Password incorrect</h3>'

if __name__ == '__main__':
    app.run()