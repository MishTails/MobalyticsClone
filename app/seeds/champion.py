from app.models import db, User, environment, SCHEMA, Champion

# name origin trait_A, trait_B tier spellName startMana manaCost spellDesc

def seed_champions():

  blank = Champion(
    name="empty"
  )
  alistar = Champion(
    name="Alistar",
    origin="Ox Force",
    # trait_A="Aegis",
    # trait_B="Mascot",
    spellName="Pulverize",
  )
