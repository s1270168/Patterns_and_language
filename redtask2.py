import numpy as np
import matplotlib as plt

# input values
while True:
    print('Input "Item"')
    subject = input()
    try:
        int(subject)
        print("\nyour input is invalid")
        print("Input again\n")
        continue
    except:
        break
while True:
    print('Input "month1 value1"')
    try:
        month1, value1 = input().split(" ")
        try:
            int(month1)
            print("\nyour input is invalid")
            print("month1 should NOT be number\n")
            continue
        except:
            try:
                int(value1)
                break
            except:
                print("\nyour input is invalid")
                print("value1 should be number\n")
                continue
    except ValueError:
        print("\nyour input is invalid")
        print("between month1 and value1, 1 space is needed")
        print("Input again\n")
        continue
while True:
    print('Input "month2 value2"')
    try:
        month2, value2 = input().split(" ")
        try:
            int(month2)
            print("\nyour input is invalid")
            print("month2 should NOT be number\n")
            continue
        except:
            try:
                int(value2)
                break
            except:
                print("\nyour input is invalid")
                print("value2 should be number\n")
                continue
    except ValueError:
        print("\nyour input is invalid")
        print("between month2 and value2, 1 space is needed")
        print("Input again\n")
        continue
while True:
    print('Input "month3 value3"')
    try:
        month3, value3 = input().split(" ")
        try:
            int(month3)
            print("\nyour input is invalid")
            print("month3 should NOT be number\n")
            continue
        except:
            try:
                int(value3)
                break
            except:
                print("\nyour input is invalid")
                print("value3 should be number\n")
                continue
    except ValueError:
        print("\nyour input is invalid")
        print("between month3 and value3, 1 space is needed")
        print("Input again\n")
        continue
while True:
    print('Input "month4 value4"')
    try:
        month4, value4 = input().split(" ")
        try:
            int(month4)
            print("\nyour input is invalid")
            print("month4 should NOT be number\n")
            continue
        except:
            try:
                int(value4)
                break
            except:
                print("\nyour input is invalid")
                print("value4 should be number\n")
                continue
    except ValueError:
        print("\nyour input is invalid")
        print("between month4 and value4, 1 space is needed")
        print("Input again\n")
        continue
while True:
    print('Input "month5,value5"')
    try:
        month5, value5 = input().split(" ")
        try:
            int(month5)
            print("\nyour input is invalid")
            print("month5 should NOT be number\n")
            continue
        except:
            try:
                int(value5)
                break
            except:
                print("\nyour input is invalid")
                print("value5 should be number\n")
                continue
    except ValueError:
        print("\nyour input is invalid")
        print("between month5 and value5, 1 space is needed")
        print("Input again\n")
        continue
while True:
    print('Input "month6,value6"')
    try:
        month6, value6 = input().split(" ")
        try:
            int(month6)
            print("\nyour input is invalid")
            print("month6 should NOT be number\n")
            continue
        except:
            try:
                int(value6)
                break
            except:
                print("\nyour input is invalid")
                print("value6 should be number\n")
                continue
    except ValueError:
        print("\nyour input is invalid")
        print("between month5 and value5, 1 space is needed")
        print("Input again\n")
        continue

# calc diff and magnitude of values
months = [month1, month2, month3, month4, month5, month6]
values = list(map(int, [value1, value2, value3, value4, value5, value6]))
diffs = [0] * 5
magnitudes = [0] * 5
for diff_i in range(5):
    diffs[diff_i] = values[diff_i + 1] - values[diff_i]
for magnitudes_i in range(5):
    magnitudes[magnitudes_i] = diffs[magnitudes_i] / values[magnitudes_i] * 100

str_up = ["rose", "went up", "climbed", "increased"]
str_down = ["dropped", "went down", "fell", "decreased"]
str_magnitudes = ["slightly", "moderately", "considerably", "extremely"]

a = 0
b = 0
c = 0

for i in range(5):
    print(subject, end=" ")

    if diffs[i] == 0:
        print("continue stable", end=" ")
    elif diffs[i] > 0:
        print(str_up[a], end=" ")
        a = a + 1
        if magnitudes[i] < 30:
            print(str_magnitudes[0], end=" ")
        elif magnitudes[i] < 50:
            print(str_magnitudes[1], end=" ")
        elif magnitudes[i] < 80:
            print(str_magnitudes[2], end=" ")
        elif magnitudes[i] >= 80:
            print(str_magnitudes[3], end=" ")
        if c % 4 == 0:
            print("from {} by {} to {}".format(values[i], diffs[i], values[i + 1]), end=" ")
        elif c % 4 == 1:
            print("from {} by {}".format(values[i], diffs[i]), end=" ")
        elif c % 4 == 2:
            print("by {} to {}".format(diffs[i], values[i + 1]), end=" ")
        elif c % 4 == 3:
            print("from {} to {}".format(values[i], values[i + 1]), end=" ")
    elif diffs[i] < 0:
        print(str_down[b], end=" ")
        b = b + 1
        if -1 * magnitudes[i] < 30:
            print(str_magnitudes[0], end=" ")
        elif -1 * magnitudes[i] < 50:
            print(str_magnitudes[1], end=" ")
        elif -1 * magnitudes[i] < 80:
            print(str_magnitudes[2], end=" ")
        elif -1 * magnitudes[i] >= 80:
            print(str_magnitudes[3], end=" ")
        if c % 4 == 0:
            print("from {} by {} to {}".format(values[i], -1 * diffs[i], values[i + 1]), end=" ")
        elif c % 4 == 1:
            print("from {} by {}".format(values[i], -1 * diffs[i]), end=" ")
        elif c % 4 == 2:
            print("by {} to {}".format(-1 * diffs[i], values[i + 1]), end=" ")
        elif c % 4 == 3:
            print("from {} to {}".format(values[i], values[i + 1]), end=" ")
    print("between {} and {}".format(months[i], months[i + 1]))
    c = c + 1

print("maximum value is", end=" ")
print(max(values))
print("minimum value is", end=" ")
print(min(values))

##plt.plot(months, values, marker="o")
##plt.xlabel("month")
##plt.ylabel("price")
##plt.show()
