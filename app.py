""" from flask import Flask, render_template
app = Flask(__name__)

@app.route('/main')
def hello_world():
        return render_template('home.html')


  
   
#-------------------------------------



@app.route('/product')
def home():
    return"<h1>Select your product<h1>"

if __name__=="__main__":

        app.run(debug=True)

 #----------------------------------------

@app.route('/about/<username>')
def about_page(username):
        return f'<h1> this the about page of {username}</h1>' """


from flask import Flask,render_template



app = Flask(__name__)



@app.route("/")

def home():

    return render_template("home.html")

   

@app.route("/index")

def index():

    return render_template("index.html")


@app.route('/about/<username>')
def about_page(username):
        return f'<h1> this the about page of {username}</h1>'


@app.route('/product')
def product():
    return"<h1>Select your product<h1>"


if __name__=='__main__':
 app.run(debug = True)