def name_formt(fname,lname):
    if fname=="" and lname=="":
        return "you should have to give the fname and lname"
    elif fname==fname and lname=="":
        return "you should have to give the lname"
    else:
        return "you should have to give the fname"
    # name=(fname+" "+lname)
    # print(f"{fname} {lname}")
    # print(name)
    formeted_fname=fname.title()
    formeted_lname=lname.title()
    return f"{formeted_fname} {formeted_lname}"
fname=input("enter your fname:- ")
lname=input("enter your lname:- ")
print(name_formt(fname=fname,lname=lname))