select * 
, row_number() over(PARTITION by ordernumber,ordertotal, orderdate order by orderdate) as row_numbr
from customer_orders_table
where ordernumber is null
