#input values
subject = input()
month1,value1 = input().split(",")
month2,value2 = input().split(",")
month3,value3 = input().split(",")
month4,value4 = input().split(",")
month5,value5 = input().split(",")
month6,value6 = input().split(",")

#calc diff and magnitude of values
months = [month1,month2,month3,month4,month5,month6]
values = list(map(int,[value1,value2,value3,value4,value5,value6]))
diffs = [0] * 5
magnitudes = [0] * 5
for diff_i in range(5):
    diffs[diff_i] = values[diff_i+1] - values[diff_i]
for magnitudes_i in range(5):
    magnitudes[magnitudes_i] = diffs[magnitudes_i]/values[magnitudes_i] * 100

for i in range(5):
    print(subject, end=" ")

    if diffs[i] == 0:
        print("continue stable", end=" ")
    elif diffs[i] > 0:
        print("increased", end=" ")
        if magnitudes[i] < 30:
            print("slightly", end=" ")
        elif magnitudes[i] < 50:
            print("moderately", end=" ")
        elif magnitudes[i] < 80:
            print("considerably", end=" ")
        elif magnitudes[i] >= 80:
            print("extremely", end=" ")
        print("from {} by {} to {}".format(values[i],diffs[i],values[i+1]), end=" ")
    elif diffs[i] < 0:
        print("decreased", end=" ")
        if -1*magnitudes[i] < 30:
            print("slightly", end=" ")
        elif -1*magnitudes[i] < 50:
            print("moderately", end=" ")
        elif -1*magnitudes[i] < 80:
            print("considerably", end=" ")
        elif -1*magnitudes[i] >= 80:
            print("extremely", end=" ")
        print("from {} by {} to {}".format(values[i],-1*diffs[i],values[i+1]), end=" ")
    
    print("between {} and {}".format(months[i],months[i+1]))