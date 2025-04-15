class Prey:

    def flee(self):
        print("This animal flees")

class Predator: 

    def hunt(self):

        print("This animal is  hunting")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()