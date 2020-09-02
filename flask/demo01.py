from flask import Flask

app = Flask(__name__)

@app.route('/')
def hell0_world():
    return "hello_world"

if __name__ == '__main__':
    app.run(debug="true")
