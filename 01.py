Fahrenheit = 0

Celsius = (Fahrenheit - 32) * 5.0/9.0
print("0 Degrees Fahrenhiet is " + str(Celsius) + " Celcius.")
Fahrenheit = 100

Celsius = (Fahrenheit - 32) * 5.0/9.0
print("100 Degrees Fahrenhiet is " + str(Celsius) + " Celcius.")

age_in_yrs = 14
secs_in_min = 60
mins_in_hr = 60
hrs_in_day = 24
days_in_yr = 365
age_in_secs = age_in_yrs * days_in_yr * hrs_in_day * mins_in_hr * secs_in_min
print("I am " + str(age_in_secs) + " seconds old!")

age_in_yrs = 50
age_in_secs = age_in_yrs * days_in_yr * hrs_in_day * mins_in_hr * secs_in_min
print("You are " + str(age_in_secs) + " seconds old!")

age_in_yrs = 9
age_in_secs = age_in_yrs * days_in_yr * hrs_in_day * mins_in_hr * secs_in_min
print("Your dog is " + str(age_in_secs) + " seconds old!")

radius = 6
sarea = (radius ** 2) * (4 * 3.14)
print("The surface area is " + str(sarea) + " when the radius is 6.")
radius = 6
volume = (radius ** 3) * (1.333333 * 3.1415)
print("The volume is " + str(volume) + " when the radius is 6.")

radius = 18
sarea = (radius ** 2) * (4 * 3.14)
print("The surface area is " + str(sarea) + " when the radius is 18.")

radius = 18
volume = (radius ** 3) * (1.333333 * 3.1415)
print("The volume is " + str(volume) + " when the radius is 18.")

an_int = 13579
num = an_int % 10000 % 1000 // 100
print("The third digit of 13579 is " + str(num) + ".")
another_int = 246810
num1 = another_int % 100000 % 10000 // 1000
print("The third digit of 246810 is " + str(num1) + ".")
