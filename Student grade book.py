grade_book={"Alice": 85, "Bob" : 92, "Charlie" : 75, "Max" : 95, "Evan" : 88}
total = 0
for student in grade_book:
    total = total + grade_book[student]
average = total / len(grade_book)
print("Class average:", average)
highest_score = max(grade_book.values())
lowest_score = min(grade_book.values())
for student in grade_book:
    if grade_book[student] == highest_score:
        highest_student = student
    if grade_book[student] == lowest_score:
        lowest_student = student
print("Top scorer:", highest_student, "with a score of", highest_score)
print("Bottom scorer:", lowest_student, "with a score of", lowest_score)
search_student = input("Enter the name of the student you want to search for:")
student_score = grade_book.get(search_student)
if student_score == None:
    print("Sorry,", search_student, "could not be found in the grade book.")
else:
    print(search_student, "got a score of", student_score)    