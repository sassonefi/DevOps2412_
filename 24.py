from flask import Flask
app = Flask("moshe")

@app.route('/')
def hello_world():
    a = 5
    b = 10
    return str(a + b)

app.run(host='127.0.0.1', port="8080")