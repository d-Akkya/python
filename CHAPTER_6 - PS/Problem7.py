post = input("Enter the post: ")

#user is writing like akkya, aKya then use:
if("Akkya".lower() in post.lower()):
    print("This post is talking about Akkya")
else:
    print("This post is not talking about Akkya")