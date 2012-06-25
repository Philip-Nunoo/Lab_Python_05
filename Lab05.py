def factorial(a):
    b = 1
    while a != 0:
        b = b * a
        a -= 1
    return b

def fibonacci(n):
    a = 1
    b = 1
    List = [a]
    for i in range(1,n):
        sum1 = a + b
        b = a        
        List.append(a)
        a = sum1
        n +=1
    return List

def prime(n):
    cnt = 0
    for j in range (1, n):
        if(n%j == 0):
            cnt += 1
            print j,
    if (cnt == 1):
        return True
    else:
        return False


def isPalindrome(string):
    for i in range(0,len(string)):
        if(string[i] == string[len(string)-i-1]):
           sum = 0
        else:
            return False
    return True

print isPalindrome('a man a plan a canal panama')

#def isSubstring(a,b):
    
    #return True
