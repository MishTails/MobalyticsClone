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
    breakpoint_A="(2) +6% Attack Speed per stack",
    breakpoint_B="(4) +12% Attack Speed per stack",
    breakpoint_C="(6) +20% Attack Speed per stack",
    breakpoint_D="(8) +30% Attack Speed per stack"
  )

  forecaster = Trait(
    name="Forecaster",
    desc="""At the start of combat, Forecaster champions grant adjacent allies different buffs depending on the current weather, which changes every game.

    Sunny Weather:
    Combat start: Grant a 400/600/4000 Health shield to adjacent allies for 10/10/45 seconds.

    Windy Weather:
    Combat start: grant bonus Attack Damage and Ability Power to adjacent allies, increasing by 15/25/150%\ every 5 seconds.

    Rainy Weather:
    At the start of combat, Forecaster champions grant adjacent allies 20 / 40 / 100 mana until they have cast 1/1/100 spells. """,
    breakpoint_A ="(1) ??? (Randomly selected per game)"

  )

  hacker = Trait(
    name="Hacker",
    desc="Hackers gain Omnivamp and summon a H4ckerr!m. Any unit placed in the rider hex will be sent to the enemy backline and is untargetable for the first 2 seconds of combat. Omnivamp: heal for a percentage of damage dealt",
    breakpoint_A="(2) 15%\ Omnivamp",
    breakpoint_B="(3) 40%\ Omnivamp",
    breakpoint_C="(4) 70%\ Omnivamp",
  )

  heart = Trait(
    name="Heart",
    desc="When Heart units cast their Ability, your team gains stacking Ability Power for the rest of combat.",
    breakpoint_A="(2) +4 Ability Power",
    breakpoint_B="(4) +7 Ability Power",
    breakpoint_C="(6) +10 Ability Power"
  )

  mascot = Trait(
    name="Mascot",
    desc="Your team heals a percentage of their maximum Health every 2 seconds, and Mascots heal double the amount. When Mascots die, they retreat to the sidelines to cheer on your team. Your team's healing increased by 1%\ for each cheering Mascot",
    breakpoint_A="(2) 1.5%\ healing",
    breakpoint_A="(4) 2.5%\ healing",
    breakpoint_A="(6) 4.5%\ healing",
    breakpoint_A="(8) 10%\ healing"
  )

  prankster = Trait(
    name="Prankster",
    desc="Once per combat at 50% Health, spawn a target dummy, move to a safe location, and restore 350 Health.",
    breakpoint_A="(2) Once per combat at 50% Health, spawn a target dummy, move to a safe location, and restore 350 Health.",
    breakpoint_B="(3) And, Prankster dummies stun the enemy that killed them for 1.5 seconds."
  )

  recon = Trait(
    name="Recon",
    desc="Innate: Gain 2 hex Attack Range. If there is an enemy nearby, Recon units will dash to safety before casting their Ability.",
    breakpoint_A="(2) +20% Crit Chance",
    breakpoint_B="(3) +75% Crit Chance",
    breakpoint_C="(4) +100% Crit Chance and Recon Abilities can critically strike"
  )

  renegade = Trait(
    name="Renegade",
    desc="Renegade units deal bonus damage, and the last sone standing deals more.",
    breakpoint_A="(3) 35%\ bonus damage, 20%\ for last alive",
    breakpoint_B="(6) 60%\ bonus damage, 40%\ for last alive"
  )
