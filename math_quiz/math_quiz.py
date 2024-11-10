import random

def get_random_integer(min_value, max_value):
    """
    Generates a random integer within the given range [min_value, max_value].

    Args:
        min_value (int): Minimum value of the range.
        max_value (int): Maximum value of the range.

    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def get_random_operator():
    """
    Chooses a random math operator from a list of ['+', '-', '*'].

    Returns:
        str: A random operator as a string.
    """
    return random.choice(['+', '-', '*'])

def generate_problem(num1, num2, operator):
    """
    Creates a math problem based on two numbers and an operator.

    Args:
        num1 (int): First number in the math problem.
        num2 (int): Second number in the math problem.
        operator (str): Math operator, one of ['+', '-', '*'].

    Returns:
        tuple: A tuple containing the problem as a string and its correct answer as an int.
    """
    problem = f"{num1} {operator} {num2}"

    # Calculate the correct answer based on the operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  # operator == '*'
        answer = num1 * num2

    return problem, answer

def math_quiz():
    """
    Main function to run the Math Quiz game.
    It generates random math questions and evaluates the user's answers.
    """
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems. Provide the correct answers to score points.")

    for _ in range(total_questions):
        num1 = get_random_integer(1, 10)
        num2 = get_random_integer(1, 5)
        operator = get_random_operator()

        problem, correct_answer = generate_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()