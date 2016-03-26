# ImportCallback


## ImportCallback Object

User-defined callback function used with [win32file::WriteEncryptedFileRaw](win32file.md#win32filewriteencryptedfileraw)
 

Function is called with 3 parameters: \(Data, CallbackContext, Length\)
 

&nbsp&nbsp Data: Writeable buffer to be filled with raw encrypted data\.  Buffer memory is only valid within the callback function\.
 

&nbsp&nbsp CallbackContext: The arbitrary object passed to WriteEncryptedFileRaw\.
 

&nbsp&nbsp Length: Size of the data buffer\.
 

Your implementation of this function should return a tuple of 2 ints containing 

an error code \(ERROR\_SUCCESS on success\), and the length of data written to the buffer\.
 

Function exits when 0 is returned for the data length\.