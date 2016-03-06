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

def newfile(filename, debug=0):
    try:
        import os
        import logger
        lloc = "File: configparser.py | Function: newfile | Message: "
        logger.write("i", "Creating new configfile with arguments: filename=["+str(filename)+"], debug=["+str(debug)+"]!", lloc=lloc)
        filename = str(filename)
        if debug == 1:
            logger.write("d", "Successfully changed/checked filename type.", lloc=lloc)
        nfile = open(str(filename), "w+")
        if debug == 1:
            logger.write("d", "Successfully opened file ["+str(filename)+"]", lloc=lloc)
        file.close()
        if debug == 1:
            logger.write("d", "Successfully created new file ["+str(filename)+"]!", lloc=lloc)
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


def delfile(filename, debug=0):
    try:
        import os
        import logger
        lloc = "File: configparser.py | Function: delfile | Message: "
        logger.write("i", "Deleting configfile with arguments: filename=["+str(filename)+"], debug=["+str(debug)+"]!", lloc=lloc)
        os.system("rm "+str(filename))
        if debug == 1:
            logger.write("d", "Successfully ran command to delete file ["+str(filename)+"] but could not check if file is fully removed!", lloc=lloc)
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


def makebackup(sourcefile="sys.xml", filepath="../settings/", debug=0):
    try:
        import os
        import logger
        lloc = "File: configparser.py | Function: makebackup | Message: "
        logger.write("i", "Trying to make a backup with arguments: sourcefile=["+str(sourcefile)+"], filepath=["+str(filepath)+"], debug=["+str(debug)+"]!", lloc=lloc)
        tmp = sourcefile
        filename = filepath + tmp
        if debug == 1:
            logger.write("d", "filename was successfully merged! filename=["+str(filename)+"]", lloc=lloc)
        sourcefile = open(filename, "r").read()
        if debug == 1:
            logger.write("d", "Sourcefile was successfully opened and red!", lloc=lloc)
        destinationfile = open(filepath + "backup_" + tmp, "w")
        if debug == 1:
            logger.write("d", "Destinationfile was successfully opened!", lloc=lloc)
        destinationfile.write(sourcefile)
        if debug == 1:
            logger.write("d", "Successfully written sourcefile to destinationfile!", lloc=lloc)
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


def loadbackup(sourcefile="backup_sys.xml", destinationfile="sys.xml", filepath="../settings/", debug=0):
    try:
        import os
        import logger
        lloc = "File: configparser.py | Function: loadbackup | Message: "
        logger.write("i", "Trying to load backup with arguments: sourcefile=["+str(sourcefile)+"], destinationfile=["+str(destinationfile)+"], filepath=["+str(filepath)+"], debug=["+str(debug)+"]!", lloc=lloc)
        tmp = sourcefile
        filename = filepath + tmp
        if debug == 1:
            logger.write("d", "filename was successfully merged! filename=["+str(filename)+"]", lloc=lloc)
        sourcefile = open(filename, "r").read()
        if debug == 1:
            logger.write("d", "Sourcefile was successfully opened and red!", lloc=lloc)
        destinationfile = open(filepath + destinationfile, "w")
        if debug == 1:
            logger.write("d", "Destinationfile was successfully opened!", lloc=lloc)
        destinationfile.write(sourcefile)
        if debug == 1:
            logger.write("d", "Successfully written sourcefile to destinationfile!", lloc=lloc)
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


