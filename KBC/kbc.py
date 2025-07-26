import random

questions = [
    ["Python code runs in?", "Terminal", "Excel", "Notepad", "Browser", 1],
    ["input() returns?", "Float", "Integer", "String", "List", 3],
    ["Python is?", "Low-level", "High-level", "Machine Language", "Assembly", 2],
    ["Python is a?", "Snake", "Browser", "Text Editor", "Programming Language", 4],
    ["Which one is a data type in Python", "int", "number", "digit", "num", 1],
    ["Which loop is used to iterate over a sequence in Python?", "for", "foreach", "loop", "repeat", 1],
    ["What is the correct file extension for Python files?", ".pt", ".txt", ".py", ".css", 3],
    ["Python was created by?", "Guido von Rossum", "Harry", "Sankalp", "Robert Smith", 1],
    ["Which of the following is used to define a function in Python?", "def", "define", "function", "func", 1],
    ["Which keyword is used for exception handling in Python?", "error", "catch", "try", "exception", 3]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
switch_question = ["What does len() do?", "Returns length", "Returns sum", "Returns max", "Returns average", 1]

money = 0
lifeline_5050_used = False
lifeline_switch_used = False

print("🙏 Welcome to Kaun Banega Crorepati")

i = 0
while i < len(questions):
    q = questions[i]
    print(f"\nQuestion {i+1} for Rs.{levels[i]}")
    print(f"Q: {q[0]}")
    print(f"a. {q[1]}       b. {q[2]}")
    print(f"c. {q[3]}       d. {q[4]}")

    lifeline_applied = False
    while True:
        try:
            reply = int(input("\nEnter Your Answer (1-4), 9 for Lifeline, or 0 to Quit: "))
            if reply == 0:
                print("\n👋 You chose to quit.")
                print(f"\n🥳 Total Money you won Rs.{money}")
                print("\n🙏 Thank you for playing Kaun Banega Crorepati!")
                exit()
            elif reply == 9:
                print("\n🛟 Lifelines Available:")
                if not lifeline_5050_used:
                    print("1. 50-50")
                if not lifeline_switch_used:
                    print("2. Switch the Question")

                lifeline_choice = int(input("Which lifeline do you want to use? (1 or 2): "))

                if lifeline_choice == 1 and not lifeline_5050_used:
                    lifeline_5050_used = True
                    correct = q[5]
                    options = [1, 2, 3, 4]
                    options.remove(correct)
                    removed = random.sample(options, 2)
                    print("\n💡 50-50 Activated! Remaining options:")
                    for opt in range(1, 5):
                        if opt not in removed:
                            print(f"{opt}. {q[opt]}")
                    lifeline_applied = True

                elif lifeline_choice == 2 and not lifeline_switch_used:
                    lifeline_switch_used = True
                    print("\n🔄 Switching the question...")

                    # Use switch question instead of current
                    print(f"\nSwitch Question for Rs.{levels[i]}")
                    print(f"Q: {switch_question[0]}")
                    print(f"a. {switch_question[1]}       b. {switch_question[2]}")
                    print(f"c. {switch_question[3]}       d. {switch_question[4]}")

                    while True:
                        try:
                            switch_reply = int(input("\nEnter Your Answer (1-4) or 0 to Quit: "))
                            if switch_reply == 0:
                                print("\n👋 You chose to quit.")
                                print(f"\n🥳 Total Money you won Rs.{money}")
                                print("\n🙏 Thank you for playing Kaun Banega Crorepati!")
                                exit()
                            elif switch_reply in [1, 2, 3, 4]:
                                if switch_reply == switch_question[5]:
                                    print(f"\n💥 Correct Answer, You Won Rs.{levels[i]}")
                                    if i == 4:
                                        money = 10000
                                    elif i == 9:
                                        money = 320000
                                    else:
                                        money = levels[i]
                                else:
                                    print("\n❌ Wrong Answer! Better Luck Next Time")
                                    print(f"\n🥳 Total Money you won Rs.{money}")
                                    print("\n🙏 Thank you for playing Kaun Banega Crorepati!")
                                    exit()
                                break
                            else:
                                print("❌ Invalid input. Please enter between 1-4.")
                        except ValueError:
                            print("❌ Please enter a number.")
                    break  # go to next main question
                else:
                    print("❌ You have already used that lifeline or invalid choice.")
                # lifeline done, ask main input again
            elif reply in [1, 2, 3, 4]:
                if reply == q[5]:
                    print(f"\n💥 Correct Answer, You Won Rs.{levels[i]}")
                    if i == 4:
                        money = 10000
                    elif i == 9:
                        money = 320000
                    else:
                        money = levels[i]
                    break
                else:
                    print("\n❌ Wrong Answer! Better Luck Next Time")
                    print(f"\n🥳 Total Money you won Rs.{money}")
                    print("\n🙏 Thank you for playing Kaun Banega Crorepati!")
                    exit()
            else:
                print("❌ Invalid input. Please choose between 1-4, 0 or 9.")
        except ValueError:
            print("❌ Please enter a number.")
    i += 1  # move to next question

# All correct
print(f"\n🥳 Total Money you won Rs.{money}")
print("\n🎉 Congratulations on completing all questions!")