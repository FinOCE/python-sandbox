"""
This file was made because MySQL Workbench was crashing when trying to import CSV files. So to deal with it I created this script to use the specified constants to get different CSVs from a file and create SQL scripts to import them. A bit of a botched solution, but it got me through the practical!
"""

import os
import csv

DIR = 'data' # name of the directory the CSV files are in relative to this python code
FILES = ['author', 'book', 'checkout', 'patron', 'writes'] # names of the CSV files in the directory to create SQL for
DB_NAME = 'mydb' # name of the database

def main():
    script_dir = os.path.dirname(__file__)
    for file in FILES:
        with open(os.path.join(script_dir, f'./{DIR}/{file}.csv'), 'r') as data:
            csv_reader = csv.DictReader(data)
            rows = []
            for row in csv_reader:
                values = list(row.values())
                properties = ''
                for i, value in enumerate(values):
                    try:
                        float(value)
                        properties += value
                    except ValueError:
                        if value == 'NULL':
                            properties += value
                        else:
                            properties += f'"{value}"'
                    if i < len(values)-1:
                        properties += ', '
                rows.append(f'INSERT INTO `{DB_NAME}`.`{file}` VALUES ({properties});')
            with open(os.path.join(script_dir, f'./{DIR}/{file}.sql'), 'w+') as file:
                for row in rows:
                    file.write(f'{row}\n')

main()