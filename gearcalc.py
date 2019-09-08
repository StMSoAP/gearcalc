#Say what you're going to do

print ("\n" + "Welcome to Zombo.com!" + "\n" + "Wait, that's not right." + "\n" + "\n"
       "Welcome to a simple gearing calculator." + "\n" +
       "Trying to keep your legs from falling off?" + "\n" +
       "This might help." + "\n")

'''implement mode choice here

single-speed

    wants ratio
        have front and back

    has ratio
        has front wants back
        has back wants front

multiple speed

    going to be a lot more work'''

print ("For now I can only help you with single speeds.")

#Ask for input

front = int ( input ("How many teeth are on the chainring? "))
back = int ( input ("How many teeth are on the sprocket? "))

#Manipulate input

ratio = front / back
ratio = float(ratio)

#Return output

print ("\n" + "Your wheel's going to rotate " + str(round(ratio,2)) + " times for every turn of your crank.")

if ratio<2.6:
    print ("Tell your grandkids I say hi!")
elif ratio>3:
    print ("How do you say \"quadzilla\" in Japanese?")
else:
    print ("That's probably pretty good.")
print ("\n")
#End or restart
