# print(2+4)
# print(type(2+4))
# print(2**3)
# print(2//4)
# print(3//4)
# print(5//4)
# print(round(3.4))
# print(abs(-10))
# print("Hello {}, your balance is {}.".format("Cindy", 50))
#
# print("Hello {0}, your balance is {1}.".format("Cindy", 50))
#
# print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
#
# print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

#
# str= "01234567"

# [strat:stop:step over]
# print (str[0:3])
# print (str[0:7:2])
#
# quote="to be or not to be"
#
# print (quote.upper())
# print (quote.capitalize())
# print (quote.find("be"))
# print (quote.replace("be","me"))

# user=input("user name")
# ps=input ("password")
#
# print (f"{user} your password {'*' * len(ps)} is  {len(ps)} letters long")

# i=10
# b=10
# while (i>1):
#     astrik= (2*(10-b))+1
#     print (f"{' '* i} {'*'*astrik}")
#     i-=1
#     b-=1
# c=1
# while(c<3):
#     print(f"{' '* 8} {'*'*5}")
#     c+=1

# basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# print(basket[1][1][0])
#
# basket = ['a','b', 'c', 'd', 'e'];
# print ("c" in basket)

# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#
# # 1. Remove the Banana from the list
#
# # 2. Remove "Blueberries" from the list.
#
# # 3. Put "Kiwi" at the end of the list.
#
# # 4. Add "Apples" at the beginning of the list
#
# # 5. Count how many apples in the basket
#
# # 6. empty the basket
# basket.remove("Banana")
# basket.pop()
# basket.append("kiwi")
# basket.insert(0,'Apples')
# print(basket)
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

#
# sentence= '!'
# new_sentence= sentence.join(['hi', 'my','name', 'is', 'john'])
# print (new_sentence)
#
#
# new_sentence1= "!".join(['hi', 'my','name', 'is', 'john'])
# print (new_sentence1)
#
#
# #fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
#
# friends.append('Stanley')
# friends.sort()
# print(friends)
#
# friends1 = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
#
# new_friend = ['Stanley']
# friends1+= new_friend
# friends1.sort()
# print(friends1)

#
# a,*b,c=[1,2,3,4,5,6,7]
# print(a)
# print(b)
# print(c)
#
#
# dictionary={
#     'name': [1,2,3],
#     'greeting':'hello',
#     'age': 20
# }
# print ( 'name' in dictionary.keys())
# print ( 'hello' in dictionary.values())


# 1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

# 2 iterate and print all the keys in the above user.

# 3 Add a new weapon to your user

# 4 Add a new key to include 'is_banned'. Set it to false

# 5 Ban the user by setting the previous key to True

# 6 create a new user2 my copying the previous user and update the age value and username value.

#
# dictionary={
#     'age':20,
#     'username':"bek",
#     'weapons':['sword', "dagger"],
#     'is_active': True,
#     'clan': 'nots'
# }
# print ( dictionary.keys())
# #dictionary.update({'weapons':['sworrd', "dagger",'saber']})
# dictionary['weapons'].append('shield')
# print ( dictionary)
# dictionary.update({'is_banned':False})
# print ( dictionary)
# dictionary.update({'is_banned':True})
# print ( dictionary)
#
# user2=dictionary.copy()
# user2.update({'age':45})
# user2.update({'username':'toro'})
# # user2.update({'age': 45, 'username': 'Toro'})
# print ( user2)

# #Scroll to bottom to see solution
# # You are working for the school Principal. We have a database of school students:
# school = {'Bobby','Tammy','Jammy','Sally','Danny'}
#
# #during class, the teachers take attendance and compile it into a list.
# attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']
#
# #using what you learned about sets, create a piece of code that the school principal can use to immediately
# # find out who missed class so they can call the parents. (Imagine if the list had 1000s of students.
# # The principal can use the lists generated by
# # the teachers + the school database to use python and make his/her job easier): Find the students
# # that miss class!
#
# print(school.difference(attendance_list))
# #Solution: Notice how we don't have to convert the attendance_list to a set...it does it for you.
# #print(school.difference(attendance_list))
#
# #Ternary Operator
# is_tall= True
# print('Tall' if is_tall else 'short')
#
# user={
#     'name': "Abed",
#     'age ': 20,
#     'is racist': True
#
# }
#
# for item in user:
#     print (item)
#
# for item in user.items():
#     print (item)
#
# for item in user.keys():
#     print (item)
#
# for item in user.values():
#     print(item)
#
# for key, value in user.items():
#     print (key, value)
#
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
# i=0
# string=''
# while i<6:
#     j = 0
#     while j<7:
#         if picture[i][j]==0:
#             print(" ", end='')
#         else:
#             print("*", end='')
#         j+=1
#     print('')
#
#
#     i+=1
#
#
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# for char in some_list:
#     checker=some_list.count(char)
#     if (checker>1):
#         print (char+ ' is a duplicate')
#         some_list.remove(char)
#
#
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#             duplicates.append(value)
#
# print(set(duplicates))

#
# # Function 101
# def say_hello(name, emoji):
#     print(f'hello {name} {emoji}')
#
# # positional argument
# say_hello('bek',':)')
#
# #keyword argument
#
# say_hello(emoji=':)',name='bek')
#
# #default parametes
# def say_hello(name="darth", emoji=':('):
#     print(f'hello {name} {emoji}')
#
# # positional argument
# say_hello('bek',':)')
# say_hello()
# say_hello('happy')
# say_hello(emoji=':0')

