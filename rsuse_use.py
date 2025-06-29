products = {"wood":["sofa","chair","bench"],"iron":["iron box","vacuum cleaner"]}
place = {"chennai":["mettukuppam","tidel park","ptc","thiruvanmyur"],"vizag":["akp","kasimkota"]}
distance = {"km":["20km","30km","40km","50km"]}
user_prod = input("what products do you want to search for?: ").strip().lower()
all_products = products["wood"] + products["iron"]
if user_prod in all_products:
    print("product is available")
    user_place = input("From what location you want to seek the product?: " ).strip().lower()
    all_places = place["chennai"] + place["vizag"]
    if user_place in all_places :
        print("product location is available")
        user_distance = input("At what range of distance are you looking for product?: ").strip()
        if user_distance in distance["km"]:
            print("You can book the product")
        else:
            print("sorry the product is not in the range")
    else:
        print("product is not available in this location")
else:
    print("product is not available")