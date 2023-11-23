import random


def generate_question(operation):
    global question, answer
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)

    if operation == "+":
        question = f"{num1} + {num2} = ?"
        answer = num1 + num2
    elif operation == "-":
        question = f"{num1} - {num2} = ?"
        answer = num1 - num2
    elif operation == "*":
        question = f"{num1} * {num2} = ?"
        answer = num1 * num2
    elif operation == "/":
        question = f"{num1} // {num2} + ?"
        answer = num1 // num2
    return question, answer


def main():
    operations = ["+", "-", "*", "/"]
    for _ in range(10):
        operation = random.choice(operations)
        question, answer = generate_question(operation)

        student_answer = int(input(question + " "))

        if student_answer == answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {answer}.")


if __name__ == "__main__":
    main()
