def ask_question(question, options, correct_answer):
    """
    Задает вопрос игроку и проверяет правильность ответа.

    Parameters:
    question (str): Вопрос.
    options (list): Варианты ответов.
    correct_answer (str): Правильный ответ.

    Returns:
    bool: True, если ответ правильный, иначе False.
    """
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    answer = input("Ваш ответ (введите номер варианта): ")

    return options[int(answer) - 1].lower() == correct_answer.lower()

def main():
    """
    Основная функция игры викторины.
    """
    questions = [
        {
            "question": "Какой язык программирования используется для веб-разработки?",
            "options": ["Python", "HTML", "Java", "C++"],
            "answer": "HTML"
        },
        {
            "question": "Какая планета ближе всего к Солнцу?",
            "options": ["Земля", "Венера", "Марс", "Меркурий"],
            "answer": "Меркурий"
        },
        {
            "question": "Какая самая большая планета в Солнечной системе?",
            "options": ["Юпитер", "Сатурн", "Уран", "Нептун"],
            "answer": "Юпитер"
        }
    ]

    score = 0
    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            print("Правильно!")
            score += 1
        else:
            print("Неправильно!")

    print(f"Вы набрали {score} из {len(questions)} баллов!")

if __name__ == "__main__":
    main()
