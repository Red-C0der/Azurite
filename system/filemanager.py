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

class file:
    def new(self, path, filename, debug=0):
        pass
        import os

class dir:
    def chmod(self, path, mode, debug=0):
        try:
            import modulemanager as mod
            mod = mod.loadmodules(["logger", "os"], debug=debug)
            lloc = "File: filemanager.py | Class: dir | Function: chmod | Message: "
            mod[0].write("i", "Trying to use chmod with arguments: path=["+str(path)+"], mode=["+str(mode)+"], debug=["+str(debug)+"]!", lloc=lloc)
            logger = mod[0]
            if debug == 1:
                logger.write("d", "Created logger instance!", lloc=lloc)
            os = mod[1]
            if debug == 1:
                logger.write("d", "Created os instance!", lloc=lloc)
            os.chmod(path, mode)
            if debug == 1:
                logger.write("d", "Successfully changed mode of path ["+str(path)+"] to mode ["+str(mode)+"]", lloc=lloc)
            return True
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