from gendiff import generate_diff
from gendiff.cli import parse_args


def main():
    args = parse_args()
    path1 = args.first_file
    path2 = args.second_file
    format = args.format
    print(generate_diff(path1, path2, format))


if __name__ == '__main__':
    main()
