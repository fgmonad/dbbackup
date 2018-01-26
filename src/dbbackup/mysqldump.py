import sys
import subprocess


def dump(url):
    try:
        return subprocess.Popen([url], stdout=subprocess.PIPE)
    except OSError as err:
        print("Error: mysqldump not found")
        print(err)
        sys.exit(2)
