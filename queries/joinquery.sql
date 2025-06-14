select co.*,
cs.customer_state
from customer_orders_table as co
INNER JOIN customer_shipping_table as cs on co.ordernumber=cs.ordernumber
