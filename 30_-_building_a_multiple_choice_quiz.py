# "Question" class is imported.
from question import Question

# Question prompts are defined in a list.
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

# List of questions is initialized through the class.
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


# Function that runs the whole test is defined.
def run_test(questions):
    score = 0
    for question in questions:
        user_answer = input(question.prompt)
        if user_answer == question.answer:
            score += 1
    print("You guessed " + str(score) + "/" + str(len(questions)) + " correct.")


# Finally, the quiz can be run using the defined list of questions.
run_test(questions)
