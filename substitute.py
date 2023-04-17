import json
import argparse
from typing import Dict


def substitute_dict(dictionary: Dict, depth: int = 0) -> Dict:
    """Performs a substitution on the input object, replacing all non-dictionary values with a dictionary
    containing the original value and its type. The substitution is performed recursively to a specified depth.

    Args:
        dictionary (dict): The input object to perform substitution on.
        depth (int): The maximum depth to perform substitution. If not specified, substitution is not performed
    Returns:
        dict: The substituted dictionary.
    """

    # if depth is reduced due to recursive call return the dictionary
    if depth is not None and depth <= 0:
        return dictionary

    new_dictionary = {}
    for key, value in dictionary.items():
        # check that if the value is dictionary than do the recursive call to reach the depth of dictionary
        if isinstance(value, dict):
            # recursive call to reach the depth of dictionary
            new_dictionary[key] = substitute_dict(value, depth=depth - 1)
        else:
            # perform substitution on non-dictionary value
            new_dictionary[key] = {'_content': value, '_type': str(type(value))}

    return new_dictionary


def substitute_file(input_file, depth, output_file):
    """Substitutes values in a JSON input file, writing the modified object to output file.

    Args:
        input_file (str): The path to the input file.
        depth (int): The maximum depth to perform substitution.
        output_file (str): The path to the output file.
    """
    # Load input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Perform substitution
    substitute_dictionary = substitute_dict(data, depth=depth)

    # Write output JSON file
    with open(output_file, 'w') as f:
        json.dump(substitute_dictionary, f)


def main():
    """Parses command-line arguments and performs substitution on the input file."""

    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Path to input JSON file')
    parser.add_argument('--depth', type=int, default=0, help='Maximum depth to perform substitution')
    parser.add_argument('output_file', help='Path to output JSON file')
    args = parser.parse_args()

    # Perform substitution
    substitute_file(args.input_file, args.depth, args.output_file)


if __name__ == '__main__':
    main()
