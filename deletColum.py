import csv

def remove_column(input_file, output_file, column_name):
    with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
        reader = csv.DictReader(file_in)
        fieldnames = [field for field in reader.fieldnames if field != column_name]
        writer = csv.DictWriter(file_out, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            del row[column_name]
            writer.writerow(row)

    print(f"A coluna '{column_name}' foi removida com sucesso do arquivo {input_file}.")

input_file = 'D:/Escola/2022_23/AO/DataSet/vendasDataNoIDCopy.csv'
output_file = 'D:/Escola/2022_23/AO/DataSet/vendasDataNoID.csv'
column_name = 'feriado'

remove_column(input_file, output_file, column_name)
