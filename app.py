
from datetime import datetime
from flask import Flask, render_template, request, flash, url_for, redirect

# ...
DATAS  =  [
        {   
            "id":"952ca0e8-d9eb-4624-94aa-0f74b6331956",
            "title":"Titre  1",
            "content":"Contenu  1",
            "category":"ecole",
        },
        {   
            "id":"fe85ef10-9bda-4869-b609-6d603eb18847",
            "title":"Titre  2",
            "content":"Contenu  2",
            "category":"travail",
        },
        {   
            "id":"881479b1-8b08-425b-add6-db1899acb259",
            "title":"Titre  3",
            "content":"Contenu  4",
            "category":"maison",
        } 
     
     ] 

def search_to_do(id):
    for data in DATAS:
        if id == data["id"]:
            return data

def delete_todo():
    for data in DATAS:
        if id ==data["id"]:
            del data["id"] 
            return data          

app = Flask(__name__)
app.config['SECRET_KEY'] = '03237566636ed31610a390d4f455d949045b5d2323363317'



@app.route("/")
def liste():
    now = datetime.now() # current date and time
    date_time = now.strftime("%d/%m/%Y")

    return render_template('table.html', date_time=date_time, data=DATAS)

@app.route('/create/', methods=('GET', 'POST'))
def create():

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        elif not category:
            flash('catégory non saisi')   
        else:
            DATAS.append({'title': title, 'content': content,'category' : category})
            return redirect(url_for('liste'))

    now = datetime.now() # current date and time
    date_time = now.strftime("%d/%m/%Y")        
        
        

    return render_template('add.html')

@app.route('/edit/<id>', methods=('GET', 'POST')) 
def edit(id):
    print(search_to_do(id))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']

    if request.method == 'GET':
        title = request.args['title']
        content = request.args['content']
        category = request.args['category']

        return render_template('edit.html', onedata = search_to_do(id))

