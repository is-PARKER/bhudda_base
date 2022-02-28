import sqlalchemy as sa
from data.modelbase import SqlAlchemyBase


#TODO:Create relation with contributors.

class Country(SqlAlchemyBase):

  id = sa.Column(sa.String,nullable=False,unique=True,index=True)
