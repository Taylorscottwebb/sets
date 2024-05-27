# Task 1

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

mutual_airlines = our_routes.intersection(competitor_routes)
print(mutual_airlines)

exclusive_airlines = our_routes.difference(competitor_routes)
print(exclusive_airlines)

exclusive_airlines = competitor_routes.difference(our_routes)
print(exclusive_airlines)

unique_airlines = our_routes.symmetric_difference(competitor_routes)
print(unique_airlines)

# Task 2

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

no_dupes = set(customer_ids)
print(no_dupes)