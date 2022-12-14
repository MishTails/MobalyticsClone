from .db import db, environment, SCHEMA, add_prefix_for_prod

buildergrids = db.Table(
  "buildergrids",
  db.Column("builder_id", db.Integer, db.ForeignKey(add_prefix_for_prod("builders.id")), primary_key = True),
  db.Column("champion_id", db.Integer, db.ForeignKey(add_prefix_for_prod("champions.id")), primary_key= True),
  db.Column("grid_index", db.Integer))
)
if environment == "production":
  buildergrids.schema = SCHEMA
