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
    # except db.OperationalError:
    #     print("Something is wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
    except:
        print("Something went wrong!")
    disconnect_db(conn, cursor)
    return new_item
