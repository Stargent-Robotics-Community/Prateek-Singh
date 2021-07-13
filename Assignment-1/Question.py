## Question 1

listOfMovies = ['Schindler\'s List','12 Angry Men','The Godfather', 'The Lord of the Rings: The Return of the King']

for movie in listOfMovies:
    print("QUESTION 1:- " + movie)


## Question 2
   
   
n=2
print("Enter 2 your Favourite Moives: ")
while n>0:
    add=input()
    listOfMovies.append(add)
    n = n-1

print("QUESTION 2: " + str(listOfMovies))


## Question 3

print("QUESTION 3: " + str(listOfMovies[1::2]))

## Question 4

listOfNumber = [11,22,33,44,55]

n=0
total=0
while n<5:
    total= total + listOfNumber[n]
    n=n+1
print("Sum of 5 integer is:",total)


## Question 5

x= int(input("Enter the number of rows: "))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end='')
    print("")