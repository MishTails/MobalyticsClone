from app.models import db, User, environment, SCHEMA, Trait

def seed_traits():

  ace = Trait(
    name="Ace",
    desc="This trait is active only when you have exactly 1 or 4 unique Aces.",
    breakpoint_A="(1) Execute enemies under 12% Health",
    breakpoint_B="(4) Execute enemies under 30% Health"
  )

  aegis = Trait(
    name="Aegis",
    desc="Your team gains bonus Magic Resist, and Aegis units gain more.",
    breakpoint_A="(2) +20 Magic Resist, +40 for Aegis",
    breakpoint_B="(3) +35 Magic Resist, +70 for Aegis",
    breakpoint_C="(4) +50 Magic Resist, +100 for Aegis",
    breakpoint_D="(5) +75 Magic Resist, +150 for Aegis"
  )

  brawler = Trait(
    name = "Brawler",
    desc = "Brawlers gain additional maximum Health",
    breakpoint_A = "(2) +20% maximum Health",
    breakpoint_B = "(4) +50% maximum Health",
    breakpoint_C = "(6) +70% maximum Health",
    breakpoint_D = "(8) +111% maximum Health"
  )

  corrupted = Trait(
    name="Corrupted",
    desc = "Once per combat at 60% Health (or when your team has died), come alive and fight.",
    breakpoint_A="(1) Combat starts: Lie dormant while absorbing the souls of allies that die. Gain 40 Ability Power for each soul."
  )

  defender = Trait(
    name="Defender",
    desc="Innate: Taunt nearby enemies after the start of combat. Your team gains bonus Armor, and Defenders gain more. Taunt: enemies that are able and in range must attack the taunter",
    breakpoint_A="(2) +30 Armor, +60 for Defenders",
    breakpoint_B="(4) +80 Armor, +150 for Defenders",
    breakpoint_C="(6) +200 Armor, +250 for Defenders"
  )

  duelist = Trait(
    name="Duelist",
    desc="Innate: increased movement speed. Duelists' basic attacks grant bonus Attack Speed, up to 10 stacks.",
    breakpoint_A="(2) +6% Attack Speed per stack"
    breakpoint_B="(4) +12% Attack Speed per stack"
    breakpoint_C="(6) +20% Attack Speed per stack"
    breakpoint_D="(8) +30% Attack Speed per stack"
  )
