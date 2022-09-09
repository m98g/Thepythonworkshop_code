class Interrogator:
    def __init__(self, questions):
        self.questions = questions

    def __iter__(self):
        return self.questions.__iter__()

questions = ["What is your name?", "What is your quest?", 
"What is the average airspeed velocity of an unladen swallow?"]

awkward_person = Interrogator(questions)

for question in awkward_person:
    print(question)