from flask import Flask

app= Flask(__name__)

@app.route('/')
def home():
    return "Hello World , this is home"

@app.route('/products')
def products():
    return "Products section"

@app.route('/sales')
def sales():
    return "Sales section"

@app.route('/stock')
def stock():
    return [1,2,3,4]


app.run()