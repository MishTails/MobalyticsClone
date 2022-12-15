from .db import db, environment, SCHEMA, add_prefix_for_prod

carouselpriorities = db.Table(
  "carouselpriorities",
  db.Column("component_id", db.Integer, db.ForeignKey(add_prefix_for_prod("components.id")), primary_key = True),
  db.Column("guide_id", db.Integer, db.ForeignKey(add_prefix_for_prod("guides.id")), primary_key= True),
  db.Column("priority", db.Integer)
  )

if environment == "production":
  carouselpriorities.schema = SCHEMA
