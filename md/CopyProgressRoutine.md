# CopyProgressRoutine

## CopyProgressRoutine Object

Python function used as a callback for[win32file::CopyFileEx](win32file.md#win32filecopyfileex)and[win32file::MoveFileWithProgress](win32file.md#win32filemovefilewithprogress)
Function will receive 9 parameters:
(TotalFileSize, TotalBytesTransferred, StreamSize, StreamBytesTransferred, 

StreamNumber, CallbackReason, SourceFile, DestinationFile, Data)
SourceFile and DestinationFile are[PyHANDLE](#pyhandle)s. 

Data is the context object passed to the calling function. 

All others are longs.
CallbackReason will be one of CALLBACK_CHUNK_FINISHED or CALLBACK_STREAM_SWITCH
Your implementation of this function must return one of the PROGRESS_* constants.