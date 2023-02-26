"""
This program converts scientific data from txt to specific format in CSV (Comma-separated values) file.
Data file must be located in the /Data folder in this project
The result file will be created in the /Data folder in this project
"""
import loader
import extractor
import processer
import writer

def main():
    """
    Main
    """
    states = loader.load_data("data")  # <--- data filename goes here
    data = extractor.extract_data(states)
    processed_data = processer.process_data(data)
    writer.write_data(processed_data, "output")  # <--- result filename goes here
    print("FINITO!")

if __name__ == "__main__":
    main()
