import psycopg2

#establishing the connection
conn=psycopg2.connect(host="localhost",database="myduka",user="postgres",password="mng_2006")

#creates a cursor object to interact with the database
cur = conn.cursor()

def get_products():
    cur.execute("select * from products")
    products_data=cur.fetchall()
    return products_data

def get_sales():
    cur.execute("select * from sales")
    sales_data=cur.fetchall()
    return sales_data

def get_stock():
    cur.execute("select * from stock")
    stock_data=cur.fetchall()
    return stock_data

def insert_sales(values):
    cur.execute("insert into sales(pid, quantity) values(%s,%s)", values)
    conn.commit()

sale1=(1, 2)
sale2=(2, 1)
insert_sales(sale1)
insert_sales(sale2)

def insert_stock(values):
    cur.execute("insert into stock(pid, stock_quantity) values(%s,%s)", values)
    conn.commit()

stock1=(1, 10)
stock2=(2, 5)
insert_stock(stock1)
insert_stock(stock2)

#cur.execute("insert into products(name, buying_price, selling_price) values('äir fryer',4000,5500)")
#conn.commit()
#print(products_data)

def insert_product(values):
    #cur.execute(f"insert into products(name, buying_price, selling_price) values{values}")
    cur.execute("insert into products(name, buying_price, selling_price) values(%s,%s,%s)",values)
    conn.commit()

product1=("LG TV", 40000, 50000)
product2=("Samsung TV", 35000, 45000)

insert_product(product1)
insert_product(product2)

# User input to add a new product
def sales_per_day():
    cur.execute("""
    SELECT DATE(sales.created_at) AS date, 
           SUM(sales.quantity * products.buying_price) AS total_sales 
    FROM sales 
    JOIN products ON products.id = sales.pid 
    GROUP BY date;
""")
    daily_sales = cur.fetchall()
    return daily_sales

def profit_per_day():
    cur.execute("""
    SELECT DATE(sales.created_at) AS date, 
           SUM(sales.quantity * (products.selling_price - products.buying_price)) AS total_profit 
    FROM products
    JOIN sales ON sales.pid = products.id 
    GROUP BY date;
""")
    daily_profit = cur.fetchall()
    return daily_profit

def sales_per_product():
    cur.execute("""
    select products.name as p_name ,
        sum(sales.quantity * products.selling_price) as total_sales 
        from products join sales on sales.pid = products.id 
        group by p_name;
""")
    product_sales = cur.fetchall()
    return product_sales

def profit_per_product():
    cur.execute("""
    select products.name as p_name ,
    sum(sales.quantity *( products.selling_price - products.buying_price)) as total_sales
    from products join sales on sales.pid = products.id 
    group by p_name;
""")
    product_profit = cur.fetchall()
    return product_profit