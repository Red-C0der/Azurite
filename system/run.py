# -*- coding: utf-8 -*-
__author__ = 'Red_C0der'

#   /=============================================================================\
#  |   ██████╗ ███████╗██████╗          ██████╗ ██████╗ ██████╗ ███████╗██████╗    |
#  |   ██╔══██╗██╔════╝██╔══██╗        ██╔════╝██╔═████╗██╔══██╗██╔════╝██╔══██╗   |
#  |   ██████╔╝█████╗  ██║  ██║        ██║     ██║██╔██║██║  ██║█████╗  ██████╔╝   |
#  |   ██╔══██╗██╔══╝  ██║  ██║        ██║     ████╔╝██║██║  ██║██╔══╝  ██╔══██╗   |
#  |   ██║  ██║███████╗██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║   |
#  |                                                                               |
#  |   Project-Name: Azurit                                                        |
#  |   Version: 0.0.3                                                              |
#  |   Development-State: Alpha                                                    |
#  |   Project-ID: 0000                                                            |
#  |   GitHub-Page: http://red-c0der.github.io/Azurite                             |
#  |   License: /LICENSE.txt                                                       |
#  |                                                                               |
#  |                                                                               |
#  |   Personal-Info:                                                              |
#  |   Twitter: https://twitter.com/red_c0der                                      |
#  |   FaceBook: -                                                                 |
#  |   E-Mail: redc0der.mail@gmail.com                                             |
#   \=============================================================================/

def run(args=[]):
    import os
    if len(args) != 0:
        buffer = ''
        for arg in args:
            buffer = buffer + arg + ' '
        os.system('python system.py ' + buffer)
    else:
        os.system('python system.py')

def showhelp():
    print 'The Azurite run.py script can be used with the following parameters:  '
    print '-d [0/1]'
    print '-shell'
    print '-'
    print '-'



if __name__ == '__main__':
    import sys
    args = sys.argv
    if len(args) > 1:
        if args[1] == 'help' or args[1] == '-h' or args[1] == '?':
            showhelp()
            sys.exit()
        else:
            run(args)
    else:
        run()