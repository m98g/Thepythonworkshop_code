students = ["Mark", "Chris", "Tim", "Max"]
scores = [70, 80, 70, 75]

# Man muss es über die Indizes abwickeln da sonst wenn man x:y nur die letzten
# key value pairs erhalten bleiben da das Dict immer nur einen uniqen Key hat 
# aber nimmt mehrere Values für einen Key

student_scores = {students[i]:scores[i] for i in range(len(students))}
print(student_scores)