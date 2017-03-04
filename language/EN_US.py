# Edit this file to create English translations.
# This translations are only for v1.0.0-alpha.
from language.root import MSG

_LOCAL_MSG = {
    'OPENING_IDE': 'Opening {0!s} with {1!s}...', # {0!s} is path of project, and {1!s} is IDE name.
    'INVALID_JETBRAINS_PROJECT': "It's not a valid Jetbrains project.",
    'UNKNOWN_JETBRAINS_PROJECT': "It's an unknown Jetbrains project.",
    'MENU_TITLE': 'Open with Jetbrains IDE',

    # Installer messages
    'PAGE_PATH_INPUT_SUBTITLE': "Please input the following program's exe file.$\\n" # Use '$\\n' to put a newline.
                                "The Python Interpreter is essential, others are optional.",

    # Uninstaller messages
    'UNINST_DELETE_CONFIRM': 'Do you want to uninstall $(^Name)?',  # $(^Name) is program name.
    'UNINST_DELETED': '$(^Name) has been completely uninstalled.',  # $(^Name) is program name.
}

MSG.update(_LOCAL_MSG)
