Students = {
  "arnv" : 2,
  "vansh" : 3,
  "soham" : 0,
  "reyansh": 0
}

Books = {
  "Hail Mary" : 5,
  "Artimis" : 3,
  "The Martian" : 5,
  "Dune" : 6
}

#average number of books borrowed by all students 

totalbooks = sum(Students.values())
average = totalbooks / len(Students)
print("average number of books borrowed by all students is:", average)

#books with higest borrowing
higest = max(Books, key=Books.get)
print("highest borrowed book is", higest)

print("most frequently borrowed book is", higest)

lowest = min(Books, key=Books.get)
print("lowest borrowed book is", lowest)


count = 0
for num in Students.values():
 if num == 0:
   count = count + 1
   
print("Number of students who have not borrowed any book are", count)

"""
Output:

(base) cg@cg-ThinkCentre-neo-50s-Gen-3:~/arnv$ python3 library.py
average number of books borrowed by all students is: 1.25
highest borrowed book is Dune
most frequently borrowed book is Dune
lowest borrowed book is Artimis
Number of students who have not borrowed any book are 2
(base) cg@cg-ThinkCentre-neo-50s-Gen-3:~/arnv$ 
"""

