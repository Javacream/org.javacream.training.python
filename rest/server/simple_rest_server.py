from flask import Flask
import datetime 

app = Flask(__name__)
@app.route('/echo/<message>', methods=['GET'])
def echo(message):
    print(message)
    return message

@app.route('/echo', methods=['POST'])
def say_hello():
    print("saying hello")
    return "Hello " + str(datetime.datetime.now()) 


app.run(port=5000)