from .db import db, environment, SCHEMA, add_prefix_for_prod

class Component(db.Model):
  __tablename__ = 'components'

  if environment == "production":
      __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, default="componentC", nullable=False)
  desc = db.Column(db.String)

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'desc': self.desc
    }
