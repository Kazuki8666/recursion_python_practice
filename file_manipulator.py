import sys
import os

def validate_args(expected, actual):
    if len(sys.argv) != expected:
        print(f"Usage: python file_manipulator.py {actual}")
        sys.exit(1)

def reverse_file(input_path, output_path):
    if not os.path.isfile(input_path):
        print(f"Error: '{input_path}' does not exist.")
        return
    with open(input_path, 'r') as f:
        content = f.read()
    with open(output_path, 'w') as f:
        f.write(content[::-1])

def copy_file(input_path, output_path):
    if not os.path.isfile(input_path):
        print(f"Error: '{input_path}' does not exist.")
        return
    with open(input_path, 'r') as f_in, open(output_path, 'w') as f_out:
        f_out.write(f_in.read())

def duplicate_contents(input_path, n):
    if not os.path.isfile(input_path):
        print(f"Error: '{input_path}' does not exist.")
        return
    if not n.isdigit() or int(n) < 1:
        print("Error: n must be a positive integer.")
        return
    with open(input_path, 'r') as f:
        content = f.read()
    with open(input_path, 'w') as f:
        f.write(content * int(n))

def replace_string(input_path, needle, newstring):
    if not os.path.isfile(input_path):
        print(f"Error: '{input_path}' does not exist.")
        return
    with open(input_path, 'r') as f:
        content = f.read()
    with open(input_path, 'w') as f:
        f.write(content.replace(needle, newstring))

def main():
    if len(sys.argv) < 2:
        print("Usage: python file_manipulator.py [command] ...")
        sys.exit(1)

    command = sys.argv[1]

    if command == "reverse":
        validate_args(4, "reverse inputpath outputpath")
        reverse_file(sys.argv[2], sys.argv[3])
    elif command == "copy":
        validate_args(4, "copy inputpath outputpath")
        copy_file(sys.argv[2], sys.argv[3])
    elif command == "duplicate-contents":
        validate_args(4, "duplicate-contents inputpath n")
        duplicate_contents(sys.argv[2], sys.argv[3])
    elif command == "replace-string":
        validate_args(5, "replace-string inputpath needle newstring")
        replace_string(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
