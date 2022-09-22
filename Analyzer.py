import logging
import os

from collections import Counter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def main():
    counter = Counter()
    path = "/anMod"
    N_list = []
    ex_List = []
    view_list = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            before_ex, ext = os.path.splitext(filename)
            counter[ext] += 1
    size = 10
    for ext, counter in counter.items():
        if ext == "":
            ext = 'Dockerfile'
        print(f"{ext:8} {counter}")
        N_list.append(counter)
        ex_List.append(ext)
    for i in range(0, 10):
        y = max(N_list)
        for z in range(len(N_list)):
            if N_list[z] == y:
                view_list.append(ex_List[z])
                N_list.remove(y)
                ex_List.remove(ex_List[z])
                break
    print(view_list)


if __name__ == '__main__':
    logger.info("Analyze module is listening...")
    main()