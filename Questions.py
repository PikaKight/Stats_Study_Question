from operator import length_hint
import pandas as pd
import random
from typing import List

class Questions:
    
    used_questions = []

    def __init__(self) -> None:
        self.__df = pd.read_excel("Stats Question.xlsx")
        self.__random_question = random.randint(0,len(self.__df))

    def get_questions(self):
        return self.__df["Question"].iloc[self.__random_question]

    def get_options(self):
        self.options = [self.__df.iloc[self.__random_question]["a"], self.__df.iloc[self.__random_question]["b"], self.__df.iloc[self.__random_question]["c"],
        self.__df.iloc[self.__random_question]["d"],self.__df.iloc[self.__random_question]["e"]]
        return self.options

    def get_answer(self):
        return self.__df.iloc[self.__random_question]["Answer"]
    
    def new_question(self):
        Questions.used_questions.append(self.__random_question)
        self.__random_question = random.randint(0,len(self.__df))
        while True:
            if len(Questions.used_questions) == len(self.__df):
                Questions.used_questions.clear()
                self.__random_question = random.randint(0,len(self.__df))
                break
            
            if self.__random_question not in Questions.used_questions:
                break

            self.__random_question = random.randint(0,len(self.__df))

    @classmethod
    def set_used_questions(Questions, questions):
        Questions.used_questions = questions

    @classmethod
    def get_used_question(Questions):
        return Questions.used_questions

        
if __name__ == "__main__":
    test = Questions()
    print(test.get_questions())
    print(test.get_options())
    test.new_question()
    print(test.get_questions())
    print(Questions.get_used_question())