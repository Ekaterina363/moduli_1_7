grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khend', "Aaron"}
students = list(students)
print(type(students))
book = dict(zip(students, grades))

book["Steve"] = sum(grades[0]) / len(grades[0])
book["Bilbo"] = sum(grades[1]) / len(grades[1])
book["Johnny"]= sum(grades[2]) / len(grades[2])
book["Khend"] = sum(grades[3]) / len(grades[3])
book["Aaron"] = sum(grades[4]) / len(grades[4])
print(book)

