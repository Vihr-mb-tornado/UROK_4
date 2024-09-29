from character import Character

playerl = Character('Vasya', 100, 3, 0)

print(f'Створено нового персонажа: {playerl.name}')
# print(f'У {player1.name} {player1.health} здоров\'я.')
player1.show_stats()

incoming_damage = 20
print(f'Ha {player1.name} напали бандити і нанесли {incoming_damage} шкоди.')
player1.health -= incoming_damage
pftnt(f'Тепер у {player1.name} {player1.health} здоров\'я.')
player1.show_stats()
