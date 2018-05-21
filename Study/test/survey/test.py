# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:5/21/2018-9:04 PM

import unittest
from test.survey import my_survey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonmyousSurvey类的测试"""

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "what language did you first learn to speak?"
        test_survey = my_survey.AnonymousSurvey(question)
        test_survey.store_response('English')

        self.assertIn('English', test_survey.responses)


if __name__ == "__main__":
    TestAnonymousSurvey().test_store_single_response()
