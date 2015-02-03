import sqlite3
from flask import Flask, request, redirect, url_for

app = Flask(__name__)
dbFile = 'db1.db'
conn = None

def get_conn():
    global conn
    if conn is None:
        conn = sqlite3.connect(dbFile)
        conn.row_factory = sqlite3.Row
    return conn

@app.teardown_appcontext
def clode_connection(exception):
    global conn
    if conn is not None:
        conn.close()
        conn = None

def query_db(query, args=(), one=False):
    cur = get_conn().cursor()
    cur.execute(query, args)
    r = cur.fetchall()
    cur.close()
    return (r[0] if r else None) if one else r

def add_task(category):
    query_db('insert into tasks(category) values(?)',[category], one=True)
    get_conn().commit()

@app.route('/')
def welcom():
    return '<h1>Welcome to Flask lab</h1>'

@app.route('/task', methods = ['GET', 'POST'])
def task():
    #POST:
    if request.method == 'POST':
        category = request.form['category']
        add_task(category)
        #return redirect('/task1')
        return redirect(url_for('task'))
    #GET:
    resp = ''
    resp = resp + '''
    <form action = "" method = post>
        <p>Category<input type=text name=category></p>
        <p><input type = submit value=Add></p>
    </form>
    '''

    #Show table
    resp = resp + '''
    <table border = "1" cellpadding="3">
        <tbody>
            <tr>
                <th>Category</th>
            </tr>
    '''

    for task in query_db('select * from tasks'):
        resp = resp + "<tr><td>%s</td></tr>" %(task['category'])
    resp = resp + '</tbody></table>'

    return resp
    

if __name__ == '__main__':
    app.debug = True;
    app.run()
