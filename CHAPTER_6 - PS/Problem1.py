user1 = int(input("Enter number 1: "))
user2 = int(input("Enter number 2: "))
user3 = int(input("Enter number 3: "))
user4 = int(input("Enter number 4: "))

if(user1>user2 and user1>user3 and user1>user4):
    print(f"Greatest no. is user1: {user1}")

elif(user2>user1 and user2>user3 and user2>user4):
    print(f"Greatest no. is user2: {user2}")

elif(user3>user1 and user3>user2 and user3>user4):
    print(f"Greatest no. is user3: {user3}")

elif(user4>user1 and user4>user2 and user4>user3):
    print(f"Greatest no. is user4: {user4}")