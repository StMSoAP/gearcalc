import math

#Say what you're going to do

print ("\n".join(["", "Welcome to Zombo.com!", "Wait, that's not right.",
                 "", "Welcome to a simple gearing calculator.",
                 "Trying to keep your legs from falling off?",
                 "This might help.", ""]))

#Ask for input

chainrings = []
total_chainrings = int ( input ("How many chainrings do you have? "))
print ("They have teeth, don't they?  How many?")
while len(chainrings) < total_chainrings:
    ring = input ("What about number " + str((1+len(chainrings))) + "? ")
    chainrings.append(ring)

sprockets = []
total_sprockets = int ( input ("And how many sprockets are back there? "))
print ("I'll bet those have teeth, too.  Care to elaborate?")
while len(sprockets) < total_sprockets:
    sprock = input ("How about number " + str((1+len(sprockets))) + "? ")
    sprockets.append(sprock)

wheel = int ( input ("What's the diameter of your rear wheel, in mm? "))

crank = int ( input ("And what about your crank length? "))

#Manipulate input

gearing_matrix = []
while len(gearing_matrix) < total_sprockets:
    temp_ratio = []
    while len(temp_ratio) < total_chainrings:
        ratio = float(chainrings[len(temp_ratio)]) / float(sprockets[len(gearing_matrix)])
        temp_ratio.append(ratio)
    gearing_matrix.append(temp_ratio)

gear_inches_matrix = [[item * wheel / 25.4 for item in row]
    for row in gearing_matrix]

development_meters_matrix = [[item * wheel / 1000 *math.pi for item in row]
    for row in gearing_matrix]

gain_ratio_matrix = [[item * wheel / 2 / crank for item in row]
    for row in gearing_matrix]

#Return output

print ("\n" + "Your wheel's going to rotate these many times for every turn of your crank:")
print ('\n'.join([' '.join(['{:.2f}'.format(item) for item in row]) 
      for row in gearing_matrix]))
print ("Here's gear-inches, if you're into that sort of thing:")
print ('\n'.join([' '.join(['{:.1f}'.format(item) for item in row]) 
      for row in gear_inches_matrix]))
print ("Or meters of development:")
print ('\n'.join([' '.join(['{:.1f}'.format(item) for item in row]) 
      for row in development_meters_matrix]))
print ("Does anyone use Gain Ratio?  Yours is:")
print ('\n'.join([' '.join(['{:.2f}'.format(item) for item in row]) 
      for row in gain_ratio_matrix]))


#End or restart
