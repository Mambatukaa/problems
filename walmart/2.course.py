
""""

pairs1 = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"],
]

pairs2 = [
    ["Algorithms", "Foundations of Computer Science"],
    ["Data Structures", "Algorithms"],
    ["Foundations of Computer Science", "Logic"],
    ["Logic", "Compilers"],
    ["Compilers", "Distributed Systems"],
]

pairs3 = [
    ["Data Structures", "Algorithms"],
]

print(halfway_course(pairs1))  # ➜ "Data Structures"
print(halfway_course(pairs2))  # ➜ "Foundations of Computer Science"
print(halfway_course(pairs3))  # ➜ "Data Structures"

"""

def halfway_course(pairs):
    # Step 1: Build map prereq -> next course
    next_course = {}
    all_courses = set()
    dependents = set()

    for prereq, course in pairs:
        next_course[prereq] = course
        all_courses.add(prereq)
        all_courses.add(course)
        dependents.add(course)

    print(dependents)
    # Step 2: Find the starting course (never a dependent)
    start = (all_courses - dependents).pop()


    # Step 3: Follow chain to build full path
    order = []
    curr = start
    while curr:
        order.append(curr)
        curr = next_course.get(curr)

    # Step 4: Return halfway course (first of two if even)
    n = len(order)
    half_index = (n - 1) // 2
    return order[half_index]


pairs1 = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"],
]


halfway_course(pairs1)
