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

class Startup:

    def __init__(self, args):
        lloc = 'File: system.py | Class: Startup | Function: __init__ | Message:'
        print "Initialising System Startup"

        print "Loading Logging Module"
        try:
            import modules.redslogger
        except ImportError as e:
            self.__end__("Startup.__init__() - import modules.redslogger could not be imported!")
            print e

        print "Creating modules.logging.Logger instance"
        try:
            Logger = modules.redslogger.Logger()
        except:
            self.__end__("Startup.__init__() - could not create modules.redslogger.Logger instance!")
        Logger.write('Created modules.logging.Logger instance!', level='i', lloc=lloc)

        print "Loading Output Module"
        try:
            import modules.output
        except ImportError as e:
            self.__end__("Startup.__init__() - import modules.output could not be imported!")
            print e

        print "Crating modules.output.Out instance"
        try:
            Out = modules.output.Out()
        except:
            self.__end__("Startup.__init__() - could not create modules.output.Out instance!")
        Out.prints('ok', 'Created modules.output.Out instance')

        Out.prints('', 'Crating System instance')
        try:
            self.System_instance = System()
        except:
            self.__end__("Startup.__init__() - could not create System instance!")
        Out.prints('ok', 'Created System instance')



        S = self.System_instance.AzuriteShell()
        S.active_user = self.System_instance.RAM['current_user']
        S.set_prompt()
        S.cmdloop()

    def __end__(self, problem):
        print ""
        print "ERROR: Startup was cancel due to this Problem:"
        print problem
        print ""
        sys.exit(0)


class System:

    def __init__(self):
        self.DEBUG = False

        self.Logger_instance = None
        self.Out_instance = None

        self.RAM = {
            'current_user': 'root'
        }


    import cmd2
    class AzuriteShell(cmd2.Cmd):
        """The Azurite Interactive Shell"""

        active_user = 'null'
        prompt = 'Azurite:'+active_user+'$ '

        def set_prompt(self):
            self.prompt = 'Azurite:'+self.active_user+'$ '




if __name__ == '__main__':
    print ""
    print ""
    print ""
    import sys
    args = sys.argv
    if len(args) > 1:
        args.pop(0)
        args.pop(0)
    elif len(args) > 0:
        args.pop(0)
    Startup = Startup(args)