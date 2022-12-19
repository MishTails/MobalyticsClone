from .db import db, environment, SCHEMA, add_prefix_for_prod

class Trait(db.Model):
  __tablename__ = 'traits'

  if environment == "production":
      __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  desc = db.Column(db.String)

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'desc': self.desc
    }
