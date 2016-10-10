def read_csv():
    import csv
    with open('predict.csv', 'r') as f:
        reader = csv.reader(f)
        row = list(reader)

        for i in range(10):
            print(row[i])
def read_xls():
    import xlrd
    book = xlrd.open_workbook('grades.xls')
    first_sheet = book.sheet_by_index(0)
    for i in range(10):
        print (first_sheet.row_values(i))
def read_webpage():
    import urllib.request
    with urllib.request.urlopen('http://python.org/') as response:
        html = response.read()
    print(html)
