import csv

# Specify the CSV file name
csv_file_name = '/home/q639524/gtsam-develop/build/examples/IMUKittiExampleGPSResults.csv'

# Specify the text file name
text_file_name = '/home/q639524/gtsam-develop/build/examples/output.txt'

# Open the CSV file and the text file
with open(csv_file_name, mode='r', newline='') as csv_file, open(text_file_name, mode='w', newline='') as text_file:
    # Create a CSV reader
    reader = csv.reader(csv_file)
    
    # Iterate over the rows in the CSV file
    for row in reader:
        # Write the row to the text file with a newline character
        text_file.write(' '.join(row) + '\n')
        

