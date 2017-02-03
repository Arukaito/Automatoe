# Requirements:
#  - Win7 or Win8.1 x64, 64-bit Python
#  - pywinauto 0.5.2+
#  - 7z920-x64.msi is in the same folder as the script
#  - UAC is fully disabled

from __future__ import print_function
import sys, os
os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

app = pywinauto.Application().Start(r'\\ramfile01\Apps\CompileNX\CompileNX.exe')
Compila = app['Compile NX electric test']

jobDir = r'C:\Users\LDELAROSA\Desktop\Jobs.txt'

jobFile= open(jobDir, 'r+')
#JobList= jobFile.readlines()
            
for index, line in enumerate(jobFile):
    job = line
    Compila.SetFocus()
    Compila.TGroupBox.TEdit.Click()
    Compila.TypeKeys(job)
    Compila.Load_Job.Click()
    Compila.Compile.Click()