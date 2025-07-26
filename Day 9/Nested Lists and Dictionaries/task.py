capitals = {
    "France": "Paris",
    "Germany":"Berlin"
}

#travel_log = {
 #   "France" : ["Paris","Lille","Dijon"],
  #  "Germany":["Stuttgart","Berlin"]
#}
#print(travel_log["France"][1])

nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])


travel_log = {
     "France" : {
         "num_times_visit":8,
         "cities_visited":["Paris","Lille","Dijon"]
     },
     "Germany":["Stuttgart","Berlin"],
    "India":{
        "visited":8,
        "cities":["Up","Mp","Ujjain"]
    }
}
print(travel_log["India"]["cities"])