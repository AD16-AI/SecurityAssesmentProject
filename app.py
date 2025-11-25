from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/logout')
def logout():
    return render_template('home.html')

username="admin"
password="Abc@1234"

@app.route('/loginsubmit',methods = ["GET","POST"])
def loginsubmit():
    message = ""
    if request.method =="POST": 
       usernm = request.form["username"]
       passwd = request.form["password"]

       if usernm == username and passwd == password:
           return render_template('newhomepage.html')
       else:
           message = "Incorrect username and password!!"

if __name__ == '__main__':
    app.run(debug=True)
