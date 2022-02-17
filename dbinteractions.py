import mariadb as db
import dbcreds


def connect_db():
    conn = None
    cursor = None
    try:
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except:
        print("Something went wrong!")
    return conn, cursor


def disconnect_db(conn, cursor):
    try:
        cursor.close()
    except:
        print("The issue with cursor")
    try:
        conn.close()
    except:
        print("The issue with connection")


def list_all_items():
    items = []
    conn, cursor = connect_db()
    try:
        cursor.execute(
            "select name, description, quantity, created_at from item i")
        items = cursor.fetchall()
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
    except:
        print("Something went wrong!")
    disconnect_db(conn, cursor)
    return items


def add_new_item(name, description, quantity):
    new_item = None
    conn, cursor = connect_db()
    try:
        cursor.execute(
            "insert into item(name, description, quantity) values(?, ?, ?)", [name, description, quantity, ])
        conn.commit()
        if(cursor.rowcount == 1):
            new_item = True
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
    except:
        print("Something went wrong!")
    disconnect_db(conn, cursor)
    return new_item


def update_item(item_id):
    success = None
    conn, cursor = connect_db()
    try:
        cursor.execute(
            "update item set quantity = quantity - 1 where id = ?", [item_id])
        conn.commit()
        if(cursor.rowcount == 1):
            success = True
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
    except:
        print("Something went wrong!")
    disconnect_db(conn, cursor)
    return success


def delete_item(item_id):
    success = None
    conn, cursor = connect_db()
    try:
        cursor.execute(
            "delete from item where id = ?", [item_id])
        conn.commit()
        if(cursor.rowcount == 1):
            success = True
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
    except:
        print("Something went wrong!")
    disconnect_db(conn, cursor)
    return success


def get_employee(employee_id):
    employee = None
    conn, cursor = connect_db()
    try:
        cursor.execute(
            "select name, hired_at, hourly_wage from employee e where id = ?", [employee_id])
        employee = cursor.fetchone()
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
    except:
        print("Something went wrong!")
    disconnect_db(conn, cursor)
    return employee


def add_new_employee(name, hourly_wage):
    new_employee = None
    conn, cursor = connect_db()
    try:
        cursor.execute(
            "insert into employee(name, hourly_wage) values(?, ?)", [name, hourly_wage])
        conn.commit()
        if(cursor.rowcount == 1):
            new_employee = True
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
    except:
        print("Something went wrong!")
    disconnect_db(conn, cursor)
    return new_employee
