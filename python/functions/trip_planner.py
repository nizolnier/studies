def trip_planner_welcome(name):
    print("welcome to trip planner, " + name)

trip_planner_welcome("nicole")

def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time

estimate = estimated_time_rounded(2.5)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "car"):
    print("your trip starts off in " + origin)
    print("and you are traveling to " + destination)
    print("you will be traveling by " + mode_of_transport)
    print("it will take approximately " + str(estimated_time) + " hours")

destination_setup("brazil", "united states", estimate)