# Requirements:
#  - Win7 or Win8.1 x64, 64-bit Python
#  - pywinauto 0.5.2+
#  - 7z920-x64.msi is in the same folder as the script
#  - UAC is fully disabled

#Importamos Librerias
from __future__ import print_function
import sys, os
os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

#Iniciamos la App de compilacion
app = pywinauto.Application().Start(r'\\ramfile01\Apps\CompileNX\CompileNX.exe')

#Hacemos Focus
Compila = app['Compile NX electric test']

#Declaramos el recurso donde nos indique que se compilara
jobDir = r'C:\Users\LDELAROSA\Desktop\Jobs.txt'

#Abrimos el archivo
jobFile= open(jobDir, 'r+')
#JobList= jobFile.readlines()
 
#Esperamos a que abra la ventana y que haga focus en el Edit3 que es el textbox
tfrmmaincompilenx = app.TfrmMainCompileNX
tfrmmaincompilenx.Wait('ready')
tedit = tfrmmaincompilenx.Edit3

#hacemos Loop por cada valor en la lista para que compile
for index, line in enumerate(jobFile):
    job = line
    Compila.SetFocus()
    tedit.DoubleClick()
    Compila.TypeKeys(job)
    #Compila.SendKeys('{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}')
    Compila.Load_Job.Click()
    Compila.Compile.Click()
   
#Matamos la aplicacion p
app.kill()