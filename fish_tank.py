length = int(input())
width = int(input())
height = int(input())
percent = float(input())

vol_aquarium = length * width * height
vol_liters = vol_aquarium / 1000
needed_litres = vol_liters * (1-(percent/100))

print(needed_litres)