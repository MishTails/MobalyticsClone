from .db import db, environment, SCHEMA, add_prefix_for_prod

class Origin(db.Model):
  __tablename__ = 'origins'

  if environment == "production":
      __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  desc = db.Column(db.String)
  breakpoint_A = db.Column(db.String)
  breakpoint_B = db.Column(db.String)
  breakpoint_C = db.Column(db.String)
  breakpoint_D = db.Column(db.String)

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'desc': self.desc
    }
