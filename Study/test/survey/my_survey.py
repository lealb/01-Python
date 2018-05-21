# -*- coding: utf-8 -*-
# Author:leali
# Description: 网友问题测试，主要解决简单的列表和面向对象使用，兼用了单元测试unittest模块的使用
# Version:v1.0
# Date:5/21/2018-9:01 PM

class AnonymousSurvey():
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单位调查答卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有的答卷"""
        print("survey results:")
        for response in self.responses:
            print('- ' + response)

