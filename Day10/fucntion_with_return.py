def name_formt(fname,lname):
    # name=(fname+" "+lname)
    # print(f"{fname} {lname}")
    # print(name)
    formeted_fname=fname.title()
    formeted_lname=lname.title()
    return f"{formeted_fname} {formeted_lname}"
fname=input("enter your fname:- ")
lname=input("enter your lname:- ")
print(name_formt(fname=fname,lname=lname))

# def function1(text):
#     return text+text

# def function2(text):
#     return text.title()
# print(function2(function1("hello")))