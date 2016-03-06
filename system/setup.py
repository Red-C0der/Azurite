# coding=utf-8
__author__ = 'Red_C0der'

#   /=============================================================================\
#  |   ██████╗ ███████╗██████╗          ██████╗ ██████╗ ██████╗ ███████╗██████╗    |
#  |   ██╔══██╗██╔════╝██╔══██╗        ██╔════╝██╔═████╗██╔══██╗██╔════╝██╔══██╗   |
#  |   ██████╔╝█████╗  ██║  ██║        ██║     ██║██╔██║██║  ██║█████╗  ██████╔╝   |
#  |   ██╔══██╗██╔══╝  ██║  ██║        ██║     ████╔╝██║██║  ██║██╔══╝  ██╔══██╗   |
#  |   ██║  ██║███████╗██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║   |
#  |                                                                               |
#  |   Project-Name: Azurite                                                       |
#  |   Version: 0.0.2                                                              |
#  |   Development-State: Alpha                                                    |
#  |   Project-ID: 0776                                                            |
#  |   GitHub-Page: http://red-c0der.github.io/Azurite                             |
#  |   License: /LICENSE.txt                                                       |
#  |                                                                               |
#  |                                                                               |
#  |   Personal-Info:                                                              |
#  |   Twitter: https://twitter.com/red_c0der                                      |
#  |   FaceBook: -                                                                 |
#  |   E-Mail: redc0der.mail@gmail.com                                             |
#   \=============================================================================/

def install():
    print " /=============================================================================\ "
    print "|   ██████╗ ███████╗██████╗          ██████╗ ██████╗ ██████╗ ███████╗██████╗    |"
    print "|   ██╔══██╗██╔════╝██╔══██╗        ██╔════╝██╔═████╗██╔══██╗██╔════╝██╔══██╗   |"
    print "|   ██████╔╝█████╗  ██║  ██║        ██║     ██║██╔██║██║  ██║█████╗  ██████╔╝   |"
    print "|   ██╔══██╗██╔══╝  ██║  ██║        ██║     ████╔╝██║██║  ██║██╔══╝  ██╔══██╗   |"
    print "|   ██║  ██║███████╗██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║   |"
    print "|                                                                               |"
    print "|   Project-Name: Azurite                                                       |"
    print "|   Version: 0.0.2                                                              |"
    print "|   Development-State: Alpha                                                    |"
    print "|   Project-ID: 0776                                                            |"
    print "|   GitHub-Page: http://red-c0der.github.io/Project-Azurite                     |"
    print "|   License: /LICENSE.txt                                                       |"
    print "|                                                                               |"
    print "|                                                                               |"
    print "|   Personal-Info:                                                              |"
    print "|   Twitter: https://twitter.com/red_c0der                                      |"
    print "|   FaceBook: -                                                                 |"
    print "|   E-Mail: redc0der.mail@gmail.com                                             |"
    print " \=============================================================================/"
    print ""
    print ""
    print ""
    print "Start installation? (y/n)"
    selection = raw_input("=> ")
    if selection.lower() == "n":
        print "Canceling installation!"
        import sys
        sys.exit(0)
    import os
    import xml.etree.ElementTree as ET
    tree = ET.parse("../settings/setup_sequence.xml")
    root = tree.getroot()
    setup_sequence = []
    for child in root:
        if child.tag == "command":
            tmp = str(child.tag) + "[:]" + str(child.attrib["exec"])
        if child.tag == "setupfile":
            tmp = str(child.tag) + "[:]" + str(child.attrib["file"])
    for item in setup_sequence:
        tmp = item.split("[:]")
        type = tmp[0]
        arg = tmp[1]
        if type == "command":
            os.system(arg)
        if type == "setupfile":
            os.system("python "+arg+" install")