def delelement(path, element, filename="sys.xml", filepath="../settings/", debug=0):
    try:
        import os
        import logger
        lloc = "File: configparser.py | Function: delelement | Message: "
        logger.write("i", "Trying to delete element in configfile with arguments: element_name=["+str(path)+"], filename=["+str(filename)+"], filepath=["+str(filepath)+"], debug=["+str(debug)+"]!", lloc=lloc)
        tmp = filename
        filename = filepath + tmp
        import xml.etree.ElementTree as ET
        tree = ET.parse(filename)
        if debug == 1:
            logger.write("d", "ElementTree parsed filename=["+str(filename)+"]!", lloc=lloc)
        root = tree.getroot()
        if debug == 1:
            logger.write("d", "ElementTree got tree-root!", lloc=lloc)
        parent = root.find(path)
        print parent
        parent.remove(element)

        tree.write(filename, encoding="UTF-8", xml_declaration=True)
        if debug == 1:
            logger.write("d", "Successfully written tree to file=["+str(filename)+"]!", lloc=lloc)
        return True
        #for elem in root.iterfind(path_before_element):
        #    print elem
        #    elem.remove(element_name)
        #    tree.write(filename, encoding="UTF-8", xml_declaration=True)
        #    if debug == 1:
        #        logger.write("d", "Successfully written tree to file=["+str(filename)+"]!", lloc=lloc)
        #    return True

            #if element.tag == element_name:
            #    if debug == 1:
            #        logger.write("d", "Found element=["+str(element_name)+"] in tree!", lloc=lloc)
            #
            #    tree.remove(element)
            #    if debug == 1:
            #        logger.write("d", "Successfully removed element=["+str(element_name)+"] from tree!", lloc=lloc)
            #    tree.write(filename, encoding="UTF-8", xml_declaration=True)
            #    if debug == 1:
            #        logger.write("d", "Successfully written tree to file=["+str(filename)+"]!", lloc=lloc)
            #    return True
        logger.write("e", "Could not remove element=["+str(element_name)+"] from file=["+str(filename)+"]!", lloc=lloc)
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


def delattrib(path, attrib_name, filename="sys.xml", filepath="../settings/", debug=0):
    try:
        import os
        import logger
        lloc = "File: configparser.py | Function: delattrib | Message: "
        logger.write("i", "Trying to delete attribute from configfile with arguments: path=["+str(path)+"], attrib_name=["+str(attrib_name)+"], filename=["+str(filename)+"], filepath=["+str(filepath)+"], debug=["+str(debug)+"]!", lloc=lloc)
        tmp = filename
        filename = filepath + tmp
        import xml.etree.ElementTree as ET
        tree = ET.parse(filename)
        if debug == 1:
            logger.write("d", "ElementTree parsed filename=["+str(filename)+"]!", lloc=lloc)
        root = tree.getroot()
        if debug == 1:
            logger.write("d", "ElementTree got tree-root!", lloc=lloc)
        for elem in root.iterfind(path):
            del elem.attrib[attrib_name]
            if debug == 1:
                logger.write("d", "Successfully removed attrib=["+str(attrib_name)+"]!", lloc=lloc)
            tree.write(filename, encoding="UTF-8", xml_declaration=True)
            if debug == 1:
                logger.write("d", "Successfully written tree to file=["+str(filename)+"]!", lloc=lloc)
            return True
        logger.write("e", "Could not remove attrib=["+str(attrib_name)+"] from file=["+str(filename)+"]!", lloc=lloc)
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


def addattrib(path, attrib_name, new_attrib_val="", filename="sys.xml", filepath="../settings/", debug=0):
    try:
        import os
        import logger
        lloc = "File: configparser.py | Function: addattrib | Message: "
        logger.write("i", "Trying to add attribute in configfile with arguments: path=["+str(path)+"], attrib_name=["+str(attrib_name)+"], new_attrib_val=["+str(new_attrib_val)+"], filename=["+str(filename)+"], filepath=["+str(filepath)+"], debug=["+str(debug)+"]!", lloc=lloc)
        tmp = filename
        filename = filepath + tmp
        import xml.etree.ElementTree as ET
        tree = ET.parse(filename)
        if debug == 1:
            logger.write("d", "ElementTree parsed filename=["+str(filename)+"]!", lloc=lloc)
        root = tree.getroot()
        if debug == 1:
            logger.write("d", "ElementTree got tree-root!", lloc=lloc)
        for elem in root.iterfind(path):
            elem.set(attrib_name, new_attrib_val)
            if debug == 1:
                logger.write("d", "Successfully added attrib=["+str(attrib_name)+"] with value=["+str(new_attrib_val)+"]!", lloc=lloc)
            tree.write(filename, encoding="UTF-8", xml_declaration=True)
            if debug == 1:
                logger.write("d", "Successfully written tree to file=["+str(filename)+"]!", lloc=lloc)
            return True
        logger.write("e", "Could not find element in path=["+str(path)+"]!")
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


