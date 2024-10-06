a = int(input("Enter your age: "))

# It statement no.1
if(a%2 == 0):
    print("Age is Even")
# End of If statement no.1

# If statement no.2
if (a >= 18):
    print("You are above the age of concent")  #indent = the space after we enter the if or any other condition
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

else:
    print("You are below the age of concent")
# End of If statement no.2

print("End of Program")