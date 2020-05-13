def myFunc(array):
    ans = 0
    length = len(array)
    #for odd.... 
    if length%2!=0:
        mid_index = (length//2)
        for i in range(0,length):
            if i < mid_index:
                ans = ans + (array[mid_index]-array[i])
            else:
                ans = ans + (array[i]-array[mid_index])
    #for even....
    else:
        mid_index = int(length/2)
        for i in range(0,length):
            if i < mid_index:
                ans = ans + (array[mid_index]-array[i])
            else:
                ans = ans + (array[i]-array[mid_index])          
    return ans
def sorting(array): 
    n = len(array)  
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if array[j] > array[j+1] : 
                array[j], array[j+1] = array[j+1], array[j]

test = int(input("No of test:"))
ls = []
demo = 0
if test>=1 and test<=10:
    for i in range(1,test+1):
        sizeOfarray = int(input("Enter size of array"))
        if sizeOfarray>=1 and sizeOfarray<=10000:
            print("Enter the elements of array")
            array = list()
            for j in range(sizeOfarray):
                val = int(input())
                if val>=1 and val<=10000:
                    array.append(val)
                else:
                    demo = 1
                    print("ERROR")
                    break
            if demo==0:
                sorting(array)    
                ls.append(myFunc(array))
        else:
            demo = 1
            print("ERROR")
            break
else:
    demo = 1
    print("ERROR")

if demo==0:
    print("OUTPUT....")
    for value in ls:
        print(value,end=" ")
    

