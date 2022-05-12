from gendiff.description import generate_diff_
from gendiff.description import args
path1 = args.first_file
path2 = args.second_file


def main():
    generate_diff_(path1, path2)


if __name__ == '__main__':
    main()
