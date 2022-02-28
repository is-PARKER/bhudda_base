from typing import List
import sqlalchemy as sa
import sqlalchemy.orm as orm

from buddha_base.data.modelbase import SqlAlchemyBase
from data.contributors import Contributor

class Books(SqlAlchemyBase):

  __tablename__ = "books"

  title = sa.Column(sa.Integer, primary_key=True, index=True)
  
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
  



  
  
  