## 1. Overview ##

f=open("movie_metadata.csv","r")
data=f.read()
rows=data.split('\n')

movie_data=[]

for row in rows:
    values=row.split(",")
    movie_data.append(values)

## 3. Writing Our Own Functions ##

def getmovie_name(movie_data1):
    movie_name=[]
    for movie in movie_data1:
        movie_name.append(movie[0])
    return movie_name
    
movie_names = getmovie_name(movie_data)
print(movie_names[0:5])

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False
wonder_woman_usa = is_usa(wonder_woman)
        
    
    

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False
    
    
def index_equals_str(input_list, index , string_value):
    if input_list[index] == string_value:
        return True
    else:
        return False
    
    
wonder_woman_in_color=index_equals_str(wonder_woman, 2, 'Color')

print(wonder_woman_in_color)
    

## 6. Optional Arguments ##

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt
def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt


num_of_us_movies = feature_counter(movie_data,6,"USA",True)

