import sys
import os.path
import subprocess
import time
import glob
import configparser
import importlib

# Read preferences.
config = configparser.ConfigParser()
config.read(os.path.dirname(__file__) + '/../prefs.ini')

LANGUAGE_NUM = config['Others']['LANGUAGE']
PYTHON_PATH = config['Path']['PYTHON']
INTELLIJ_PATH = config['Path']['INTELLIJ']
ANDROID_STUDIO_PATH = config['Path']['ANDROID_STUDIO']
PYCHARM_PATH = config['Path']['PYCHARM']

# Load language resources.
if LANGUAGE_NUM == '1042':
    # from language.KO import MSG
    # DEFAULT_LANG = __import__('language.KO')
    DEFAULT_LANG = importlib.import_module('language.KO')
    print('한국어')
elif LANGUAGE_NUM == '1033':
    # from language.EN_US import MSG
    # DEFAULT_LANG = __import__('language.EN_US')
    DEFAULT_LANG = importlib.import_module('language.EN_US')
    print('English')
else:
    # from language.root import MSG
    # DEFAULT_LANG = __import__('language.root')
    DEFAULT_LANG = importlib.import_module('language.root')
MSG = DEFAULT_LANG.MSG


def is_android_studio_project(path: str) -> bool:
    """
    Check if it's a Android Studio project.
    """
    if os.path.exists(path + '\\settings.gradle') and os.path.exists(path + '\\build.gradle'):
        return True
    else: return False


def is_intellij_project(path: str) -> bool:
    """
    Check if it's a IntelliJ project.
    """
    iml_files = glob.glob(path + '\\*.iml')
    print(iml_files)

    if len(iml_files) > 0:
        fp = open(iml_files[0], 'r')
        content = fp.read()
        fp.close()

        if content.find('JAVA_MODULE') != -1:
            return True
    return False


def is_pycharm_project(path: str) -> bool:
    """
    Check if it's a Pycharm project.
    """
    iml_files = glob.glob(path + '\\.idea\\*.iml')
    print(iml_files)
    if len(iml_files) != 0:
        return True
    else: return True


# Execute Android Studio
if len(sys.argv) == 2:

    try:
        # Check if it's a valid Jetbrains project.
        project_path = sys.argv[1]

        if not os.path.exists(project_path + '\\.idea'):
            raise Exception(MSG['INVALID_JETBRAINS_PROJECT'])

        # Open the project.
        if ANDROID_STUDIO_PATH != '' and is_android_studio_project(project_path):
            ide_path = ANDROID_STUDIO_PATH
            project_type = 'Android Studio'

        elif INTELLIJ_PATH != '' and is_intellij_project(project_path):
            ide_path = INTELLIJ_PATH
            project_type = 'IntelliJ'

        elif PYCHARM_PATH != '' and is_pycharm_project(project_path):
            ide_path = PYCHARM_PATH
            project_type = 'Pycharm'

        else: raise Exception(MSG['UNKNOWN_JETBRAINS_PROJECT'])

        print(MSG['OPENING_IDE'].format(project_path, project_type))
        subprocess.call(ide_path + ' ' + project_path)

    except Exception as e:
        print(e)
        time.sleep(2.5)
