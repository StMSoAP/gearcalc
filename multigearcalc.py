import math

#Say what you're going to do

print ("\n" + "Welcome to Zombo.com!" + "\n" + "Wait, that's not right." + "\n" + "\n"
       "Welcome to a simple gearing calculator." + "\n" +
       "Trying to keep your legs from falling off?" + "\n" +
       "This might help." + "\n")

'''implement mode choice here

    going to be a lot more work

print ("For now I can only help you with single speeds.")
'''

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
#wheel = int ( input ("What's the diameter of your rear wheel, in mm? "))
#crank = int ( input ("And what about your crank length? "))

#Manipulate input

gearing_matrix = []
while len(gearing_matrix) < total_sprockets:
    temp_ratio = []
    while len(temp_ratio) < total_chainrings:
        ratio = float(chainrings[len(temp_ratio)]) / float(sprockets[len(gearing_matrix)])
        temp_ratio.append(ratio)
    gearing_matrix.append(temp_ratio)

#Implement in a minute:        
#gear_inches = ratio * wheel / 25.4
#dev_meters = ratio * wheel / 1000 * math.pi
#gain_ratio = ratio * wheel / 2 / crank

#Return output

#print ("\n", "Your wheel's going to rotate " + str(round(ratio,2)) + " times for every turn of your crank.")
#print ("That's " + str(round(gear_inches,1)) + "\" in gear-inches, if you're into that sort of thing.")
#print ("Or " + str(round(dev_meters,2)) + " meters of development.")
#print ("Does anyone use Gain Ratio?  Yours is " + str(round(gain_ratio,2)) + ".")

print('\n'.join([' '.join(['{:.2f}'.format(item) for item in row]) 
      for row in gearing_matrix]))

#End or restart
