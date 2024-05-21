
def prime_func(the_num):


    if the_num <= 1:
        #print(entered_number," is not prime")
        #return False
        return False
        
    for i in range(2,the_num):
        if the_num % i == 0:
            #print(entered_number," is not prime")
            return the_num % i == 0
            
    else:
        #print(the_num," is prime")    
        #return the_num % i != 0
        return True
    

#print(prime_func(entered_number))

mylist = []

def fibo_func(the_num):
    a = 0
    mylist.append(a)
    b = 1
    mylist.append(b)
    c = a+b
    mylist.append(c)
    for i in range(2,the_num):
        a = b
       
        b= c
       
        c= a+b
        mylist.append(c)
    print(mylist)
    if the_num in mylist:
        
    #if num is in fibonacci sequence:
        #print(the_num, " is in the Fibonacci")
        return the_num in mylist
    

#Function to check where the number is for both
def check(the_num):
    prime = prime_func(the_num)
    fibo = fibo_func(the_num)
    if prime and fibo:
        print(the_num," is prime and in the fibonacci")
    elif prime:
        print(the_num," is prime")
    elif fibo:
        print(the_num," is in the fibonacci")
    else:
        print(the_num," is neither")


  
entered_number = int(input())
check(entered_number)
