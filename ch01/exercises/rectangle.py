shape = 'hexagon'
sides = 6

internal_angle_sum = (sides - 2) * 180
external_angle_sum = 360 / sides
angle_sum = internal_angle_sum / sides

print("The shape", shape, "has internal angles which measure", angle_sum, "degrees.")
print("The shape " + shape + " has external angles which measure " + str(external_angle_sum) + " degrees.")
