class Zombie:

    def __init__( self , name ):
        self.name = name
        self.energy = 15        
        self.health = 500

    def show_stats( self ):
        print(f"Name: {self.name}\nEnergy: {self.energy}\nHealth: {self.health}\n")

    def bite ( self , student ):
        student.health -= 30
        print(f"You got bit by Zombie! Your current health level is {student.health}.Be careful,{student.name}!")

        if student.health <= 0:
            print(f"You turned to Zombie!")
        return self

