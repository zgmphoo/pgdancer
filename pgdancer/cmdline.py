import sys
import os
from shutil import copyfile

def main():
    s1 = sys.argv[1]
    if s1 == "-h" or s1 == "--h" or "help" in s1:
        print("""
        -help : get help message;
        startproject dirname: create dirname project folder;
        """)
    elif s1 in "startproject":
        if len(sys.argv) >= 3:
            dirname = os.path.join(os.getcwd(), sys.argv[2])
            file = os.path.join(dirname, "settings.py")
            if os.path.exists(dirname):
                if os.path.exists(file):
                    pass
                else:
                    copyfile(os.path.join(os.path.dirname(__file__), "settings.py"), file)
            else:
                os.mkdir(dirname)
                copyfile(os.path.join(os.path.dirname(__file__), "settings.py"), file)

        else:
            raise Exception("please input dirname")
    else:
        raise Exception("you can input -help or startproject command")


if __name__ == '__main__':
    main()

