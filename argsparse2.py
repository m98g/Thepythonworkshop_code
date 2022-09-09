import argparse

parser = argparse.ArgumentParser(description="Interpret postitional arguments")

parser.add_argument('source', action='store', help='The source of an opertaion.')
parser.add_argument('destination', action='store', help='The destination of the operation')

arguments = parser.parse_args()

print(f"Picasso will cycle from {arguments.source} to {arguments.destination}")