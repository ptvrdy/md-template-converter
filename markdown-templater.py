import codecs
import csv
import datetime
import sys

# This function converts the CSV file to a dictionary
def csv_to_dict(csv_reader):
    output = []
    header_row = True
    keys = {}

    for row in csv_reader:
        if header_row:
            print("=> Parsing CSV")
            row[0] = row[0].strip(codecs.BOM_UTF8.decode(sys.stdin.encoding))
            keys = {i: row[i].strip() for i in range(len(row)) if row[i] != ''}
            header_row = False
            continue

        output_obj = {}
        for i in range(len(keys)):
            key = keys[i]
            element = row[i]

            if element.strip() != '':
                output_obj[key] = element

        if output_obj != {}:
            output.append(output_obj)

    return output

# Converts dates from mm/dd/yyyy format to yyyy-mm-dd format. Ex: 7/20/2024 --> 2024-07-20
def convert_date_format(indate):
    input_date_time = "%m/%d/%Y"
    output_date_time = "%Y-%m-%d"
    final_date = datetime.datetime.strptime(indate, input_date_time).strftime(output_date_time)
    return final_date

def main():
    input_csv = input("Please name the CSV file you wish to use: ")
    input_template = input("Please name the Markdown template you wish to use: ")

    with open(input_template, 'r', encoding='utf-8') as file:
        template_content = file.read()

    with open(input_csv, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        output = csv_to_dict(reader)
        
        for i, row in enumerate(output):
            # This takes the title so that the README can be named after the Title of the item
            title = row.get("`Insert Title Here`", f"README_{i+1}")
            
            filled_content = template_content
            for key, value in row.items():
                if key == "`Insert Today's Date YYYY-MM-DD Here`":
                    value = convert_date_format(value)
                if key == "`Insert Date of Collection Here`":
                    value = convert_date_format(value)
                
                placeholder = key
                filled_content = filled_content.replace(placeholder, value)
            
            output_filename = f"readme_{title}.md"
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(filled_content)
                
            print(f"Generated {output_filename}")

if __name__ == '__main__':
    main()
