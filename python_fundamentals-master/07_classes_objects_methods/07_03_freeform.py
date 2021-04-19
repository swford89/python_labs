'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''
# I went beyond the main scope of the assignment because I found this more fun

import random
import sys
import time

class Player():

    def __init__(self, name, life=50, level=1, attack_damage=25) -> None:
        self.name = name
        self.life = life
        self.level = level
        self.attack_damage = attack_damage   

    def __str__(self) -> str:
        return f"{self.name}"

    def roll_dice(self):
        """ determines who gets to attack, and maybe get healed with fruit"""
        role_value = random.randint(1,6)
        print(f"{self.name} rolled a {role_value}")
        if role_value % 2 == 0:
            self.eat_food()
        return role_value

    def eat_food(self):
        """ heals life with appropriate roll value """
        some_food = random.choice(food_list)
        self.life += some_food.energy
        print(f"This nutritious {some_food.name} gave {self.name} {some_food.energy} life!")
        return self.life

    def rest_and_relaxation(self):
        while self.life < 50:
            self.life +=  1
            sys.stdout.write(f"{self.life}\r")
            sys.stdout.flush()
            time.sleep(0.1)
            if self.life == 50:
                print(f"\n{self.name}, you're fully recovered!\n")
        return self.life

    def level_up(self):
        """ add life and increase strength after winning """
        self.life += 10
        self.level += 1
        self.attack_damage += 10
        print(f"""
        {self.name}, you've leveled up!
        {self.name} life: {self.life}
        {self.name} level: {self.level}
        {self.name} attack damage: {self.attack_damage}
        """)
        return

class Hero(Player):

    def attack_enemy(self, some_enemy):
        """ to attack an enemy """
        some_enemy.life -= self.attack_damage
        print(f"""
        {self.name} did {self.attack_damage} damage to {some_enemy.name}
        {some_enemy.name} life: {some_enemy.life}
        """)
        return some_enemy.life

    def battle_prompt(self):
        """ selects an enemy to battle """
        selected_enemy = random.choice(enemy_list)
        print(f"A wild {selected_enemy} has appeared!")
        return selected_enemy

    def battle_attack(self, selected_enemy, round_counter):
        """ battling until someone has zero life """
        while self.life > 0 and selected_enemy.life > 0:
            continue_prompt = input(f"\nRound {round_counter}! Press the enter key to continue.\n")
            hero_roll = self.roll_dice()
            enemy_role = selected_enemy.roll_dice()
            if hero_roll == enemy_role:
                print(f"TIE")
                round_counter += 1
            elif hero_roll > enemy_role:
                some_hero.attack_enemy(selected_enemy)
                round_counter += 1
            elif enemy_role > hero_roll:
                selected_enemy.attack_hero(some_hero)
                round_counter += 1
        return

    def battle_result(self, selected_enemy):
        """ level up or recovering at the end of the battle """
        if self.life > 0:
            self.rest_and_relaxation()
            self.level_up()
            enemy_list.remove(selected_enemy)
            defeated_enemies.append(selected_enemy)
        elif selected_enemy.life > 0:
            selected_enemy.rest_and_relaxation()
        return

class Enemy(Player):

    def attack_hero(self, some_hero):
        """ to attack a hero """
        some_hero.life -= self.attack_damage
        print(f"""
        {self.name} did {self.attack_damage} damage to {some_hero.name}
        {some_hero.name} life: {some_hero.life}
        """)
        return some_hero.life

class Food():
    
    def __init__(self, name, energy) -> None:
        self.name = name
        self.energy = energy

    def __str__(self) -> str:
        return f"A nutritious {self.name}"

apple = Food("apple", 5)
banana = Food("banana", 5)
mango = Food("mango", 10)
omelette = Food("tasty omelette", 20)

food_list = [apple, banana, mango, omelette]

some_hero = Hero("Scott", life=50, level=1, attack_damage=25)
some_enemy_one = Enemy("Foo", life=50, level=1, attack_damage =20)
some_enemy_two = Enemy("Bar", life=50, level=1, attack_damage=25)
some_enemy_three = Enemy("Baz", life=50, level=1, attack_damage=30)
some_enemy_four = Enemy("Qux", life=50, level=1, attack_damage=35)

enemy_list = [some_enemy_one, some_enemy_two, some_enemy_three, some_enemy_four]
defeated_enemies = []

while enemy_list:
    round_counter = 1
    selected_enemy = some_hero.battle_prompt()
    some_hero.battle_attack(selected_enemy, round_counter)
    some_hero.battle_result(selected_enemy)

defeated_order = 1
for enemy in defeated_enemies:
    print(f"Defeated enemy #{defeated_order}: {enemy}")
    defeated_order += 1