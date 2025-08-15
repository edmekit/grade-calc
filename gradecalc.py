scores = int(input("Enter quiz score: "))
over = int(input("How many items? "))
grade = []
overall = []

with open("scores.txt", "a") as f:
    f.write(str(scores) + "\n")

with open("scores.txt", "r") as f:
    grades = f.readlines()
    for gradee in grades:
        gradee = gradee.strip()
        if gradee:
            grade.append(int(gradee))

with open("over.txt", "a") as f:
    f.write(str(over) + "\n")
    
with open("over.txt", "r") as f:
    overs = f.readlines()
    for total in overs:
        total = total.strip()
        if total:
            overall.append(int(total))

quiz = (sum(grade) / sum(overall)) * 40
print("For exercises, you have a grade of ", quiz)
