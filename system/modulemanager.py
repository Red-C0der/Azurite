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


def loadmodules(module_list, debug=0):
    try:
        import logger
        import configparser as cfg
        lloc = "File: modulemanager.py | Function: loadmodules | Message: "
        logger.write("i", "Trying to load modules from list with arguments: module_list=["+str(module_list)+"], debug=["+str(debug)+"]!", lloc=lloc)
        elems = cfg.getelementlist(debug=debug)
        if debug == 1:
            logger.write("d", "Got elems from cfg.getelementlist()!", lloc=lloc)
        if debug == 1:
            logger.write("d", "Starting ordering ids, types, actives and paths!", lloc=lloc)
        ids = []
        types = []
        actives = []
        paths = []
        i = 0
        for elem in elems:
            ids.append(elem["id"])
            types.append(elem["type"])
            actives.append(elem["active"])
            if types[i] == "custom":
                paths.append(elem["importpath"])
            else:
                pass
            i = i + 1
        if debug == 1:
            logger.write("d", "Finished ordering ids, types, actives and paths!", lloc=lloc)
        realimport = []
        if debug == 1:
            logger.write("d", "Created realimport list!", lloc=lloc)
        for module in module_list:
            i = 0
            for id in ids:
                if id == module:
                    if actives[i] == "True":
                        if types[i] == "custom":
                            realimport.append(paths[i])
                        elif types[i] == "system":
                            realimport.append(module)
                    else:
                        logger.write("ex", "Exception while trying to import none-active module! module=["+str(module)+"]", lloc=lloc)
                i = i + 1
        if debug == 1:
            logger.write("d", "Filled realimport list! ["+str(realimport)+"]", lloc=lloc)
        modules = map(__import__, realimport)
        if debug == 1:
            logger.write("d", "Successfully imported from realimport list!", lloc=lloc)
        return modules
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


def checkforactivemodules(module_list, debug=0):
    try:
        import logger
        import configparser as cfg
        lloc = "File: modulemanager.py | Function: checkforactivemodules | Message: "
        logger.write("i", "Trying to check module-list in sys.xml with arguments: debug=["+str(debug)+"]!", lloc=lloc)
        elems = cfg.getelementlist(debug=debug)
        if debug == 1:
            logger.write("d", "Got elems from cfg.getelementlist()!", lloc=lloc)
        modules = {}
        for module in module_list:
            modules[module] = False
        if debug == 1:
            logger.write("d", "Created and filled modules dictionary!", lloc=lloc)
        activemodules = []
        for elem in elems:
            attrib = elem
            id = attrib["id"]
            active = attrib["active"]
            if active == "True":
                activemodules.append(id)
        if debug == 1:
            logger.write("d", "Searched and filled active modules into activemodules dictionary!", lloc=lloc)
        for module in modules:
            for amodul in activemodules:
                if amodul == module:
                    modules[module] = True
        if debug == 1:
            logger.write("d", "Updated active states in modules dictionary!", lloc=lloc)
        return modules
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