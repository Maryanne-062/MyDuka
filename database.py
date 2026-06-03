import psycopg2

#establishing the connection
conn=psycopg2.connect(host="localhost",database="myduka",user="postgres",password="mng_2006")

#creates a cursor object to interact with the database
cur = conn.cursor()

cur.execute("select * from products")
products_data=cur.fetchall()
print(products_data)

cur.execute("select * from sales")
sales_data=cur.fetchall()
print(sales_data)

cur.execute("insert into products(name, buying_price, selling_price) values('äir fryer',4000,5500)")
conn.commit()

print(products_data)

def insert_product(values):
    #cur.execute(f"insert into products(name, buying_price, selling_price) values{values}")
    cur.execute("insert into products(name, buying_price, selling_price) values(%s,%s,%s)",values)
    conn.commit()

product1=("LG TV", 40000, 50000)
product2=("Samsung TV", 35000, 45000)

insert_product(product1)
insert_product(product2)