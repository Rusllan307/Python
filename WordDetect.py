import logging
import os

def main():
    path = "/psMod"
    file_list = []
    root_list = []

    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(".txt"):
                root_list.append(root)
                file_list.append(filename)

    i = 0
    for file in file_list:
        os.chdir(root_list[i])
        fr = open(file, 'r')
        for line in fr:
            if line.startswith("password"):
                x = line
                print(x)
                if line == "password":
                    print(line)

        i += 1

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("Password module is listening...")
    main()


