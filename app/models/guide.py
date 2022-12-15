from .db import db, environment, SCHEMA, add_prefix_for_prod

class Guide(db.Model):
  __tablename__ = 'guides'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String, nullable=False, default="Untitled")
  playstyle = db.Column(db.String)
  tier = db.Column(db.String, default="S Tier")
  difficulty = db.Column(db.String)
  general_info = db.Column(db.String)
  when_to_make = db.Column(db.String)
  additional_tips = db.Column(db.String)
  early_build_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('builds.id')))
  early_build_desc = db.Column(db.String)
  mid_build_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('builds.id')))
  mid_build_desc = db.Column(db.String)
  final_build_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('builds.id')))
  final_build_desc = db.Column(db.String)

  def to_dict(self):
    return {
      'id': self.id,
      'title': self.title,
      'playstyle': self.playstyle,
      'tier': self.tier,
      'difficulty': self.difficulty,
      'general_info': self.general_info,
      'when_to_make': self.when_to_make,
      'additional_tips': self.additional_tips,
      'early_build_id': self.early_build_id,
      'early_build_desc': self.early_build_desc,
      'mid_build_id': self.mid_build_id,
      'mid_build_desc': self.mid_build_desc,
      'final_build_id': self.final_build_id,
      'final_build_desc': self.final_build_desc
    }
