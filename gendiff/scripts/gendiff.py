from gendiff import generate_diff
from gendiff.cli import args


def main():
    path1 = args.first_file
    path2 = args.second_file
    print(generate_diff(path1, path2))


if __name__ == '__main__':
    main()
