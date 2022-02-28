import sqlalchemy as sa

from buddha_base.data.modelbase import SqlAlchemyBase

class Quotes(SqlAlchemyBase):
  id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
  quote = sa.Column(sa.String)
  
  
  book = sa.column(sa.String)
  author
  #TODO: Write out more aspects for quotes.