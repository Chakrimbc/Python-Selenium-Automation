Greet = input("what you want to greet the employee?: ").strip().title()
if Greet == "Good Morning":
    print("Good Morning!.How is your day started?")
elif Greet == "Good Afternoon":
    print("Good Afternoon.Are you feeling hungry?")
else:
    print("Good Evening! It is time to punchout!!")
