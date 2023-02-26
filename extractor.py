"""
Format data by extracting only relevant pieces.
"""
import pprint
import json
import re


def extract_data(unformatted_ex_states):
    """
    Extracts data.
    """
    print("EXTRACTING DATA...")
    data = {}
    for state in unformatted_ex_states:
        # Splitting state
        state_list = state.strip().split()
        final_array = []
        for i in range(len(state_list)):
            # Formatting - removing units, empty spaces, extra characters etc.
            substring = re.sub('[a-zA-Z, :=>-]', '', state_list[i]).strip()
            if is_not_empty(substring):
                if substring.find('*') == -1:
                    final_array.append(substring.strip())

        # Add single formatted state data to the output map in format (State number : Data)
        state_number = str(final_array[0])
        final_array.pop(0)
        data[state_number] = final_array

    # Print contents of data
    pprint.pprint(data, width=1000)
    print(json.dumps(data, indent=1))

    return data


def is_not_empty(s):
    """
    Check whether string is not empty
    """
    return bool(s and not s.isspace())


def format_data(data):
    """
    Formats data (removes units, empty spaces etc.)
    """
    energy = str(data[0]).lower()
    data[0] = re.sub('[a-z]', '', energy).strip()
    
    length = str(data[1]).lower()
    data[1] = re.sub('[a-z]', '', length).strip()
    
    f = str(data[2]).strip().lower()
    data[2] = f[2:]
    
    # major contributions
    for x in range(3, len(data)):
        transition = str(data[x]).strip().lower()
        data[x] = re.sub(' ', '', transition)

    return data
