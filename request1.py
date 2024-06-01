from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    # username = request.form
    # gender = request.form
    # hobbies = request.form
    # return render_template('result1.html',username = username, gender=gender , hobbies = hobbies)
    return render_template('result1.html', data=data)

if __name__ =='__main__' :
    app.run(debug=True)