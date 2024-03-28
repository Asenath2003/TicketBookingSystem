import pyodbc

def get_db_connection():
    try:
        connection = pyodbc.connect('Driver={SQL Server};'
                                    'Server=LAPTOP-LOUFODEH\SQLEXPRESS;'
                                    'Database=TicketBookingSystem;'
                                    'Trusted_Connection=yes;')
        print("Connected to the database")
        return connection
    except pyodbc.Error as err:
        print(f"Error: {err}")
        return None

def get_ids(table_name, id_column_name):
    mydb = get_db_connection()
    my_cursor = mydb.cursor()
    sql = 'SELECT TOP 1 ' + id_column_name + ' FROM ' + table_name + ' ORDER BY ' + id_column_name + ' DESC'
    my_cursor.execute(sql)
    x = my_cursor.fetchone()
    if x:
        return int(x[0]) + 1
    else:
        return 1

def get_cnts(table_name, id_column_name, column_id):
    mydb = get_db_connection()
    my_cursor = mydb.cursor()
    sql = 'SELECT count(*) as count FROM ' + table_name + ' WHERE ' + id_column_name + '=' + str(column_id)
    my_cursor.execute(sql)
    x = my_cursor.fetchone()
    if x:
        return int(x[0])
    else:
        return 0

def get_counts(table_name, id_column_name1, id_column_name2, column_id1, column_id2):
    mydb = get_db_connection()
    my_cursor = mydb.cursor()
    sql = 'SELECT count(*) as count FROM ' + table_name + ' WHERE ' + id_column_name1 + '=' + str(column_id1) + ' AND ' + id_column_name2 + '=' + "'" + str(column_id2) + "'"
    my_cursor.execute(sql)
    x = my_cursor.fetchone()
    if x:
        return int(x[0])
    else:
        return 0
