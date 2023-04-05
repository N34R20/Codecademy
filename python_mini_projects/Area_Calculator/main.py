"""
Area calculator
"""

print('Sarting calculator... \n')

option = input('Enter C for Circle or T for Triangle \n >')

if option == 'C':
  radius = float(input('enter the radius \n >'))
  area = 3.14159 * (radius ** 2)
  print ("Area: %f" % area)

elif option == 'T':
  base = float(input('enter the base \n>'))
  height = float(input('enter the height \n>'))
  area = base * height * 0.5
  print ("Area: %f" % area)
else:
  print ("Error! Invalid shape.")

print("Exiting...")
