# Import dog.py
from dog import Dog

# Instantiation call
my_dog = Dog("Rex", "SuperDog")

# Invoking bark_action method
my_dog.bark_action()

my_other_dog = Dog("Annie", "SuperDog")
print(my_other_dog.name)
my_other_dog.sit_action()
my_other_dog.roll_action()
