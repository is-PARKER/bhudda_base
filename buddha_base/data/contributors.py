from typing import List
import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from data.modelbase import SqlAlchemyBase

class Contributor(SqlAlchemyBase):

  __tablename__ = "contributors"

  last_name = sa.Column(sa.String,primary_key=True,index=True,nullable=False)
  first_name = sa.Column(sa.String,primary_key=True,nullable=False)
  year_born = sa.Column(sa.Integer)
  year_died = sa.Column(sa.Integer)

  birth_country = sa.Column(sa.String)
  bio = sa.Column(sa.String)

  created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)

  
