"""
script to sum line items from Chase bank statement
"""
import sys


def process_line(line):
    return line.strip().split(',')


def amount_from_line(line):
    """
    :returns: string `'Amount'` from header row or int amount from regular row
    """
    return line[-1]


def sum_chase_bank_statement(file_path):
    with open(file_path) as file_handle:
        header = file_handle.readline()
        if amount_from_line(process_line(header)) != 'Amount':
            raise ValueError('Amount column not in expected position')

        amounts = [
            float(amount_from_line(process_line(val))) for val
            in file_handle.readlines()
        ]
        return sum(amounts)


if __name__ == '__main__':
    print(sum_chase_bank_statement(sys.argv[1]))
