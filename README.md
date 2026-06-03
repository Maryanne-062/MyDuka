sales_per_day -> select date(sales.created_at) as date, sum(sales.quantity * products.selling_price) as total_sales from sales join products on products.id = sales.pid group by date;

profit_per_day -> select date(sales.created_at) as date, sum(sales.quantity *( products.selling_price - products.buying_price)) as total_sales from sales join products on products.id = sales.pid group by date;

sales_per_product -> select products.name as p_name , sum(sales.quantity * products.selling_price) as total_sales from products join sales on sales.pid = products.id group by p_name;

profit_per_product -> select products.name as product_name , sum(sales.quantity *( products.selling_price - products.buying_price)) as total_sales from products join sales on sales.pid = products.id group by p_name;