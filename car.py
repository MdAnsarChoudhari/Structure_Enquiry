def car_details():
    name = input("Enter Car Name: ")
    model = input("Enter Car Model: ")
    price = int(input("Enter Car Price: "))
    fuel_type = input("Enter Fuel Type: ")
    mileage = float(input("Enter Mileage (km/l): "))
    run_per_year = int(input("Enter Run per Year (km): "))
    petrol_price = float(input("Enter Petrol Price per liter: "))

    return name, model, price, fuel_type, mileage, run_per_year, petrol_price


def display_car_details(name, model, price, fuel_type, mileage, run_per_year, petrol_price):


    yearly_cost = (run_per_year / mileage) * petrol_price
    normal_limit = 80000


    if yearly_cost > normal_limit:
        decision = "DO NOT BUY (High yearly handling cost)"
    else:
        decision = "BUY (Handling cost is acceptable)"

    details = (
        f"Car Name : {name}\n"
        f"Car Model : {model}\n"
        f"Car Price : {price}\n"
        f"Fuel Type : {fuel_type}\n"
        f"Mileage : {mileage} km/l\n"
        f"Run per Year : {run_per_year} km\n"
        f"Petrol Price : ₹{petrol_price}/liter\n"
        f"Yearly Handling Cost : ₹{yearly_cost:.2f}\n"
        f"Decision : {decision}"
    )

    return details



data = car_details()
print(display_car_details(*data))
