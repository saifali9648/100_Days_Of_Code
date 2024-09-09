def calculate_love_score(name1,name2):
    name_list=name1+name2
    t=0
    r=0
    u=0
    e=0
    l=0
    o=0
    v=0
    for i in name_list:
        if i=="t":
            t+=1
        elif i=="r":
            r+=1
        elif i=="u":
            u+=1
        elif i=="e":
            e+=1
        elif i=="l":
            l+=1
        elif i=="o":
            o+=1
        elif i=="v":
            v+=1
        elif i=="e":
            e+=1
    print(f"T occurs {t} times\nR occurs {r} times\n U occurs {u} times\nE occurs {e} times")
    total_of_true=str(t+r+u+e)
    print(f"Total= {total_of_true}")
    print(f"L occurs {l} times\nO occurs {o} times\n V occurs {v} times\nE occurs {e} times")
    tota_of_love=str(l+o+v+e)
    print(f"Total= {tota_of_love}")
    love_socre=total_of_true+tota_of_love
    print(f"Total love score {love_socre}")
        

Name1=input("enter your bf/gf name: ")
Name2=input("enter your bf/gf name: ")
calculate_love_score(name1=Name1,name2=Name2)