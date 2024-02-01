student_name = input("\nWhat is your name: ")
course_work_mark = int(input("\nCourse work marks: "))
exam_score = int(input("\nExam scores: "))

exam_score_70 = exam_score/100*70
 
final_score = course_work_mark + float(exam_score_70)

print(f"exam score out of 70:  {exam_score_70} and final score: {final_score}\n")

   