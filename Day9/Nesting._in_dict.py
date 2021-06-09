# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary

travel_log ={
    "France" :["Paris", "Lille," "Dijon"],

    # Or we can use dict in list for nesting like below
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12}
}

# Nesting a disctionary in a List
travel_log =[
   {
       "country": "France", 
       "cities_visited"  :["Paris", "Lille," "Dijon"],
        "total_vistis":5 
        },

    {
        "country" :"Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 12
        },
]

print(travel_log)