from .db import db, environment, SCHEMA, add_prefix_for_prod

class Champion(db.Model):
  __tablename__ = 'champions'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False, default="empty")
  origin = db.Column(db.String)
  trait = db.Column(db.String)
  tier = db.Column(db.Integer, default=0)
  spellName = db.Column(db.String)
  startMana = db.Column(db.Integer, default=0)
  manaCost = db.Column(db.Integer, default=0)
  spellDesc = db.Column(db.String(500))
  item_id_A = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('items.id')))
  item_id_B = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('items.id')))
  item_id_C = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('items.id')))

  def to_dict
