class Participant:
    def __init__(self, en_no, name):
        self.en_no = en_no
        self.name = name

    def participant_details(self):
        print("PARTICIPANT DETAILS")
        print("-----------------")
        print("Enrollment no:", self.en_no)
        print("name :", self.name)


class Question:
    def __init__(self, score, time):
        self.score = score
        self.time = time

    def quizz_score(self):
        print("score:", self.score, "\ntime:", self.time)


def tracking(en_no, name, score, time):
    print("\nRESULt")
    print("-----------------")
    print(name, "[EnrollmentNo:", en_no, "]", "scored", score, "at", time)


class Quizz_final:
    def __init__(self, part, ques):
        self.part = part
        self.ques = ques


part_obj = Participant("58644", "Anu")
q_obt = Question("20points", "12:00pm")
final_obj = Quizz_final(part_obj, q_obt)
part_obj.participant_details()
q_obt.quizz_score()
tracking(final_obj.part.en_no,
         final_obj.part.name,
         final_obj.ques.score,
         final_obj.ques.time)
