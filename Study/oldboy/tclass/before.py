# -*- coding: utf-8 -*-
# Author:leali
# Description: 作为雷和对象的引子
# Version:v1.0
# Date:5/16/2018-10:06 PM


"""
你现在是一家游戏公司的开发人员，现在需要你开发一款叫做<人狗大战>的游戏，你就思考呀，人狗作战，
那至少需要2个角色，一个是人， 个是狗，
且人和狗都有不同的技能，比如人拿棍打狗， 狗可以咬人，怎么描述这种不同的角色和他们的功能呢
"""


def person(name, age, sex, job):
    data = {
        "name": name,
        "age": age,
        "sex": sex,
        "job": job
    }
    return data


def dog(name, dog_type):
    data = {
        "name": name,
        "dog_type": dog_type
    }
    return data


def bark(d):
    print("dog %s:wang.wang..wang..." % d['name'])


def walk(p):
    print("person %s is walking..." % p['name'])


if __name__ == "__main__":
    d1 = dog("李磊", "京巴")
    p1 = person("严帅", 36, "F", "运维")
    p2 = person("林海峰", 27, "F", "Teacher")
    walk(p1)
    bark(d1)
    #意外处理 人调用狗的方法
    bark(p1) # 严格意义是不允许的
    # 可把方法当做内置方法限制使用，但是这样会完全隔离两个角色的方法

