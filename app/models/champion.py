from .db import db, environment, SCHEMA, add_prefix_for_prod

class Champion(db.Model):
  __tablename__ = 'champions'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False, default="empty")
  origin_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('origins.id')))
  trait_id_A = db.Column(db.String, db.ForeignKey(add_prefix_for_prod('traits.id')))
  trait_id_B = db.Column(db.String, db.ForeignKey(add_prefix_for_prod('traits.id')))
  tier = db.Column(db.Integer, default=0)
  spellName = db.Column(db.String)
  startMana = db.Column(db.Integer, default=0)
  manaCost = db.Column(db.Integer, default=0)
  spellDesc = db.Column(db.String(500))
  item_id_A = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('items.id')))
  item_id_B = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('items.id')))
  item_id_C = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('items.id')))

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'origin': self.origin,
      'trait_A': self.trait_A,
      'trait_B': self.trait_B,
      'tier': self.tier,
      'spellName': self.spellName,
      'startMana': self.startMana,
      'manaCost': self.manaCost,
      'spellDesc': self.spellDesc,
      'item_id_A': self.item_id_A,
      'item_id_B': self.item_id_B,
      'item_id_C': self.item_id_C
    }
