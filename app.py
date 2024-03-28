from flask import Flask, render_template
# from flask_sqlalchemy import  SQLAlchemy
import sqlite3

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

# db = SQLAlchemy(app)

# con= sqlite3.connect("test.db")
# cur = con.cursor()

# cur.execute("CREATE TABLE data(id, name, address, phone, email, message)")


# class  User(db.Model):
#     id= db.Column(db.Integer, primary_key=True)
#     name=db.Column(db.String(20), nullable=False)
#     address=db.Column(db.String(20), nullable=False)
#     phone=db.Column(db.Integer, nullable=False)
#     email=db.Column(db.String(30), nullable=False)
#     message=db.Column(db.String(100), nullable=False)

#     def __repr__(self) -> str:
#         return  f'{self.name} - {self.email}'


@app.route("/")
def home ():
    return render_template('index.html')


@app.route("/resume")
def resume ():
    return render_template('resume.html')

@app.route("/about")
def about ():
    return render_template('about.html')

@app.route("/contact")
def contact ():
    # data= User(name="deepak", address="basundhara",phone=9823832716, email="deepakkdas77@gmail.com", message="i am here")
    # db.session.add(data)
    # db.session.commit()
    return render_template('contact.html')

if __name__ == "__main__" :
    app.run(debug= True)



# from app import app, db

# with app.app_context():
#     db.create_all()