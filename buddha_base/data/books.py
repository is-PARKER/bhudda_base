from typing import List
import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from data.modelbase import SqlAlchemyBase
from data.contributors import Contributor

class Book(SqlAlchemyBase):

  __tablename__ = "books"

  title = sa.Column(sa.String, primary_key=True, index=True)
  created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
  
  #TODO: Create scraper to populate database. 
  description = sa.Column(sa.String)

  # Author Relations:
  authors: List[Contributor] = orm.relation("Contributor", order_by=[
    Contributor.last_name.desc(),
    Contributor.first_name.desc()
  ])

  editors: List[Contributor] = orm.relation("Contributor", order_by=[
    Contributor.last_name.desc(),
    Contributor.first_name.desc()
  ])

  translators: List[Contributor] = orm.relation("Contributor", order_by=[
    Contributor.last_name.desc(),
    Contributor.first_name.desc()
  ])
  



  
  
  