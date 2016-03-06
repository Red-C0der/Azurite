# -*- coding: utf-8 -*-
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
#  |   Project-ID: 0777                                                            |
#  |   GitHub-Page: https://github.com/Red-C0der/Azurite-Raspberry                 |
#  |   License: /LICENSE.txt                                                       |
#  |                                                                               |
#  |                                                                               |
#  |   Personal-Info:                                                              |
#  |   Twitter: https://twitter.com/red_c0der                                      |
#  |   FaceBook: -                                                                 |
#  |   E-Mail: redc0der.mail@gmail.com                                             |
#   \=============================================================================/


def newconsole(user, host, title, debug=0):
    try:
        import logger
        import sys
        lloc = "File: console.py | Function: newconsole | Message: "
        logger.write("i", "Trying create new console with arguments: user=["+str(user)+"], host=["+str(host)+"], title=["+str(title)+"], debug=["+str(debug)+"]!", lloc=lloc)
        while True:
            userinput = raw_input(user+"$ ")
            uinsplit(userinput, debug=debug)
    except:
        pass


def uinsplit(userinput, debug=0):
    try:
        import logger
        lloc = "File: console.py | Function: uinsplit | Message: "
        logger.write("i", "Trying to split userinput with arguments: userinput=["+str(userinput)+"], debug=["+str(debug)+"]!", lloc=lloc)
        splitted = userinput.split(" ")
        command = splitted[0]
        del splitted[0]
        args = splitted
        print "args: "+args
        commandanalyzer(command, args, debug=debug)
    except:
        pass


def commandanalyzer(command, args, debug=0):
    try:
        import logger
        import termcolor
        lloc = "File: console.py | Function: commandanalyzer | Message: "
        logger.write("i", "Trying to analyze command with arguments: command=["+str(command)+"], args=["+str(args)+"], debug=["+str(debug)+"]!", lloc=lloc)

        if command == "shutdown":
            if not args:
                print(termcolor.colored("USAGE: shutdown [option]", "red", attrs=["bold"]))
            else:
                if len(args) > 0:
                    print "more than 0"
                if len(args) > 1:
                    print "more than 1"

    except:
        pass


def getTerminalSize(debug=0):
    try:
        import os
        env = os.environ
        def ioctl_GWINSZ(fd):
            try:
                import fcntl, termios, struct, os
                cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
            '1234'))
            except:
                return
            return cr
        cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
        if not cr:
            try:
                fd = os.open(os.ctermid(), os.O_RDONLY)
                cr = ioctl_GWINSZ(fd)
                os.close(fd)
            except:
                pass
        if not cr:
            cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
        return int(cr[1]), int(cr[0])
    except ImportError:
        logger.write("e", "ImportError: Some module in list created the error!", lloc=lloc)
        return False
    except StopIteration:
        logger.write("e", "StopIteration: next() method does not point at any object!", lloc=lloc)
        return False
    except SystemExit:
        logger.write("e", "SystemExit: sys.exit() was executed!", lloc=lloc)
        return False
    except ArithmeticError:
        logger.write("e", "ArithmeticError: Numeric calculation error!", lloc=lloc)
        return False
    except OverflowError:
        logger.write("e", "OverflowError: Calculation exceeded maximum limit for numeric type!", lloc=lloc)
        return False
    except FloatingPointError:
        logger.write("e", "FloatingPointError: FloatingPoint calculation failed!", lloc=lloc)
        return False
    except ZeroDivisionError:
        logger.write("e", "ZeroDivisionError: Division or modulo by Zero took place!", lloc=lloc)
        return False
    except AssertionError:
        logger.write("e", "AssertionError: Assert statement failed!", lloc=lloc)
        return False
    except AttributeError:
        logger.write("e", "AttributeError: Failure of attribute reference or assignment!", lloc=lloc)
        return False
    except EOFError:
        logger.write("e", "EOFError: No input from raw_input() or input() as the file has ended!", lloc=lloc)
        return False
    except ImportError:
        logger.write("e", "ImportError: Import statement failed!", lloc=lloc)
        return False
    except KeyboardInterrupt:
        logger.write("e", "KeyboardInterrupt: Program has ended, during KeyboardInterrupt (Ctrl + C)!", lloc=lloc)
        return False
    except LookupError:
        logger.write("e", "LookupError: LookupError!", lloc=lloc)
        return False
    except IndexError:
        logger.write("e", "IndexError: Index in sequence was not found!", lloc=lloc)
        return False
    except KeyError:
        logger.write("e", "KeyError: Key in dictionary was not found!", lloc=lloc)
        return False
    except NameError:
        logger.write("e", "NameError: Identifier was not found in local or global namespace!", lloc=lloc)
        return False
    except UnboundLocalError:
        logger.write("e", "UnboundLocalError: No value was assigned to variable in function or method!", lloc=lloc)
        return False
    except EnvironmentError:
        logger.write("e", "EnvironmentError: Exception occurred outside the Python environment!", lloc=lloc)
        return False
    except IOError:
        logger.write("e", "IOError: Input / Output operation failed!", lloc=lloc)
        return False
    except SyntaxError:
        logger.write("e", "SyntaxError: Syntax error in python code!", lloc=lloc)
        return False
    except IndentationError:
        logger.write("e", "IndentationError: Indentation is not specified properly!", lloc=lloc)
        return False
    except SystemError:
        logger.write("e", "SystemError: Interpreter found internal problem, but interpreter has not exited!", lloc=lloc)
        return False
    except TypeError:
        logger.write("e", "TypeError: Operation or Function is attempted which is invalid for the specific data type!", lloc=lloc)
        return False
    except ValueError:
        logger.write("e", "ValueError: Built-in function for data type has valid type of arguments, but arguments have invalid values specified!", lloc=lloc)
        return False
    except RuntimeError:
        logger.write("e", "RuntimeError: Generated error does not fall into any category!", lloc=lloc)
        return False
    except NotImplementedError:
        logger.write("e", "NotImplementedError: Abstract method that needs to be implemented in an inherited class is not actually implemented!", lloc=lloc)
        return False