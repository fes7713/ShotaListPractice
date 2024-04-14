# 20240414 Data Structure 


## Why Data Structure

To store data and process data efficiently.

var a = 2
var b = 3
var c = 4

var list = [2, 3, 4]

var list = ["str3", "str2", "str1"]

## Topics 

- List
- Set
- Map
- Stack
- Queue

## List

Can store single data type of many object.

### Two types of List

- Array List 
- Linked List 

### Array VS List

array[0] = 1

array[0] = 2

array[1] = 3

list = []

list.append(1)
list.append(2)
list.append(3)
list.append(4)

= [1, 2, 3, 4]

### Pros and cons of List

#### Pros 

Useful 

You dont have to code to manage storing data

#### Cons

Slow

Referencing Memory
- array[0] = 1
- Calculate position of array[0] in memory
- Update value 


Unnecessary Variable
- Calculate position of array[0] in memory
- Get value
- CPU calc
- Update value

Function Stack
- Calling Function
- Pushing function stack
- Stackoverflow

### Where to use

Web application

×　Gaming
×　Batch Processing




### Array List 

List that uses Array as internal function.

var array = new int[10];

Pros
- Get O(1)
- Append O(1)


Cons
- Insertion O(n)
- Deletion O(n)
  - Shifting
- Search O(n)

### Linked List 

List that uses "Node" tas internal function

Pros
- Deletion O(n) * O(1)
- Insertion O(n) * O(1)
- Append O(n) * O(1)

Cons
- Get O(n)
- 
- Search O(n)
- Lower storage efficiency
- 

### Singly Linked List

- Head


### Doubly Linked List

- Head 
- Tail

## Set 

- Orderless

List -> [1, 4, 6, 8, 11, 34, 55]

Set -> ["Sedan", "Quepe", "Sports", "SUV"]

### Implementation
- HashSet()

## Map

- Orderless


Python : Dictionary

Key-Value Set

cakePriceMap = {"CheesesCake": 190, "ChocolateCake": 220, "PlainCake": "120", "StroberryCake": 250}

cakePriceMap.get("CheesesCake") returns 190

CalculateMemoryPosition("CheesesCake") -> Memory Position

### Runtime

cakeList = ["CheesesCake", "ChocolateCake", "PlainCake", "StroberryCake"]
priceList = [190, 220, 250, 320]

List Search -> O(n)

Map  Search -> O(1)

Search -> O(1)
Insertion -> O(1)
Deletion -> O(1)
Access -> O(1)

### Cons

- Lower storage efficiency 
- Collision
  - Lower runtime
  - 75 %
  - depends on Quolity of Hash function
- Orderless

### HashMap

Uses Hash function to calculate memory position 


## Stack

FILO

LIFO

積み重ねる

## Queue

FIFO




