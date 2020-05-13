def myFunc(N):
    coin_list = []
    while True:
        x = int(N/2)
        N = N - x
        coin_list.append(x)
        if N==2:
            if 1 in coin_list:
                coin_list.append(2)
                return len(coin_list)
            else:
                coin_list.append(1)
                coin_list.append(1)
                return len(coin_list)

test = int(input("No of test:"))
ans_list = []
flag = 0
if test>=1 and test<=100:
    for i in range(1,test+1):
        print("Enter Value of N")
        N = int(input())
        if N>=1 and N<=5000:
            value = myFunc(N)
            ans_list.append(value)
        else:
            flag = 1
            print("ERROR")
            break
else:
    flag = 1
    print("ERROR")

if flag == 0:
    print("OUTPUT...")
    for val in ans_list:
        print(val)