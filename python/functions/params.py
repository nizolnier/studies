# def my_function(single_param):

def generate_trip_instructions(location):
    print("looks like you are planning a trip to " + location)
    print("you can use the public subway system to get to " + location)


generate_trip_instructions("central park")

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time 
    hotel_total = (hotel_rate * trip_time) - 10
    print(car_rental_total + hotel_total + plane_ticket_price)

calculate_expenses(200, 100, 100, 5)

def trip_planner(first_destination, second_destination, final_destination = "code academy hq"):
    print("here is what the trip will look like!")
    print("first we will stop in " + first_destination + ", then " + second_destination + ", and lastly" + final_destination)

trip_planner("france", "germany", "denmark")

trip_planner("brooklyn", "queens")

trip_planner(first_destination="iceland", final_destination="germany", second_destination="india")
