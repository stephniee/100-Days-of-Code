print("Time to praise a student!")
english_score = int(input("What is your score on the English Exam?"))
math_score = int(input("What is your score on the Math Exam?"))

if math_score >= 90:
    if english_score >= 90:
     print("Holy cow! You're good!")
    else:
      print("Work on your english, scrub")
else:
    print("Work on your mathh, nub")

