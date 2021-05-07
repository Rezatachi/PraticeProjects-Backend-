from data import question_data
from question_model import Question


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

print(question_bank)
#     question_bank.append(question_data["text"])


# def Query(question, answer):
#     print(f"{question} ? {answer}")


# Query(question_bank["text"], question_bank["answer"])

# question_bank = Question(QuestionJSON["text"], QuestionJSON["answer"])


print("Welcome to the boolean true or false game!!✍")
