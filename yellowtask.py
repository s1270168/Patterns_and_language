# input the value
value1 = input("Input a subject ")
value2 = input("Input a first month ")
value3 = input("Input a value of first month ")
value4 = input("Input a second month ")
value5 = input("Input a value of second month ")

# caculate the difference between value3 and value5
trend = int(value5) - int(value3)

# print the main sentence
print(value1 + " is", end=' ')

# Print main sentence
# There are some divided cases depends on difference between value3 and value5
if trend == 0:
    print("equal", end=' ')
elif trend > 0:
    print(str(trend) + " yen up", end=' ')
elif trend < 0:
    print(str(-1 * trend) + " yen down", end=' ')
print("between " + value2 + " and " + value4)