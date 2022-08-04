from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


 
app = Flask(__name__)
app.secret_key = 'config.py'
 

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/productiondiary'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 

#Creating model for our incident database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime())
    name = db.Column(db.String(100))
    machine_id = db.Column(db.String(100))
    material = db.Column(db.String(100))
    cell_id = db.Column(db.String(100))
    assembly_code = db.Column(db.String(100))
    comment = db.Column(db.String(255))
 
    def __init__(self, date, name, machine_id, material, cell_id, assembly_code, comment):

        self.date = date
        self.name = name
        self.machine_id = machine_id
        self.material = material
        self.cell_id = cell_id
        self.assembly_code = assembly_code
        self.comment = comment
 
  
#query all the incident data
@app.route('/')
def Index():

    all_data = Data.query.all()
 
    return render_template("index.html", data = all_data)
 

#inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':

        date = request.form['date']
        name = request.form['name']
        machine_id = request.form['machine_id']
        material = request.form['material']
        cell_id = request.form['cell_id']
        assembly_code = request.form['assembly_code']
        comment = request.form['comment']
        my_data = Data(date, name, machine_id, material, cell_id, assembly_code, comment)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Incident Report Inserted Successfully")
 
        return redirect(url_for('Index'))
 
 
#updating a incident's information
@app.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
        
        my_data.date = request.form['date']
        my_data.name = request.form['name']
        my_data.machine_id = request.form['machine_id']
        my_data.material = request.form['material']
        my_data.cell_id = request.form['cell_id']
        my_data.assembly_code = request.form['assembly_code']
        my_data.comment = request.form['comment']
 
        db.session.commit()
        flash("Incident Updated Successfully")
 
        return redirect(url_for('Index'))
 
#deleting a incident
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):

    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    flash("Incident Deleted Successfully")
 
    return redirect(url_for('Index'))
 
 
 
if __name__ == "__main__":
    app.run(debug=False)