create TABLE customer_shipping_table(ordernumber int, customer_state varchar(50));
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;
select * from customer_orders_table
select * from customer_shipping_table

/*Terminal command 
.mode csv
.separator ","
.import shipping_data.csv customer_shipping_table