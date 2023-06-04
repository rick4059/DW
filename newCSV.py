from ast import arg
import csv
import sys

# Open the input and output CSV files
with open('D:/Escola/2022_23/AO/DataSet/vendas.csv', 'r') as input_file, open('D:/Escola/2022_23/AO/DataSet/data.csv', 'w', newline='') as output_file:
    # Define the fields to be extracted from the input file
    input_fields = ['loja_id', 'departamento_id', 'data_id', 'Weekly_Sales', 'feriado']
    
    # Define the fields to be included in the output file
    output_fields = ['data_id', 'dia', 'mes', 'ano', 'feriado']

    # Create CSV reader and writer objects
    reader = csv.DictReader(input_file)
    writer = csv.DictWriter(output_file, fieldnames=output_fields)

    # Write the header row in the output file
    writer.writeheader()

    # Set to store the dates that have already been written to the output file
    dates_written = set()

    # Loop through each row of the input file and write the selected fields to the output file
    count = 1
    for row in reader:
        # Extract day, month, and year from data_id field
        print(row)
        day, month, year = row['data_id '].split('/')
        date_key = f"{year}-{month}-{day}"

        # Check if the date has already been written to the output file
        if date_key in dates_written:
            continue

        # Add the date to the set of dates that have been written to the output file
        dates_written.add(date_key)    

        if(row['feriado'] == 'FALSE'):
            row['feriado'] = 0
        else:
            row['feriado'] = 1
        # Create output row with selected fields
        output_row = {
            'data_id': count,
            'dia': day,
            'mes': month,
            'ano': year,
            'feriado': row['feriado']
        }
        count = count + 1
        # Write the output row to the output file
        writer.writerow(output_row)
        
        
