# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file not exists just return 0

to_find = 'a'

def letter_a_frequency_in_file(filename):
    try:
        with open(filename, 'r') as file_to_check:
            file_content = file_to_check.read()
            amount = 0
            for letter in file_content:
                if letter == to_find:
                    amount += 1
            return amount
        file_to_check.close()
    except FileNotFoundError:
        return '0'
