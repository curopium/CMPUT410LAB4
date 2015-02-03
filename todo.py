from flask import Flask, request, redirect, url_for
app = Flask(__name__)

tasks = []

@app.route('/')
def welcome():
    return '<h1>Welcome to 410 - Flask lab!</h1>'
   
@app.route('/task1', methods = ['GET', 'POST'])
def task():
    #POST
    if request.method == 'POST':
        category = request.form['category']
        tasks.append({'category':category})
        #return redirect('/task1')
        return redirect(url_for('task'))

    #GET
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

    for task in tasks:
        resp = resp + "<tr><td>%s</td></tr>" %(task['category'])
    resp = resp + '</tbody></table>'

    return resp
    
if __name__ == '__main__':
    app.run()
