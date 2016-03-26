# ExportCallback

## ExportCallback Object

User-defined callback function used with[win32file::ReadEncryptedFileRaw](win32file.md#win32filereadencryptedfileraw)\.
Function is called with 3 parameters: \(Data, CallbackContext, Length\)
&nbsp&nbsp Data: Read-only buffer containing the raw data read from the file\.  Must not be referenced outside of the callback function\.
&nbsp&nbsp CallbackContext: Arbitrary object passed to ReadEncryptedFileRaw\.
&nbsp&nbsp Length: Number of bytes in the Data buffer\.
On success, function should return ERROR\_SUCCESS\.  Otherwise, it can return a win32 error code, or simply raise an exception\.