def addelement():
    pass


def setattrib(path, attrib_name, new_attrib_val="", filename="sys.xml", filepath="../settings/", debug=0):
    try:
        import os
        import logger
        lloc = "File: configparser.py | Function: setattrib | Message: "
        logger.write("i", "Trying to set value of attribute in configfile with arguments: path=["+str(path)+"], attrib_name=["+str(attrib_name)+"], new_attrib_val=["+str(new_attrib_val)+"], filename=["+str(filename)+"], filepath=["+str(filepath)+"], debug=["+str(debug)+"]!", lloc=lloc)
        tmp = filename
        filename = filepath + tmp
        import xml.etree.ElementTree as ET
        tree = ET.parse(filename)
        if debug == 1:
            logger.write("d", "ElementTree parsed filename=["+str(filename)+"]!", lloc=lloc)
        root = tree.getroot()
        if debug == 1:
            logger.write("d", "ElementTree got tree-root!", lloc=lloc)
        for elem in root.iterfind(path):
            elem.set(attrib_name, new_attrib_val)
            if debug == 1:
                logger.write("d", "Successfully set value of attrib=["+str(attrib_name)+"] to value=["+str(new_attrib_val)+"]!", lloc=lloc)
            tree.write(filename, encoding="UTF-8", xml_declaration=True)
            if debug == 1:
                logger.write("d", "Successfully written tree to file=["+str(filename)+"]!", lloc=lloc)
            return True
        logger.write("e", "Could not find attrib in path=["+str(path)+"]!")
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


def getattrib(path, attrib_name, filename="sys.xml", filepath="../settings/", debug=0):
    try:
        import os
        import logger
        lloc = "File: configparser.py | Function: getattrib | Message: "
        logger.write("i", "Trying to get value of attribute from configfile with arguments: path=["+str(path)+"], attrib_name=["+str(attrib_name)+"], filename=["+str(filename)+"], filepath=["+str(filepath)+"], debug=["+str(debug)+"]!", lloc=lloc)
        tmp = filename
        filename = filepath + tmp
        import xml.etree.ElementTree as ET
        tree = ET.parse(filename)
        if debug == 1:
            logger.write("d", "ElementTree parsed filename=["+str(filename)+"]!", lloc=lloc)
        root = tree.getroot()
        if debug == 1:
            logger.write("d", "ElementTree got tree-root!", lloc=lloc)
        for elem in root.iterfind(path):
            if debug == 1:
                logger.write("d", "Found attrib=["+str(attrib_name)+"]! Returning value ["+str(elem.attrib[attrib_name])+"]!", lloc=lloc)
            return str(elem.attrib[attrib_name])
        logger.write("e", "Could not find attrib in path=["+str(path)+"]!")
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


def getelementlist(path="systemmodules/module", filename="sys.xml", filepath="../settings/", debug=0):
    try:
        import os
        import logger
        lloc = "File: configparser.py | Function: getelementlist | Message: "
        logger.write("i", "Trying to get list of elements from configfile with arguments: path=["+str(path)+"], filename=["+str(filename)+"], filepath=["+str(filepath)+"], debug=["+str(debug)+"]!", lloc=lloc)
        tmp = filename
        filename = filepath + tmp
        import xml.etree.ElementTree as ET
        tree = ET.parse(filename)
        if debug == 1:
            logger.write("d", "ElementTree parsed filename=["+str(filename)+"]!", lloc=lloc)
        root = tree.getroot()
        if debug == 1:
            logger.write("d", "ElementTree got tree-root!", lloc=lloc)
        elems = []
        for elem in root.iterfind(path):
            elems.append(elem.attrib)
        if debug == 1:
            logger.write("d", "Created elems list!", lloc=lloc)
        return elems
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