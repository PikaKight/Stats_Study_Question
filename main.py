import Questions
import json

while True:

    print("""
          Hello and welcome to Study Buddy!
          Please select what you want to do:
          1. Answer 15 questions
          2. Quit
          """)

    choice = int(input())

    match choice:
        case 1:
            questions = Questions.Questions()
            with open('questions.json', 'r') as f:
                used_q = json.load(f)

            Questions.Questions.set_used_questions(used_q["questions"])

            i = 1
            score = 0
            char_set = ['a', 'b', 'c', 'd', 'e']
            while i < 16:
                print(questions.get_questions())
                
                for j in range(len(questions.get_options())):
                    print(f"{char_set[j]}: {questions.get_options()[j]}")

                answer = input("Answer:") 

                if answer == questions.get_answer():
                    print("\nYou are correct.\nNext Question\n")
                    score += 1

                else:
                    print(f"\nYou are wrong. Correct answer is {questions.get_answer()}\nNext Question\n")
                
                i+=1
                questions.new_question()
                print(Questions.Questions.get_used_question())

            print(Questions.Questions.get_used_question())
            temp = {"questions": Questions.Questions.get_used_question()}

            with open('questions.json', 'w') as f:
                json.dump(temp, f) 


            print(score)           
            break
        case 2:
            quit()