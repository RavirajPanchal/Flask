from flask import Flask, render_template



app = Flask(__name__)



@app.route('/main')

def hello_world():

    return render_template('index.html')



   




@app.route('/product')



def home():

    return"<h1>Select your product<h1>"



if __name__=="__main__":

        app.run(debug=True)