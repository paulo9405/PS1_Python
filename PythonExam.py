while True:
    # get age and price
    age = int(input("Please enter your age: "))
    price = float(input("Price of the product: "))

    # discount
    age_discount = 0
    promotion_discount = 0

    # discount based in their age
    if age < 18:
        age_discount = price * 0.10
        price -= age_discount

    # applying discount
    if price > 100:
        promotion_discount = 10
        price -= promotion_discount

    # outputs
    print(f"\nPrice: €{price:.2f}.")
    if age_discount > 0 and promotion_discount > 0:
        print("You earned: 10% discount and €10 promotion discount.")
    elif age_discount > 0:
        print("You earned: 10% off.")
    elif promotion_discount > 0:
        print("You earned: €10 promotion discount.")
    else:
        print("You earned: No discounts or promotions.")

    # Ask if user wanna add another customer
    another = input("\nWould you like to enter another customer? (yes/no): ").strip().lower()
    if another == "no" or 'n':
        print("Exiting program.")
        break


