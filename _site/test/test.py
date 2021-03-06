#to run test
#python3 test.py

import pytablereader as ptr
import pytablewriter as ptw

def modify(table_data):
    print('table data ->')
    print(table_data)
    return table_data

def io_test():
    # prepare data ---
    file_path = "sample_data.csv"
    csv_text = "\n".join([
        '"attr_a","attr_b","attr_c"',
        '1,4,"a"',
        '2,2.1,"bb"',
        '3,120.9,"ccc"',
    ])

    with open(file_path, "w") as f:
        f.write(csv_text)
        
    
        # load from a csv text ---
        
    loader = ptr.CsvTableTextLoader(csv_text)
    for table_data in loader.load():
        print("\n".join([
            "load from text",
        "==============",
            "{:s}".format(ptw.dumps_tabledata(table_data)),
        ]))

    
    # load from a csv file ---
    loader = ptr.CsvTableFileLoader(file_path)
    for table_data in loader.load():
        print("\n".join([
            "load from file",
            "==============",
            "{:s}".format(ptw.dumps_tabledata(modify(table_data))),
        ]))

def value_matrix_test():
    file_path = "sample_data.csv"
    writer=ptw.HtmlTableWriter()
    writer.from_csv(file_path)
    print(writer.value_matrix)
    for row in writer.value_matrix:
        row[2]="<a href=\""+row[2]+"\">link</a>"
    #writer.value_matrix[1][2]=    writer.value_matrix[1][2] +     writer.value_matrix[1][2]
    print(writer.value_matrix)

def main():
    value_matrix_test()
    
if __name__=="__main__":
    main()

