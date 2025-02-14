#!/usr/bin/env python3
# Author ID: 105830228

def read_file_string(file_name):
    f = open(file_name, 'r')
    read_data = f.read()
    return read_data

def read_file_list(file_name):
    f = open(file_name, 'r')
    read_data = f.read().splitlines()
    return read_data

def append_file_string(file_name, string_of_lines):
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()


def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w')
    for line in list_of_lines:
        line = line + "\n"
        f.write(line)
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    f1 = open(file_name_read, "r")
    f2 = open(file_name_write, "w")
    lines = f1.read().splitlines()
    for i in range(len(lines)):
        new_line = str(i+1) + ":" + lines[i] + "\n"
        f2.write(new_line)
    f1.close()
    f2.close()


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))