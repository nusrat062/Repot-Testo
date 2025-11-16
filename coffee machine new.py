def main():
    menu = {
        "cappuccino": {
            "ingredients": {"water": 200, "milk": 100, "coffee": 24},
            "price": 150  
        },
        "latte": {
            "ingredients": {"water": 200, "milk": 150, "coffee": 24},
            "price": 180
        },
        "espresso": {
            "ingredients": {"water": 50, "milk": 0, "coffee": 18},
            "price": 120
        }
    }
    resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
    coin_values = {"r1": 1, "r2": 2, "r5": 5, "r10": 10, "r100": 100}
    while True:
        order = input("\nWhat would you like? (cappuccino/latte/espresso) Type 'report' or 'off': ").strip().lower()

        if order == "off":
            print("Shutting down.")
            break

        if order == "report":
            print(
                f"We have the following resources:\n"
                f"Water: {resources['water']}ml\n"
                f"Milk: {resources['milk']}ml\n"
                f"Coffee: {resources['coffee']}g\n"
                f"Money: Rs {resources['money']}"
            )
            continue

        if order not in menu:
            print("Unknown selection. Please choose a valid drink.")
            continue

        needed = menu[order]["ingredients"]
        lacking = [k for k, amt in needed.items() if resources.get(k, 0) < amt]
        if lacking:
            print("Resources insufficient! Not enough:", ", ".join(lacking))
            continue

        price = menu[order]["price"]
        print(f"Please pay Rs {price}. Insert coins:")
        total = 0
        for key, val in (("Rs.5", 5), ("Rs.10", 10), ("Rs.100", 100)):
            try:
                count = input(f"Insert {key} coins (enter 0 if none): ").strip()
                count = int(count) if count != "" else 0
                if count < 0:
                    print("Negative count treated as 0.")
                    count = 0
            except ValueError:
                print("Invalid input treated as 0.")
                count = 0
            total += count * val
        print(f"Total inserted: Rs {total}")
        if total < price:
            print("Payment not complete. Transaction cancelled. Money refunded.")
            continue
        for k, amt in needed.items():
            resources[k] -= amt

        resources["money"] += price
        change = total - price
        if change > 0:
            print(f"Here is your change: Rs {change}")
        print("Transaction successful. Here is your coffee ☕")
if __name__ == "__main__":
    main()