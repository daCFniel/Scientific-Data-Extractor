"""
Load data from the data file.
"""


def load_data(filename):
    """
    Loads data from given file and return it.
    """
    with open('../Data/{}.txt'.format(filename)) as f:
        print("LOADING FILE...")
        loaded_file_array = f.readlines()

        return group_states(loaded_file_array)


def group_states(file):
    """
    Group excited states
    """
    print("GROUPING STATES...")
    grouped_excited_states = []
    n_of_lines = len(file)
    es = ""
    for i in range(n_of_lines):
        if file[i].startswith(" Excited"):
            grouped_excited_states.append(es)
            es = file[i]
        elif i == n_of_lines - 1:
            es += file[i]
            grouped_excited_states.append(es)
        else:
            es += file[i]
    # Remove empty element
    grouped_excited_states.pop(0)
    return grouped_excited_states
