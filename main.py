# print(2+4)
# print(type(2+4))
# print(2**3)
# print(2//4)
# print(3//4)
#print(5//4)
# print(round(3.4))
# print(abs(-10))
# print("Hello {}, your balance is {}.".format("Cindy", 50))
#
# print("Hello {0}, your balance is {1}.".format("Cindy", 50))
#
# print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
#
# print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))


str= "01234567"

#[strat:stop:step over]
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


a,*b,c=[1,2,3,4,5,6,7]
print(a)
print(b)
print(c)


dictionary={
    'name': [1,2,3],
    'greeting':'hello',
    'age': 20
}
print ( 'name' in dictionary.keys())
print ( 'hello' in dictionary.values())



#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

#2 iterate and print all the keys in the above user.

#3 Add a new weapon to your user

#4 Add a new key to include 'is_banned'. Set it to false

#5 Ban the user by setting the previous key to True

#6 create a new user2 my copying the previous user and update the age value and username value.

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

school = {'Bobby','Tammy','Jammy','Sally','Danny'}

#during class, the teachers take attendance and compile it into a list.
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']