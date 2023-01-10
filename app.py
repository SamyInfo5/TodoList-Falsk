
from datetime import datetime
from flask import Flask, render_template, request, flash, url_for, redirect
import uuid

now = datetime.now() # current date and time
date_time = now.strftime("%d/%m/%Y")

# ...
DATAS  =  [
        {   
            "id":"952ca0e8-d9eb-4624-94aa-0f74b6331956",
            "title":"Titre  1",
            "content":"Contenu  1",
            "category":"ecole",
            "edit_date":date_time,
        },
        {   
            "id":"fe85ef10-9bda-4869-b609-6d603eb18847",
            "title":"Titre  2",
            "content":"Contenu  2",
            "category":"travail",
            "edit_date":date_time,
        },
        {   
            "id":"881479b1-8b08-425b-add6-db1899acb259",
            "title":"Titre  3",
            "content":"Contenu  4",
            "category":"maison",
            "edit_date":date_time,
        } 
     
     ] 

def search_to_do(id):
    for data in DATAS:
        if id == data["id"]:
            return data

def delete_todo(id):
    for data in DATAS:
        if id ==data["id"]:
            DATAS.remove(data)    
            return True

def edit_toDo(id,title,content,category):
    for data in DATAS:
        if id == data["id"]:
            data["title"]=title
            data["content"]=content
            data["category"]=category
            return True

app = Flask(__name__)
app.config['SECRET_KEY'] = '03237566636ed31610a390d4f455d949045b5d2323363317'



@app.route("/")
def liste():

    return render_template('table.html', date_time=date_time, data=DATAS)

@app.route('/create/', methods=('GET', 'POST'))
def create():

    now = datetime.now() # current date and time
    date_time = now.strftime("%d/%m/%Y")

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
            DATAS.append({"id":str(uuid.uuid4()),'title': title, 'content': content,'category' : category,'edit_date': date_time})
            return redirect(url_for('liste'))

            
        
        

    return render_template('add.html')

@app.route('/edit/<id>', methods=('GET', 'POST')) 
def edit(id):
    print(search_to_do(id))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        print(title)
        print(content)
        print(category)
        edit_toDo(id,title,content,category)


        return render_template('table.html', data=DATAS)

    if request.method == 'GET':

        return render_template('edit.html', onedata = search_to_do(id))

@app.route("/delete/<id>") 
def delete(id):
    print(delete_todo(id))

    return render_template('table.html', data=DATAS)   

