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

class Out:
    def prints(self, state, message):
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
            # 208 241
            from colored import fg, attr, style
            print("[" + fg(208) + attr("bold") + attr("blink") + "WARNING" + style.RESET + "] " + fg(208) + attr("bold") + message + style.RESET)
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

    def printc(self, text, fgc=500, bgc=500, attrc="", newline=True):
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