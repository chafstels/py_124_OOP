'''
Ролевая игра:
Создайте базовый класс Character с атрибутами name, health, attack_power, defense_power, и методами attack(), heal().
Создайте производные классы:
Warrior (воин) с высоким показателем атаки и низким показателем защиты
Mage (маг) с низким показателем атаки и высоким показателем защиты
Archer (лучник) с средними показателями атаки и защиты
Каждый подкласс должен иметь соответствующие методы attack() и heal(), а также уникальные способности.'''
import random

class Character:
    def __init__(self, name , health, attack_power, defense_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense_power = defense_power
    def attack(self, target):
        damage = self.attack_power - target.defense_power
        if damage > 0:
            print(f'{self.name} атакует {target.name} и наносит {damage} урона!')
            target.health -= damage
        else:
            print(f'Атака {self.name} не пробила защиту {target.name}')
    def heal(self, amount=0):
        self.health += amount
        print(f'{self.name} восстанавливает {amount} здоровья.')

class Warrior(Character):
    def __init__(self, name, health=100, attack_power=25, defense_power=5):
        super().__init__(name, health, attack_power, defense_power)

    def attack(self, target):
        super().attack(target)
        if random.random() < 0.3:
            print(f'{self.name} оглушает {target.name}!')
            target.defense_power //= 2
    def heal(self):
        print(f'{self.name} не умеет лечиться.')

class Mage(Character):
    def __init__(self, name, health=75, attack_power=15, defense_power=5):
        super().__init__(name, health, attack_power, defense_power)
    def attack(self, target):
        super().attack(target)
        if random.random() < 0.6:
            print(f'{self.name} создает магический щит!')
            self.defense_power += 1
    def heal(self, amount=10):
        self.health += amount
        print(f'{self.name} восстанавливает {amount} здоровья с помощью магии')

class Archer(Character):
    def __init__(self, name, health=85, attack_power=20, defense_power=10):
        super().__init__(name, health, attack_power, defense_power)
    def attack(self, target):
        super().attack(target)
        if random.random() < 0.4:
            print(f'{self.name} делает залп из двух стрел!')
            self.attack(target)
    def heal(self, amount=5):
        self.health += amount
        print(f'{self.name} использует целебную траву, чтобы восстановить {amount} здровья.')

warrior = Warrior('Maratbek')
mage = Mage('Anton')
archer = Archer('Chika')

def main():
    heroes = [warrior, mage, archer]
    while len(heroes) > 1:
        random.shuffle(heroes)
        attacker = heroes[0]
        defender = heroes[1]
        action = random.choice(['attack', 'heal'])
        if action == 'attack':
            attacker.attack(defender)
        else:
            attacker.heal()

        if defender.health <= 0:
            print(f'{defender.name} погибает в бою от рук {attacker.name}')
            heroes.remove(defender)
    winner = heroes[0]
    print(f'Победитель: {winner.name}')

main()
