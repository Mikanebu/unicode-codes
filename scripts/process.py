import requests
import csv

def read_remote_txt_and_save_as_csv(url, csv_filename):
    # Fetching the remote text file
    response = requests.get(url)
    # Checking if request was successful
    if response.status_code == 200:
        # Splitting text into lines
        lines = response.text.split('\n')
        # Removing any empty lines
        lines = [line.strip() for line in lines if line.strip()]
        # Saving the lines into a CSV file
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter =",")
            header = ['Unicode','Schematic Name','General_Category property value','','','CJK Radical','Code Point Sequence for USI','','','ast_Asian_Width property','The formal name aliases','','','mapping']
            writer.writerow(header)
            for line in lines:
                # Splitting each line by a space assuming it's a delimiter
                row = line.split(";")
                writer.writerow(row)
        print(f"CSV file '{csv_filename}' created successfully.")
    else:
        print(f"Failed to fetch the file. Status code: {response.status_code}")

url = "http://www.unicode.org/Public/UNIDATA/UnicodeData.txt"  # Replace this with your remote text file URL
csv_filename = "data/output.csv"  # Name of the CSV file to be created
read_remote_txt_and_save_as_csv(url, csv_filename)