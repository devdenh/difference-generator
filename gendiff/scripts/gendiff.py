from gendiff.flat_diff import generate_diff_
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    path1 = args.first_file
    path2 = args.second_file
    generate_diff_(path1, path2)
    print(generate_diff_(path1, path2))


if __name__ == '__main__':
    main()
