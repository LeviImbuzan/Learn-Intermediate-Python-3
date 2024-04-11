# Import necessary functions and variables from other modules
from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define the function calculate_shipping_cost()
def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
    # Unpack coordinates into separate variables
    from_lat, from_long = from_coords
    to_lat, to_long = to_coords
    
    # Calculate the distance between the coordinates
    distance = get_distance(from_lat, from_long, to_lat, to_long)
    
    # Get the shipping rate based on the shipping type
    shipping_rate = SHIPPING_PRICES[shipping_type]
    
    # Calculate the total price for shipping
    price = distance * shipping_rate

    # Format the price and return it
    return format_price(price)

# Test the calculate_shipping_cost() function
test_function(calculate_shipping_cost)

# Define the function calculate_driver_cost()
def calculate_driver_cost(distance, *drivers):
    # Initialize variables for the cheapest driver and their price
    cheapest_driver = None
    cheapest_driver_price = None

    # Iterate through each driver to find the cheapest one
    for driver in drivers:
        # Calculate the time taken for the driver to cover the distance
        driver_time = distance / driver.speed
        
        # Calculate the price for the driver based on their time and salary
        price_for_driver = driver_time * driver.salary
        
        # Update the cheapest driver and their price if necessary
        if cheapest_driver is None:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
        elif price_for_driver < cheapest_driver_price:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
    
    # Return the price and details of the cheapest driver
    return cheapest_driver_price, cheapest_driver

# Test the calculate_driver_cost() function
test_function(calculate_driver_cost)

# Define the function calculate_money_made()
def calculate_money_made(**trips):
    # Initialize variable to store total money made
    total_money_made = 0
    
    # Iterate through each trip and calculate the revenue
    for trip_id, trip in trips.items():
        # Calculate the revenue for each trip
        trip_revenue = trip.cost - trip.driver.cost
        
        # Update the total money made
        total_money_made += trip_revenue
    
    # Return the total money made
    return total_money_made

# Test the calculate_money_made() function
test_function(calculate_money_made)
