test_string1 = "python"
res = len(test_string1.split())
print ("The number of words in string1 : ",res)
test_string2 = "is an"
res =len(test_string2.split())
print ("the number of words in string2 :",res)
test_string3= "interactive language"
res=len(test_string3.split())
print("the number of words in string3:",res)
list=[len(test_string1.split()),len(test_string2.split()),len(test_string3.split())]
print( max(list))
