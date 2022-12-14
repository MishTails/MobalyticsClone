from .db import db, environment, SCHEMA, add_prefix_for_prod

class Item(db.Model):
  __tablename__ = 'items'

  if environment == "production":
      __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  component_id_A = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('components.id')))
  component_id_B = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('components.id')))
  isCraftable = db.Column(db.Boolean)
  name = db.Column(db.String, default="itemP", nullable=False)
  desc = db.Column(db.String)

  def to_dict(self):
    return {
      'id': self.id,
      'component_id_A': self.component_id_A,
      'component_id_B': self.component_id_B,
      'isCraftable': self.isCraftable,
      'name': self.name,
      'desc': self.desc
    }
