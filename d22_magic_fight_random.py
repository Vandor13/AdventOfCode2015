import random


DEBUG = True

MAGIC_MISSILE = "Magic Missile"
DRAIN = "Drain"
SHIELD = "Shield"
POISON = "Poison"
RECHARGE = "Recharge"
SPELLS = [MAGIC_MISSILE, DRAIN, SHIELD, POISON, RECHARGE]


class MagicFight:
    def __init__(self):
        self.player_hp = 50
        self.mana = 500
        self.poison = 0
        self.shield = 0
        self.recharge = 0
        self.boss_hp = 58
        self.boss_damage = 9
        self.mana_spent = 0

    def __cmp__(self, other):
        return self.mana - other.mana

    def handle_effects(self):
        if self.shield > 0:
            self.shield -= 1
            if DEBUG:
                print(f"Shield's timer is now {self.shield}.")
        if self.poison > 0:
            self.boss_hp -= 3
            self.poison -= 1
            if DEBUG:
                print(f"Poison deals 3 damage; its timer is now {self.poison}.")
        if self.recharge > 0:
            self.recharge -= 1
            self.mana += 101
            if DEBUG:
                print(f"Recharge provides 101 mana; its timer is now {self.recharge}")
        # if self.drain > 0:
        #     self.drain -= 1
        #     self.player_hp += 2
        #     self.boss_hp -= 2
        #     if DEBUG:
        #         print(f"Drain deals 2 damage and heals 2 hit points. Its timer is now {self.drain}")

    def player_turn(self, magic):
        if DEBUG:
            print()
            print("-- Player turn --")
            self.print_current_state()
        self.handle_effects()
        if magic == MAGIC_MISSILE:
            assert self.mana >= 53, "Not enough mana for Magic Missile."
            self.mana -= 53
            self.mana_spent += 53
            self.boss_hp -= 4
            if DEBUG:
                print(f"Player casts Magic Missile, dealing 4 damage.")
        elif magic == DRAIN:
            assert self.mana >= 73, "Not enough mana for Drain."
            self.mana -= 73
            self.mana_spent += 73
            self.boss_hp -= 2
            self.player_hp += 2
            print(f"Player casts Drain and it deals 2 damage and heals 2 hit points.")
        elif magic == SHIELD:
            assert self.mana >= 113, "Not enough mana for Shield."
            self.mana -= 113
            self.mana_spent += 113
            assert self.shield == 0, "Shield was already active and can't be cast again"
            self.shield = 6
            print(f"Player casts Shield.")
        elif magic == POISON:
            assert self.mana >= 173, "Not enough mana for Poison."
            self.mana -= 173
            self.mana_spent += 173
            assert self.poison == 0, "Poison was already active and can't be cast again"
            self.poison = 6
            print(f"Player casts Poison.")
        elif magic == RECHARGE:
            assert self.mana >= 229, "Not enough mana for Recharge."
            self.mana -= 229
            self.mana_spent += 229
            assert self.recharge == 0, "Recharge was already active and can't be cast again"
            self.recharge = 6
            print(f"Player casts Recharge.")
        print(f"{self.mana_spent} Mana spent. {self.mana} Mana left.")
        game_done = self.check_end()
        return game_done

    def boss_turn(self):
        if DEBUG:
            print()
            print("-- Boss turn --")
            self.print_current_state()
        self.handle_effects()
        armor = (7 if self.shield > 0 else 0)
        damage = max(self.boss_damage - armor, 1)
        self.player_hp -= damage
        if DEBUG:
            print(f"Boss attacks for {damage} damage.")
        game_done = self.check_end()
        return game_done

    def check_end(self):
        if self.boss_hp <= 0:
            print(f"This kills the boss, and the player wins.")
            return True
        elif self.player_hp <= 0:
            print(f"This kills the player, and the player loses.")
            return True
        return False

    def get_possible_spells(self):
        possible_spells = SPELLS.copy()
        potential_mana = self.mana
        if self.recharge > 1:
            potential_mana += 101
        if potential_mana < 53:
            possible_spells.remove(MAGIC_MISSILE)
        if potential_mana < 73:
            possible_spells.remove(DRAIN)
        if self.shield > 0 or potential_mana < 113:
            possible_spells.remove(SHIELD)
        if self.poison > 0 or potential_mana < 173:
            possible_spells.remove(POISON)
        if self.recharge > 0 or potential_mana < 229:
            possible_spells.remove(RECHARGE)
        return possible_spells

    def print_current_state(self):
        print(f"- Player has {self.player_hp} hit points, {7 if self.shield > 0 else 0} armor, " +
              f"{self.mana} mana")
        print(f"- Boss has {self.boss_hp} hit points")


def fight_to_the_death():
    game = MagicFight()
    while True:
        possible_spells = game.get_possible_spells()
        if not possible_spells:
            print("Nothing left to do. Player loses.")
            break
        spell = random.choice(possible_spells)
        game_end = game.player_turn(spell)
        if game_end:
            break
        game_end = game.boss_turn()
        if game_end:
            break


fight_to_the_death()
