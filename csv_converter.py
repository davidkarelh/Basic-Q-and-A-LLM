import csv
from dotenv import load_dotenv
import os

load_dotenv()

def convert_txt_to_csv(txt_file, csv_file, selected_columns):
    # with open(txt_file, 'r', encoding='utf-8') as infile, open(csv_file, 'w', newline='', encoding='utf-8') as outfile:
    with open(txt_file, 'r', encoding='cp1252') as infile, open(csv_file, 'w', newline='', encoding='cp1252') as outfile:
        # Create a CSV writer object with tab delimiter
        csv_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        header_row = True
        # Read the tab-delimited file and write to CSV
        for line in infile:
            # Split the line by tabs
            row = line.strip().split('\t')

            # Extract selected columns based on indices
            selected_data = [row[idx] for idx in selected_columns]
            if header_row:
                selected_data_formatted = [selected_data[1], selected_data[2]]
                header_row = False
            else:
                # selected_data_formatted = [f"({selected_data[0]}) {selected_data[1]}", selected_data[2]]
                selected_data_formatted = [f"({selected_data[0]}) {selected_data[1]}", f"{selected_data[2]} (related to: {selected_data[0]})"]
            
            # Write each row to the CSV file
            # csv_writer.writerow(row)
            # csv_writer.writerow(selected_data)
            csv_writer.writerow(selected_data_formatted)

if __name__  == "__main__":
    # Example usage:

    TXT_FILE_PATH=os.getenv("TXT_FILE_PATH")
    CSV_CONVERTED_FILE_PATH = os.getenv("CSV_CONVERTED_FILE_PATH")

    columns_to_select = [0, 1, 2]
    # txt_filename = 'input_data.txt'  # Replace with your tab-delimited file name
    # csv_filename = 'output_data.csv'  # Replace with the desired CSV file name

    convert_txt_to_csv(TXT_FILE_PATH, CSV_CONVERTED_FILE_PATH, columns_to_select)
