# -*- coding: utf-8 -*-
# Author:leali
# Description: ConfigParser
# Version:v1.0
# Date:4/18/2018-11:09 PM

import configparser as conf


def read_config(file):
    """
    read config from file
    :param file:
    :return:
    """
    config = conf.ConfigParser()
    config.read(file)
    # 获得配置文件根的列表
    section = config.sections()
    print(section)
    # if not exists, throw NoSectionError
    try:
        db = config.options("db")
        print(db)
        # ['db_host', 'db_port', 'db_user', 'db_pass']
        print(config.items("db"))
        # [('db_host', '192.168.1.1'), ('db_port', '3306'), ('db_user', 'root'), ('db_pass', 'leal520')]
        db_host = config.get("db", "db_host")
        print(db_host)
        print(config.getint("db", 'db_port'))
        print(config.getfloat("db", "db_port"))  # 会自动转换
    except Exception as error:
        print("Conf Exception:", error)


def write_config(file):
    """
    modify value
    :param file:
    :return:
    """
    config = conf.ConfigParser()
    config.read(file)
    # update
    config.set("db", "db_host", "127.0.0.1")
    with open(file, "w") as f:
        config.write(f)
    print(config.items("db")[0][1])


def remove_config(file):
    """
    remove cconfig
    :param file:
    :return:
    """
    config = conf.ConfigParser()
    config.read(file)
    if config.items("leal") is None:
        config.add_section('leal')
        config.set('leal', 'int', '15')
        config.set('leal', 'bool', 'true')
        config.set('leal', 'float', '3.1415')
        config.write(open(file, "w"))
    try:
        config.remove_option('leal', 'int')
        config.remove_section('liuqing') # if not exists not throw exception
        config.write(open(file, "w"))
    except Exception as error:
        print("Conf Exception:", error)
    print(config.items("leal"))


if __name__ == "__main__":
    file = "data/mysql.conf"
    # read_config(file)
    # write_config(file)
    remove_config(file)
