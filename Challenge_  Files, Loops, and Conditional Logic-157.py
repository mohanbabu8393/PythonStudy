## 3. Read the File Into a String ##

f=open('dq_unisex_names.csv','r')
names=f.read()
rows=names.split('\n')

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list=names.split("\n")

first_five=names_list[0:5]

print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list=[]

for row in names_list:
    comma_list=row.split(',')
    nested_list.append(comma_list)
    
print(nested_list[0:5])

## 6. Convert Numerical Values ##

print(nested_list[0:5])

numerical_list=[]

for values in nested_list:
    name=values[0]
    count=float(values[1])
    new_list=[name,count]
    numerical_list.append(new_list)
    
print(numerical_list[0:5])


## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]

thousand_or_greater=[]

for name in numerical_list:
    if(name[1]>=1000):
        thousand_or_greater.append(name[0])
    
print(thousand_or_greater[1:10])