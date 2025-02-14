#!/usr/bin/env python3
# Author ID: 105830228

def read_file_string(file_name):
    f = open('data.txt', 'r')
    read_lines = f.read()
    f.close()
    return read_lines

def read_file_list(file_name):
    f = open(file_name, 'r')
    read_data = f.read().splitlines()
    return read_data

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))