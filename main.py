from app import App
from questions import Questions

import time


def main():
    questions = Questions()
    start = time.time()
    App(questions)
    end = time.time()

    print('Gratulacje, uczyłeś się', round(end-start), 's.')


if __name__ == "__main__":
    main()
