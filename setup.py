from cx_Freeze import setup, Executable

base = None

executables = [Executable("myfirstprog.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Dell",
    options = options,
    version = "1",
    description = 'description',
    executables = executables
)

import tabula
import tabulate
import pandas as pd
from tabula import read_pdf
from tabulate import tabulate

df = open(r'C:\Users\Dell\Desktop\Django project material\Food Calories List.pdf')
df = read_pdf
print(df)


df = pd.DataFrame({r'C:\Users\Dell\Desktop\Django project material\Food Calories List.pdf'})
df = df.dropna(axis='columns')
print(df)

df = open(r'C:\Users\Dell\Desktop\Django project material\Food Calories List.pdf')
#df = read_pdf(r'C:\Users\Dell\Desktop\Django project material\Food Calories List.pdf',pages=3)
#df = read_pdf(r'C:\Users\Dell\Desktop\Django project material\Food Calories List.pdf', pages=3, output_format="json")
#df = read_pdf(r'C:\Users\Dell\Desktop\Django project material\Food Calories List.pdf', pages='all', multiple_tables=True)
#print(tabulate(df))


#df = read_pdf("http://www.uncledavesenterprise.com/file/health/Food%20Calories%20List.pdf", pages=3)
#print(df)



#df = read_pdf(r'C:\Users\Dell\Desktop\Django project material\Food Calories List.pdf', encoding = 'ISO-8859-1',
                # stream=True, area = [269.875, 12.75, 790.5, 961], pages = 4, guess = False,  pandas_options={'header':None})
#print(df)



#df = open(r'C:\Users\Dell\Desktop\Django project material\Food Calories List.pdf')

#df = read_pdf(r'C:\Users\Dell\Desktop\Django project material\Food Calories List.pdf',
              #encoding='ISO-8859-1', stream=True, guess=False)
#print(tabulate(df))
#print()
#print()
#print(df)


df = read_pdf(r'C:\Users\Dell\Desktop\Django project material\Food Calories List.pdf',encoding = 'ISO-8859-1',
         stream=True, area=[269.875, 12.75, 790.5, 961], guess = False)
#print(df)

import PyPDF2
pdf_file = open(r'C:\Users\Dell\Desktop\Django project material\Food Calories List.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(r'C:\Users\Dell\Desktop\Django project material\Food Calories List.pdf')
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(2)
page_content = page.extractText()
print (page_content.encode('utf-8'))

import numpy
table_list = page_content.split('\n')
l = numpy.array_split(table_list, len(table_list)/4)
for i in range(0,5):
    print(l[i])

import xlsxwriter
def write_column(csvlist):
    workbook = xlsxwriter.Workbook(r"C:\Users\Dell\Desktop\Django project material\foodcalories.xlsx",{'strings_to_numbers': True})
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    for i in csvlist:
        worksheet.write(col,row, i)
        col += 1
    workbook.close()

# filepath = r"C:\Users\Dell\Desktop\Django project material\foodcalories.csv"
# fout = open(filepath, "w")

df.to_excel(r"C:\Users\Dell\Desktop\Django project material\foodcalories.xlsx")

print(df)