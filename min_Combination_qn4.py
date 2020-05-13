def computeGCD(num_1, num_2): 
   while(num_2): 
       num_1, num_2 = num_2,(num_1 % num_2) 
   return num_1

def myFunction(num_1,num_2):
    itr = 1
    while itr:    
        if (itr % computeGCD(num_1,num_2)) == 0:
            return itr
        itr = itr + 1

test = int(input("No of test:"))
ans_list = []
if test>=1 and test<=1000:
    for i in range(1,test+1):
        print("Enter n1 and n2 seperated by space :")
        num_1,num_2 = input().split(" ")
        num_1 = int(num_1)
        num_2 = int(num_2)
        if (num_1>=0 and num_1<=100000000) and (num_1>=0 and num_1<=100000000):
            answer = myFunction(num_1,num_2)
            ans_list.append(answer)
        else:
            exit()
else:
    exit()
    
for ans in ans_list:
    print(ans)
