# -*- coding: utf-8 -*-
# Author:leali
# Description: 操作注册表
# Version:v1.0
# Date:4/24/2018-10:02 AM

import win32api
import win32con


def simple_test():
    """
    简单读取,windows 有权限问题，需要以管理员权限运行
    :return:
    """
    name = r"SOFTWARE\Adobe\Photoshop\120.0\ApplicationPath"
    try:
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE, name, 0, win32con.KEY_ALL_ACCESS)
        try:
            # 查询默认值
            value = win32api.RegQueryValue(key, "")
            print(value)
        except Exception as error:
            """
            (2, 'RegQueryValue', 'The system cannot find the file specified.')
            """
            print("Error:", error)
        finally:
            win32api.RegCloseKey(key)
    except Exception as error:
        """
        Error: (5, 'RegOpenKeyEx', 'Access is denied.')
        """
        print("Error:", error)


def operate_regedit_query(name):
    """
    以IE 为例
    :return:
    """
    # 查询
    try:
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE, name, 0, win32con.KEY_ALL_ACCESS)
        try:
            # 查询默认值
            print("Default Value:", win32api.RegQueryValue(key, ""))
            # 读取Version
            print("Version:", win32api.RegQueryValueEx(key, "Version"))
            # 读取项的基本信息
            print("Other Info:", win32api.RegQueryInfoKey(key))
        except Exception as error:
            """
            (2, 'RegQueryValue', 'The system cannot find the file specified.')
            """
            print("Error:", error)
        finally:
            win32api.RegCloseKey(key)
    except Exception as error:
        """
        Error: (5, 'RegOpenKeyEx', 'Access is denied.')
        """
        print("Error:", error)


def operate_regedit_update(name):
    """
    如果key不存在，则新增
    :return:
    """
    # 设置
    try:
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE, name, 0, win32con.KEY_ALL_ACCESS)
        try:
            # 设置默认值
            win32api.RegSetValue(key, "", win32con.REG_SZ, "test")
            print("Default Value:", win32api.RegQueryValue(key, ""))
            win32api.RegSetValue(key, "", win32con.REG_SZ, "")
            # 设置Version 9.11.16299.0
            win32api.RegSetValueEx(key, "Version", 0, win32con.REG_SZ, "9.11.16299.1")
            print("Version:", win32api.RegQueryValueEx(key, "Version"))
            # 恢复版本信息
            win32api.RegSetValueEx(key, "Version", 0, win32con.REG_SZ, "9.11.16299.0")
            # 设置不存在的key
            win32api.RegSetValueEx(key, "testNot", 0, win32con.REG_SZ, "Leal")
            print("Read Test Info:", win32api.RegQueryValueEx(key, "testNot"))
        except Exception as error:
            """
            (2, 'RegQueryValue', 'The system cannot find the file specified.')
            """
            print("Error:", error)
        finally:
            win32api.RegCloseKey(key)
    except Exception as error:
        """
        Error: (5, 'RegOpenKeyEx', 'Access is denied.')
        """
        print("Error:", error)


def operate_regedit_create(name):
    """
    add
    :return:
    """
    # 增加
    try:
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE, name, 0, win32con.KEY_ALL_ACCESS)
        try:
            # 设置默认值
            win32api.RegCreateKey(key, "CreateLeal")
            print("CreateLeal:", win32api.RegQueryInfoKey(key))
            # 删除
            win32api.RegDeleteKey(key, "Python")
            print("CreateLeal:", win32api.RegQueryInfoKey(key))
            # win32api.RegCreateKeyEx(key, "CreateLeal123", 0, win32con.REG_SZ, "123")
            # print("CreateLeal123:", win32api.RegQueryInfoKeyW(key, "CreateLeal123"))

        except Exception as error:
            """
            (2, 'RegQueryValue', 'The system cannot find the file specified.')
            """
            print("Error:", error)
        finally:
            win32api.RegCloseKey(key)
    except Exception as error:
        """
        Error: (5, 'RegOpenKeyEx', 'Access is denied.')
        """
        print("Error:", error)


def auto_run():
    key_Names = [
        r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
        r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce',
        r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnceEx',
        r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
        r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce'
    ]

    for key_name in key_Names:
        name = key_name.split("\\", 1)
        # print(name[0])
        if name[0] == "HKEY_LOCAL_MACHINE":
            key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE, name[1], 0, win32con.KEY_READ)
        elif name[0] == "HKEY_CURRENT_USER":
            key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, name[1], 0, win32con.KEY_READ)
        elif name[0] == "HKEY_CLASSES_ROOT":
            key = win32api.RegOpenKey(win32con.HKEY_CLASSES_ROOT, name[1], 0, win32con.KEY_READ)
        elif name[0] == "HKEY_CURRENT_CONFIG":
            key = win32api.RegOpenKey(win32con.HKEY_CURRENT_CONFIG, name[1], 0, win32con.KEY_READ)
        elif name[0] == "HKEY_USERS":
            key = win32api.RegOpenKey(win32con.HKEY_USERS, name[1], 0, win32con.KEY_READ)
        else:
            print("ERROR:", name[0])
        info = win32api.RegQueryInfoKey(key)
        for i in range(0, info[1]):
            value = win32api.RegEnumValue(key, i)
            print(value[0], value[1])
        win32api.RegCloseKey(key)


if __name__ == "__main__":
    # simple_test()
    name = r"SOFTWARE\Microsoft\Internet Explorer"
    # operate_regedit_query(name)
    # operate_regedit_update(name)
    # operate_regedit_create(name)
    auto_run()
