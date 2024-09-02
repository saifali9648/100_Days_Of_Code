print("wellcome to the tip calculator")
total_bill=float(input("what was the total bill?"))
tip=int(input("How much tip would you like to give?"))
number_of_people=int(input("How many people to split the bill?"))
tip_percentage=(total_bill*tip)/100
final_bill=total_bill+tip_percentage
per_people_bill=final_bill/number_of_people
print(f"Each person should pay= {round(per_people_bill,2)}")