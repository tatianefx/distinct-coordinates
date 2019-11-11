#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "tatianefx"

import os

DIRECTORY_PATH = os.path.dirname(os.path.realpath('__file__'))
FILE_NAME = 'distinct-coordinates-'

file_name = input("Enter file name: ")
full_path = DIRECTORY_PATH + "/" + file_name

print(full_path)

try:
    # Read information
    with open(full_path) as f:
        final_file = []
        dictionary = {}

        for (i, line) in enumerate(f):
            array = line.split()

            # Number of columns where the coordinates are in the file
            if len(array) == 11:
                # x coordinate column
                x = array[5]
                # y coordinate column
                y = array[6]
                # z coordinate column
                z = array[7]

                key = x + y + z

                # Dictionary to save distinct values by coordinates
                dictionary[key] = line

            else:
                # Saves other information
                final_file.append(line)

    # Write information
    new_name = FILE_NAME + file_name
    with open(new_name, 'a') as out:
        for value in list(dictionary.values()):
            out.write(str(value))
        for value in final_file:
            out.write(str(value))

except FileNotFoundError:
    print("ERROR: File not found")
