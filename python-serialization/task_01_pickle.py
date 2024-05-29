#!/usr/bin/python3
"""python serialization task 1"""
import pickle


class CustomObject:
    """class that defines a custom object"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """prints out the opbjects attrs"""
        print("Name: {}\nAge: {}\nIs Student: {}".format(
            self.name, self.age, self.is_student))

    def serialize(self, filename):
        """serialize current instance of object and save it to provided file"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """load and return an instance of CustomObject from provided file"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None


# example
# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()
