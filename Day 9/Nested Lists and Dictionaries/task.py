# my_dictionary = {
#     "Dialogue": ["Hmm"],
#     "Normal Dialogue": "Hey"
# }
#
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }
#
#
# travel_log = {
#   "France": {
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "total_visits": 12
#    },
#   "Germany": {
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "total_visits": 5
#    },
# }
#
# print(travel_log["Germany"]["cities_visited"][2])
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["dessert"][1])