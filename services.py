import sqlite3

connect = sqlite3.connect('sql.db', check_same_thread=False)
cursor = connect.cursor()


def get_log(user_id):
    sql = f"SELECT * FROM log where user_id={user_id}"
    return cursor.execute(sql).fetchone()


def create_log(user_id):
    state = {'state': 0}
    sql = f"""INSERT into Log(menu, user_id, log) VALUES({0}, {user_id}, "{state}")"""
    cursor.execute(sql)
    connect.commit()
    return get_log(user_id)


def update_log(user_id, log):
    sql = f"""UPDATE Log SET log="{log}" where user_id={user_id}"""
    cursor.execute(sql)
    connect.commit()


def update_menu(user_id, menu):
    sql = f"""UPDATE Log SET menu={menu} where user_id={user_id}"""
    cursor.execute(sql)
    connect.commit()


def clear_log(user_id, menu):
    state = {'state': 0}
    sql = f"""UPDATE Log SET menu={menu}, user_id={user_id}, log="{state}" where user_id={user_id}"""
    cursor.execute(sql)
    connect.commit()

