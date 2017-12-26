## 1. Booleans ##

cat = True
dog = False

print(type(cat))

## 2. Boolean Operators ##

print(cities)

first_alb = (cities[0] == "Albuquerque")
second_alb = (cities[1] == "Albuquerque")
first_last = (cities[0] == cities[72])

## 5. If Statements ##

result = 0

if (cities[2] == "Anchorage"):
    result =1

## 6. Nesting If Statements ##

both_conditions = False

if crime_rates[0] > 50:
    if crime_rates[1] > 300:
        both_conditions = True

## 7. If Statements and For Loops ##

five_hundred_list = []

for cr in crime_rates:
    if cr>500:
        five_hundred_list.append(cr)





## 8. Find the Highest Crime Rate ##

print(crime_rates)
highest = crime_rates[0]
for cr in crime_rates:
    if cr > highest:
        highest = cr