def greet_with(name,location):
    print(f"Hello {name}")
    print(f"are you from {location} ?")

name=input("enter your name: ")
location=input("enter your location: ")
greet_with(location=location,name=name)