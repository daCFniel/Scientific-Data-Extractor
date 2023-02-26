"""
Write data to file in CSV format.
"""
import csv


def write_data(final_data, filename):
    """
    Writes data in CSV.
    """
    print("WRITING TO FILE...")
    header = ['Transition', 'E[eV]', 'λ[nm]', 'ƒ', 'Major contributions', 'Λ']

    with open('../Data/{}.csv'.format(filename), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        for state in final_data:
            writer.writerow(state)
