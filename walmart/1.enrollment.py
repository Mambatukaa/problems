""""
enrollments1 = [
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"],
    ["25", "Economics"],
    ["58", "Software Design"],
]

enrollments2 = [
    ["0", "Advanced Mechanics"],
    ["0", "Art History"],
    ["1", "Course 1"],
    ["1", "Course 2"],
    ["2", "Computer Architecture"],
    ["3", "Course 1"],
    ["3", "Course 2"],
    ["4", "Algorithms"],
]

enrollments3 = [
    ["23", "Software Design"],
    ["3", "Advanced Mechanics"],
    ["2", "Art History"],
    ["33", "Another"],
]

print("Test 1:")
print(find_pairs(enrollments1))
print("\nTest 2:")
print(find_pairs(enrollments2))
print("\nTest 3:")
print(find_pairs(enrollments3))

"""

def findPairs(enrollments):
    student_courses = {}

    for sId, course in enrollments:
        if sId not in student_courses:
            student_courses[sId] = set()
        student_courses[sId].add(course)


    students = sorted(student_courses.keys(), key=int)
    pairs = {}
    
    for i in range(len(students)):
        for j in range(i + 1, len(student_courses)):
            s1, s2 = students[i], students[j]

            shared = list(student_courses[s1].intersection(student_courses[s2]))
            pairs[f"{s1},{s2}"] = shared
    return pairs



enrollments1 = [
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"],
    ["25", "Economics"],
    ["58", "Software Design"],
]

findPairs(enrollments1)