# age = input("What is your age?: ")
#
# if int(age) < 18:
# 	print("Sorry, you are too young to drive this car. Powering off")
# elif int(age) > 18:
# 	print("Powering On. Enjoy the ride!");
# elif int(age) == 18:
# 	print("Congratulations on your first year of driving. Enjoy the ride!")

# 1. Wrap the above code in a function called checkDriverAge(). Whenever you call t
# his function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an
# argument of age, so that if you enter:
# checkDriverAge(92);
# it returns "Powering On. Enjoy the ride!"
# also make it so that the default age is set to 0 if no argument is given.

# def checkDriverAge(age=0):
#     p=""
#     if int(age) < 18:
#         p= "Sorry, you are too young to drive this car. Powering off"
#     elif int(age) > 18:
#         p="Powering On. Enjoy the ride!"
#     elif int(age) == 18:
#         p= "Congratulations on your first year of driving. Enjoy the ride!"
#     return print(p)
#
# checkDriverAge(95)

# def highest_even(li):
#     even=[]
#     for item in li:
#         if item%2==0:
#             even.append(item)
#     print (even)
#     j=1
#     highet = even[0]
#     while j<len(even):
#
#         if even[j]>highet:
#                highet=even[j]
#                j+=1
#
#         else:
#
#             j+=1
#     return print(highet)
#
# highest_even([10,8,5,3,7,2,11,12,14])


# class playerCharacter:
#     membership= True
#     def __init__(self, name ,age):
#         self.a=name
#         self.b=age
#
# player1= playerCharacter('Cindy', 20)
# player1.membership= False
#
# print(player1.a)
# print(player1.membership)

# 1 Instantiate the Cat object with 3 cats



# 2 Create a function that finds the oldest cat



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# def oldestCat(list):
#         return max(list)
#
# cat1 = Cat('tokyo', 3)
# cat2 = Cat('simp', 2)
# cat3 = Cat('toro', 4)
#
#
#
# cats = [cat1.age, cat2.age, cat3.age]
#
#
# print(f"The oldest cat is {oldestCat(cats)} years old.")


# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def adding(cls, num1, num2):
#         return cls('ted', num1+num2)
#
# pcat3=Cat.adding(2,3)
#
# print(pcat3.age)

# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Garfild(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# simon=Simon('simon', 4)
# sally=Sally('sally', 6)
# garfield=Garfild('garfield', 3)
# my_cats= [simon,sally,garfield]
#
# my_pets= Pets(my_cats)
# my_pets.walk()
#
# #1 Add nother Cat
#
# #2 Create a list of all of the pets (create 3 cat instances from the above)
#
#
# #3 Instantiate the Pet class with all your cats use variable my_pets
#
# #4 Output all of the cats walking using the my_pets instance
#
# class SuperList(list):
#
#     def __len__(self):
#         return 1000
#
# super_list=SuperList()
# print(len(super_list))


# def func1(li):
#     new_list=[]
#     for item in li:
#         new_list.append(item*2)
#
#     return new_list
#
# print(func1([1,2,3,4]))


# def func1(item):
#     return item*2
#
# print(list (map(func1, [1,2,3,4])))
#
# def func1(item):
#     return item*2
#
# def odd(ii):
#     return ii % 2== 0
#
# print(list (filter(odd, [1,2,3,4])))



# from functools import reduce
#
# #1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']
# def capitalize(item):
#     return item.upper()
#
# print(list(map(capitalize,my_pets)))
#
# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]
# my_numbers.sort()
#
# print (list(zip(my_numbers, my_strings)))
#
# # better to use
# #
# # print(list(zip(my_strings, sorted(my_numbers))))
# #
# # because sorted() doesnt affect the original list
#
#
# #3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]
#
# def passed(pp):
#     return pp>50
#
# print(list(filter(passed,scores)))
#
# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
#
# def accumulator(acc, item):
#     return acc+item
#
# print(reduce(accumulator, (my_numbers+ scores)))
#
# my_pets = ['sisi', 'bibi', 'titi', 'carla']
#
# print(list(map(lambda item: item.upper(), my_pets)))

# print(list(map(lambda num: num**2, [1,2,3])))
#
# a = [(0, 2), (5, 2), (9, 9), (10, -1)]
# a.sort(key=lambda x: x[1])
#
# print(a)
#
# my_list=[num for num in range (0,20)]
# my_list1=[2*num for num in range (0,20)]
# my_list2=[2*num for num in range (0,20) if num %2==0]
#
# print(my_list)
# print(my_list1)
# print(my_list2)

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
#
# duplicates={dup for dup in  some_list if some_list.count(dup) >1 }
# print(list(duplicates))

#performance decorator.
# from time import time
# def performance(fn):
#   def wrapper(*args, **kwargs):
#     t1 = time()
#     result = fn(*args, **kwargs)
#     t2 = time()
#     print(f'took {t2-t1}')
#     return result
#   return wrapper
#
# @performance
# def long_time():
#     for i in range(10000):
#         i*5
#
# long_time()

# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': False #changing this will either run or not run the message_friends function.
# }
#
# def authenticated(fn):
#   # code here
#   def test(x):
#     if bool(x['valid']) == True:
#       fn(x)
#
#   return test
#
# @authenticated
# def message_friends(user):
#     print('message has been sent')
#
# message_friends(user1)

from time import time
def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(100000):
        i*5
@performance
def long_time2():
    print('2')
    for i in list(range(100000)):
        i*5


long_time()
long_time2()

