from car import display_car_details

def test_display_car_details():
    expected_output = (
        "Car Name : Honda\n"
        "Car Model : City\n"
        "Car Price : 1200000\n"
        "Fuel Type : Petrol\n"
        "Mileage : 18 km/l\n"
        "Run per Year : 8000 km\n"
        "Petrol Price : 100/liter\n"
        "Yearly Handling Cost : 44444.44\n"
        "Decision : BUY (Handling cost is acceptable)"
    )

    assert display_car_details(
        "Honda", "City", 1200000, "Petrol", 18, 8000, 100
    ) == expected_output
