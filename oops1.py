 ## initioate a class

class emplolyee:
    def __init__(self):
        print("started executing the attributes/data")
        self.id=123
        self.salary=50000
        self.designation = "SDE"
        print("attributes/data have been initiated")

    def travel(self,destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")

# create an object/instance of the class
sam=emplolyee()

# Priting the attributes of the class
#print(sam.id)

# Calling the method of the class
#sam.travel("New York")

print(type(sam))