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
