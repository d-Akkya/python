marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# Check for total percentage
totalPercentage = ((marks1 + marks2 + marks3)/300)*100

if(totalPercentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed:", totalPercentage)

else:
    print("You are Failed!", totalPercentage)