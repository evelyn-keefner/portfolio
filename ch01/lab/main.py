import random

# Part A
weeks = 16
print("Weeks:", weeks, type(weeks))

classes = 5
print("Classes:", classes, type(classes))

tuition = 6000
print("Tuition:", tuition, type(tuition))

cost_per_week = (tuition / classes) / weeks
print("Cost per week:", cost_per_week, type(cost_per_week))

classes_per_week = 2
print("Classes per week:", classes_per_week, type(classes_per_week))

cost_per_class = cost_per_week / classes_per_week
print("Cost per class:", cost_per_class, type(cost_per_class))

# Part B
my_list = [16, 3, "Turmoil", 3.0, "Complacent"]

random_selection = random.choice(my_list)
print(random_selection)


