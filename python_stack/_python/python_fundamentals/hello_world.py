# tuple1 = (1,2,3,4)
# new = {
#     'name':'ahmed',
#     'last':'nadawy',
#     'age':25
# }


# print(new[0])

#how to access dict (hash table) values
#answer
#new['name']



# 1. TASK: print "Hello World"
# from platform import python_version

print( "Hello World" )
# # 2. print "Hello Noelle!" with the name in a variable
name = "Ahmed"
print( "Hello",name )	# with a comma
print( "Hello"+name )	# with a +
# # 3. print "Hello 42!" with the number in a variable
age = 27
print( "your",age )	# with a comma
print( "your"+str(age) )	# with a +	-- this one should give us an error!
# # 4. print "I love to eat sushi and pizza." with the foods in variables
# # String Interpolation
fave_food1 = "sushi"
fave_food2 = "pizza"
# #string.format()
print("I love to eat {} and {}.".format(fave_food1 ,fave_food2) ) # with .format()
print("I love to eat {1} and {0}.".format(fave_food1 ,fave_food2) ) # with .format()

# #F-Strings (Literal String Interpolation)
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string

# #%-formatting
hw = "Hello %s" % "world" 	# with literal values
print("My name is %s and I'm %d" % (name, age))		# or with variables


#ternary operator  shortcut for conditions   js and other languages are similar and python is different