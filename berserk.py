from character import Character
class Berserk(Character):
    max_health = 100

    def __init__(self, name, health, damage, defence):
        Character.__init__(self, name, health, damage, defence)

    def __str__(self):
        return Character.__str__(self) + \
        f'Додаткова шкода: {self.count_additional_damage()}'

    def count_additional_damage(self):
        return max(self.damage * (1 - self.health / self.max_health), 0)

    def attack(self, target):
        return target.take_damage(
            self.damage + self.count_damage_offset() + self.count_additional_damage()
        )
