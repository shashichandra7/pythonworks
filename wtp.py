import sys
import os
import comtypes.client

wdFormatPDF = 17
#while compiling add your doc and pdf which you would expect 
in_file = os.path.abspath(sys.argv[1])
out_file = os.path.abspath(sys.argv[2])

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()
