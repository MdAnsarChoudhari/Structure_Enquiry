import sys

if len(sys.argv)==8:
    sctiptname = sys.argv[0]
    name = sys.argv[1]
    model = sys.argv[2]
    price = int(sys.argv[3])
    fuel_type = sys.argv[4]
    mileage = float(sys.argv[5])
    run_per_year = int(sys.argv[6])
    petrol_price = float(sys.argv[7])
else:
    scriptname= sys.argv[0]
    name="xuv700"
    model=2023
    price=1700000   
    fuel_type="petrol"
    mileage=16.5
    run_per_year=15000
    petrol_price=110.0



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
            f"Petrol Price : {petrol_price}/liter\n"
            f"Yearly Handling Cost : {yearly_cost:.2f}\n"
            f"Decision : {decision}"
        )

        return details



    print(display_car_details(name, model, price, fuel_type, mileage, run_per_year, petrol_price))
