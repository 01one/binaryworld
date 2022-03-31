x=str(input("Enter In which scale you measured temperature (Celsius, Fahrenheit, Kelvin)? Enter C or F or K: "))



if x=="C" or x=="c":
    c=eval(input("Enter your temperature in Celsius scale: "))
    to_fahrenheit=(9*c+160)/5
    to_kelvin=c+273
    print("Celsius :", c,  "\nFahrenheit :", to_fahrenheit,  "\nKelvin: ", to_kelvin)
    
elif x=="F" or x=="f":
    f=eval(input("Enter your temperature in Fahrenheit scale: "))
    to_celsius=(5*f-160)/9
    to_kelvin=((5*f-160)/9)+273
    print("Celsius :", to_celsius,  "\nFahrenheit :", f,  "\nKelvin: ", to_kelvin)
    

elif x== "K" or x=="k":
    k=eval(input("Enter your temperature in Kalvin scale: "))
    to_celsius=k-273
    to_fahrenheit=(9*(k-273)+160)/5
    print("Celsius :", to_celsius,  "\nFahrenheit :", to_fahrenheit,  "\nKelvin: ", k)

    






""" Advanced
x=str(input("Enter In which scale you measured temperature (Celsius, Fahrenheit, Kelvin)? Enter C or F or K: "))


if x=="C" or x=="c":
    c=eval(input("Enter your temperature in Celsius scale: "))
    to_fahrenheit=(9*c+160)/5
    to_kelvin=c+273
    while to_kelvin<0:
        print("Temperature can not be less than absolute zero")
        c=eval(input("Enter your temperature in Celsius scale: "))
        to_fahrenheit=(9*c+160)/5
        to_kelvin=c+273
        
    else:
        print("Celsius :", c,  "\nFahrenheit :", to_fahrenheit,  "\nKelvin: ", to_kelvin)
    
elif x=="F" or x=="f":
    f=eval(input("Enter your temperature in Fahrenheit scale: "))
    to_celsius=(5*f-160)/9
    to_kelvin=((5*f-160)/9)+273
    while to_kelvin<0:
        print("Temperature can not be less than absolute zero")
        f=eval(input("Enter your temperature in Fahrenheit scale: "))
        to_celsius=(5*f-160)/9
        to_kelvin=((5*f-160)/9)+273
    else:
        print("Celsius :", to_celsius,  "\nFahrenheit :", f,  "\nKelvin: ", to_kelvin)
    

elif x== "K" or x=="k":
    k=eval(input("Enter your temperature in Kalvin scale: "))
    while k<0:
        print("Temperature can not be less than absolute zero")
        k=eval(input("Enter your temperature in Kalvin scale: "))
    else:
        to_celsius=k-273
        to_fahrenheit=(9*(k-273)+160)/5
        print("Celsius :", to_celsius,  "\nFahrenheit :", to_fahrenheit,  "\nKelvin: ", k)"""
