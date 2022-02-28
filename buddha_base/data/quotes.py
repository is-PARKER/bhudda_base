from typing import List
import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from data.modelbase import SqlAlchemyBase
from data.books import Book

class Quotes(SqlAlchemyBase):

  __tablename__ = "quotes"

  id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
  quote = sa.Column(sa.String)

  created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
  
  #Relations with Books
  book_title = sa.Column(sa.String,sa.ForeignKey("books.title"))

  book = orm.relation("Book")

  #TODO: Write out more aspects for quotes.
  def __repr__(self):
    return '<quote {}>'.format(self.id)