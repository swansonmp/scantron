"""Script to help with quizzing"""

from colorama import Fore, Back, Style
import argparse

def get_color_from_score(score):
    if score < 0.6:
        return Fore.MAGENTA
    elif score < 0.7:
        return Fore.RED
    elif score < 0.8:
        return Fore.YELLOW
    elif score < 0.9:
        return Fore.GREEN
    elif score < 1:
        return Fore.CYAN
    else:
        return Fore.WHITE

def scantron(expected_file_name, actual_file_name):
    with open(expected_file_name, 'r') as expected_file:
        expected_list = [line.rstrip() for line in expected_file]
    with open(actual_file_name, 'r') as actual_file:
        actual_list = [line.rstrip() for line in actual_file]
    
    print(Style.BRIGHT + 'Q\tE\tA')
    print(Style.RESET_ALL + '-' * 24)
    zipped_list = zip(expected_list, actual_list)
    correct = 0
    total = 0
    for (expected, actual) in zipped_list:
        expected = expected.upper()
        actual = actual.upper()
        
        color = None
        total += 1
        if expected == actual:
            correct += 1
            color = Fore.GREEN
        else:
            # If multiple selection question
            if ',' in expected:
                expecteds = set(expected.split(','))
                actuals = set(actual.split(','))
                part_correct = 0
                any_part = False
                part_value = 1 / len(expecteds)
                for a in actuals:
                    if a in expecteds:
                        part_correct += part_value
                        any_part = True
                    else:
                        part_correct -= part_value
                
                # Only add partial credit if it's positive
                if part_correct > 0:
                    correct += part_correct
                    
                if any_part:
                    color = Fore.YELLOW
                else:
                    color = Fore.RED
            else:
                color = Fore.RED
        
        print(f'{color}{total}.\t{Fore.RESET}{expected}\t{color}{actual}')
    print(Fore.RESET + '-' * 24)
    score = correct / total
    print(f'{Style.BRIGHT}Results: {correct:.2g} of {total} ({get_color_from_score(score)}{score:.2f}{Fore.RESET}){Style.RESET_ALL}')

def main():
    parser = argparse.ArgumentParser(description='Tabulates results of tests')
    parser.add_argument('-e', '--expected', default='expected', help='Expected answers file name')
    parser.add_argument('-a', '--actual', default='actual', help='Actual answers file name')
    args = parser.parse_args()
    scantron(args.expected, args.actual)
    
if __name__ == '__main__':
    main()
