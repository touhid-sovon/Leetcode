# Mutable and Immutable Objects in python
import math


# str1 = 'sovon'
#
# print(f'Memory Location of str1 is {id(str1)}')
#
# str1 += ' touhid'
# print(str1)
# print(f'Memory Location of str1 is {id(str1)}')

# why mutability can be costly

# names = ['sovon','shahed','oni','nasima','faysal']
#
# output = '<ul>\n'
#
# for name in names:
#     output += f'\t<li>{name}</li>\n'
#     #print(f'address of each name {id(output)}')
#
# output += '</ul>'
#
# print(output)


def swap2(a, b):
  temp = a
  a = b
  b = temp

num1, num2 = 10, 20

swap2(num1, num2)

#print(num1, num2)

######
# def modify_list(lst):
#     lst.append(4)
#
# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # Output: [1, 2, 3, 4]


# set

set1 = {1,2,3}

set1.add(4)
set1.add(5)
set1.add(6)
set1.pop()

set2 = {'a','b','c'}
#print(type(set1))
#print(set1)

#print(set1.union(set2))

# list comprehension

# even = [num for num in range(2,11,2)]
# even2 =list(range(11,21,2))
# print(even)
# print(even2)
#
# odd = [num for num in range(1,100) if num%2!=0]

# print(odd)

# lambda function

def add(a,b):
  return a+b

#print(add(10,20))

# same thing can be done with labda which is an anonymous function
sum = lambda x,y:x+y
#print(sum(20,120))

# passing function as a parameter

# callback in python
# def function1():
#   print('Function 1 callback')
#
# def function2(text:str,callback)->None:
#   print(text)
#   callback()
#
# function2('sovon',function1)

# can be done using lambda function
# function2('Touhid',lambda : print('Function 1'))

# list1 = [1,2,3]
# num = 3
# def func3(arr:list,n:int)-> list:
#   print(arr)
#   print(n)
#   return arr * n

#print(func3(list1,num))


## lambda with map()

def square(n:int)->int:
  return n*n

list1= [1,2,3]
#print(list(map(square,list1)))

# building iterator class

class MyRange:

  def __init__(self,start,end):
    self.value = start
    self.end = end

  def __iter__(self):
    return self

  def __next__(self):
    if self.value >= self.end:
      raise StopIteration
    current = self.value
    self.value += 1
    return current

nums = MyRange(1,10)

# for num in nums:
#   print(num)

#print(next(nums))

names = ['sovon','shahed','oni','faysal','nasima']

#print(names)
#print(*names) # unpacking the list

def pizza(size,*toppings,**details):
  print(f'Ordered a {size}size pizza with the following toppings')
  for topping in toppings:
    print(topping)
  print(f'details of the order is')
  for key,value in details.items():
    print(f'{key}:{value}')

#pizza('Large','cheese','pepparoni','sauce',delivery = True,price = 10)

''' floor/ceil'''

# print(math.floor(3.4))
# print(math.ceil(3.4))
# print(math.floor(-3.4))
# print(math.ceil(-3.4))

num_in_range = list(range(1,10))
#num_in_xrange = list(xrange(1,10))

#print(num_in_range)
#zip

roll = [4,5,6]
clas_name = ['sovon','shahed','oni']

my_dict = dict(zip(roll,clas_name))
#print(my_dict)
#print(list(zip(roll,clas_name)))

# dictionary comprehension

# syntax ={key_expression:value_expression for item in iterable if condition}

# dictionary of prime numbers

# normal approach
def is_prime(n:int)->bool:
  prime = [2,3]
  if n==2 or n==3:
    return True
  for i in range(2,(n//2)+1):
    if n%i ==0:
      return False
  prime.append(n)
  return True

#print(is_prime(93))

#prime_list = [x: for x in range(1,50) if x]

# seive of erathosthenes

def sieve_of_eratosthenes(limit):
  # Step 1: Create a list of boolean values
  is_prime = [True] * (limit + 1)
  is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

  # Step 2: Mark non-prime numbers
  p = 2
  while p * p <= limit:
    if is_prime[p]:
      for multiple in range(p * p, limit + 1, p):
        is_prime[multiple] = False
    p += 1

  # Step 3: Collect all prime numbers
  primes = [number for number, prime in enumerate(is_prime) if prime]
  return primes


# Example usage
limit = 50
#print(f"Prime numbers up to {limit}: {sieve_of_eratosthenes(limit)}")

# optimed prime

def optime_prime_list(limit:int)->list:
  is_prime = [True] * (limit +1)
  is_prime[0] = is_prime[1] = False

  p = 2
  while p*p <=limit:
    if is_prime[p]:
      for i in range(p*p,(limit+1),p):
        is_prime[i] = False
    p+=1
  primes =[]

  for i in range(len(is_prime)):
    if is_prime[i]:
      primes.append(i)

  #primes = [index for index,prime in enumerate(is_prime) if prime]

  return primes


#print(optime_prime_list(10))

''' prime for one number'''
def prime(n:int)->bool:
  if n<=1:
    return False
  if n <= 3:
    return True
  if n%2==0 or n%3==0:
    return False

  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6

  return True


''' dictionary comperehension'''

my_dict2 = {str(x):x*x for x in range(1,10)}

#print(my_dict2)

# interchaning the key-value pair

interchange_dict = {value:key for key,value in my_dict2.items()}

#print(interchange_dict)

'''OOP Python'''

class Deparment:
  varsity = 'BU'

  def __init__(self,name):
    self._name = name

  def __str__(self):
    return self._name


d1 = Deparment('CSE')

print(d1._name)