import word_counter
import sys


def main(argv):
    with open(argv[1], "rb") as fp:
        counted = word_counter.count_words(fp.read())
    word_counter.print_counted_words(counted)

if __name__ == "__main__":
    main(sys.argv)
