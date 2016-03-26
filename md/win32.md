# WIN32


## WIN32\_FIND\_DATA Object

A tuple representing a WIN32\_FIND\_DATA structure\.

#### Items

  - \[0\] int : attributes

    File Attributes\.  A combination of the win32com\.FILE\_ATTRIBUTE\_\* flags\.

  - \[1\] [PyTime](PyTime.md) : createTime

    File creation time\.

  - \[2\] [PyTime](PyTime.md) : accessTime

    File access time\.

  - \[3\] [PyTime](PyTime.md) : writeTime

    Time of last file write

  - \[4\] int : nFileSizeHigh

    high order DWORD of file size\.

  - \[5\] int : nFileSizeLow

    low order DWORD of file size\.

  - \[6\] int : reserved0

    Contains reparse tag if path is a reparse point

  - \[7\] int : reserved1

    Reserved\.

  - \[8\] str/unicode : fileName

    The name of the file\.

  - \[9\] str/unicode : alternateFilename

    Alternative name of the file, expressed in 8\.3 format\.