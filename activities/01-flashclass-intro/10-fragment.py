"""

This code is used as a way to bridge the gap between text and technology.

This software is written in a language called Python.

It's very readable as a native English speaker.

And the code actually runs and you can try it yourself.
But now you're on your own.

Try asking any LLM like ChatGPT, Gemini or Claude this question:

    "How can I run Python code on my computer?"

You can assume the entire contents of this file are the Python code, including
the comments you are reading now.

"""
class flash:
    def __init__(self, student_name = ""):
        if student_name == "":
            self.student_name = input("What's your name? ")
        else:
            self.student_name = student_name

    def build_custom_course_for(self):
        # flashclass builds custom courses just for you.
        print(f"flashclass is building a transformational experience for {self.student_name}...")
        self.start_transformational_experience_for()

    def start_transformational_experience_for(self):
        print(f"{self.student_name} is embarking on a new learning journey.")
        self.offer_ambitious_journey_to()

    def offer_ambitious_journey_to(self):
        # flashclass breaks the speed barriers of learning
        print("Starting an ambitious transformation...")
        self.engage_in_activities_to_transform()

    def engage_in_activities_to_transform(self):
        print("Engaging in activity 1...")
        print("Engaging in activity 2...")
        print(f"{self.student_name} feels overwhelmed and starts to panic!")

        # "calm AND under serious pressure" helps our memory work
        self.breathe()

        print("Engaging in activity 3...")

    def breathe(self):
        print(f"{self.student_name} takes a slow, deep breath and regains focus.  Count 4 in quick, 8 out slow.")

    def ask_student(self, question):
        response = input(f"flashclass asks {self.student_name}: \"{question}\" ")
        print(f"{self.student_name} responds: {response}")

        student = self.student_name
        gnosis.ask(student, "Do you see beauty in things that others might not notice?")
        gnosis.ask(student, "Do you enjoy trying new and difficult things?")
        gnosis.ask(student, "Are you relaxed most of the time?")

    def notice_student_feelings(self):
        self.ask_student("How do you feel right now?")

class gnosis:
    def ask(student, question):
        response = input(f"flashclass asks: {question} ")


# Example usage of the class
student = flash()
student.build_custom_course_for()
student.notice_student_feelings()

