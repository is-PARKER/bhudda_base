import sqlalchemy as sa

from buddha_base.data.modelbase import SqlAlchemyBase

class Contributor(SqlAlchemyBase):

  last_name = sa.Column(sa.String,primary_key=True,index=True,nullable=False)
  first_name = sa.Column(sa.String,primary_key=True,nullable=False)
  year_born = sa.Column(sa.Integer)
  year_died = sa.Column(sa.Integer)

  birth_country = sa.Column(sa.String)
  bio = sa.Column(sa.String)

  
  
  book = sa.column(sa.String)
  author
  #TODO: Write out more aspects for quotes.