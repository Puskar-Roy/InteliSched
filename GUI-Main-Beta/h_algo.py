# class temp:
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#     classesYearOne = ["Basic Electrical Engneering", "Graphics And Design", "Engneering Math", "Engineering Physics", "Programming C"]
#     classesYearTwoTheory = ["Analog Electronic Circuits", "Data structure & Algorithms", "IT Workshop (Sci Lab/MATLAB) Theory", "Digital Logic", "Differential Calculus", "Engineering Biology", "Linguistics & Oral Communication"]
#     classesYearTwoAssigned = [False] * len(classesYearTwoTheory)
#     classesYearTwoPractical = ["Analog Electronic Circuits Laboratory", "Data structure & Algorithms Laboratory", "IT Workshop (Sci Lab/MATLAB) Laboratory", "Digital Logic Laboratory"]
#     classeshavePractical = [1, 1, 1, 1, 0, 0, 0]
#     classesYearTwoPriority = [2, 1, 1, 1, 1, 3, 3]
#     classesYearTwoAssignedTheory = [False] * len(classesYearTwoTheory)
#     classesYearTwoTheoryCredit = [3, 3, 1, 3, 2, 3, 0]
#     classesYearTwoPracticalCredit = [2, 2, 2, 2]
#     classesYearTwoPracticalClass = ["212", "G01", "G03", "218"]
#     laboratoryClassRoomsPool = ["212", "GO1", "G02", "GO3", "G20", "218", "203", "204"]
#     laboratoryTeacherPool = ["APR", "CK", "PDE", "IC", "CT", "PPS", "AR", "KKC"]
#     theoryClassFacultyPoolCSE = ["SGP", "SS", "SB", "DD", "SG", "AB", "SKG"]
#     theoryClassFacultyPoolIT = ["KGH", "PSC", "SPJ", "NSM", "ND", "ACH", "PKS"]
#     classesYearOneEvenSemesterTheory = ["Basic Electrical Engineering", "Graphics And Design", "Engneering Math", "Engineering Physics", "Problem for Problem Solving in C"]
#     classesYearOneEvenSemesterPractical = ["Basic Electrical Engineering Laboratory", "Graphics And Design Laboratory", "Engineering Physics Laboratory", "Problem for Problem Solving in C Laboratory"]
#     classesYearOneEvenSemesterPracticalCredit = [2, 2, 2, 2]
#     classesYearTwoEvenSemesterTheory = ["Discrete Mathematics", "Computer Organization & Architecture", "Operating Systems", "Design & Analysis of Algorithms", "Economics & Accountancy", "Environmental Sciences", "Business Communications"]
#     classesYearTwoEvenSemesterTheoryCredit = [4, 3, 3, 3, 2, 0, 0]
#     classesYearTwoEvenSemesterPractical = ["Computer Organization & Architecture Laboratory", "Operating Systems Laboratory", "Design & Analysis of Algorithms Laboratory"]
#     classesYearTwoEvenSemesterPracticalCredit = [2, 2, 2]
#     classesYearTwoEvenSemesterHoursRequiredTheory = [0] * len(classesYearTwoEvenSemesterTheoryCredit)
#     classesYearTwoEvenSemesterAssignedTheory = [False] * len(classesYearTwoEvenSemesterHoursRequiredTheory)
#     classesYearThreeEvenSemesterTheory = ["Compiler Design", "Computer Networks", "Professional Elective-II", "Professional Elective-III", "Open Elective I"]
#     classesYearThreeEvenSemesterTheoryCredit = [3, 3, 3, 3, 3]
#     classesYearThreeEvenSemesterPractical = ["Compiler Design Laboratory", "Computer Networks Laboratory", "Python Programming Laboratory", "Project-I", "Group Discussion & Personal Interview"]
#     classesYearThreeEvenSemesterPracticalCredit = [2, 2, 2, 3, 1]

#     classesYearThreeEvenSemesterHoursRequiredTheory = [0] * len(classesYearThreeEvenSemesterTheoryCredit)
#     classesYearThreeEvenSemesterAssignedTheory = [False] * len(classesYearThreeEvenSemesterHoursRequiredTheory)

#     classesYearFourEvenSemesterTheory = ["Professional Elective VI", "Open Elective III", "Open Elective IV"]
#     classesYearFourEvenSemesterTheoryCredit = [3, 3, 3]
#     classesYearFourEvenSemesterPractical = ["Project-III"]
#     classesYearFourEvenSemesterPracticalCredit = [6]

#     classesYearFourEvenSemesterHoursRequiredTheory = [0] * len(classesYearFourEvenSemesterTheoryCredit)
#     classesYearFourEvenSemesterAssignedTheory = [False] * len(classesYearFourEvenSemesterHoursRequiredTheory)
#     def classes_hours_required():
#         # use switch case to determine which year you will take into account
#         for i in range(len(classesYearTwoTheoryCredit)):
#             if classesYearTwoTheoryCredit[i] == 0:
#                 # when the subject is non-credit course, we need to give it 1 class in a week
#                 classesYearTwoEvenSemesterHoursRequiredTheory[i] = classesYearTwoTheoryCredit[i] + 1
#             else:
#                 classesYearTwoEvenSemesterHoursRequiredTheory[i] = classesYearTwoTheoryCredit[i]

#         for i in range(len(classesYearThreeEvenSemesterTheoryCredit)):
#             if classesYearTwoTheoryCredit[i] == 0:
#                 # when the subject is non-credit course, we need to give it 1 class in a week
#                 classesYearThreeEvenSemesterHoursRequiredTheory[i] = classesYearThreeEvenSemesterTheoryCredit[i] + 1
#             else:
#                 classesYearThreeEvenSemesterHoursRequiredTheory[i] = classesYearThreeEvenSemesterTheoryCredit[i]

#         for i in range(len(classesYearFourEvenSemesterTheoryCredit)):
#             if classesYearFourEvenSemesterTheoryCredit[i] == 0:
#                 # when the subject is non-credit course, we need to give it 1 class in a week
#                 classesYearFourEvenSemesterHoursRequiredTheory[i] = classesYearFourEvenSemesterTheoryCredit[i] + 1
#             else:
#                 classesYearFourEvenSemesterHoursRequiredTheory[i] = classesYearFourEvenSemesterTheoryCredit[i]

#     def get_day(day):
#         switcher = {
#         "Monday": 1,
#         "Tuesday": 2,
#         "Wednesday": 3,
#         "Thursday": 4,
#         }
#         return switcher.get(day, 5)
    

#     def map_teachers(sub, teacher, teacher_off_days):
#         for i in range(len(teacher_off_days)):
#             if teacher_off_days[i] is None:  # teacher can take all the days
#                 sub[teacher[i]] = Time(True)
#             else:
#                 j = get_day(teacher_off_days[i]) - 1
#                 t = Time(j)
#                 sub[teacher[i]] = t




    
