import sys



def display_car_details(name, model, price, fuel_type, mileage, run_per_year, petrol_price):

    yearly_cost = (run_per_year / mileage) * petrol_price
    normal_limit = 80000

    if yearly_cost > normal_limit:
        decision = "DO NOT BUY (High yearly handling cost)"
    else:
        decision = "BUY (Handling cost is acceptable)"

    result = (
        f"Car Name : {name}\n"
        f"Car Model : {model}\n"
        f"Car Price : {price}\n"
        f"Fuel Type : {fuel_type}\n"
        f"Mileage : {mileage} km/l\n"
        f"Run per Year : {run_per_year} km\n"
        f"Petrol Price : {petrol_price}/liter\n"
        f"Yearly Handling Cost : {yearly_cost:.2f}\n"
        f"Decision : {decision}"
    )

    return result


if __name__ == "__main__":
    # Sample data (like your product_details example)
    name = "Honda"
    model = "City"
    price = 1200000
    fuel_type = "Petrol"
    mileage = 18
    run_per_year = 8000
    petrol_price = 100

    print(display_car_details(
        name, model, price, fuel_type, mileage, run_per_year, petrol_price
    ))
