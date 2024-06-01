from flask import *

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/about/<username>')
def message(username):
    return render_template('index.html', name=username)

@app.route('/embed/<int:num>')
def table(num):
    return render_template('embed.html',n=num)

if __name__ =='__main__' :
    app.run(debug=True)