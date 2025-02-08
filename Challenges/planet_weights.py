# HARD level

e_weight = float(input("What is your Weight on Earth? "))
planet = int(input("What is the Planet number? "))

if planet == 1:
  planet_name = str("Mercury")
  r_gravity = 0.38
elif planet == 2:
  planet_name = str("Venus")
  r_gravity = 0.91
elif planet == 3:
  planet_name = str("Mars")
  r_gravity = 0.38
elif planet == 4:
  planet_name = str("Jupiter")
  r_gravity = 2.53
elif planet == 5:
  planet_name = str("Saturn")
  r_gravity = 1.07
elif planet == 6:
  planet_name = str("Uranus")
  r_gravity = 0.89
elif planet == 7:
  planet_name = str("Neptune")
  r_gravity = 1.14
else:
  print('Invalid planet number')
  exit(1)

d_weight= e_weight * r_gravity

print(f"Your Weight on {planet_name} is {d_weight}")