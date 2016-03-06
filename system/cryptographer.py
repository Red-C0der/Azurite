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


def newkey(debug=0):
    try:
        import os
        import logger
        lloc = "File: cryptographer.py | Function: newkey | Message: "
        logger.write("i", "Generating new Security Key with arguments: debug=["+str(debug)+"]!", lloc=lloc)
        BLOCK_SIZE = 32
        PADDING = '{'
        if debug == 1:
            logger.write("d", "BLOCK_SIZE = ["+str(BLOCK_SIZE)+"]", lloc=lloc)
            logger.write("d", "PADDING = ["+str(PADDING)+"]", lloc=lloc)
        pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
        if debug == 1:
            logger.write("d", "pad = ["+str(pad)+"]", lloc=lloc)
        secret = os.urandom(BLOCK_SIZE)
        if debug == 1:
            logger.write("d", "secret is hidden for security reasons!", lloc=lloc)
        logger.write("i", "Successfully generated new Security Key!", lloc=lloc)
        return secret
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


def encrypt(key, string, debug=0):
    try:
        import logger
        lloc = "File: cryptographer.py | Function: encrypt| Message: "
        logger.write("i", "Encrypting string with arguments: key=hidden, string=["+string+"], debug=["+str(debug)+"]!", lloc=lloc)
        from Crypto.Cipher import AES
        import base64
        BLOCK_SIZE = 32
        PADDING = '{'
        if debug is 1:
            logger.write("d", "BLOCK_SIZE = ["+str(BLOCK_SIZE)+"]", lloc=lloc)
            logger.write("d", "PADDING = ["+str(PADDING)+"]", lloc=lloc)
        pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
        if debug is 1:
            logger.write("d", "pad = ["+str(pad)+"]", lloc=lloc)
        EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
        if debug is 1:
            logger.write("d", "EncodeAES = ["+str(EncodeAES)+"]", lloc=lloc)
        cipher = AES.new(key)
        if debug is 1:
            logger.write("d", "cipher = ["+str(cipher)+"]", lloc=lloc)
        encoded = EncodeAES(cipher, string)
        if debug is 1:
            logger.write("d", "encoded = ["+str(encoded)+"]", lloc=lloc)
        logger.write("i", "Successfully encoded string!", lloc=lloc)
        return encoded
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


def decrypt(key, token, debug=0):
    try:
        import logger
        lloc = "File: cryptographer.py | Function: decrypt | Message: "
        logger.write("i", "Decrypting string with arguments: key=hidden, token=["+token+"], debug=["+str(debug)+"]!", lloc=lloc)
        from Crypto.Cipher import AES
        import base64
        BLOCK_SIZE = 32
        PADDING = '{'
        if debug is 1:
            logger.write("d", "BLOCK_SIZE = ["+str(BLOCK_SIZE)+"]", lloc=lloc)
            logger.write("d", "PADDING = ["+str(PADDING)+"]", lloc=lloc)
        pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
        if debug is 1:
            logger.write("d", "pas = ["+str(pad)+"]", lloc=lloc)
        DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
        if debug is 1:
            logger.write("d", "DecodeAES = ["+str(DecodeAES)+"]", lloc=lloc)
        cipher = AES.new(key)
        if debug is 1:
            logger.write("d", "cipher = ["+str(cipher)+"]", lloc=lloc)
        decoded = DecodeAES(cipher, token)
        if debug is 1:
            logger.write("d", "decoded = ["+str(decoded)+"]", lloc=lloc)
        logger.write("i", "Successfully decoded string!", lloc=lloc)
        return decoded
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

class SHA256:
    def hash_string(self, string, debug=0):
        try:
            import uuid
            import hashlib
            import logger
            lloc = "File: cryptographer.py | Class: SHA256 | Function: hash_string | Message: "
            logger.write("i", "Hashing string with arguments: string=["+str(string)+"], debug=["+str(debug)+"]!", lloc=lloc)
            salt = uuid.uuid4().hex
            if debug == 1:
                logger.write("d", "Generated salt! ["+str(salt)+"]", lloc=lloc)
            if debug == 1:
                logger.write("d", "Returning hashed String!", lloc=lloc)
            return hashlib.sha256(salt.encode() + string.encode()).hexdigest() + ':' + salt
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

    def check_string(self, hashed_string, inp_string, debug=0):
        try:
            import uuid
            import hashlib
            import logger
            lloc = "File: cryptographer.py | Class: SHA256 | Function: check_string | Message: "
            logger.write("i", "Hashing string with arguments: hashed_string=["+str(hashed_string)+"], inp_string=["+str(inp_string)+"], debug=["+str(debug)+"]!", lloc=lloc)
            if debug == 1:
                logger.write("d", "Splitting Salt from String", lloc=lloc)
            string, salt = hashed_string.split(':')
            if debug == 1:
                logger.write("d", "Returning check!", lloc=lloc)
            return string == hashlib.sha256(salt.encode() + inp_string.encode()).hexdigest()

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