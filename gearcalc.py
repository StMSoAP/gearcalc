import math

#Say what you're going to do

print ("\n" + "Welcome to Zombo.com!" + "\n" + "Wait, that's not right." + "\n" + "\n"
       "Welcome to a simple gearing calculator." + "\n" +
       "Trying to keep your legs from falling off?" + "\n" +
       "This might help." + "\n")

'''implement mode choice here

single-speed

multiple speed

    going to be a lot more work'''

print ("For now I can only help you with single speeds.")

#Ask for input

front = int ( input ("How many teeth are on the chainring? "))
back = int ( input ("How many teeth are on the sprocket? "))
wheel = int ( input ("What's the diameter of your rear wheel, in mm? "))
crank = int ( input ("And what about your crank length? "))

#Manipulate input

ratio = float (front / back)
gear_inches = ratio * wheel / 25.4
dev_meters = ratio * wheel / 1000 * math.pi
gain_ratio = ratio * wheel / 2 / crank

#Return output

print ("\n" + "Your wheel's going to rotate " + str(round(ratio,2)) + " times for every turn of your crank.")
print ("That's " + str(round(gear_inches,1)) + "\" in gear-inches, if you're into that sort of thing.")
print ("Or " + str(round(dev_meters,2)) + " meters of development.")
print ("Does anyone use Gain Ratio?  Yours is " + str(round(gain_ratio,2)) + ".")

if ratio<2.6:
    print ("Tell your grandkids I say hi!")
elif ratio>3:
    print ("How do you say \"quadzilla\" in Japanese?")
else:
    print ("That's probably pretty good.")
print ("\n")
#End or restart
