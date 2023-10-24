"""i = 0
for i in range(0,11,2):
    print(i)
# range(x,y,z)
# x = the number you start from
# y = the number you end at.
# Note: this excludes the number you have put down (e.g., in this example 11 is excluded)
# z = the step (i.e, how you are going through the list)
# i can be replaced for anything

# how to use for loops for string or list
string = "Hello World"
for letter in string:
    print(letter)

# this print one letter then skip next. it does this until it reach the end of string
for j in range(0,9,2):
    print(string[j])

print("")
# len function
# len is useful when you don't know the length of your string
# for Zain the len function will return 4
print(len("Zain"))
name = input("Enter your name")
for i in range(len(name)-1):
    print(name[i])
"""
# You can even print backwards using -1 as the step
name = "Zain"
for i in range(len(name)-1,-1,-1):
    print(name[i])
