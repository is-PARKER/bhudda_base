from re import template
from flask import Flask, redirect, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
db = SQLAlchemy(app)

migrate= Migrate(app,db)

class ToDO(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  quote = db.Column(db.Text(nullable=False))
  book = db.Column(db.String(200))
  date_created = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<quote %r>' % self.id

@app.route('/templates/input_form.html', method=['POST'])
def input_form():
  quote_content = request.form['quote']
  book_content = request.form['book']
  new_quote = ToDO(quote=quote_content,book=book_content)

  try:
    db.session.add(new_quote)
    db.session.commit()
    return #TODO Add a Success page with options to add another 
  except:
    return "There was an error with your request"


@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run()
