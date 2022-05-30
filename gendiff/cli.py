import argparse


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.',
    usage='[options] <filepath1> <filepath2>')
parser.add_argument('first_file', help=argparse.SUPPRESS)
parser.add_argument('second_file', help=argparse.SUPPRESS)
parser.add_argument('-V', '--version', help='output the version number', metavar="")
parser.add_argument('-f', '--format [type]', help='output format (default: "stylish")', metavar="")
args = parser.parse_args()
