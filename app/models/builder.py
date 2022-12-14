from .db import db, environment, SCHEMA, add_prefix_for_prod

class Builder(db.Model):
  __tablename__ = 'builder'

  if environment == "production":
      __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  guide_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('guides.id')))
  name = db.Column(db.String, default="Untitled", nullable=False)

  def to_dict(self):
    return {
      'id': self.id,
      'guide_id': self.guide_id,
      'email': self.email
    }
