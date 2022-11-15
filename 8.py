grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    new_student = []
    i = 1
    for k, v in students.items():
        str_i = str(i)
        new_student.append(
            "{:>4}|{:<10}|{:^5}|{:^5}".format(str_i, k, v, grades[v]))
        i = i+1
    return new_student
