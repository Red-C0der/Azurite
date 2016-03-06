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


def colorPrint(text, fgc=500, bgc=500, attrc="", newline=True, debug=0):
    try:
        import logger
        lloc = "File: output.py | Function: colorPrint | Message: "
        logger.write("i", "Trying to use colorPrint with arguments: text=["+str(text)+"], fgc=["+str(fgc)+"], bgc=["+str(fgc)+"], attrc=["+str(attrc)+"], newline=["+str(newline)+"],debug=["+str(debug)+"]!", lloc=lloc)
        from colored import fg, style, attr, bg
        import sys
        if newline is True:
            if fgc != 500:
                if bgc == 500:
                    if attrc == "":
                        color = fg(fgc)
                        att = attr(attrc)
                        print (color + text + style.RESET)
                        return True
                    else:
                        color = fg(fgc)
                        att = attr(attrc)
                        print (color + att + text + style.RESET)
                        return True
                else:
                    if attrc == "":
                        color = fg(fgc) + bg(bgc)
                        att = attr(attrc)
                        print (color + text + style.RESET)
                        return True
                    else:
                        color = fg(fgc) + bg(bgc)
                        att = attr(attrc)
                        print (color + att + text + style.RESET)
                        return True
            else:
                if bgc != 500:
                    if attrc == "":
                        color = bg(bgc)
                        att = attr(attrc)
                        print (color + text + style.RESET)
                        return True
                    else:
                        color = bg(bgc)
                        att = attr(attrc)
                        print (color + att + text + style.RESET)
                        return True
        else:
            if fgc != 500:
                if bgc == 500:
                    if attrc == "":
                        color = fg(fgc)
                        att = attr(attrc)
                        sys.stdout.write(color + text + style.RESET)
                        return True
                    else:
                        color = fg(fgc)
                        att = attr(attrc)
                        sys.stdout.write(color + att + text + style.RESET)
                        return True
                else:
                    if attrc == "":
                        color = fg(fgc) + bg(bgc)
                        att = attr(attrc)
                        sys.stdout.write(color + text + style.RESET)
                        return True
                    else:
                        color = fg(fgc) + bg(bgc)
                        att = attr(attrc)
                        sys.stdout.write(color + att + text + style.RESET)
                        return True
            else:
                if bgc != 500:
                    if attrc == "":
                        color = bg(bgc)
                        att = attr(attrc)
                        sys.stdout.write(color + text + style.RESET)
                        return True
                    else:
                        color = bg(bgc)
                        att = attr(attrc)
                        sys.stdout.write(color + att + text + style.RESET)
                        return True
    except ImportError:
        logger.write("e", "ImportError: Some module could not be imported!", lloc=lloc)
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


def statePrint(state, message, debug=0):
    try:
        import logger
        lloc = "File: output.py | Function: statePrint | Message: "
        logger.write("i", "Trying to use statePrint with arguments: state=["+str(state)+"], message=["+str(message)+"], debug=["+str(debug)+"]!", lloc=lloc)
        import termcolor
        if state == "":
            print("[....] " + message)
            return True
        if state == "ok":
            print("[ " + termcolor.colored("OK", "green", attrs=["bold"]) + " ] " + termcolor.colored(message, "green", attrs=["bold"]))
            return True
        if state == "error":
            print("[" + termcolor.colored("ERROR", "red", attrs=["blink", "bold"]) + "] " + termcolor.colored(message, "red", attrs=["bold"]))
            return True
        if state == "warning":
            # 208
            from colored import fg, attr, style
            print("[" + fg(241) + attr("bold") + attr("blink") + "WARNING" + style.RESET + "] " + fg(241) + attr("bold") + message + style.RESET)
            return True
        if state == "info":
            print("[" + termcolor.colored("INFO", "cyan", attrs=["bold"]) + "] " + termcolor.colored(message, "cyan", attrs=["bold"]))
            return True
        if state == "debug":
            print("[" + termcolor.colored("DEBUG", "magenta", attrs=["bold"]) + "] " + termcolor.colored(message, "magenta", attrs=["bold"]))
            return True
        if state == "sys":
            print("[" + termcolor.colored("SYSTEM", "blue", attrs=["bold"]) + "] " + termcolor.colored(message, "blue", attrs=["bold"]))
            return True
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