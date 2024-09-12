# travel_log={
#     "france": ["paris","lille","dijon"],
#     "germany": ["stuttgart","berlin"]
# }
# print(travel_log["france"][1])

# nested_list=["a","b",["c","d"]]
# print(nested_list[2][0])

travel_log={
    "france": {
        "cities_visited": ["paris","lille","dijon"],
        "total_visites":12
    },
    "germany": {
        "cities_visited": ["berlin","humburg","stuttgart"],
        "total_visites":5
    }
}
print(travel_log["germany"]["cities_visited"][2])