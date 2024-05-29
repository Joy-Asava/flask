from flask import Flask,url_for,redirect #import the class

app = Flask(__name__)#create an instance of the class


@app.route('/')#decorater defines the route
def hello():
    return "<h1>Hello World</h1>"
@app.route('/about')
def about():
    return "<h1>About Us</h1>"

#Variable Rules:
@app.route('/user/<username>')
def showuser(username):
    return f'Good Afternooon , My name is {username}'
#pass int:
@app.route('/user/<int:user_id>')
def showid(user_id):
    return f'My user_id is {user_id}'

#add Url rule()
def profile():
    return "This is my profile"
app.add_url_rule('/profile',"profile",profile)

#Building Urls:
#url for() ..dynamic building
@app.route('/director')
def director():
    return "<h1>director</h1>"

@app.route('/student')
def student():
    return "<h1>student</h1>"

@app.route('/teacher')
def teacher():
    return "<h1>teacher</h1>"

@app.route('/personel/<name>')
def personel(name):
    if name == 'director':
        return redirect(url_for('director'))
    if name == 'teacher':
        return redirect(url_for('teacher'))
    if name == 'student':
        return redirect(url_for('student'))

if __name__ =='__main__' :
    app.run(debug=True)