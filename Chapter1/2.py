print(" *** Wind classification ***")
speed = float(input("Enter wind speed (km/h) : "))

print("Wind classification is ",end="")
if speed <=51.99 :
    print("Breeze.")
elif speed <=55.99:
    print("Depression.")
elif speed <=101.99:
    print("Tropical Storm.")
elif speed <=208.99:
    print("Typhoon.")
else:
    print("Super Typhoon.")