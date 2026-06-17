from flask import Flask, render_template,request,redirect,url_for,flash
from database import get_products,get_sales,get_stock,insert_products,check_available_stock,insert_sales,check_user_exists,create_user
from flask_bcrypt import Bcrypt


app= Flask(__name__)

bcrypt = Bcrypt(app)

app.secret_key= '78cbn88enhcucbhd99njsnns'

@app.route('/')
def home():
    name="Jack"
    return render_template("index.html", name=name)

@app.route('/products')
def products():
    products_data=get_products()
    return render_template("products.html",products_data=products_data)

@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']

        new_product = (product_name,buying_price,selling_price)
        insert_products(new_product)
        flash("Product added successfully",'success') 

    return redirect(url_for('products'))

@app.route('/sales')
def sales():
    sales=get_sales()
    products=get_products()
    return render_template("sales.html",sales=sales,products=products)

@app.route('/make_sale',methods=['GET','POST'])
def make_sale():
    if request.method == 'POST':
        pid = request.form['pid']
        quantity = request.form['quantity']

        new_sale = (pid,quantity)
        available_stock = check_available_stock(pid)

        if available_stock < float(quantity):
            flash("Insufficient stock,add more",'danger')
            return redirect(url_for('sales'))

        insert_sales(new_sale)
        flash("Sale added successfully",'success')
    return redirect(url_for('sales'))

@app.route('/stock')
def stock():
    stock=get_stock
    products=get_products
    return render_template("stock.html",stock=stock,products=products)

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/register')
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone_number = request.form['phone']
        password = request.form['password']

        existing_user = check_user_exists(email)
        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = (full_name,email,phone_number,hashed_password)
            create_user(new_user)
            flash("User created successfully",'success')
            return redirect(url_for('login'))
        else:
            flash("User already exists,please login instead",'danger')

    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")

app.run()