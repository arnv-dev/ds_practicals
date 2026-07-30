Students = {
  "arnv": 2,
  "reyansh": 4,
  "vaibhav": 0,
  "soham": 0,
  "rudra": 3
}

books = {
    "Hail mary":5,
    "The Martian":3,
    "Artemis": 2,
    "Dune": 4
}


#average no. of books borrowed by all students 

totalbooks = sum(Students.values())
average = totalbooks / len(Students)
print("average books borrowed by students =", average)

#books with higest borrowing 
highest_borrow = max(books, key=books.get)
print("most borrowed book is ",highest_borrow)

#most frequently borrowed book 
print("Most frequently borrowed book is ",highest_borrow)

#books with higest borrowing 
least_borrow = min(books, key=books.get)
print("Least borrowed book is ",least_borrow)

#no. of members who have not borrowed any book 

count = 0

for num_borrow in Students.values():
    if num_borrow == 0:
        count = count + 1


print("Number of students who have not borrowed any book:", count)



