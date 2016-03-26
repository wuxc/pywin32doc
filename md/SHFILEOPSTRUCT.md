# SHFILEOPSTRUCT


## SHFILEOPSTRUCT Object

A tuple representing a Win32 shell SHFILEOPSTRUCT structure, used with [shell::SHFileOperation](shell.md#shellshfileoperation)

#### Comments

From and To can contain multiple file names concatenated with a single null between them, eg 

"c:\\\\file1\.txt\\\\0c:\\\\file2\.txt"\.  A double null terminator will be appended automatically\. 

If To specifies multiple file names, flags must contain FOF\_MULTIDESTFILES

#### Items

  - \[0\] int : hwnd

    Handle of window in which to display status messages

  - \[1\] int : wFunc

    One of the shellcon\.FO\_\* values

  - \[2\] str/unicode : From

    String containing source file name\(s\) separated by nulls

  - \[3\] str/unicode : To

    String containing destination file name\(s\) separated by nulls, can be None

  - \[4\] int : flags

    Combination of shellcon\.FOF\_\* flags\. Default=0

  - \[5\] None : NameMappings

    Maps input file names to their new names\.  This is actually output, and must be None if passed as input\. Default=None

  - \[6\] string : ProgressTitle

    Title for progress dialog \(flags must contain FOF\_SIMPLEPROGRESS\)\. Default=None