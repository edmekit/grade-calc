def calculate(sub, scorefile, overfile, part):
    scores = int(input("Enter quiz score: "))
    over = int(input("How many items? "))
    grade = []
    overall = []

    with open(scorefile, "a+") as f:
        f.write(str(scores) + "\n")
        f.seek(0)
        grades = f.readlines()
        for gradee in grades:
            gradee = gradee.strip()
            if gradee:
                grade.append(int(gradee))

    with open(overfile, "a+") as f:
        f.write(str(over) + "\n")
        f.seek(0)
        overs = f.readlines()
        for total in overs:
            total = total.strip()
            if total:
                overall.append(int(total))

    quiz = (sum(grade) / sum(overall)) * part
    print("For exercises in ", sub," you have a grade of ", quiz)

subject = input("Enter subject: ")

if subject == "MATH 27":
    calculate("MATH 27","scores/mathscores.txt", "scores/mathover.txt", 40)

elif subject == "CMSC 56":
    calculate("CMSC 56","scores/cmsc56scores.txt", "scores/cmsc56over.txt", 35)

elif subject == "CMSC 12":
    calculate("CMSC 12","scores/cmsc12scores.txt", "scores/cmsc12over.txt", 45)


