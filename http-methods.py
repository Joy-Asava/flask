from flask import *

app = Flask(__name__)

# @app.route('/login' , methods = ['POST'])
# def login():
#     uname=request.form['uname']
#     password=request.form['pass']
#     if uname == 'Joy' and password == 'trial':
#         return "Hello there %s"%uname

@app.route('/login',methods=['GET'])
def login():
    uname = request.args.get('uname')
    password = request.args.get('pass')
    if uname == 'jenny' and password =='camy':
        return "heyyyy,%s"%uname


if __name__ =='__main__' :
    app.run(debug=True)