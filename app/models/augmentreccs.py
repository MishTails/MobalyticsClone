from .db import db, environment, SCHEMA, add_prefix_for_prod

augmentreccs = db.Table(
  "augmentreccs",
  db.Column("guide_id", db.Integer, db.ForeignKey(add_prefix_for_prod("guides.id")), primary_key = True),
  db.Column("augment_id", db.Integer, db.ForeignKey(add_prefix_for_prod("augmentss.id")), primary_key= True),
  )

if environment == "production":
  buildergrids.schema = SCHEMA
