from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class tarea(db.Model):
   id = db.Column('tarea_id', db.Integer, primary_key = True)
   cod = db.Column(db.String(50))
   name = db.Column(db.String(100))
   link = db.Column(db.String(200))
   date = db.Column(db.String(10))

   def __init__(self, cod, name, link, date):
       self.cod = cod
       self.name = name
       self.link = link
       self.date = date

@app.route('/')
def show_all():
   return render_template('show_all.html', tareas = tarea.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['cod'] or not request.form['name'] or not request.form['link']:
         flash('Please enter all the fields', 'error')
      else:
         tarea1 = tarea(request.form['cod'], request.form['name'],request.form['link'], request.form['date'])

         db.session.add(tarea1)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

@app.route("/update", methods=["POST"])
def update():
    name = request.form.get("oldname")
    tarea = tareas.query.filter_by(name=name).first()
    return render_template('update.html', result = tarea, oldname = name)

@app.route("/update_record", methods=["POST"])
def update_record():
    name = request.form.get("oldname")
    tarea = tareas.query.filter_by(name=name).first()
    tarea.cod = request.form['cod']
    tarea.name = request.form['name']
    tarea.link = request.form['link']
    tarea.date = request.form['date']
    db.session.commit()
    return redirect('/')

@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("oldname")
    tarea1 = tarea.query.filter_by(name=name).first()
    db.session.delete(tarea1)
    db.session.commit()
    return redirect("/")

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
