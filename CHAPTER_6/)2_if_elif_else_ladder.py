a = int(input("Enter your age: "))

# If elif else ladder
if (a >= 18):
    print("You are above the age of concent")  #indent = the space after we enter the if or any other condition
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")

else:
    print("You are below the age of concent")

print("End of Program")
