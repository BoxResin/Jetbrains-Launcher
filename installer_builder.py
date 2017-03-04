# Write release/lang.nsh file.
fp = open('release/lang.nsh', 'w')

fp.write('; Korean Support\n')
from language.KO import MSG
for key, value in MSG.items():
    print(key, value)
    fp.write('LangString %s ${LANG_KOREAN} "%s"\n' % (key, value))


fp.write('\n; English Support\n')
from language.EN_US import MSG
for key, value in MSG.items():
    print(key, value)
    fp.write('LangString %s ${LANG_ENGLISH} "%s"\n' % (key, value))

fp.close()


# Build a NSIS installer
import subprocess
subprocess.call('"C:/Program Files (x86)/NSIS/makensis.exe" release/installer_script.nsi')
#
