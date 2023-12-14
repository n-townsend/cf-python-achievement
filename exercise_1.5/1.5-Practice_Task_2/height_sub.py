class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __sub__(self, other):
        feet = self.feet - other.feet
        inches = self.inches - other.inches
        return Height(feet, inches)

    def __str__(self):
        return f"{self.feet} feet and {self.inches} inches"

person_a = Height(5, 10)
person_b = Height(3, 9)
height_diff = person_a - person_b

print(f"Height difference: {height_diff}")