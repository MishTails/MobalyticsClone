from app.models import db, User, environment, SCHEMA, Origin

def seed_origins():

  admin = Origin(
    name="A.D.M.I.N"
    desc="A.D.M.I.N programs a custom configuration per player each game."
    breakpoint_A="(2) [Initialize ADMIN cause and effect]"
    breakpoint_B="(4) [Add another effect to the program]"
    breakpoint_C="(6) Boost previous tier by 180%"
  )
  anima_squad = Origin(
    name="Anima Squad"
    desc="Anima Squad members build fame for scoring champion kills. When they pause to celebrate a kill, they permanently gain 6 maximum Health per point of fame. Fame immediately benefits the whole Anima Squad."
    breakpoint_A="(3) 15% Attack Damage and 15 Ability Power"
    breakpoint_B="(5) 35% Attack Damage and 35 Ability Power"
    breakpoint_C="(7) 55% Attack Damage and 55 Ability Power"

  )
  arsenal = Origin(
    name="Arsenal"
    desc="(1) When deploying the Arsenal champion, players may choose which weapon he will equip."
  )
