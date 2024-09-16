import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Naramale@25",
    database="track_n_treat"
)



def insert_order_item(food_item,quantity,order_id):
    try:
        cursor= cnx.cursor()
        # Calling the stored procedure
        cursor.callproc('insert_order_item', (food_item, quantity, order_id))
        # Committing the changes
        cnx.commit()
        # Closing the cursor
        cursor.close()
        print("Order item inserted successfully!")
        return 1
    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")

        cnx.rollback()

    except Exception as e:
        print(f"An error occurred: {e}")

        cnx.rollback()

        return -1

def insert_order_tracking(order_id, status):
    cursor = cnx.cursor()

    # Inserting the record into the order_tracking table
    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (order_id, status))

    # Committing the changes
    cnx.commit()

    # Closing the cursor
    cursor.close()

def get_next_order_id():
    cursor = cnx.cursor()
    
    # Executing the SQL query to get the next available order_id
    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)
    
    # Fetching the result
    result = cursor.fetchone()[0]
    
    # Closing the cursor
    cursor.close()

    # Returning the next available order_id
    if result is None:
        return 1
    else:
        return result +1

def get_total_order_price(order_id):
    cursor = cnx.cursor()

    # Executing the SQL query to get the total order price
    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()[0]

    # Closing the cursor
    cursor.close()

    return result

# Function to fetch the order status from the order_tracking table
def get_order_status(order_id: int):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = ("SELECT status FROM order_tracking WHERE order_id = %s")
    cursor.execute(query,(order_id,))

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    if result is not None:
        return result[0]
    else:
        return None
