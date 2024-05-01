class School:
    def __init__(self, name, level, numberOfStudents):
        # Initialize attributes
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    # Getter methods
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def get_numberOfStudents(self):
        return self.numberOfStudents 
    
    # Setter method
    def set_numberOfStudents(self, newNumberOfStudents):
        self.numberOfStudents = newNumberOfStudents
    
    # String representation method
    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberOfStudents} students."


# Test Code
a = School("Codecademy", "high", 100)
print(a)
print(a.get_name())
print(a.get_level())
a.set_numberOfStudents(200)
print(a.get_numberOfStudents())


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    # Getter method for pickup policy
    def get_pickupPolicy(self):
        return self.pickupPolicy

    # String representation method
    def __repr__(self):
        return super().__repr__() + f" The Pickup Policy is: {self.pickupPolicy}"


# Test Code
b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(b.get_pickupPolicy())
print(b)


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, "high", numberOfStudents)
        self.sportsTeams = sportsTeams

    # Getter method for sports teams
    def get_sportsTeams(self):
        return self.sportsTeams

    # String representation method
    def __repr__(self):
        return super().__repr__() + f" The Sports Teams are: {self.sportsTeams}"


c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.get_sportsTeams())
print(c)
