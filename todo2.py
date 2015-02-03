import sqlite3
dbFile = 'db1.db'
conn = None

def get_conn():
    global conn
    if conn is None:
        conn = sqlite3.connect(dbFile)
        conn.row_factory = sqlite3.Row
    return conn

def clode_connection():
    global conn
    if conn is not None:
        conn.close()

def query_db(query, args=(), one=False):
    cur = get_conn().cursor()
    cur.execute(query, args)
    r = cur.fetchall()
    cur.close()
    return (r[0] if r else None) if one else r

def add_task(catagory):
    query_db('insert into tasks(category) values(?)',['category'], one=True)
    get_conn().commit()

def print_tasks():
    tasks = query_db('select * from tasks')
    for task in tasks:
        print("Task(category): %s " %task['category'])
    print ("%d tasks in total. " %len(tasks))

if __name__ == '__main__':
    query_db('delete from tasks')
    print_tasks()
    add_task('Shopping')
    add_task('Friends')
    add_task('Tv')
    print_tasks()
