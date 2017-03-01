import sys
import os.path
import subprocess
import time
import glob
from language.EN_US import *

ANDROID_STUDIO_PATH = 'C:/Program Files/Android/Android Studio/bin/studio64.exe'
INTELLIJ_PATH = 'C:/Program Files (x86)/JetBrains/IntelliJ IDEA Community Edition 2016.3.4/bin/idea64.exe'
PYCHARM_PATH = 'C:/Program Files (x86)/JetBrains/PyCharm Community Edition 2016.3.2/bin/pycharm64.exe'

_TIME_TO_SLEEP_SEC = 2.5


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
            raise Exception(MSG_INVALID_JETBRAINS_PROJECT)

        # Open the project.
        if ANDROID_STUDIO_PATH != '' and is_android_studio_project(project_path):
            time.sleep(_TIME_TO_SLEEP_SEC)
            ide_path = ANDROID_STUDIO_PATH
            project_type = 'Android Studio'

        elif INTELLIJ_PATH != '' and is_intellij_project(project_path):
            ide_path = INTELLIJ_PATH
            project_type = 'IntelliJ'

        elif PYCHARM_PATH != '' and is_pycharm_project(project_path):
            ide_path = PYCHARM_PATH
            project_type = 'Pycharm'

        else: raise Exception(MSG_UNKNOWN_JETBRAINS_PROJECT)

        print(MSG_OPENING_IDE.format(project_path, project_type))
        subprocess.call(ide_path + ' ' + project_path)

    except Exception as e:
        print(e)
        time.sleep(_TIME_TO_SLEEP_SEC)
