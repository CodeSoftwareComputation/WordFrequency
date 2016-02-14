import word_counter
import sys


def main(argv):
    file_name = "words.txt" if len (argv) == 1 else argv[1]
    with open(file_name, "rb") as fp:
        counted = word_counter.count_words(fp.read())
    word_counter.print_counted_words(counted)

if __name__ == "__main__":
    main(sys.argv)
