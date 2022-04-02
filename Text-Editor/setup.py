import cx_Freeze
from cx_Freeze import setup,Executable
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\python3.8\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\python3.8\tcl\tk8.6"

executables = [cx_Freeze.Executable("Mboard_texteditor.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "MBoard ",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll']}},
    version = "0.01",
    author="Bhaskar & Maahi",
    description = "Text Editor A text editor is a computer program that lets a user enter, change, store, and usually print text (characters and numbers, each encoded by the computer and its input and output devices, arranged to have meaning to users or to other programs",
    executables = [Executable("Mboard_texteditor.py",icon="icon.ico",shortcutName="Mboard")]
    )
