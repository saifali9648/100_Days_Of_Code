score=[34,56,123,546,89,12,3,45,55,102, 544,234,567,27,89,90]
print(score)
for i in score:
    print(i)
high=0
for i in score:
    if i>high:
        high=i
print(f"heighest number is {high}")
print(max(score))    #using max function
