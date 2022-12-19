from app.models import db, User, environment, SCHEMA, Champion

# name origin trait_A, trait_B tier spellName startMana manaCost spellDesc
# come back to this once traits are done
def seed_champions():

  alistar = Champion(
    name="Alistar",
    origin="Ox Force",
    # trait_A="Aegis",
    # trait_B="Mascot",
    spellName="Pulverize",
  )
