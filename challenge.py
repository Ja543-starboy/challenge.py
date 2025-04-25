"""
OOP Assignment Combining:
1. Class Design with Inheritance and Encapsulation (Superheroes)
2. Polymorphism Challenge (Animals & Vehicles)
"""

# ==================== PART 1: SUPERHERO CLASS DESIGN ====================

class Superhero:
    def __init__(self, name, secret_identity, power_level):
        self.name = name
        self._secret_identity = secret_identity  # Protected attribute
        self.power_level = power_level
        self.__health = 100  # Private attribute (name mangling)

    def reveal_identity(self):
        """Encapsulation example - controlled access to protected attribute"""
        return f"{self.name}'s secret identity is {self._secret_identity}!"

    def attack(self):
        """Polymorphic method to be overridden by subclasses"""
        return f"{self.name} attacks with power level {self.power_level}!"

    def get_health(self):
        """Encapsulation example - getter method"""
        return self.__health

    def take_damage(self, amount):
        """Encapsulation example - controlled modification"""
        self.__health = max(0, self.__health - amount)
        return f"{self.name} now has {self.__health} health!"

    def move(self):
        """Base movement method for polymorphism"""
        return f"{self.name} moves heroically!"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} | Power: {self.power_level}"


class FlyingHero(Superhero):
    def __init__(self, name, secret_identity, power_level, flight_speed):
        super().__init__(name, secret_identity, power_level)
        self.flight_speed = flight_speed

    def attack(self):
        """Polymorphism - overriding parent method"""
        return f"{self.name} dive-bombs at {self.flight_speed} mph!"

    def move(self):
        """Unique movement implementation"""
        return f"{self.name} soars through the sky at {self.flight_speed} mph! 🦸♂️✈️"


class TechHero(Superhero):
    def __init__(self, name, secret_identity, power_level, gadget):
        super().__init__(name, secret_identity, power_level)
        self.gadget = gadget

    def attack(self):
        """Polymorphism - different implementation"""
        return f"{self.name} uses {self.gadget} to attack with power {self.power_level * 1.5}!"

    def move(self):
        """Unique movement implementation"""
        return f"{self.name} teleports using {self.gadget}! ⚡"


# ==================== PART 2: POLYMORPHISM CHALLENGE ====================

class Animal:
    def move(self):
        """Base move method to be overridden"""
        raise NotImplementedError("Subclasses must implement this method")


class Bird(Animal):
    def move(self):
        return "Flapping wings and flying through the air! 🦅"


class Fish(Animal):
    def move(self):
        return "Swimming gracefully through the water! 🐟"


class Cheetah(Animal):
    def move(self):
        return "Running at 70 mph across the savanna! 🐆"


class Vehicle:
    def move(self):
        """Base move method to be overridden"""
        raise NotImplementedError("Subclasses must implement this method")


class SportsCar(Vehicle):
    def move(self):
        return "Accelerating to 200 mph on the highway! 🚗💨"


class Submarine(Vehicle):
    def move(self):
        return "Diving deep underwater! 🚢"


class Helicopter(Vehicle):
    def move(self):
        return "Hovering and flying with rotors! 🚁"


# ==================== DEMONSTRATION ====================

def showcase_movement(entities):
    """Polymorphism in action - single function handles different types"""
    print("\n=== Movement Showcase ===")
    for i, entity in enumerate(entities, 1):
        print(f"{i}. {entity.move()}")


def hero_battle(hero1, hero2):
    """Demonstrate encapsulation and polymorphism"""
    print("\n=== Hero Battle ===")
    print(hero1.attack())
    print(hero2.attack())
    print(hero1.take_damage(30))
    print(hero2.take_damage(25))
    print(f"{hero1.name}'s health: {hero1.get_health()}")
    print(f"{hero2.name}'s health: {hero2.get_health()}")


if __name__ == "__main__":
    # Create superhero instances
    sky_guardian = FlyingHero("Sky Guardian", "Alex Johnson", 8500, 500)
    tech_wizard = TechHero("Tech Wizard", "Jamie Smith", 7800, "Quantum Blaster")

    # Create animal instances
    eagle = Bird()
    shark = Fish()
    speedy = Cheetah()

    # Create vehicle instances
    ferrari = SportsCar()
    nautilus = Submarine()
    black_hawk = Helicopter()

    # Part 1: Superhero demonstration
    print("\n" + "="*50)
    print("SUPERHERO DEMONSTRATION")
    print("="*50)
    print(sky_guardian)
    print(tech_wizard)
    print(sky_guardian.reveal_identity())
    print(tech_wizard.reveal_identity())
    hero_battle(sky_guardian, tech_wizard)
    print(sky_guardian.move())
    print(tech_wizard.move())

    # Part 2: Polymorphism demonstration
    print("\n" + "="*50)
    print("POLYMORPHISM DEMONSTRATION")
    print("="*50)
    showcase_movement([eagle, shark, speedy])
    showcase_movement([ferrari, nautilus, black_hawk])