# All System Modules

Here you can see a short description of ALL system modules,

to know what the do.


## test.py


Theoretically we could skip this file, because essentially there is nothing special

in there. It's just used to test things.


## setup.py

### install()
    This function starts the installation-progress.
    It reads each tag from the setting/setup_sequence.xml and
    runs the corresponding action.


## logger.py

### write(level, message, lloc="", LogFile="")
    This function opens a logfile, if it is specified in * `LogFile=""` !