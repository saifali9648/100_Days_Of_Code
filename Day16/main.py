# from time import process_time_ns
# from turtle import Turtle, Screen, color
#
# timmy=Turtle()
# print(timmy)
# my_screen=Screen()
# my_screen.bgcolor("green")
# timmy.color("red")
# timmy.shape("turtle")
# for num in range(1,2):
#     for step in range(50,100):
#             timmy.color("red")
#             timmy.forward(step)
#             timmy.left(90)
#             # timmy.forward(step)
#             # timmy.right(100)
#
#         # timmy.right(50)
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
# table.field_names=["student_name","student_roll","marks"]
# table.add_row(["saif","1322703","90"])
# table.add_row(
# [
#     ["ramu","1322720","96"],
#     ["shanghai","1322702","96"],
#     # ["kaif","1322704","96"],
#     # ["sonu","1322705","96"],
#     # ["jan","1322706","95"],
#     # ["sachin","1322709","96"],
#     # ["dhoti","1322710","96"],
#     # ["Ali","1322711","96"],
# ]
# )
# table.add_column("student_name",["ram", "shyam", "ramu"])
# table.add_column("student_roll",[1322703, 23565, 23564])
# table.add_column("mark", [96, 89, 68])

table.field_names=["student_name", "student_roll", "marks"]
table.add_rows(
[
    ["ramu", "1322720", "96"],
    ["shanghai", "1322702", "96"],
    ["kaif", "1322704", "96"],
    ["sonu", "1322705", "96"],
    ["jan", "1322706", "95"],
    ["sachin", "1322709", "96"],
    ["dhoti", "1322710", "96"],
    ["Ali", "1322711", "96"],
]
)



# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_rows(
#     [
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         ["Sydney", 2058, 4336374, 1214.8],
#         ["Melbourne", 1566, 3806092, 646.9],
#         ["Perth", 5386, 1554769, 869.4],
#     ]
# )




print(table)
