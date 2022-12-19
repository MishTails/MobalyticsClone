from app.models import db, User, environment, SCHEMA, Origin

def seed_origins():

  admin = Origin(
    name="A.D.M.I.N",
    desc="A.D.M.I.N programs a custom configuration per player each game.",
    breakpoint_A="(2) [Initialize ADMIN cause and effect]",
    breakpoint_B="(4) [Add another effect to the program]",
    breakpoint_C="(6) Boost previous tier by 180%"
  )
  animasquad = Origin(
    name="Anima Squad",
    desc="Anima Squad members build fame for scoring champion kills. When they pause to celebrate a kill, they permanently gain 6 maximum Health per point of fame. Fame immediately benefits the whole Anima Squad.",
    breakpoint_A="(3) 15% Attack Damage and 15 Ability Power",
    breakpoint_B="(5) 35% Attack Damage and 35 Ability Power",
    breakpoint_C="(7) 55% Attack Damage and 55 Ability Power"

  )
  arsenal = Origin(
    name="Arsenal",
    desc="(1) When deploying the Arsenal champion, players may choose which weapon he will equip."
  )

  civilian = Origin(
    name="Civilian",
    desc="If there is a Civilian alive, your team is inspired to protect them by gaining Mana every 2 seconds.",
    breakpoint_A="(1) +2 Mana",
    breakpoint_B="(2) +4 Mana",
    breakpoint_C="(3) +10 Mana"
  )

  gadgeteen = Origin(
    name="Gadgeteen",
    desc="Gadgeteens create random modified weapon which with powerful effects. Any champion can equip the items, but they fall apart after 1 round.",
    breakpoint_A="(3) Create 1 item(s) each round",
    breakpoint_B="(5) Create 2 item(s) each round"
  )

  lasercorps = Origin(
    name="LaserCorps",
    desc="When a LaserCorp agent attacks or is hit by an attack, their combat drone has a 50%\ chance to deal magic damage to the agent's target (0.5 second cooldown). When a LaserCorps agent dies, their drone is reassigned to the nearest living agent.",
    breakpoint_A="(3) 60 magic damage",
    breakpoint_B="(6) 150 magic damage",
    breakpoint_C="(9) 150 magic damage, and each agent gets a 2nd drone"
  )

  mechaprime = Origin(
    name="Mecha: PRIME",
    desc="Use the Mecha selector item to choose a PRIME. Combat start: the PRIME combines with the 2 nearest Mecha, absorbing 100%\ of their Health.",
    breakpoint_A="(3) The PRIME gains 60 Ability Power and 60% Attack Damage",
    breakpoint_B="(5) All Mechas gain 45 Ability Power and 45% Attack Damage; The PRIME gains double this amount."
  )

  oxforce = Origin(
    name="Ox Force",
    desc= "Ox Force units gain a range of Attack Speed that ramps as they lose Health. Once per combat, they become invulnerable for 1 seconds as they defend the city with their last breath.",
    breakpoint_A="(2) 15%\ - 30%\ Attack Speed.",
    breakpoint_B="(4) 35%\ - 70%\ Attack Speed.",
    breakpoint_C="(6) 70%\ - 140%\ Attack Speed.",
    breakpoint_D="(8) 125%\ - 250%\ Attack Speed."
  )

  starguardian = Origin(
    name="Star Guardian",
    desc="Gain more Mana from all sources",
    breakpoint_A="(3) 40%\ additional mana",
    breakpoint_B="(5) 70%\ additional mana",
    breakpoint_C="(7) 120%\ additional mana",
    breakpoint_D="(9) 200%\ additional mana"
  )

  supers = Origin(
    name="Supers",
    desc="(3) Combat start: strike a pose that grants your team 20%\ bonus damage, which increases by 5%\ for every 3-star champion on your team."
  )

  threat = Origin(
    name="Threat",
    desc="(1) Threats do not have a Trait bonus, but instead have powerful Abilities and increased base stats."
  )

  underground = Origin(
    name="Underground",
    desc="The Underground must sneak through the sewers and crack 10 locks to open a vault. When the vault opens, you may choose to take the loot now, or attempt another heist for even better rewards.",
    breakpoint_A="(3) Crack 1 vault lock after a player combat win, and 3 after a player combat loss",
    breakpoint_B="(5) Crack 2 vault lock after a player combat win, and 5 after a player combat loss"
  )
  db.session.add(admin)
  db.session.add(animasquad)
  db.session.add(arsenal)
  db.session.add(civilian)
  db.session.add(gadgeteen)
  db.session.add(lasercorps)
  db.session.add(mechaprime)
  db.session.add(oxforce)
  db.session.add(starguardian)
  db.session.add(supers)
  db.session.add(threat)
  db.session.add(underground)
  db.session.commit()

def undo_origins():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.origins RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM origins")

    db.session.commit()
