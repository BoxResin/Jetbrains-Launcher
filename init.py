# A script that is executed when the proejct is open with Jetbrains Launcher.
import subprocess
import webbrowser

# Open git bash.
subprocess.Popen('"C:/Program Files/Git/git-bash.exe" "--cd=."')

# Open GitHub pages.
webbrowser.open('https://github.com/BoxResin/Jetbrains-Launcher', new = True)
webbrowser.open('https://github.com/BoxResin/Jetbrains-Launcher/issues', new = True)
webbrowser.open('https://github.com/BoxResin/Jetbrains-Launcher/network', new = True)
