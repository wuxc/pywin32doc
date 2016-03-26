# win32com.shell

## win32com\.shell and Windows Shell Links


Following is documentation for the PyIShellLink object\.

#### Example
To create a[PyIShellLink](#pyishelllink) object
from win32com\.shell import shell

import pythoncom

shortcut = pythoncom\.CoCreateInstance\(

&\#09shell\.CLSID\_ShellLink, None,

&\#09pythoncom\.CLSCTX\_INPROC\_SERVER, shell\.IID\_IShellLink

\)

To load information from existing shortcut file
shortcut\.QueryInterface\( pythoncom\.IID\_IPersistFile \)\.Load\( filename \)

To save information to a file
shortcut\.QueryInterface\( pythoncom\.IID\_IPersistFile \)\.Save\( filename, 0 \)

This documentation class is based on: 

http://msdn\.microsoft\.com/isapi/msdnlib\.idc?theURL=/library/sdkdoc/shellcc/shell/ifaces/ishelllink/ishelllink\.htm 

With only minor alterations and notations by Mike Fletcher\. 

Errors may be present, read at your own risk\. 

See also: 

http://msdn\.microsoft\.com/isapi/msdnlib\.idc?theURL=/library/books/win95ui/chpt09-01\.htm 

A tutorial-like introduction, includes brief discussion 

of non-file linking, and a fairly simple C sample application 

for file-based linking\.