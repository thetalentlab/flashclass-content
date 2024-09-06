"""

- No one ASKS you about what you already know

- No one OFFERS beginners any serious breadth or depth

- No one NOTICES how you feel during the lesson ... you are a transaction


  ... unless you find a teacher that takes an interest, and even then it
  can lead to teacher burnout, something like "empathy fatigue"



"""

import gnosis

class flash:

    def ask_student(self, question):
        response = input(f"flashclass asks {self.student_name}: {question}")
        print(f"{self.student_name} responds: {response}")

        gnosis.ask("Do you see beauty in things that others might not notice?")
        gnosis.ask("Do you enjoy trying new and difficult things?")
        gnosis.ask("Are you relaxed most of the time?")

    def notice_student_feelings(self):
        self.ask_student("How do you feel right now?")
