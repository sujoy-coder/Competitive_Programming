colour_code = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def reverse(string):
    rev_string = string[::-1]
    return rev_string

def myFunction(string):
    my_set = list(set(string))
    rev_string = reverse(string)
    answer1 = 0
    answer2 = 0
    for j in my_set:
        if j in colour_code:
            indx = (string.index(j)) + 1
            val = (colour_code.index(j)) + 1
            answer1 = answer1 + (indx * val)
    for j in my_set:
        if j in colour_code:
            indx = (rev_string.index(j)) + 1
            val = (colour_code.index(j)) + 1
            answer2 = answer2 + (indx * val)
    if answer1>answer2:
        ans_list.append(answer2)
    else:
        ans_list.append(answer1)
        
    return

test = int(input())
ans_list = []
if test>=1 and test<=100:
    for i in range(1,test+1):
        print()
        string = input()
        myFunction(string)
else:
    exit()     

for itm in ans_list:
    print(itm)
