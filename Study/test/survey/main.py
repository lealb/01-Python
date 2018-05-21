# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:5/21/2018-9:03 PM
from test.survey import my_survey

if __name__ == "__main__":
    # 定义一个问题，并创建一个表示调查的AnonymouSurvey对象
    question = "What language did you fist learn to speak?"
    my_survey = my_survey.AnonymousSurvey(question)

    # 显示问题并储存答案
    my_survey.show_question()
    print("enter 'q' at any time to quit.\n")
    while True:
        response = input("language:")
        if response == 'q':
            break
        my_survey.store_response(response)

    # 显示调查结果
    print("\n'Thank you to everyone who participated in the survey!")
    my_survey.show_results()
