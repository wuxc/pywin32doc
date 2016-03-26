# Source

## Source Safe Integration
Note you will need to restart Pythonwin for this option to take effect.
Before using the VSS integration, you must create a "mssccprj.scc" file 

in the directory, or a parent directory, of the files you wish to 

integrate. There are no limits on how many of these files exist. This is 

the same name and format as VB uses for VSS integration - a Windows INI 

file.
This file must have a section [Python] with entry "Project=ProjectName". 

The project name is the name of the VSS project used to check the out 

the file. If the .scc file is in a parent directory, the correct 

relative VSS path is built - so if your file system matches your VSS 

structure, you only need a single .scc file in the VSS "root" directory.

For example, assuming you have the file c:\\src\\mssccprj.scc with the contents:
[Python]
Project=OurProject
-eof-
The file c:\\src\\source1.py will be checked out from project OurProject, 

c:\\src\\sub\\source2.py will be checked out from project OurProject\\sub, 

etc.

## Source code folding in the editor
Thanks to Scintilla (http://www.scintilla.org), Pythonwin supports 

source code folding.  Folding is the ability to collapse sections of 

your source-code into a single line, making it easier to navigate 

around large files.  Any Python statement which introduces a new block 

can be folded either by clicking on the indicator in the folding 

margin (if enabled via the View-&gtOptions-&gtEditor dialog), by 

selecting one of the folding keystrokes (see[Keyboard Bindings](Keyboard.md#keyboardbindings), or 

by using View-&gtFolding menu.)

All find/replace or 'goto linenumber' functions work correctly when 

code is folded - the code is simply unfolded if necessary before the 

relevant operation.

You may configure Pythonwin so that all files have their top-levels 

folded when opened.  Only the first level folds are collapsed using 

this function, so expanding the top-level fold reveals the entire 

class/method that was folded.  Alternatively, you can use the 

Keypad-Multiply key to toggle the first level folds for the entire 

file at any time.
