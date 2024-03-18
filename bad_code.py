def c2f(c):
    f=(c* 9/5)+32
    return f

while 1==1:
    celsius = input("Enter temperature in Celsius: ")
    celsius = float(celsius)
    fahrenheit = c2f(celsius)
    print("Temperature in Fahrenheit: " + str(fahrenheit))
    answer = input("more?")
    if answer=="no":
        break
    