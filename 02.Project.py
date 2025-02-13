import math

def great_circle_distance(r, x1, y1, x2, y2):
    
    x1 = x1 * math.pi / 180
    y1 = y1 * math.pi / 180
    x2 = x2 * math.pi / 180
    y2 = y2 * math.pi / 180
    
    distance = r * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
    
    distance = round(distance, 2)
    return distance

r = float(input("Enter Radius of Sphere: "))
x1 = float(input("Starting Point - Enter Latitude: "))
y1 = float(input("Starting Point - Enter Longitude: "))
x2 = float(input("Ending Point - Enter Latitude: "))
y2 = float(input("Ending Point - Enter Longitude: "))

distance = great_circle_distance(r, x1, y1, x2, y2)

print(f"The Great Circle Distance is {distance:.2f}")