# Welcome to project Azurite

Here you can find information about the Azurite project!

Check out the GitHub repository [GitHub](https://github.com/Red-C0der/Azurite).

# What is Azurite?

Basically it it a personal assistant, which can help you perform different tasks and help you keep organized.

It can perform tasks like:

- Organize Contacts
- Browse the Web
- Manage your Calendar
- Check and sort your E-Mail
- Check Youtube Videos and get + organize your favorites in a playlist
- Manage your social media like Facebook, Twitter etc. (More information below.)
- Update GitHub repository's
- Intelligent Background Sentence Recognition - More Information below
- Get News
- Keep your computer secure
- Keep track of your activity
- Organize Files
- Organize Music

**And much more!**

Plus one of the biggest features: **Voice Recognition**

With the integrated voice recognition, Azurite can react and interpret your voice commands.

### Intelligent Background Sentence Recognition - IBSR
IBSR is a basic feature which allows Azurite to listen to speech in the background and intelligently recognize sentences like: 
> We will meet at 10 a.m. at the park

then Azurite will ask you if you want to create a reminder.

If you choose so, you can add something like the name of the person you'll meet.

After that, Azurite will automatically create a reminder at 10 a.m. to meet somebody

### Work in progress!

As you can see, all these beautiful features above wait to be implemented into Azurite.

If you want to you can contribute your idea or feature to the project and we'll implement it.

Request Feature / Contribute Idea - [Click HERE](https://github.com/Red-C0der/Project-Azurite/wiki/Request-Feature)

## Project layout:

    README.md                   # Readme file.
    LICENSE.txt                 # License File
    DOCS/                       # Just leave this as it is.
        ...
    dependencies/               # Some files etc. for setup.
        ...
    grammar/                    # Grammar data for the voice recognition.
        ...
    logs/                       # Obviously log-files get stored here.
        00-00-0000.log
    protocols/                  # Protocols get stored here.
        0000.py
    settings/
        backup_sys.xml          # First backup file for sys.xml.
        person_database.xml     # Person database (holds information about people).
        session_tmp.xml         # Get's used as Azurite runs.
        setup_sequence.xml      # Tells setup.py what to do while installing.
        sys.xml                 # Main configuration file.
    system/                     # Directory for all system files.
        ...
    tmp/                        # TMP data.
        ...
    voice/                      # Additional stuff for voice recognition.

