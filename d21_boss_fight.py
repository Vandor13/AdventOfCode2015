from itertools import combinations


weapons = {
    # Weapons:    Cost  Damage  Armor
    "Dagger":       (8,      4,       0),
    "Shortsword":   (10,     5,       0),
    "Warhammer":    (25,     6,       0),
    "Longsword":    (40,     7,       0),
    "Greataxe":     (74,     8,       0)
}

armors = {
    # Armor:      Cost  Damage  Armor
    "None":          (0,      0,       0),
    "Leather":      (13,     0,       1),
    "Chainmail":    (31,     0,       2),
    "Splintmail":   (53,     0,       3),
    "Bandedmail":   (75,     0,       4),
    "Platemail":   (102,     0,       5),
}

rings = {
    # Rings:      Cost  Damage  Armor
    "None":         (0,      0,       0),
    "Also None":    (0,      0,       0),
    "Damage +1":    (25,     1,       0),
    "Damage +2":    (50,     2,       0),
    "Damage +3":   (100,     3,       0),
    "Defense +1":   (20,     0,       1),
    "Defense +2":   (40,     0,       2),
    "Defense +3":   (80,     0,       3),
}

boss = {
    "Hit Points": 103,
    "Damage": 9,
    "Armor": 2
}


def find_cheapest_win(player_hit_points = 100):
    cheapest_win = 9999
    cheapest_equipment = None
    most_expensive_loss = 0
    most_expensive_equipment = None
    for weapon in weapons.keys():
        for armor in armors.keys():
            for ring_combo in combinations(rings, 2):
                player_attack = (
                    weapons[weapon][1]
                    + rings[ring_combo[0]][1]
                    + rings[ring_combo[1]][1]
                )
                player_defense = (
                    armors[armor][2]
                    + rings[ring_combo[0]][2]
                    + rings[ring_combo[1]][2]
                )
                total_cost = (
                    weapons[weapon][0]
                    + armors[armor][0]
                    + rings[ring_combo[0]][0]
                    + rings[ring_combo[1]][0]
                )
                if total_cost < cheapest_win and fight(player_hit_points, player_attack, player_defense):
                    cheapest_win = total_cost
                    cheapest_equipment = (weapon, armor, ring_combo[0], ring_combo[1])
                elif total_cost > most_expensive_loss and not fight(player_hit_points, player_attack, player_defense):
                    most_expensive_loss = total_cost
                    most_expensive_equipment = (weapon, armor, ring_combo[0], ring_combo[1])
    print("Cheapest Equipment:", cheapest_equipment)
    print("Total Cost:", cheapest_win)
    print("Most expensive loss equipment:", most_expensive_equipment)
    print("Total Cost:", most_expensive_loss)


def fight(player_hit_points, player_damage, player_armor) -> bool:
    boss_hit_points = boss["Hit Points"]
    while True:
        boss_hit_points -= calculate_damage(player_damage, boss["Armor"])
        if boss_hit_points <= 0:
            return True
        player_hit_points -= calculate_damage(boss["Damage"], player_armor)
        if player_hit_points <= 0:
            return False


def calculate_damage(attack, defense):
    damage = max(1, attack - defense)
    return damage


find_cheapest_win()