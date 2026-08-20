import pickle
import shelve


# --------------------------------
# Example Class
# --------------------------------

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Marks:", self.marks)


# --------------------------------
# Pickle: Save Object
# --------------------------------

def save_pickle(obj, filename):
    with open(filename, "wb") as file:
        pickle.dump(obj, file)

    print("Object saved using pickle.")


# --------------------------------
# Pickle: Load Object
# --------------------------------

def load_pickle(filename):
    with open(filename, "rb") as file:
        obj = pickle.load(file)

    print("Object restored using pickle.")
    return obj


# --------------------------------
# Shelve: Store Object
# --------------------------------

def save_shelve(key, obj, filename="students.db"):
    with shelve.open(filename) as database:
        database[key] = obj

    print("Object saved using shelve.")


# --------------------------------
# Shelve: Load Object
# --------------------------------

def load_shelve(key, filename="students.db"):
    with shelve.open(filename) as database:
        obj = database.get(key)

    print("Object restored using shelve.")
    return obj


# --------------------------------
# Example
# --------------------------------

student = Student(
    "Rahul",
    21,
    [85, 90, 78]
)

print("Original Object:")
student.display()


# Save using pickle
save_pickle(student, "student.pkl")

# Restore using pickle
restored_student = load_pickle("student.pkl")

print("\nRestored Object:")
restored_student.display()


# Save using shelve
save_shelve("student1", student)

# Restore using shelve
shelved_student = load_shelve("student1")

print("\nShelved Object:")
shelved_student.display()
