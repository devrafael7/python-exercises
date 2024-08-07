
#pdf merger (automation)

import PyPDF2 
import os

merger = PyPDF2.PdfMerger()

files_list = os.listdir("files")
files_list.sort()
print(files_list)

for file in files_list:
    if ".pdf" in file:
        merger.append(f"files/{file}")
        
merger.write("Final-PDF.pdf")