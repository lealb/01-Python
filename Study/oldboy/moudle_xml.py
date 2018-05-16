# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:4/19/2018-11:11 AM
import xml.etree.ElementTree as ET


def read_xml(file):
    """
    可通过root[0][1].text获得没有属性的text
    :param file:
    :return:
    """
    tree = ET.parse(file)
    root = tree.getroot()
    # print("root:" % (root.tag, root.attrib))
    print(root.tag, ":", root.attrib)
    for child in root:
        print(child.tag, ":", child.attrib)
        for i in child:
            print(i.tag, ":", i.attrib)


if __name__ == "__main__":
    file = "data/country.xml"
    read_xml(file)
