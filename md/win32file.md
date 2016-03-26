
## Module win32file

An interface to the win32 File API's
This module includes the tranactional NTFS operations introduced with 

Vista.  The transacted functions are not wrapped separately, but are invoked by 

passing a transaction handle to the corresponding Unicode API function. 

This makes it simple to convert a set of file operations into a transaction by 

simply adding Transaction=[PyHANDLE](README.md#PyHANDLE)to the passed arguments. 

If Transaction is None, 0, or not specified, the non-transacted API function will 

be called.
Functions combined in this manner:
CreateFile / CreateFileTransacted
DeleteFile / DeleteFileTransacted
CreateDirectoryEx / CreateDirectoryTransacted
MoveFileWithProgress / MoveFileTransacted
CopyFileEx / CopyFileTransacted
GetFileAttributes / GetFileAttributesTransacted
SetFileAttributes / SetFileAttributesTransacted
CreateHardLink / CreateHardLinkTransacted
CreateSymbolicLink / CreateSymbolicLinkTransacted
RemoveDirectory / RemoveDirectoryTransacted

#### Methods


  - [AreFileApisANSI](win32file.md#win32fileAreFileApisANSI)

    Determines whether a set of Win32 file functions is using the ANSI or OEM character set code page. This function is useful for 8-bit console input and output operations.&nbsp;

  - [CancelIo](win32file.md#win32fileCancelIo)

    Cancels pending IO requests for the object.&nbsp;

  - [CopyFile](win32file.md#win32fileCopyFile)

    Copies a file&nbsp;

  - [CopyFileW](win32file.md#win32fileCopyFileW)

    Copies a file (NT/2000 Unicode specific version)&nbsp;

  - [CreateDirectory](win32file.md#win32fileCreateDirectory)

    Creates a directory&nbsp;

  - [CreateDirectoryW](win32file.md#win32fileCreateDirectoryW)

    Creates a directory (NT/2000 Unicode specific version)&nbsp;

  - [CreateDirectoryEx](win32file.md#win32fileCreateDirectoryEx)

    Creates a directory&nbsp;

  - [CreateFile](win32file.md#win32fileCreateFile)

    Creates or opens the a file or other object and returns a handle that can be used to access the object.&nbsp;

  - [CreateIoCompletionPort](win32file.md#win32fileCreateIoCompletionPort)

    Can associate an instance of an opened file with a newly created or an existing input/output (I/O) completion port; or it can create an I/O completion port without associating it with a file.&nbsp;

  - [CreateMailslot](win32file.md#win32fileCreateMailslot)

    Creates a mailslot on the local machine&nbsp;

  - [GetMailslotInfo](win32file.md#win32fileGetMailslotInfo)

    Retrieves information about a mailslot&nbsp;

  - [SetMailslotInfo](win32file.md#win32fileSetMailslotInfo)

    Sets a mailslot's timeout&nbsp;

  - [DefineDosDevice](win32file.md#win32fileDefineDosDevice)

    Lets an application define, redefine, or delete MS-DOS device names.&nbsp;

  - [DefineDosDeviceW](win32file.md#win32fileDefineDosDeviceW)

    Lets an application define, redefine, or delete MS-DOS device names. (NT/2000 Unicode specific version)&nbsp;

  - [DeleteFile](win32file.md#win32fileDeleteFile)

    Deletes a file.&nbsp;

  - [DeviceIoControl](win32file.md#win32fileDeviceIoControl)

    Sends a control code to a device or file system driver&nbsp;

  - [FindClose](win32file.md#win32fileFindClose)

    Closes a find handle.&nbsp;

  - [FindCloseChangeNotification](win32file.md#win32fileFindCloseChangeNotification)

    Closes a handle.&nbsp;

  - [FindFirstChangeNotification](win32file.md#win32fileFindFirstChangeNotification)

    Creates a change notification handle and sets up initial change notification filter conditions. A wait on a notification handle succeeds when a change matching the filter conditions occurs in the specified directory or subtree.&nbsp;

  - [FindNextChangeNotification](win32file.md#win32fileFindNextChangeNotification)

    Requests that the operating system signal a change notification handle the next time it detects an appropriate change,&nbsp;

  - [FlushFileBuffers](win32file.md#win32fileFlushFileBuffers)

    Clears the buffers for the specified file and causes all buffered data to be written to the file.&nbsp;

  - [GetBinaryType](win32file.md#win32fileGetBinaryType)

    Determines whether a file is executable, and if so, what type of executable file it is. That last property determines which subsystem an executable file runs under.&nbsp;

  - [GetDiskFreeSpace](win32file.md#win32fileGetDiskFreeSpace)

    Determines the free space on a device.&nbsp;

  - [GetDiskFreeSpaceEx](win32file.md#win32fileGetDiskFreeSpaceEx)

    Determines the free space on a device.&nbsp;

  - [GetDriveType](win32file.md#win32fileGetDriveType)

    Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive.&nbsp;

  - [GetDriveTypeW](win32file.md#win32fileGetDriveTypeW)

    Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive. (NT/2000 Unicode specific version).&nbsp;

  - [GetFileAttributes](win32file.md#win32fileGetFileAttributes)

    Determines a files attributes.&nbsp;

  - [GetFileAttributesW](win32file.md#win32fileGetFileAttributesW)

    Determines a files attributes (NT/2000 Unicode specific version).&nbsp;

  - [GetFileTime](win32file.md#win32fileGetFileTime)

    Returns a file's creation, last access, and modification times.&nbsp;

  - [SetFileTime](win32file.md#win32fileSetFileTime)

    Sets the date and time that a file was created, last accessed, or last modified.&nbsp;

  - [GetFileInformationByHandle](win32file.md#win32fileGetFileInformationByHandle)

    Retrieves file information for a specified file.&nbsp;

  - [GetCompressedFileSize](win32file.md#win32fileGetCompressedFileSize)

    Determines the compressed size of a file.&nbsp;

  - [GetFileSize](win32file.md#win32fileGetFileSize)

    Determines the size of a file.&nbsp;

  - [AllocateReadBuffer](win32file.md#win32fileAllocateReadBuffer)

    Allocates a buffer which can be used with an overlapped Read operation using[win32file::ReadFile](win32file.md#win32fileReadFile)&nbsp;

  - [ReadFile](win32file.md#win32fileReadFile)

    Reads a string from a file&nbsp;

  - [WriteFile](win32file.md#win32fileWriteFile)

    Writes a string to a file&nbsp;

  - [CloseHandle](win32file.md#win32fileCloseHandle)

    Closes an open handle.&nbsp;

  - [LockFileEx](win32file.md#win32fileLockFileEx)

    Locks a file. Wrapper for LockFileEx win32 API.&nbsp;

  - [UnlockFileEx](win32file.md#win32fileUnlockFileEx)

    Unlocks a file. Wrapper for UnlockFileEx win32 API.&nbsp;

  - [GetQueuedCompletionStatus](win32file.md#win32fileGetQueuedCompletionStatus)

    Attempts to dequeue an I/O completion packet from a specified input/output completion port.&nbsp;

  - [PostQueuedCompletionStatus](win32file.md#win32filePostQueuedCompletionStatus)

    lets you post an I/O completion packet to an I/O completion port. The I/O completion packet will satisfy an outstanding call to the GetQueuedCompletionStatus function.&nbsp;

  - [GetFileType](win32file.md#win32fileGetFileType)

    Determines the type of a file.&nbsp;

  - [GetLogicalDrives](win32file.md#win32fileGetLogicalDrives)

    Returns a bitmaks of the logical drives installed.&nbsp;

  - [GetOverlappedResult](win32file.md#win32fileGetOverlappedResult)

    Determines the result of the most recent call with an OVERLAPPED object.&nbsp;

  - [LockFile](win32file.md#win32fileLockFile)

    Locks a specified file for exclusive access by the calling process.&nbsp;

  - [MoveFile](win32file.md#win32fileMoveFile)

    Renames an existing file or a directory (including all its children).&nbsp;

  - [MoveFileW](win32file.md#win32fileMoveFileW)

    Renames an existing file or a directory (including all its children). (NT/2000 Unicode specific version).&nbsp;

  - [MoveFileEx](win32file.md#win32fileMoveFileEx)

    Renames an existing file or a directory (including all its children).&nbsp;

  - [MoveFileExW](win32file.md#win32fileMoveFileExW)

    Renames an existing file or a directory (including all its children). (NT/2000 Unicode specific version).&nbsp;

  - [QueryDosDevice](win32file.md#win32fileQueryDosDevice)

    Returns the mapping for a device name, or all device names&nbsp;

  - [ReadDirectoryChangesW](win32file.md#win32fileReadDirectoryChangesW)

    retrieves information describing the changes occurring within a directory.&nbsp;

  - [FILE_NOTIFY_INFORMATION](win32file.md#win32fileFILE_NOTIFY_INFORMATION)

    Decodes a PyFILE_NOTIFY_INFORMATION buffer.&nbsp;

  - [SetCurrentDirectory](win32file.md#win32fileSetCurrentDirectory)

    Sets the current directory.&nbsp;

  - [SetEndOfFile](win32file.md#win32fileSetEndOfFile)

    Moves the end-of-file (EOF) position for the specified file to the current position of the file pointer.&nbsp;

  - [SetFileApisToANSI](win32file.md#win32fileSetFileApisToANSI)

    Causes a set of Win32 file functions to use the ANSI character set code page. This function is useful for 8-bit console input and output operations.&nbsp;

  - [SetFileApisToOEM](win32file.md#win32fileSetFileApisToOEM)

    Causes a set of Win32 file functions to use the OEM character set code page. This function is useful for 8-bit console input and output operations.&nbsp;

  - [SetFileAttributes](win32file.md#win32fileSetFileAttributes)

    Changes a file's attributes.&nbsp;

  - [SetFilePointer](win32file.md#win32fileSetFilePointer)

    Moves the file pointer of an open file.&nbsp;

  - [SetVolumeLabel](win32file.md#win32fileSetVolumeLabel)

    Sets a volume label for a disk drive.&nbsp;

  - [UnlockFile](win32file.md#win32fileUnlockFile)

    Unlocks a region of a file locked by[win32file::LockFile](win32file.md#win32fileLockFile)or[win32file::LockFileEx](win32file.md#win32fileLockFileEx)&nbsp;

  - [_get_osfhandle](win32file.md#win32file_get_osfhandle)

    Gets operating-system file handle associated with existing stream&nbsp;

  - [_open_osfhandle](win32file.md#win32file_open_osfhandle)

    Associates a C run-time file handle with a existing operating-system file handle.&nbsp;

  - [_setmaxstdio](win32file.md#win32file_setmaxstdio)

    Set the maximum allowed number of open stdio handles&nbsp;

  - [_getmaxstdio](win32file.md#win32file_getmaxstdio)

    Returns the maximum number of CRT io streams.&nbsp;

  - [TransmitFile](win32file.md#win32fileTransmitFile)

    Transmits a file over a socket 

TransmitFile(sock, filehandle, bytes_to_write, bytes_per_send, overlap, flags [, (prepend_buf, postpend_buf)])&nbsp;

  - [ConnectEx](win32file.md#win32fileConnectEx)

    Version of connect that uses Overlapped I/O 

ConnectEx(sock, (addr, port), buf, overlap)&nbsp;

  - [AcceptEx](win32file.md#win32fileAcceptEx)

    Version of accept that uses Overlapped I/O&nbsp;

  - [CalculateSocketEndPointSize](win32file.md#win32fileCalculateSocketEndPointSize)

    Calculate how many bytes are needed for the connection endpoints data for a socket.&nbsp;

  - [GetAcceptExSockaddrs](win32file.md#win32fileGetAcceptExSockaddrs)

    Parses the connection endpoints from the buffer passed into AcceptEx&nbsp;

  - [WSAEventSelect](win32file.md#win32fileWSAEventSelect)

    Specifies an event object to be associated with the supplied set of FD_XXXX network events.&nbsp;

  - [WSAEnumNetworkEvents](win32file.md#win32fileWSAEnumNetworkEvents)

    Return network events that caused the event associated with the socket to be signaled.&nbsp;

  - [WSAAsyncSelect](win32file.md#win32fileWSAAsyncSelect)

    Request windows message notification for the supplied set of FD_XXXX network events.&nbsp;

  - [WSASend](win32file.md#win32fileWSASend)

    Winsock send() equivalent function for Overlapped I/O.&nbsp;

  - [WSARecv](win32file.md#win32fileWSARecv)

    Winsock recv() equivalent function for Overlapped I/O.&nbsp;

  - [BuildCommDCB](win32file.md#win32fileBuildCommDCB)

    Fills the specified DCB structure with values specified in a device-control string. The device-control string uses the syntax of the mode command&nbsp;

  - [ClearCommError](win32file.md#win32fileClearCommError)

    retrieves information about a communications error and reports the current status of a communications device.&nbsp;

  - [EscapeCommFunction](win32file.md#win32fileEscapeCommFunction)

    directs a specified communications device to perform an extended function.&nbsp;

  - [GetCommState](win32file.md#win32fileGetCommState)

    Returns a device-control block (a DCB structure) with the current control settings for a specified communications device.&nbsp;

  - [SetCommState](win32file.md#win32fileSetCommState)

    Configures a communications device according to the specifications in a device-control block. 

The function reinitializes all hardware and control settings, but it does not empty output or input queues.&nbsp;

  - [ClearCommBreak](win32file.md#win32fileClearCommBreak)

    Restores character transmission for a specified communications device and places the transmission line in a nonbreak state&nbsp;

  - [GetCommMask](win32file.md#win32fileGetCommMask)

    Retrieves the value of the event mask for a specified communications device.&nbsp;

  - [SetCommMask](win32file.md#win32fileSetCommMask)

    Sets the value of the event mask for a specified communications device.&nbsp;

  - [GetCommModemStatus](win32file.md#win32fileGetCommModemStatus)

    Retrieves modem control-register values.&nbsp;

  - [GetCommTimeouts](win32file.md#win32fileGetCommTimeouts)

    Retrieves the time-out parameters for all read and write operations on a specified communications device.&nbsp;

  - [SetCommTimeouts](win32file.md#win32fileSetCommTimeouts)

    Sets the time-out parameters for all read and write operations on a specified communications device.&nbsp;

  - [PurgeComm](win32file.md#win32filePurgeComm)

    Discards all characters from the output or input buffer of a specified communications resource. It can also terminate pending read or write operations on the resource.&nbsp;

  - [SetCommBreak](win32file.md#win32fileSetCommBreak)

    Suspends character transmission for a specified communications device and places the transmission line in a break state until the[win32file::ClearCommBreak](win32file.md#win32fileClearCommBreak)function is called.&nbsp;

  - [SetupComm](win32file.md#win32fileSetupComm)

    Initializes the communications parameters for a specified communications device.&nbsp;

  - [TransmitCommChar](win32file.md#win32fileTransmitCommChar)

    Transmits a specified character ahead of any pending data in the output buffer of the specified communications device.&nbsp;

  - [WaitCommEvent](win32file.md#win32fileWaitCommEvent)

    Waits for an event to occur for a specified communications device. The set of events that are monitored by this function is contained in the event mask associated with the device handle.&nbsp;

  - [SetVolumeMountPoint](win32file.md#win32fileSetVolumeMountPoint)

    Mounts the specified volume at the specified volume mount point.&nbsp;

  - [DeleteVolumeMountPoint](win32file.md#win32fileDeleteVolumeMountPoint)

    Unmounts the volume from the specified volume mount point.&nbsp;

  - [GetVolumeNameForVolumeMountPoint](win32file.md#win32fileGetVolumeNameForVolumeMountPoint)

    Returns unique volume name.&nbsp;

  - [GetVolumePathName](win32file.md#win32fileGetVolumePathName)

    Returns volume mount point for a path&nbsp;

  - [GetVolumePathNamesForVolumeName](win32file.md#win32fileGetVolumePathNamesForVolumeName)

    Returns mounted paths for a volume&nbsp;

  - [CreateHardLink](win32file.md#win32fileCreateHardLink)

    Establishes an NTFS hard link between an existing file and a new file.&nbsp;

  - [CreateSymbolicLink](win32file.md#win32fileCreateSymbolicLink)

    Creates a symbolic link (reparse point)&nbsp;

  - [EncryptFile](win32file.md#win32fileEncryptFile)

    Encrypts specified file (requires Win2k or higher and NTFS)&nbsp;

  - [DecryptFile](win32file.md#win32fileDecryptFile)

    Decrypts specified file (requires Win2k or higher and NTFS)&nbsp;

  - [EncryptionDisable](win32file.md#win32fileEncryptionDisable)

    Enables/disables encryption for a directory (requires Win2k or higher and NTFS)&nbsp;

  - [FileEncryptionStatus](win32file.md#win32fileFileEncryptionStatus)

    retrieves the encryption status of the specified file.&nbsp;

  - [QueryUsersOnEncryptedFile](win32file.md#win32fileQueryUsersOnEncryptedFile)

    Returns list of users for an encrypted file as tuples of (SID, certificate hash blob, display info)&nbsp;

  - [QueryRecoveryAgentsOnEncryptedFile](win32file.md#win32fileQueryRecoveryAgentsOnEncryptedFile)

    Lists recovery agents for file as a tuple of tuples.&nbsp;

  - [RemoveUsersFromEncryptedFile](win32file.md#win32fileRemoveUsersFromEncryptedFile)

    Removes specified certificates from file - if certificate is not found, it is ignored&nbsp;

  - [AddUsersToEncryptedFile](win32file.md#win32fileAddUsersToEncryptedFile)

    Allows user identified by SID and EFS certificate access to decrypt specified file&nbsp;

  - [DuplicateEncryptionInfoFile](win32file.md#win32fileDuplicateEncryptionInfoFile)

    Duplicates EFS encryption from one file to another&nbsp;

  - [BackupRead](win32file.md#win32fileBackupRead)

    Reads streams of data from a file&nbsp;

  - [BackupSeek](win32file.md#win32fileBackupSeek)

    Seeks forward in a file stream&nbsp;

  - [BackupWrite](win32file.md#win32fileBackupWrite)

    Restores file data&nbsp;

  - [SetFileShortName](win32file.md#win32fileSetFileShortName)

    Set the 8.3 name of a file&nbsp;

  - [CopyFileEx](win32file.md#win32fileCopyFileEx)

    Restartable file copy with optional progress routine&nbsp;

  - [MoveFileWithProgress](win32file.md#win32fileMoveFileWithProgress)

    Moves a file, and reports progress to a callback function&nbsp;

  - [ReplaceFile](win32file.md#win32fileReplaceFile)

    Replaces one file with another&nbsp;

  - [OpenEncryptedFileRaw](win32file.md#win32fileOpenEncryptedFileRaw)

    Initiates a backup or restore operation on an encrypted file&nbsp;

  - [ReadEncryptedFileRaw](win32file.md#win32fileReadEncryptedFileRaw)

    Reads the encrypted bytes of a file for backup and restore purposes&nbsp;

  - [WriteEncryptedFileRaw](win32file.md#win32fileWriteEncryptedFileRaw)

    Writes raw bytes to an encrypted file&nbsp;

  - [CloseEncryptedFileRaw](win32file.md#win32fileCloseEncryptedFileRaw)

    Frees a context created by[win32file::OpenEncryptedFileRaw](win32file.md#win32fileOpenEncryptedFileRaw)&nbsp;

  - [CreateFileW](win32file.md#win32fileCreateFileW)

    Unicode version of CreateFile - see[win32file::CreateFile](win32file.md#win32fileCreateFile)for more information.&nbsp;

  - [DeleteFileW](win32file.md#win32fileDeleteFileW)

    Deletes a file (Unicode version)&nbsp;

  - [GetFileAttributesEx](win32file.md#win32fileGetFileAttributesEx)

    Retrieves attributes for a specified file or directory.&nbsp;

  - [SetFileAttributesW](win32file.md#win32fileSetFileAttributesW)

    Sets a file's attributes&nbsp;

  - [CreateDirectoryExW](win32file.md#win32fileCreateDirectoryExW)

    Creates a directory (Unicode version)&nbsp;

  - [RemoveDirectory](win32file.md#win32fileRemoveDirectory)

    Removes an existing directory&nbsp;

  - [FindFilesW](win32file.md#win32fileFindFilesW)

    Retrieves a list of matching filenames, using the Windows Unicode API.  An interface to the API FindFirstFileW/FindNextFileW/Find close functions.&nbsp;

  - [FindFilesIterator](win32file.md#win32fileFindFilesIterator)

    Returns an interator based on 

FindFirstFile/FindNextFile. Similar to **win32file::FindFiles** , but 

avoids the creation of the list for huge directories.&nbsp;

  - [FindStreams](win32file.md#win32fileFindStreams)

    List the data streams for a file&nbsp;

  - [FindFileNames](win32file.md#win32fileFindFileNames)

    Enumerates hard links that point to specified file&nbsp;

  - [GetFinalPathNameByHandle](win32file.md#win32fileGetFinalPathNameByHandle)

    Returns the file name for an open file handle&nbsp;

  - [SfcGetNextProtectedFile](win32file.md#win32fileSfcGetNextProtectedFile)

    Returns list of protected operating system files&nbsp;

  - [SfcIsFileProtected](win32file.md#win32fileSfcIsFileProtected)

    Checks if a file is protected&nbsp;

  - [GetLongPathName](win32file.md#win32fileGetLongPathName)

    Retrieves the long path for a short path (8.3 filename)&nbsp;

  - [GetFullPathName](win32file.md#win32fileGetFullPathName)

    Returns full path for path passed in&nbsp;

  - [Wow64DisableWow64FsRedirection](win32file.md#win32fileWow64DisableWow64FsRedirection)

    Disables file system redirection for 32-bit processes running on a 64-bit system&nbsp;

  - [Wow64RevertWow64FsRedirection](win32file.md#win32fileWow64RevertWow64FsRedirection)

    Reenables file system redirection for 32-bit processes running on a 64-bit system&nbsp;

  - [GetFileInformationByHandleEx](win32file.md#win32fileGetFileInformationByHandleEx)

    Retrieves extended file information for an open file handle.&nbsp;

  - [SetFileInformationByHandle](win32file.md#win32fileSetFileInformationByHandle)

    Changes file characteristics by file handle&nbsp;

  - [ReOpenFile](win32file.md#win32fileReOpenFile)

    Creates a new handle to an open file&nbsp;

  - [OpenFileById](win32file.md#win32fileOpenFileById)

    Opens a file by File Id or Object Id&nbsp;

## [win32file](README.md#win32file).AcceptEx

 **AcceptEx( *sListening*  *, sAccepting*  *, buffer*  *, ol* ** )
Version of accept that uses Overlapped I/O

#### Parameters


  -  *sListening* : **PySocket** /int

    Socket that had listen() called on.

  -  *sAccepting* : **PySocket** /int

    Socket that will be used as the incoming connection.

  -  *buffer* : **buffer** 

    Buffer to read incoming data and connection point information into. This buffer MUST be big enough to recieve your connection endpoints... AF_INET sockets need to be at least 64 bytes. The correct minimum of the buffer is determined by the protocol family that the listening socket is using.

  -  *ol* :[PyOVERLAPPED](README.md#PyOVERLAPPED)

    An overlapped structure

#### Comments
In order to make sure the connection has been accepted, either use the hEvent in PyOVERLAPPED, GetOverlappedResult, or GetQueuedCompletionStatus.
To use this with I/O completion ports, don't forget to attach sAccepting to your completion port.
Pass a buffer of exactly the size returned by[win32file::CalculateSocketEndPointSize](win32file.md#win32fileCalculateSocketEndPointSize)to have AcceptEx return without reading any bytes from the remote connection.

#### Example
To have sAccepting inherit the properties of sListening, you need to do the following after a connection is successfully accepted
import struct

sAccepting.setsockopt(socket.SOL_SOCKET, win32file.SO_UPDATE_ACCEPT_CONTEXT, struct.pack("I", sListening.fileno()))
#### Return Value
The result is 0 or ERROR_IO_PENDING.  All other values will raise 

win32file.error.  Specifically: if the win32 function returns FALSE, 

WSAGetLastError() is checked for ERROR_IO_PENDING.

## [win32file](README.md#win32file).AddUsersToEncryptedFile

 **AddUsersToEncryptedFile( *FileName*  *, pUsers* ** )
Allows user identified by SID and EFS certificate access to decrypt specified file

#### Parameters


  -  *FileName* : string/unicode

    File that additional users will be allowed to decrypt

  -  *pUsers* : (([PySID](README.md#PySID),string,int),...)

    Sequence representing 

ENCRYPTION_CERTIFICATE_LIST - elements are sequences consisting of 

users' Sid, encoded EFS certficate (user must export a .cer to obtain 

this data), and encoding type (usually 1 for X509_ASN_ENCODING)

## [win32file](README.md#win32file).AllocateReadBuffer

[PyOVERLAPPEDReadBuffer](README.md#PyOVERLAPPEDReadBuffer)= **AllocateReadBuffer( *bufSize* ** )
Allocates a buffer which can be used with an overlapped Read operation using[win32file::ReadFile](win32file.md#win32fileReadFile)

#### Parameters


  -  *bufSize* : int

    The size of the buffer to allocate.

## [win32file](README.md#win32file).AreFileApisANSI

int = **AreFileApisANSI(** )
Determines whether a set of Win32 file functions is using the ANSI or OEM character set code page. This function is useful for 8-bit console input and output operations.

## [win32file](README.md#win32file).BackupRead

(int, buffer, int) = **BackupRead( *hFile*  *, NumberOfBytesToRead*  *, Buffer*  *, bAbort*  *, bProcessSecurity*  *, lpContext* ** )
Reads streams of data from a file

#### Parameters


  -  *hFile* :[PyHANDLE](README.md#PyHANDLE)

    File handle opened by CreateFile

  -  *NumberOfBytesToRead* : int

    Number of bytes to be read from file

  -  *Buffer* : buffer

    Writeable buffer object that receives data read

  -  *bAbort* : int

    If true, ends read operation and frees backup context

  -  *bProcessSecurity* : int

    Indicates whether file's ACL stream should be read

  -  *lpContext* : int

    Pass 0 on first call, then pass back value returned from last call thereafter

#### Comments
Returns number of bytes read, data buffer, and context pointer for next operation 

If Buffer is None, a new buffer will be created of size NbrOfBytesToRead that can be passed 

back in subsequent calls

## [win32file](README.md#win32file).BackupSeek

long = **BackupSeek( *hFile*  *, NumberOfBytesToSeek*  *, lpContext* ** )
Seeks forward in a file stream

#### Parameters


  -  *hFile* :[PyHANDLE](README.md#PyHANDLE)

    File handle used by a BackupRead operation

  -  *NumberOfBytesToSeek* : long

    Number of bytes to move forward in current stream

  -  *lpContext* : int

    Context pointer returned from a BackupRead operation

#### Comments
Function will only seek to end of current stream, used to seek past bad data 

or find beginning position for read of next stream 

Returns number of bytes actually moved

## [win32file](README.md#win32file).BackupWrite

(int,int) = **BackupWrite( *hFile*  *, NumberOfBytesToWrite*  *, Buffer*  *, bAbort*  *, bProcessSecurity*  *, lpContext* ** )
Restores file data

#### Parameters


  -  *hFile* :[PyHANDLE](README.md#PyHANDLE)

    File handle opened by CreateFile

  -  *NumberOfBytesToWrite* : int

    Length of data to be written to file

  -  *Buffer* : string

    A string or buffer object that contains the data to be written

  -  *bAbort* : int

    If true, ends write operation and frees backup context

  -  *bProcessSecurity* : int

    Indicates whether ACL's should be restored

  -  *lpContext* : int

    Pass 0 on first call, then pass back value returned from last call thereafter

#### Comments
Returns number of bytes written and context pointer for next operation

## [win32file](README.md#win32file).BuildCommDCB

[PyDCB](README.md#PyDCB)= **BuildCommDCB( *def*  *, dcb* ** )
Fills the specified DCB structure with values specified in a device-control string. The device-control string uses the syntax of the mode command

#### Parameters


  -  *def* : string

    device-control string

  -  *dcb* :[PyDCB](README.md#PyDCB)

    The device-control block

## CALLBACK_CHUNK_FINISHED
 **const win32file.CALLBACK_CHUNK_FINISHED;** 


## CALLBACK_STREAM_SWITCH
 **const win32file.CALLBACK_STREAM_SWITCH;** 


## CBR_110
 **const win32file.CBR_110;** 


## CBR_115200
 **const win32file.CBR_115200;** 


## CBR_1200
 **const win32file.CBR_1200;** 


## CBR_128000
 **const win32file.CBR_128000;** 


## CBR_14400
 **const win32file.CBR_14400;** 


## CBR_19200
 **const win32file.CBR_19200;** 


## CBR_2400
 **const win32file.CBR_2400;** 


## CBR_256000
 **const win32file.CBR_256000;** 


## CBR_300
 **const win32file.CBR_300;** 


## CBR_38400
 **const win32file.CBR_38400;** 


## CBR_4800
 **const win32file.CBR_4800;** 


## CBR_56000
 **const win32file.CBR_56000;** 


## CBR_57600
 **const win32file.CBR_57600;** 


## CBR_600
 **const win32file.CBR_600;** 


## CBR_9600
 **const win32file.CBR_9600;** 


## CLRBREAK
 **const win32file.CLRBREAK;** 
Restores character transmission and places the transmission line in a nonbreak state. The CLRBREAK extended function code is identical to the ClearCommBreak function.

## CLRDTR
 **const win32file.CLRDTR;** 
Clears the DTR (data-terminal-ready) signal.

## CLRRTS
 **const win32file.CLRRTS;** 
Clears the RTS (request-to-send) signal.

## [win32file](README.md#win32file).COMSTAT

[PyCOMSTAT](README.md#PyCOMSTAT)= **COMSTAT(** )
Creates a new COMSTAT object

## COPY_FILE_ALLOW_DECRYPTED_DESTINATION
 **const win32file.COPY_FILE_ALLOW_DECRYPTED_DESTINATION;** 


## COPY_FILE_COPY_SYMLINK
 **const win32file.COPY_FILE_COPY_SYMLINK;** 


## COPY_FILE_FAIL_IF_EXISTS
 **const win32file.COPY_FILE_FAIL_IF_EXISTS;** 


## COPY_FILE_OPEN_SOURCE_FOR_WRITE
 **const win32file.COPY_FILE_OPEN_SOURCE_FOR_WRITE;** 


## COPY_FILE_RESTARTABLE
 **const win32file.COPY_FILE_RESTARTABLE;** 


## CREATE_ALWAYS
 **const win32file.CREATE_ALWAYS;** 
Creates a new file. The function overwrites the file if it exists.

## CREATE_FOR_DIR
 **const win32file.CREATE_FOR_DIR;** 


## CREATE_FOR_IMPORT
 **const win32file.CREATE_FOR_IMPORT;** 


## CREATE_NEW
 **const win32file.CREATE_NEW;** 
Creates a new file. The function fails if the specified file already exists.

## [win32file](README.md#win32file).CalculateSocketEndPointSize

int = **CalculateSocketEndPointSize( *socket* ** )
Calculate how many bytes are needed for the connection endpoints data for a socket.

#### Parameters


  -  *socket* : **PySocket** /int

    The socket for which to determine the size.

#### Comments
This function allows you to determine the minumum buffer size 

which can be passed to[win32file::AcceptEx](win32file.md#win32fileAcceptEx)

## [win32file](README.md#win32file).CancelIo

 **CancelIo( *handle* ** )
Cancels pending IO requests for the object.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle being cancelled.

## [win32file](README.md#win32file).ClearCommBreak

 **ClearCommBreak( *handle* ** )
Restores character transmission for a specified communications device and places the transmission line in a nonbreak state

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the communications device.

## [win32file](README.md#win32file).ClearCommError

int,[PyCOMSTAT](README.md#PyCOMSTAT)= **ClearCommError( *[PyHANDLE](README.md#PyHANDLE)* ** )
retrieves information about a communications error and reports the current status of a communications device.

#### Parameters


  -  *[PyHANDLE](README.md#PyHANDLE)* : handle

    A handle to the device.

## [win32file](README.md#win32file).CloseEncryptedFileRaw

 **CloseEncryptedFileRaw( *Context* ** )
Frees a context created by[win32file::OpenEncryptedFileRaw](win32file.md#win32fileOpenEncryptedFileRaw)

#### Parameters


  -  *Context* : PyCObject

    Context object returned from[win32file::OpenEncryptedFileRaw](win32file.md#win32fileOpenEncryptedFileRaw)

#### Comments
Only available on Windows 2000 or later

## [win32file](README.md#win32file).CloseHandle

 **CloseHandle( *handle* ** )
Closes an open handle.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)/int

    A previously opened handle.

## [win32file](README.md#win32file).ConnectEx

(int, int) = **ConnectEx( *s*  *, name*  *, Overlapped*  *, SendBuffer* ** )
Version of connect that uses Overlapped I/O 

ConnectEx(sock, (addr, port), buf, overlap)

#### Parameters


  -  *s* : **PySocket** /int

    A bound, unconnected socket that will be used to connect

  -  *name* : tuple

    Address to connect to (host, port)

  -  *Overlapped* :[PyOVERLAPPED](README.md#PyOVERLAPPED)

    An overlapped structure

  -  *SendBuffer=None* : buffer

    Buffer to send on the socket after connect

#### Return Value
Returns the completion code and number of bytes sent. 

The completion code will be 0 for a completed operation, or ERROR_IO_PENDING for a pending overlapped operation.
If the platform does not support ConnectEx (eg, Windows 2000), an 

exception will be thrown indicating the WSAIoctl function (which is used to 

fetch the function pointer) failed with error code WSAEINVAL (10022).

## [win32file](README.md#win32file).CopyFile

 **CopyFile( *from*  *, to*  *, bFailIfExists* ** )
Copies a file

#### Parameters


  -  *from* :[PyUnicode](README.md#PyUnicode)

    The name of the file to copy from

  -  *to* :[PyUnicode](README.md#PyUnicode)

    The name of the file to copy to

  -  *bFailIfExists* : int

    Indicates if the operation should fail if the file exists.

## [win32file](README.md#win32file).CopyFileEx

 **CopyFileEx( *ExistingFileName*  *, NewFileName*  *, ProgressRoutine*  *, Data*  *, Cancel*  *, CopyFlags*  *, Transaction* ** )
Restartable file copy with optional progress routine

#### Parameters


  -  *ExistingFileName* :[PyUNICODE](README.md#PyUNICODE)

    File to be copied

  -  *NewFileName* :[PyUNICODE](README.md#PyUNICODE)

    Place to which it will be copied

  -  *ProgressRoutine=None* :[CopyProgressRoutine](README.md#CopyProgressRoutine)

    A python function that receives progress updates, can be None

  -  *Data=None* : object

    An arbitrary object to be passed to the callback function

  -  *Cancel=False* : boolean

    Pass True to cancel a restartable copy that was previously interrupted

  -  *CopyFlags=0* : int

    Combination of COPY_FILE_* flags

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a transaction as returned by[win32transaction::CreateTransaction](win32transaction.md#win32transactionCreateTransaction)

#### Comments
Accepts keyword args.
On Vista and later, the Transaction arg can be passed to invoke CopyFileTransacted

#### Win32 API References


  - Search for *CopyFileEx* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CopyFileEx),[google](README.md#http://www.google.com/search?q=CopyFileEx)or[google groups](README.md#http://groups.google.com/groups?q=CopyFileEx).

  - Search for *CopyFileTransacted* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CopyFileTransacted),[google](README.md#http://www.google.com/search?q=CopyFileTransacted)or[google groups](README.md#http://groups.google.com/groups?q=CopyFileTransacted).

## [win32file](README.md#win32file).CopyFileW

 **CopyFileW( *from*  *, to*  *, bFailIfExists* ** )
Copies a file (NT/2000 Unicode specific version)

#### Parameters


  -  *from* :[PyUnicode](README.md#PyUnicode)

    The name of the file to copy from

  -  *to* :[PyUnicode](README.md#PyUnicode)

    The name of the file to copy to

  -  *bFailIfExists* : int

    Indicates if the operation should fail if the file exists.

## [win32file](README.md#win32file).CreateDirectory

 **CreateDirectory( *name*  *, sa* ** )
Creates a directory

#### Parameters


  -  *name* :[PyUnicode](README.md#PyUnicode)

    The name of the directory to create

  -  *sa* :[PySECURITY_ATTRIBUTES](PySECURITY.md#PySECURITYATTRIBUTES)

    The security attributes, or None

## [win32file](README.md#win32file).CreateDirectoryEx

 **CreateDirectoryEx( *templateName*  *, newDirectory*  *, sa* ** )
Creates a directory

#### Parameters


  -  *templateName* :[PyUnicode](README.md#PyUnicode)

    Specifies the path of the directory to use as a template when creating the new directory.

  -  *newDirectory* :[PyUnicode](README.md#PyUnicode)

    Specifies the name of the new directory

  -  *sa* :[PySECURITY_ATTRIBUTES](PySECURITY.md#PySECURITYATTRIBUTES)

    The security attributes, or None

## [win32file](README.md#win32file).CreateDirectoryExW

 **CreateDirectoryExW( *TemplateDirectory*  *, NewDirectory*  *, SecurityAttributes*  *, Transaction* ** )
Creates a directory (Unicode version)

#### Parameters


  -  *TemplateDirectory* :[PyUnicode](README.md#PyUnicode)

    Directory to use as a template, can be None

  -  *NewDirectory* :[PyUnicode](README.md#PyUnicode)

    Name of directory to be created

  -  *SecurityAttributes=None* :[PySECURITY_ATTRIBUTES](PySECURITY.md#PySECURITYATTRIBUTES)

    Security for new directory (optional)

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a transaction (optional).  See[win32transaction::CreateTransaction](win32transaction.md#win32transactionCreateTransaction).

#### Comments
If a transaction handle is passed, CreateDirectoryTransacted will be called (requires Vista or later).
Accepts keyword arguments.

#### Win32 API References


  - Search for *CreateDirectoryEx* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CreateDirectoryEx),[google](README.md#http://www.google.com/search?q=CreateDirectoryEx)or[google groups](README.md#http://groups.google.com/groups?q=CreateDirectoryEx).

  - Search for *CreateDirectoryTransacted* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CreateDirectoryTransacted),[google](README.md#http://www.google.com/search?q=CreateDirectoryTransacted)or[google groups](README.md#http://groups.google.com/groups?q=CreateDirectoryTransacted).

## [win32file](README.md#win32file).CreateDirectoryW

 **CreateDirectoryW( *name*  *, sa* ** )
Creates a directory (NT/2000 Unicode specific version)

#### Parameters


  -  *name* :[PyUnicode](README.md#PyUnicode)

    The name of the directory to create

  -  *sa* :[PySECURITY_ATTRIBUTES](PySECURITY.md#PySECURITYATTRIBUTES)

    The security attributes, or None

## [win32file](README.md#win32file).CreateFile

[PyHANDLE](README.md#PyHANDLE)= **CreateFile( *fileName*  *, desiredAccess*  *, shareMode*  *, attributes*  *, CreationDisposition*  *, flagsAndAttributes*  *, hTemplateFile* ** )
Creates or opens the a file or other object and returns a handle that can be used to access the object.

#### Parameters


  -  *fileName* :[PyUnicode](README.md#PyUnicode)

    The name of the file

  -  *desiredAccess* : int

    access (read-write) mode 

Specifies the type of access to the object. An application can obtain read access, write access, read-write access, or device query access. This parameter can be any combination of the following values.

 **Value**  **Meaning** 0Specifies device query access to the object. An application can query device attributes without accessing the device.GENERIC_READSpecifies read access to the object. Data can be read from the file and the file pointer can be moved. Combine with GENERIC_WRITE for read-write access.GENERIC_WRITESpecifies write access to the object. Data can be written to the file and the file pointer can be moved. Combine with GENERIC_READ for read-write access.
  -  *shareMode* : int

    Set of bit flags that specifies how the object can be shared. If dwShareMode is 0, the object cannot be shared. Subsequent open operations on the object will fail, until the handle is closed. 

To share the object, use a combination of one or more of the following values:

 **Value**  **Meaning** FILE_SHARE_DELETEWindows NT: Subsequent open operations on the object will succeed only if delete access is requested.FILE_SHARE_READSubsequent open operations on the object will succeed only if read access is requested.FILE_SHARE_WRITESubsequent open operations on the object will succeed only if write access is requested.
  -  *attributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#PySECURITYATTRIBUTES)

    The security attributes, or None

  -  *CreationDisposition* : int

    Specifies which action to take on files that exist, and which action to take when files do not exist. For more information about this parameter, see the Remarks section. This parameter must be one of the following values:

 **Value**  **Meaning** CREATE_NEWCreates a new file. The function fails if the specified file already exists.CREATE_ALWAYSCreates a new file. If the file exists, the function overwrites the file and clears the existing attributes.OPEN_EXISTINGOpens the file. The function fails if the file does not exist. 

See the Remarks section for a discussion of why you should use the OPEN_EXISTING flag if you are using the CreateFile function for devices, including the console.OPEN_ALWAYSOpens the file, if it exists. If the file does not exist, the function creates the file as if dwCreationDisposition were CREATE_NEW.TRUNCATE_EXISTINGOpens the file. Once opened, the file is truncated so that its size is zero bytes. The calling process must open the file with at least GENERIC_WRITE access. The function fails if the file does not exist.
  -  *flagsAndAttributes* : int

    file attributes

  -  *hTemplateFile* :[PyHANDLE](README.md#PyHANDLE)

    Specifies a handle with GENERIC_READ access to a template file. The template file supplies file attributes and extended attributes for the file being created.   Under Win95, this must be 0, else an exception will be raised.

#### Comments
The following objects can be opened:
files
pipes
mailslots
communications resources
disk devices (Windows NT only)
consoles
directories (open only)

## [win32file](README.md#win32file).CreateFileW

[PyHANDLE](README.md#PyHANDLE)= **CreateFileW( *FileName*  *, DesiredAccess*  *, ShareMode*  *, SecurityAttributes*  *, CreationDisposition*  *, FlagsAndAttributes*  *, TemplateFile*  *, Transaction*  *, MiniVersion*  *, ExtendedParameter* ** )
Unicode version of CreateFile - see[win32file::CreateFile](win32file.md#win32fileCreateFile)for more information.

#### Parameters


  -  *FileName* :[PyUnicode](README.md#PyUnicode)

    Name of file

  -  *DesiredAccess* : int

    Combination of access mode flags.  See MSDN docs.

  -  *ShareMode* : int

    Combination of FILE_SHARE_READ, FILE_SHARE_WRITE, FILE_SHARE_DELETE

  -  *SecurityAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#PySECURITYATTRIBUTES)

    Specifies security descriptor and handle inheritance, can be None

  -  *CreationDisposition* : int

    One of CREATE_ALWAYS,CREATE_NEW,OPEN_ALWAYS,OPEN_EXISTING or TRUNCATE_EXISTING

  -  *FlagsAndAttributes* : int

    Combination of FILE_ATTRIBUTE_* and FILE_FLAG_* flags

  -  *TemplateFile=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to file to be used as template, can be None

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to the transaction as returned by[win32transaction::CreateTransaction](win32transaction.md#win32transactionCreateTransaction)

  -  *MiniVersion=None* : int

    Transacted version of file to open, can be None

  -  *ExtendedParameter=None* : None

    Reserved, use only None

#### Comments
If Transaction is specified, CreateFileTransacted will be called (requires Vista or later)
Accepts keyword arguments.

#### Win32 API References


  - Search for *CreateFile* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CreateFile),[google](README.md#http://www.google.com/search?q=CreateFile)or[google groups](README.md#http://groups.google.com/groups?q=CreateFile).

  - Search for *CreateFileTransacted* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CreateFileTransacted),[google](README.md#http://www.google.com/search?q=CreateFileTransacted)or[google groups](README.md#http://groups.google.com/groups?q=CreateFileTransacted).

## [win32file](README.md#win32file).CreateHardLink

 **CreateHardLink( *FileName*  *, ExistingFileName*  *, SecurityAttributes*  *, Transaction* ** )
Establishes an NTFS hard link between an existing file and a new file.

#### Parameters


  -  *FileName* :[PyUnicode](README.md#PyUnicode)

    The name of the new directory entry to be created.

  -  *ExistingFileName* :[PyUnicode](README.md#PyUnicode)

    The name of the existing file to which the new link will point.

  -  *SecurityAttributes=None* :[PySECURITY_ATTRIBUTES](PySECURITY.md#PySECURITYATTRIBUTES)

    Optional SECURITY_ATTRIBUTES object. MSDN describes this parameter as reserved, so use only None

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a transaction, as returned by[win32transaction::CreateTransaction](win32transaction.md#win32transactionCreateTransaction)

#### Comments
An NTFS hard link is similar to a POSIX hard link.
This function creates a second directory entry for an existing file, can be different name in 

same directory or any name in a different directory. 

Both file paths must be on the same NTFS volume.
To remove the link, simply delete 

it and the original file will still remain.
This method exists on Windows 2000 and later.  Otherwise NotImplementedError will be raised.
Accepts keyword args.
If the Transaction parameter is specified, CreateHardLinkTransacted will be called (requires Vista or later)

#### Example
Usage

## [win32file](README.md#win32file).CreateIoCompletionPort

[PyHANDLE](README.md#PyHANDLE)= **CreateIoCompletionPort( *handle*  *, existing*  *, completionKey*  *, numThreads* ** )
Can associate an instance of an opened file with a newly created or an existing input/output (I/O) completion port; or it can create an I/O completion port without associating it with a file.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    file handle to associate with the I/O completion port

  -  *existing* :[PyHANDLE](README.md#PyHANDLE)

    handle to the I/O completion port

  -  *completionKey* : int

    per-file completion key for I/O completion packets

  -  *numThreads* : int

    number of threads allowed to execute concurrently

#### Return Value
If an existing handle to a completion port is passed, the result 

of this function will be that same handle.  See MSDN for more details.

## [win32file](README.md#win32file).CreateMailslot

[PyHANDLE](README.md#PyHANDLE)= **CreateMailslot( *Name*  *, MaxMessageSize*  *, ReadTimeout*  *, SecurityAttributes* ** )
Creates a mailslot on the local machine

#### Parameters


  -  *Name* : str

    Name of the mailslot, of the form \\.\\mailslot\\[path]name

  -  *MaxMessageSize* : int

    Largest message size.  Use 0 for unlimited.

  -  *ReadTimeout* : int

    Timeout in milliseconds.  Use -1 for no timeout.

  -  *SecurityAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#PySECURITYATTRIBUTES)

    Determines if returned handle is inheritable, can be None

#### Win32 API References


  - Search for *CreateMailslot* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CreateMailslot),[google](README.md#http://www.google.com/search?q=CreateMailslot)or[google groups](README.md#http://groups.google.com/groups?q=CreateMailslot).

## [win32file](README.md#win32file).CreateSymbolicLink

 **CreateSymbolicLink( *SymlinkFileName*  *, TargetFileName*  *, Flags*  *, Transaction* ** )
Creates a symbolic link (reparse point)

#### Parameters


  -  *SymlinkFileName* :[PyUnicode](README.md#PyUnicode)

    Path of the symbolic link to be created

  -  *TargetFileName* :[PyUnicode](README.md#PyUnicode)

    The name of file to which link will point

  -  *Flags=0* : int

    SYMBOLIC_LINK_FLAG_DIRECTORY is only defined flag

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a transaction, as returned by[win32transaction::CreateTransaction](win32transaction.md#win32transactionCreateTransaction)

#### Comments
This method only exists on Vista and later.
Accepts keyword args.
Requires SeCreateSymbolicLink priv.
If the Transaction parameter is passed in, CreateSymbolicLinkTransacted will be called

## [win32file](README.md#win32file).DCB

[PyDCB](README.md#PyDCB)= **DCB(** )
Creates a new DCB object

## DRIVE_CDROM
 **const win32file.DRIVE_CDROM;** 
The drive is a CD-ROM drive.

## DRIVE_FIXED
 **const win32file.DRIVE_FIXED;** 
The disk cannot be removed from the drive.

## DRIVE_NO_ROOT_DIR
 **const win32file.DRIVE_NO_ROOT_DIR;** 
The root directory does not exist.

## DRIVE_RAMDISK
 **const win32file.DRIVE_RAMDISK;** 
The drive is a RAM disk.

## DRIVE_REMOTE
 **const win32file.DRIVE_REMOTE;** 
The drive is a remote (network) drive.

## DRIVE_REMOVABLE
 **const win32file.DRIVE_REMOVABLE;** 
The disk can be removed from the drive.

## DRIVE_UNKNOWN
 **const win32file.DRIVE_UNKNOWN;** 
The drive type cannot be determined.

## DTR_CONTROL_DISABLE
 **const win32file.DTR_CONTROL_DISABLE;** 
Disables the DTR line when the device is opened and leaves it disabled.

## DTR_CONTROL_ENABLE
 **const win32file.DTR_CONTROL_ENABLE;** 
Enables the DTR line when the device is opened and leaves it on.

## DTR_CONTROL_HANDSHAKE
 **const win32file.DTR_CONTROL_HANDSHAKE;** 
Enables DTR handshaking. If handshaking is enabled, it is an error for the application to adjust the line by using the EscapeCommFunction function.

## [win32file](README.md#win32file).DecryptFile

 **DecryptFile( *filename* ** )
Decrypts specified file (requires Win2k or higher and NTFS)

#### Parameters


  -  *filename* : string/unicode

    File to decrypt

## [win32file](README.md#win32file).DefineDosDevice

 **DefineDosDevice( *flags*  *, deviceName*  *, targetPath* ** )
Lets an application define, redefine, or delete MS-DOS device names.

#### Parameters


  -  *flags* : int

    flags specifying aspects of device definition

  -  *deviceName* :[PyUnicode](README.md#PyUnicode)

    MS-DOS device name string

  -  *targetPath* :[PyUnicode](README.md#PyUnicode)

    MS-DOS or path string for 32-bit Windows.

## [win32file](README.md#win32file).DefineDosDeviceW

 **DefineDosDeviceW( *flags*  *, deviceName*  *, targetPath* ** )
Lets an application define, redefine, or delete MS-DOS device names. (NT/2000 Unicode specific version)

#### Parameters


  -  *flags* : int

    flags specifying aspects of device definition

  -  *deviceName* :[PyUnicode](README.md#PyUnicode)

    MS-DOS device name string

  -  *targetPath* :[PyUnicode](README.md#PyUnicode)

    MS-DOS or path string for 32-bit Windows.

## [win32file](README.md#win32file).DeleteFile

 **DeleteFile( *fileName* ** )
Deletes a file.

#### Parameters


  -  *fileName* :[PyUnicode](README.md#PyUnicode)

    The filename to delete

## [win32file](README.md#win32file).DeleteFileW

 **DeleteFileW( *FileName*  *, Transaction* ** )
Deletes a file (Unicode version)

#### Parameters


  -  *FileName* :[PyUnicode](README.md#PyUnicode)

    Name of file to be deleted

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Transaction handle as returned by[win32transaction::CreateTransaction](win32transaction.md#win32transactionCreateTransaction)

#### Comments
If a transaction handle is passed in, DeleteFileTransacted will be called (requires Windows Vista).
Accepts keyword arguments.

#### Win32 API References


  - Search for *DeleteFile* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DeleteFile),[google](README.md#http://www.google.com/search?q=DeleteFile)or[google groups](README.md#http://groups.google.com/groups?q=DeleteFile).

  - Search for *DeleteFileTransacted* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DeleteFileTransacted),[google](README.md#http://www.google.com/search?q=DeleteFileTransacted)or[google groups](README.md#http://groups.google.com/groups?q=DeleteFileTransacted).

## [win32file](README.md#win32file).DeleteVolumeMountPoint

 **DeleteVolumeMountPoint( *VolumeMountPoint* ** )
Unmounts the volume from the specified volume mount point.

#### Parameters


  -  *VolumeMountPoint* :[PyUnicode](README.md#PyUnicode)

    The mount point to delete - must have a trailing backslash.

#### Comments
Accepts keyword args.
Throws&#09an error if&#09it is not a&#09valid mount&#09point, returns None&#09on success.
Use carefully - will&#09remove drive letter&#09assignment if no directory specified
This method requires Windows 2000 or later.  On earlier platforms, NotImplementedError will be raised.

#### Example
Usage

## [win32file](README.md#win32file).DeviceIoControl

str/buffer = **DeviceIoControl( *Device*  *, IoControlCode*  *, InBuffer*  *, OutBuffer*  *, Overlapped* ** )
Sends a control code to a device or file system driver

#### Parameters


  -  *Device* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a file, device, or volume

  -  *IoControlCode* : int

    IOControl Code to use, from winioctlcon

  -  *InBuffer* : str/buffer

    The input data for the operation, can be None for some operations.

  -  *OutBuffer* : int/buffer

    Size of the buffer to allocate for output, or a writeable buffer 

as returned by[win32file::AllocateReadBuffer](win32file.md#win32fileAllocateReadBuffer).

  -  *Overlapped=None* :[PyOVERLAPPED](README.md#PyOVERLAPPED)

    An overlapped object for async operations.  Device 

handle must have been opened with FILE_FLAG_OVERLAPPED.

#### Comments
Accepts keyword args

#### Return Value
If a preallocated output buffer is passed in, the returned object 

may be the original buffer, or a view of the buffer with only the actual 

size of the retrieved data.
If OutBuffer is a buffer size and the operation is synchronous (ie no 

Overlapped is passed in), returns a plain string containing the retrieved 

data.  For an async operation, a new writeable buffer is returned.

## [win32file](README.md#win32file).DuplicateEncryptionInfoFile

 **DuplicateEncryptionInfoFile( *SrcFileName*  *, DstFileName*  *, CreationDisposition*  *, Attributes*  *, SecurityAttributes* ** )
Duplicates EFS encryption from one file to another

#### Parameters


  -  *SrcFileName* :[PyUnicode](README.md#PyUnicode)

    Encrypted file to read EFS metadata from

  -  *DstFileName* :[PyUnicode](README.md#PyUnicode)

    File to be encrypted using EFS data from source file

  -  *CreationDisposition* : int

    Specifies whether an existing file should be overwritten (CREATE_NEW or CREATE_ALWAYS)

  -  *Attributes* : int

    File attributes

  -  *SecurityAttributes=None* :[PySECURITY_ATTRIBUTES](PySECURITY.md#PySECURITYATTRIBUTES)

    Specifies security for destination file

#### Comments
Requires Windows XP or later
Accepts keyword arguments.

#### Win32 API References


  - Search for *DuplicateEncryptionInfoFile* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DuplicateEncryptionInfoFile),[google](README.md#http://www.google.com/search?q=DuplicateEncryptionInfoFile)or[google groups](README.md#http://groups.google.com/groups?q=DuplicateEncryptionInfoFile).

## EVENPARITY
 **const win32file.EVENPARITY;** 


## EV_BREAK
 **const win32file.EV_BREAK;** 
A break was detected on input.

## EV_CTS
 **const win32file.EV_CTS;** 
The CTS (clear-to-send) signal changed state.

## EV_DSR
 **const win32file.EV_DSR;** 
The DSR (data-set-ready) signal changed state.

## EV_ERR
 **const win32file.EV_ERR;** 
A line-status error occurred. Line-status errors are CE_FRAME, CE_OVERRUN, and CE_RXPARITY.

## EV_RING
 **const win32file.EV_RING;** 
A ring indicator was detected.

## EV_RLSD
 **const win32file.EV_RLSD;** 
The RLSD (receive-line-signal-detect) signal changed state.

## EV_RXCHAR
 **const win32file.EV_RXCHAR;** 
A character was received and placed in the input buffer.

## EV_RXFLAG
 **const win32file.EV_RXFLAG;** 
The event character was received and placed in the input buffer. The event character is specified in the device's DCB structure, which is applied to a serial port by using the SetCommState function.

## EV_TXEMPTY
 **const win32file.EV_TXEMPTY;** 
The last character in the output buffer was sent.

## [win32file](README.md#win32file).EncryptFile

 **EncryptFile( *filename* ** )
Encrypts specified file (requires Win2k or higher and NTFS)

#### Parameters


  -  *filename* : string/unicode

    File to encrypt

## [win32file](README.md#win32file).EncryptionDisable

 **EncryptionDisable( *DirName*  *, Disable* ** )
Enables/disables encryption for a directory (requires Win2k or higher and NTFS)

#### Parameters


  -  *DirName* : string/unicode

    Directory to enable or disable

  -  *Disable* : boolean

    Set to False to enable encryption

## [win32file](README.md#win32file).EscapeCommFunction

 **EscapeCommFunction( *handle* ** )
directs a specified communications device to perform an extended function.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the communications device.


## FD_ACCEPT
 **const win32file.FD_ACCEPT;** 


## FD_ADDRESS_LIST_CHANGE
 **const win32file.FD_ADDRESS_LIST_CHANGE;** 


## FD_CLOSE
 **const win32file.FD_CLOSE;** 


## FD_CONNECT
 **const win32file.FD_CONNECT;** 


## FD_GROUP_QOS
 **const win32file.FD_GROUP_QOS;** 


## FD_OOB
 **const win32file.FD_OOB;** 


## FD_QOS
 **const win32file.FD_QOS;** 


## FD_READ
 **const win32file.FD_READ;** 


## FD_ROUTING_INTERFACE_CHANGE
 **const win32file.FD_ROUTING_INTERFACE_CHANGE;** 


## FD_WRITE
 **const win32file.FD_WRITE;** 


## FILE_ALL_ACCESS
 **const win32file.FILE_ALL_ACCESS;** 


## FILE_ATTRIBUTE_ARCHIVE
 **const win32file.FILE_ATTRIBUTE_ARCHIVE;** 
The file should be archived. Applications use this attribute to mark files for backup or removal.

## FILE_ATTRIBUTE_COMPRESSED
 **const win32file.FILE_ATTRIBUTE_COMPRESSED;** 
The file or directory is compressed. For a file, this means that all of the data in the file is compressed. For a directory, this means that compression is the default for newly created files and subdirectories.

## FILE_ATTRIBUTE_DIRECTORY
 **const win32file.FILE_ATTRIBUTE_DIRECTORY;** 
The file is a directory

## FILE_ATTRIBUTE_HIDDEN
 **const win32file.FILE_ATTRIBUTE_HIDDEN;** 
The file is hidden. It is not to be included in an ordinary directory listing.

## FILE_ATTRIBUTE_NORMAL
 **const win32file.FILE_ATTRIBUTE_NORMAL;** 
The file has no other attributes set. This attribute is valid only if used alone.

## FILE_ATTRIBUTE_OFFLINE
 **const win32file.FILE_ATTRIBUTE_OFFLINE;** 
The data of the file is not immediately available. Indicates that the file data has been physically moved to offline storage.

## FILE_ATTRIBUTE_READONLY
 **const win32file.FILE_ATTRIBUTE_READONLY;** 
The file is read only. Applications can read the file but cannot write to it or delete it.

## FILE_ATTRIBUTE_SYSTEM
 **const win32file.FILE_ATTRIBUTE_SYSTEM;** 
The file is part of or is used exclusively by the operating system.

## FILE_ATTRIBUTE_TEMPORARY
 **const win32file.FILE_ATTRIBUTE_TEMPORARY;** 
The file is being used for temporary storage. File systems attempt to keep all of the data in memory for quicker access rather than flushing the data back to mass storage. A temporary file should be deleted by the application as soon as it is no longer needed.

## FILE_BEGIN
 **const win32file.FILE_BEGIN;** 


## FILE_CURRENT
 **const win32file.FILE_CURRENT;** 


## FILE_ENCRYPTABLE
 **const win32file.FILE_ENCRYPTABLE;** 


## FILE_END
 **const win32file.FILE_END;** 


## FILE_FLAG_BACKUP_SEMANTICS
 **const win32file.FILE_FLAG_BACKUP_SEMANTICS;** 
Windows NT only: Indicates that the file is being opened or created for a backup or restore operation. 

The operating system ensures that the calling process overrides file security checks, provided it has the necessary permission to do so. The relevant permissions are SE_BACKUP_NAME and SE_RESTORE_NAME. 

You can also set this flag to obtain a handle to a directory. A directory handle can be passed to some Win32 functions in place of a file handle.

## FILE_FLAG_DELETE_ON_CLOSE
 **const win32file.FILE_FLAG_DELETE_ON_CLOSE;** 
Indicates that the operating system is to delete the file immediately after all of its handles have been closed, 

not just the handle for which you specified FILE_FLAG_DELETE_ON_CLOSE. Subsequent open requests for the file will fail, unless FILE_SHARE_DELETE is used.

## FILE_FLAG_NO_BUFFERING
 **const win32file.FILE_FLAG_NO_BUFFERING;** 
Instructs the system to open the file with no intermediate buffering or caching. 

When combined with FILE_FLAG_OVERLAPPED, the flag gives maximum asynchronous performance, 

because the I/O does not rely on the synchronous operations of the memory 

manager. However, some I/O operations will take longer, because data is 

not being held in the cache. An application must meet certain requirements 

when working with files opened with FILE_FLAG_NO_BUFFERING:
-&#09File access must begin at byte offsets within the file that are integer multiples of the volume's sector size.
-&#09File access must be for numbers of bytes that are integer multiples of the volume's sector size. 

For example, if the sector size is 512 bytes, an application can request reads and writes of 512, 1024, or 2048 bytes, but not of 335, 981, or 7171 bytes.
-&#09Buffer addresses for read and write operations must be aligned on addresses in memory that are integer multiples of the volume's sector size. 

One way to align buffers on integer multiples of the volume sector size is to use VirtualAlloc to allocate the 

buffers. It allocates memory that is aligned on addresses that are integer multiples of the operating system's memory page size. Because both memory page 

and volume sector sizes are powers of 2, this memory is also aligned on addresses that are integer multiples of a volume's sector size. An application can 

determine a volume's sector size by calling the GetDiskFreeSpace function.

## FILE_FLAG_OPEN_REPARSE_POINT
 **const win32file.FILE_FLAG_OPEN_REPARSE_POINT;** 
used to open a handle for use with DeviceIoControl and FSCTL_GET_REPARSE_POINT/FSCTL_SET_REPARSE_POINT)

## FILE_FLAG_OVERLAPPED
 **const win32file.FILE_FLAG_OVERLAPPED;** 
Instructs the system to initialize the object, so that operations that take a significant amount of time to process return ERROR_IO_PENDING. When the operation is finished, the specified event is set to the signaled state. 

When you specify FILE_FLAG_OVERLAPPED, the ReadFile and WriteFile functions must specify an OVERLAPPED structure. That is, when FILE_FLAG_OVERLAPPED is specified, an application must perform overlapped reading and writing. 

When FILE_FLAG_OVERLAPPED is specified, the system does not maintain the file pointer. The file position must be passed as part of the lpOverlapped parameter (pointing to an OVERLAPPED structure) to the ReadFile and WriteFile functions. 

This flag also enables more than one operation to be performed simultaneously with the handle (a simultaneous read and write operation, for example).

## FILE_FLAG_POSIX_SEMANTICS
 **const win32file.FILE_FLAG_POSIX_SEMANTICS;** 
Indicates that the file is to be accessed according to POSIX rules. 

This includes allowing multiple files with names, differing only in case, for file systems that support such naming. 

Use care when using this option because files created with this flag may not be accessible by applications written for MS-DOS or Windows.

## FILE_FLAG_RANDOM_ACCESS
 **const win32file.FILE_FLAG_RANDOM_ACCESS;** 
Indicates that the file is accessed randomly. The system can use this as a hint to optimize file caching.

## FILE_FLAG_SEQUENTIAL_SCAN
 **const win32file.FILE_FLAG_SEQUENTIAL_SCAN;** 
Indicates that the file is to be accessed sequentially from beginning to end. The system can use this as a hint to optimize file caching. 

If an application moves the file pointer for random access, optimum caching may not occur; however, correct operation is still guaranteed. 

Specifying this flag can increase performance for applications that read large files using sequential access. 

Performance gains can be even more noticeable for applications that read large files mostly sequentially, but occasionally skip over small ranges of bytes.

## FILE_FLAG_WRITE_THROUGH
 **const win32file.FILE_FLAG_WRITE_THROUGH;** 
Instructs the system to write through any intermediate cache and go directly to disk. Windows can still cache write operations, but cannot lazily flush them.

## FILE_GENERIC_READ
 **const win32file.FILE_GENERIC_READ;** 


## FILE_GENERIC_WRITE
 **const win32file.FILE_GENERIC_WRITE;** 


## FILE_IS_ENCRYPTED
 **const win32file.FILE_IS_ENCRYPTED;** 


## [win32file](README.md#win32file).FILE_NOTIFY_INFORMATION

[(action, filename), ... = **FILE_NOTIFY_INFORMATION( *buffer*  *, size* ** )
Decodes a PyFILE_NOTIFY_INFORMATION buffer.

#### Parameters


  -  *buffer* : string

    The buffer to decode.

  -  *size* : int

    The number of bytes to refer to.  Generally this 

will be smaller than the size of the buffer (and certainly never greater!)

#### Comments
See[win32file::ReadDirectoryChangesW](win32file.md#win32fileReadDirectoryChangesW)for more information.

## FILE_READ_ONLY
 **const win32file.FILE_READ_ONLY;** 


## FILE_ROOT_DIR
 **const win32file.FILE_ROOT_DIR;** 


## FILE_SHARE_DELETE
 **const win32file.FILE_SHARE_DELETE;** 
Windows NT only: Subsequent open operations on the object will succeed only if delete access is requested.

## FILE_SHARE_READ
 **const win32file.FILE_SHARE_READ;** 
Subsequent open operations on the object will succeed only if read access is requested.

## FILE_SHARE_WRITE
 **const win32file.FILE_SHARE_WRITE;** 
Subsequent open operations on the object will succeed only if write access is requested.

## FILE_SYSTEM_ATTR
 **const win32file.FILE_SYSTEM_ATTR;** 


## FILE_SYSTEM_DIR
 **const win32file.FILE_SYSTEM_DIR;** 


## FILE_SYSTEM_NOT_SUPPORT
 **const win32file.FILE_SYSTEM_NOT_SUPPORT;** 


## FILE_TYPE_CHAR
 **const win32file.FILE_TYPE_CHAR;** 
The specified file is a character file, typically an LPT device or a console.

## FILE_TYPE_DISK
 **const win32file.FILE_TYPE_DISK;** 
The specified file is a disk file.

## FILE_TYPE_PIPE
 **const win32file.FILE_TYPE_PIPE;** 
The specified file is either a named or anonymous pipe.

## FILE_TYPE_UNKNOWN
 **const win32file.FILE_TYPE_UNKNOWN;** 
The type of the specified file is unknown.

## FILE_UNKNOWN
 **const win32file.FILE_UNKNOWN;** 


## FILE_USER_DISALLOWED
 **const win32file.FILE_USER_DISALLOWED;** 


## FileAllocationInfo
 **const win32file.FileAllocationInfo;** 


## FileAttributeTagInfo
 **const win32file.FileAttributeTagInfo;** 


## FileBasicInfo
 **const win32file.FileBasicInfo;** 


## FileCompressionInfo
 **const win32file.FileCompressionInfo;** 


## FileDispositionInfo
 **const win32file.FileDispositionInfo;** 


## [win32file](README.md#win32file).FileEncryptionStatus

int = **FileEncryptionStatus( *FileName* ** )
retrieves the encryption status of the specified file.

#### Parameters


  -  *FileName* : string/unicode

    file to query

#### Comments
Requires Windows 2000 or higher.

#### Return Value
The result is documented as being one of FILE_ENCRYPTABLE, 

FILE_IS_ENCRYPTED, FILE_SYSTEM_ATTR, FILE_ROOT_DIR, FILE_SYSTEM_DIR, 

FILE_UNKNOWN, FILE_SYSTEM_NOT_SUPPORT, FILE_USER_DISALLOWED, 

or FILE_READ_ONLY

## FileEndOfFileInfo
 **const win32file.FileEndOfFileInfo;** 


## FileIdBothDirectoryInfo
 **const win32file.FileIdBothDirectoryInfo;** 


## FileIdBothDirectoryRestartInfo
 **const win32file.FileIdBothDirectoryRestartInfo;** 


## FileIdType
 **const win32file.FileIdType;** 


## FileIoPriorityHintInfo
 **const win32file.FileIoPriorityHintInfo;** 


## FileNameInfo
 **const win32file.FileNameInfo;** 


## FileRenameInfo
 **const win32file.FileRenameInfo;** 


## FileStandardInfo
 **const win32file.FileStandardInfo;** 


## FileStreamInfo
 **const win32file.FileStreamInfo;** 


## [win32file](README.md#win32file).FindClose

 **FindClose( *hFindFile* ** )
Closes a find handle.

#### Parameters


  -  *hFindFile* : int

    file search handle

## [win32file](README.md#win32file).FindCloseChangeNotification

 **FindCloseChangeNotification( *hChangeHandle* ** )
Closes a handle.

#### Parameters


  -  *hChangeHandle* : int

    handle to change notification to close

## [win32file](README.md#win32file).FindFileNames

[[PyUnicode](README.md#PyUnicode),...] = **FindFileNames( *FileName*  *, Transaction* ** )
Enumerates hard links that point to specified file

#### Parameters


  -  *FileName* :[PyUnicode](README.md#PyUnicode)

    Name of file for which to find links

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a transaction, can be None

#### Comments
This uses the API functions FindFirstFileNameW, FindNextFileNameW and FindClose
Available on Vista and later
If Transaction is specified, a transacted search is performed using FindFirstFileNameTransacted

## [win32file](README.md#win32file).FindFilesIterator

iterator = **FindFilesIterator( *FileName*  *, Transaction* ** )
Returns an interator based on 

FindFirstFile/FindNextFile. Similar to **win32file::FindFiles** , but 

avoids the creation of the list for huge directories.

#### Parameters


  -  *FileName* : string

    A string that specifies a valid directory or path and filename, which can contain wildcard characters (* and ?).

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a transaction, can be None. 

If this parameter is not None, FindFirstFileTransacted will be called to perform a transacted search

#### Comments
Accepts keyword args.
FindFirstFileTransacted will be called if a transaction handle is passed in.

#### Return Value
The result is a Python iterator, with each next() method 

returning a[WIN32_FIND_DATA](WIN32.md#WIN32FIND_DATA)tuple.

## [win32file](README.md#win32file).FindFilesW

list = **FindFilesW( *FileName*  *, Transaction* ** )
Retrieves a list of matching filenames, using the Windows Unicode API.  An interface to the API FindFirstFileW/FindNextFileW/Find close functions.

#### Parameters


  -  *FileName* : string

    A string that specifies a valid directory or path and filename, which can contain wildcard characters (* and ?).

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Transaction handle as returned by[win32transaction::CreateTransaction](win32transaction.md#win32transactionCreateTransaction).  Can be None. 

If this parameter is not None, FindFirstFileTransacted will be called to perform a transacted search

#### Comments
Accepts keyword args.
FindFirstFileTransacted will be called if a transaction handle is passed in.

#### Win32 API References


  - Search for *FindFirstFile* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindFirstFile),[google](README.md#http://www.google.com/search?q=FindFirstFile)or[google groups](README.md#http://groups.google.com/groups?q=FindFirstFile).

  - Search for *FindFirstFileTransacted* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindFirstFileTransacted),[google](README.md#http://www.google.com/search?q=FindFirstFileTransacted)or[google groups](README.md#http://groups.google.com/groups?q=FindFirstFileTransacted).

  - Search for *FindNextFile* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindNextFile),[google](README.md#http://www.google.com/search?q=FindNextFile)or[google groups](README.md#http://groups.google.com/groups?q=FindNextFile).

  - Search for *FindClose* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindClose),[google](README.md#http://www.google.com/search?q=FindClose)or[google groups](README.md#http://groups.google.com/groups?q=FindClose).

#### Return Value
The return value is a list of[WIN32_FIND_DATA](WIN32.md#WIN32FIND_DATA)tuples.

## [win32file](README.md#win32file).FindFirstChangeNotification

int = **FindFirstChangeNotification( *pathName*  *, bWatchSubtree*  *, notifyFilter* ** )
Creates a change notification handle and sets up initial change notification filter conditions. A wait on a notification handle succeeds when a change matching the filter conditions occurs in the specified directory or subtree.

#### Parameters


  -  *pathName* :[PyUnicode](README.md#PyUnicode)

    Name of directory to watch

  -  *bWatchSubtree* : int

    flag for monitoring directory or directory tree

  -  *notifyFilter* : int

    filter conditions to watch for.  See[win32api::FindFirstChangeNotification](win32api.md#win32apiFindFirstChangeNotification)for details.

## [win32file](README.md#win32file).FindNextChangeNotification

int = **FindNextChangeNotification( *hChangeHandle* ** )
Requests that the operating system signal a change notification handle the next time it detects an appropriate change,

#### Parameters


  -  *hChangeHandle* : int

    handle to change notification to signal

## [win32file](README.md#win32file).FindStreams

[(long,[PyUnicode](README.md#PyUnicode)),...] = **FindStreams( *FileName*  *, Transaction* ** )
List the data streams for a file

#### Parameters


  -  *FileName* :[PyUnicode](README.md#PyUnicode)

    Name of file (or directory) to operate on

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a transaction, can be None

#### Comments
This uses the API functions FindFirstStreamW, FindNextStreamW and FindClose
Available on Windows Server 2003 and Vista
If the Transaction arg is not None, FindFirstStreamTransacted will be called in place of FindFirstStreamW

#### Return Value
Returns a list of tuples containing each stream's size and name

## [win32file](README.md#win32file).FlushFileBuffers

 **FlushFileBuffers( *hFile* ** )
Clears the buffers for the specified file and causes all buffered data to be written to the file.

#### Parameters


  -  *hFile* :[PyHANDLE](README.md#PyHANDLE)

    open handle to file whose buffers are to be flushed

## GENERIC_EXECUTE
 **const win32file.GENERIC_EXECUTE;** 
Specifies execute access.

## GENERIC_READ
 **const win32file.GENERIC_READ;** 
Specifies read access to the object. Data can be read from the file and the file pointer can be moved. Combine with GENERIC_WRITE for read-write access.

## GENERIC_WRITE
 **const win32file.GENERIC_WRITE;** 
Specifies write access to the object. Data can be written to the file and the file pointer can be moved. Combine with GENERIC_READ for read-write access.

## [win32file](README.md#win32file).GetAcceptExSockaddrs

(iFamily, **LocalSockAddr** , **RemoteSockAddr** ) = **GetAcceptExSockaddrs( *sAccepting*  *, buffer* ** )
Parses the connection endpoints from the buffer passed into AcceptEx

#### Parameters


  -  *sAccepting* : **PySocket** /int

    Socket that was passed into the sAccepting parameter of AcceptEx

  -  *buffer* :[PyOVERLAPPEDReadBuffer](README.md#PyOVERLAPPEDReadBuffer)

    Buffer you passed into AcceptEx

#### Comments
LocalSockAddr and RemoteSockAddr are ("xx.xx.xx.xx", port#) if iFamily == AF_INET
otherwise LocalSockAddr and RemoteSockAddr are just binary strings
and they should be unpacked with the struct module.

## [win32file](README.md#win32file).GetBinaryType

int = **GetBinaryType( *appName* ** )
Determines whether a file is executable, and if so, what type of executable file it is. That last property determines which subsystem an executable file runs under.

#### Parameters


  -  *appName* :[PyUnicode](README.md#PyUnicode)

    Fully qualified path of file to test

## [win32file](README.md#win32file).GetCommMask

int = **GetCommMask( *handle* ** )
Retrieves the value of the event mask for a specified communications device.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the communications device.

## [win32file](README.md#win32file).GetCommModemStatus

int = **GetCommModemStatus( *handle* ** )
Retrieves modem control-register values.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the communications device.

## [win32file](README.md#win32file).GetCommState

[PyDCB](README.md#PyDCB)= **GetCommState( *handle* ** )
Returns a device-control block (a DCB structure) with the current control settings for a specified communications device.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the communications device.

## [win32file](README.md#win32file).GetCommTimeouts

 **PyCOMMTIMEOUTS** = **GetCommTimeouts( *handle* ** )
Retrieves the time-out parameters for all read and write operations on a specified communications device.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the communications device.

## [win32file](README.md#win32file).GetCompressedFileSize

long = **GetCompressedFileSize(** )
Determines the compressed size of a file.

## [win32file](README.md#win32file).GetDiskFreeSpace

(int, int, int, int) = **GetDiskFreeSpace( *rootPathName* ** )
Determines the free space on a device.

#### Parameters


  -  *rootPathName* :[PyUnicode](README.md#PyUnicode)

    address of root path

#### Return Value
The result is a tuple of integers representing (sectors per cluster, bytes per sector, number of free clusters, total number of clusters)

## [win32file](README.md#win32file).GetDiskFreeSpaceEx

long, long, long = **GetDiskFreeSpaceEx( *rootPathName* ** )
Determines the free space on a device.

#### Parameters


  -  *rootPathName* :[PyUnicode](README.md#PyUnicode)

    address of root path

#### Return Value
The result is a tuple of long integers:

#### Items


  - [0] *long integer* : freeBytes

    The total number of free bytes on the disk that are available to the user associated with the calling thread.

  - [1] *long integer* : totalBytes

    The total number of bytes on the disk that are available to the user associated with the calling thread. 

Windows 2000: If per-user quotas are in use, this value may be less than the total number of bytes on the disk.

  - [2] *long integer* : totalFreeBytes

    The total number of free bytes on the disk.

## [win32file](README.md#win32file).GetDriveType

int = **GetDriveType( *rootPathName* ** )
Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive.

#### Parameters


  -  *rootPathName* : string

    

#### Return Value
The result is one of the DRIVE_* constants.

## [win32file](README.md#win32file).GetDriveTypeW

int = **GetDriveTypeW( *rootPathName* ** )
Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive. (NT/2000 Unicode specific version).

#### Parameters


  -  *rootPathName* : string

    

#### Return Value
The result is one of the DRIVE_* constants.

## [win32file](README.md#win32file).GetFileAttributes

int = **GetFileAttributes( *fileName* ** )
Determines a files attributes.

#### Parameters


  -  *fileName* :[PyUnicode](README.md#PyUnicode)

    Name of the file to retrieve attributes for.

#### Comments
The win32file module exposes[win32file::GetFileAttributes](win32file.md#win32fileGetFileAttributes)and[win32file::GetFileAttributesW](win32file.md#win32fileGetFileAttributesW)separately - both functions will accept 

either strings or Unicode objects but will always call the named function. 

This is different than[win32api::GetFileAttributes](win32api.md#win32apiGetFileAttributes), which only exposes 

one Python function and automatically calls the appropriate win32 function 

based on the type of the filename param.

## [win32file](README.md#win32file).GetFileAttributesEx

tuple = **GetFileAttributesEx( *FileName*  *, InfoLevelId*  *, Transaction* ** )
Retrieves attributes for a specified file or directory.

#### Parameters


  -  *FileName* :[PyUnicode](README.md#PyUnicode)

    File or directory for which to retrieve information 

In the ANSI version of this function, the name is limited to 

MAX_PATH characters. To extend this limit to nearly 32,000 wide characters, 

call the Unicode version of the function ( **win32file::GetFileAttributesExW** ) and prepend 

r"\\?\\" to the path.

  -  *InfoLevelId=GetFileExInfoStandard* : int

    An integer that gives the set of attribute information to obtain. 

See the Win32 SDK documentation for more information.

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a transaction (optional).  See[win32transaction::CreateTransaction](win32transaction.md#win32transactionCreateTransaction). 

If this parameter is specified, GetFileAttributesTransacted will be called (requires Vista or later).

#### Comments
Not all file systems can record creation and last access time and not all file systems record 

them in the same manner. For example, on Windows NT FAT, create time has a resolution of 

10 milliseconds, write time has a resolution of 2 seconds, and access time has a resolution 

of 1 day (really, the access date). On NTFS, access time has a resolution of 1 hour. 

Furthermore, FAT records times on disk in local time, while NTFS records times on disk in UTC, 

so it is not affected by changes in time zone or daylight saving time.
Accepts keyword arguments.

 **InfoLevelId**  **Information returned** GetFileExInfoStandardTuple representing a WIN32_FILE_ATTRIBUTE_DATA struc
#### Win32 API References


  - Search for *GetFileAttributesEx* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetFileAttributesEx),[google](README.md#http://www.google.com/search?q=GetFileAttributesEx)or[google groups](README.md#http://groups.google.com/groups?q=GetFileAttributesEx).

  - Search for *GetFileAttributesTransacted* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetFileAttributesTransacted),[google](README.md#http://www.google.com/search?q=GetFileAttributesTransacted)or[google groups](README.md#http://groups.google.com/groups?q=GetFileAttributesTransacted).

#### Return Value
The result is a tuple of:

#### Items


  - [0] *int* : attributes

    File Attributes.  A combination of the win32com.FILE_ATTRIBUTE_* flags.

  - [1] *[PyTime](README.md#PyTime)* : creationTime

    Specifies when the file or directory was created.

  - [2] *[PyTime](README.md#PyTime)* : lastAccessTime

    For a file, specifies when the file was last read from 

or written to. For a directory, the structure specifies when the directory was created. For 

both files and directories, the specified date will be correct, but the time of day will 

always be set to midnight.

  - [3] *[PyTime](README.md#PyTime)* : lastWriteTime

    For a file, the structure specifies when the file was last 

written to. For a directory, the structure specifies when the directory was created.

  - [4] *int/long* : fileSize

    The size of the file. This member has no meaning for directories.

## [win32file](README.md#win32file).GetFileAttributesW

int = **GetFileAttributesW( *fileName* ** )
Determines a files attributes (NT/2000 Unicode specific version).

#### Parameters


  -  *fileName* :[PyUnicode](README.md#PyUnicode)

    Name of the file to retrieve attributes for.

#### Comments
Note that[win32api::GetFileAttributes](win32api.md#win32apiGetFileAttributes)will automatically call 

GetFileAttributesW when passed a unicode filename param.  See[win32file::GetFileAttributes](win32file.md#win32fileGetFileAttributes)and[win32api::GetFileAttributes](win32api.md#win32apiGetFileAttributes)for more.

## GetFileExInfoStandard
 **const win32file.GetFileExInfoStandard;** 


## [win32file](README.md#win32file).GetFileInformationByHandle

tuple = **GetFileInformationByHandle( *handle* ** )
Retrieves file information for a specified file.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)/int

    Handle to the file for which to obtain information.
This handle should not be a pipe handle. The GetFileInformationByHandle function does not work with pipe handles.

#### Comments
Depending on the underlying network components of the operating system and the type of server 

connected to, the GetFileInformationByHandle function may fail, return partial information, 

or full information for the given file. In general, you should not use GetFileInformationByHandle 

unless your application is intended to be run on a limited set of operating system configurations.

#### Return Value
The result is a tuple of:

#### Items


  - [0] *int* : dwFileAttributes

    

  - [1] *[PyTime](README.md#PyTime)* : ftCreationTime

    

  - [2] *[PyTime](README.md#PyTime)* : ftLastAccessTime

    

  - [3] *[PyTime](README.md#PyTime)* : ftLastWriteTime

    

  - [4] *int* : dwVolumeSerialNumber

    

  - [5] *int* : nFileSizeHigh

    

  - [6] *int* : nFileSizeLow

    

  - [7] *int* : nNumberOfLinks

    

  - [8] *int* : nFileIndexHigh

    

  - [9] *int* : nFileIndexLow

    

## [win32file](README.md#win32file).GetFileInformationByHandleEx

object = **GetFileInformationByHandleEx( *File*  *, FileInformationClass* ** )
Retrieves extended file information for an open file handle.

#### Parameters


  -  *File* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a file or directory.  Do not pass a pipe handle.

  -  *FileInformationClass* : int

    Type of data to return, one of win32file.File*Info values

#### Comments
Available on Vista and later.
Accepts keyword args.

#### Return Value
Type of returned object is determined by the requested information class


## [win32file](README.md#win32file).GetFileSize

long = **GetFileSize(** )
Determines the size of a file.

## [win32file](README.md#win32file).GetFileTime

([PyTime](README.md#PyTime),[PyTime](README.md#PyTime),[PyTime](README.md#PyTime)) = **GetFileTime( *handle*  *, creationTime*  *, accessTime*  *, writeTime* ** )
Returns a file's creation, last access, and modification times.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    Handle to the file.

  -  *creationTime* :[PyTime](README.md#PyTime)

    

  -  *accessTime* :[PyTime](README.md#PyTime)

    

  -  *writeTime* :[PyTime](README.md#PyTime)

    

#### Comments
Times are returned in UTC time.

## [win32file](README.md#win32file).GetFileType

int = **GetFileType( *hFile* ** )
Determines the type of a file.

#### Parameters


  -  *hFile* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the file.

## [win32file](README.md#win32file).GetFinalPathNameByHandle

[PyUnicode](README.md#PyUnicode)= **GetFinalPathNameByHandle( *File*  *, Flags* ** )
Returns the file name for an open file handle

#### Parameters


  -  *File* :[PyHANDLE](README.md#PyHANDLE)

    An open file handle

  -  *Flags* : int

    Specifies type of path to return. (win32con.FILE_NAME_NORMALIZED,FILE_NAME_OPENED,VOLUME_NAME_DOS,VOLUME_NAME_GUID,VOLUME_NAME_NONE,VOLUME_NAME_NT)

#### Comments
Exists on Windows Vista or later.
Accepts keyword arguments.

#### Win32 API References


  - Search for *GetFinalPathNameByHandle* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetFinalPathNameByHandle),[google](README.md#http://www.google.com/search?q=GetFinalPathNameByHandle)or[google groups](README.md#http://groups.google.com/groups?q=GetFinalPathNameByHandle).

## [win32file](README.md#win32file).GetFullPathName

str/unicode = **GetFullPathName( *FileName*  *, Transaction* ** )
Returns full path for path passed in

#### Parameters


  -  *FileName* : str/unicode

    Path on which to operate

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a transaction as returned by[win32transaction::CreateTransaction](win32transaction.md#win32transactionCreateTransaction)

#### Comments
This function takes either a plain string or a unicode string, and returns the same type 

If unicode is passed in, GetFullPathNameW is called, which supports filenames longer than MAX_PATH
If Transaction parameter is specified, GetFullPathNameTransacted is called (requires Vista or later)

## [win32file](README.md#win32file).GetLogicalDrives

int = **GetLogicalDrives(** )
Returns a bitmaks of the logical drives installed.

## [win32file](README.md#win32file).GetLongPathName

[PyUnicode](README.md#PyUnicode)= **GetLongPathName( *ShortPath*  *, Transaction* ** )
Retrieves the long path for a short path (8.3 filename)

#### Parameters


  -  *ShortPath* :[PyUnicode](README.md#PyUnicode)

    8.3 path to be expanded

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a transaction.  If specified, GetLongPathNameTransacted will be called.

#### Comments
Accepts keyword args

## [win32file](README.md#win32file).GetMailslotInfo

(int,int,int,int) = **GetMailslotInfo( *Mailslot* ** )
Retrieves information about a mailslot

#### Parameters


  -  *Mailslot* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a mailslot

#### Win32 API References


  - Search for *GetMailslotInfo* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetMailslotInfo),[google](README.md#http://www.google.com/search?q=GetMailslotInfo)or[google groups](README.md#http://groups.google.com/groups?q=GetMailslotInfo).

#### Return Value
Returns (maximum message size, next message size, message count, timeout)

## [win32file](README.md#win32file).GetOverlappedResult

int = **GetOverlappedResult( *hFile*  *, overlapped*  *, bWait* ** )
Determines the result of the most recent call with an OVERLAPPED object.

#### Parameters


  -  *hFile* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the pipe or file

  -  *overlapped* :[PyOVERLAPPED](README.md#PyOVERLAPPED)

    The overlapped object to check.

  -  *bWait* : int

    Indicates if the function should wait for data to become available.

#### Comments
The result is the number of bytes transferred.  The overlapped object's attributes will be changed during this call.

## [win32file](README.md#win32file).GetQueuedCompletionStatus

(int, int, int,[PyOVERLAPPED](README.md#PyOVERLAPPED)) = **GetQueuedCompletionStatus( *hPort*  *, timeOut* ** )
Attempts to dequeue an I/O completion packet from a specified input/output completion port.

#### Parameters


  -  *hPort* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the completion port.

  -  *timeOut* : int

    Timeout in milli-seconds.

#### Comments
This method never throws an API error.
The result is a tuple of (rc, numberOfBytesTransferred, completionKey, overlapped)
If the function succeeds, rc will be set to 0, otherwise it will be set to the win32 error code.

## [win32file](README.md#win32file).GetVolumeNameForVolumeMountPoint

[PyUnicode](README.md#PyUnicode)= **GetVolumeNameForVolumeMountPoint( *VolumeMountPoint* ** )
Returns unique volume name.

#### Parameters


  -  *VolumeMountPoint* :[PyUnicode](README.md#PyUnicode)

    Volume mount point or root drive - trailing backslash required

#### Comments
Requires Win2K or later.
Accepts keyword args.

## [win32file](README.md#win32file).GetVolumePathName

[PyUnicode](README.md#PyUnicode)= **GetVolumePathName( *FileName*  *, BufferLength* ** )
Returns volume mount point for a path

#### Parameters


  -  *FileName* :[PyUnicode](README.md#PyUnicode)

    File/dir for which to return volume mount point

  -  *BufferLength=0* : int

    Optional parm to allocate extra space for returned string

#### Comments
Api gives no indication of how much memory is needed, so function assumes returned path 

will not be longer that length of input path + 1. 

Use GetFullPathName first for relative paths, or GetLongPathName for 8.3 paths. 

Optional second parm can also be used to override the buffer size for returned path
Accepts keyword args.

## [win32file](README.md#win32file).GetVolumePathNamesForVolumeName

[[PyUnicode](README.md#PyUnicode),...] = **GetVolumePathNamesForVolumeName( *VolumeName* ** )
Returns mounted paths for a volume

#### Parameters


  -  *VolumeName* :[PyUnicode](README.md#PyUnicode)

    Name of a volume as returned by[win32file::GetVolumeNameForVolumeMountPoint](win32file.md#win32fileGetVolumeNameForVolumeMountPoint)

#### Comments
Requires WinXP or later
Accepts keyword args

## IoPriorityHintLow
 **const win32file.IoPriorityHintLow;** 


## IoPriorityHintNormal
 **const win32file.IoPriorityHintNormal;** 


## IoPriorityHintVeryLow
 **const win32file.IoPriorityHintVeryLow;** 


## [win32file](README.md#win32file).LockFile

 **LockFile( *hFile*  *, offsetLow*  *, offsetHigh*  *, nNumberOfBytesToLockLow*  *, nNumberOfBytesToLockHigh* ** )
Locks a specified file for exclusive access by the calling process.

#### Parameters


  -  *hFile* :[PyHANDLE](README.md#PyHANDLE)

    handle of file to lock

  -  *offsetLow* : int

    low-order word of lock region offset

  -  *offsetHigh* : int

    high-order word of lock region offset

  -  *nNumberOfBytesToLockLow* : int

    low-order word of length to lock

  -  *nNumberOfBytesToLockHigh* : int

    high-order word of length to lock

## [win32file](README.md#win32file).LockFileEx

 **LockFileEx( *hFile*  *, int*  *, int*  *, int*  *, ol* ** )
Locks a file. Wrapper for LockFileEx win32 API.

#### Parameters


  -  *hFile* :[PyHANDLE](README.md#PyHANDLE)/int

    Handle to the file

  -  *int* : dwFlags

    Flags that specify exclusive/shared and blocking/non-blocking mode

  -  *int* : nbytesLow

    low-order part of number of bytes to lock

  -  *int* : nbytesHigh

    high-order part of number of bytes to lock

  -  *ol=None* :[PyOVERLAPPED](README.md#PyOVERLAPPED)

    An overlapped structure

## MARKPARITY
 **const win32file.MARKPARITY;** 


## MOVEFILE_COPY_ALLOWED
 **const win32file.MOVEFILE_COPY_ALLOWED;** 
If the file is to be moved to a different volume, the function simulates the move by using the CopyFile and DeleteFile functions. Cannot be combined with the MOVEFILE_DELAY_UNTIL_REBOOT flag.

## MOVEFILE_CREATE_HARDLINK
 **const win32file.MOVEFILE_CREATE_HARDLINK;** 


## MOVEFILE_DELAY_UNTIL_REBOOT
 **const win32file.MOVEFILE_DELAY_UNTIL_REBOOT;** 
Windows NT only: The function does not move the file until the operating system is restarted. The system moves the file immediately after AUTOCHK is executed, but before creating any paging files. Consequently, this parameter enables the function to delete paging files from previous startups.

## MOVEFILE_FAIL_IF_NOT_TRACKABLE
 **const win32file.MOVEFILE_FAIL_IF_NOT_TRACKABLE;** 


## MOVEFILE_REPLACE_EXISTING
 **const win32file.MOVEFILE_REPLACE_EXISTING;** 
If a file of the name specified by lpNewFileName already exists, the function replaces its contents with those specified by lpExistingFileName.

## MOVEFILE_WRITE_THROUGH
 **const win32file.MOVEFILE_WRITE_THROUGH;** 
Windows NT only: The function does not return until the file has actually been moved on the disk. Setting this flag guarantees that a move perfomed as a copy and delete operation is flushed to disk before the function returns. The flush occurs at the end of the copy operation.
This flag has no effect if the MOVEFILE_DELAY_UNTIL_REBOOT flag is set.

## [win32file](README.md#win32file).MoveFile

 **MoveFile( *existingFileName*  *, newFileName* ** )
Renames an existing file or a directory (including all its children).

#### Parameters


  -  *existingFileName* :[PyUnicode](README.md#PyUnicode)

    Name of the existing file

  -  *newFileName* :[PyUnicode](README.md#PyUnicode)

    New name for the file

## [win32file](README.md#win32file).MoveFileEx

 **MoveFileEx( *existingFileName*  *, newFileName*  *, flags* ** )
Renames an existing file or a directory (including all its children).

#### Parameters


  -  *existingFileName* :[PyUnicode](README.md#PyUnicode)

    Name of the existing file

  -  *newFileName* :[PyUnicode](README.md#PyUnicode)

    New name for the file, can be None for delayed delete operation

  -  *flags* : int

    flag to determine how to move file (win32file.MOVEFILE_*)

## [win32file](README.md#win32file).MoveFileExW

 **MoveFileExW( *existingFileName*  *, newFileName*  *, flags* ** )
Renames an existing file or a directory (including all its children). (NT/2000 Unicode specific version).

#### Parameters


  -  *existingFileName* :[PyUnicode](README.md#PyUnicode)

    Name of the existing file

  -  *newFileName* :[PyUnicode](README.md#PyUnicode)

    New name for the file, can be None for delayed delete operation

  -  *flags* : int

    flag to determine how to move file (win32file.MOVEFILE_*)

## [win32file](README.md#win32file).MoveFileW

 **MoveFileW( *existingFileName*  *, newFileName* ** )
Renames an existing file or a directory (including all its children). (NT/2000 Unicode specific version).

#### Parameters


  -  *existingFileName* :[PyUnicode](README.md#PyUnicode)

    Name of the existing file

  -  *newFileName* :[PyUnicode](README.md#PyUnicode)

    New name for the file

## [win32file](README.md#win32file).MoveFileWithProgress

 **MoveFileWithProgress( *ExistingFileName*  *, NewFileName*  *, ProgressRoutine*  *, Data*  *, Flags*  *, Transaction* ** )
Moves a file, and reports progress to a callback function

#### Parameters


  -  *ExistingFileName* :[PyUNICODE](README.md#PyUNICODE)

    File or directory to be moved

  -  *NewFileName* :[PyUNICODE](README.md#PyUNICODE)

    Destination, can be None if flags contain MOVEFILE_DELAY_UNTIL_REBOOT

  -  *ProgressRoutine=None* :[CopyProgressRoutine](README.md#CopyProgressRoutine)

    A python function that receives progress updates, can be None

  -  *Data=None* : object

    An arbitrary object to be passed to the callback function

  -  *Flags=0* : int

    Combination of MOVEFILE_* flags

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a transaction (optional).  See[win32transaction::CreateTransaction](win32transaction.md#win32transactionCreateTransaction).

#### Comments
Only available on Windows 2000 or later
Accepts keyword arguments.
On Vista and later, the Transaction arg can be passed to invoke MoveFileTransacted

## NOPARITY
 **const win32file.NOPARITY;** 


## ODDPARITY
 **const win32file.ODDPARITY;** 


## ONE5STOPBITS
 **const win32file.ONE5STOPBITS;** 


## ONESTOPBIT
 **const win32file.ONESTOPBIT;** 


## OPEN_ALWAYS
 **const win32file.OPEN_ALWAYS;** 
Opens the file, if it exists. If the file does not exist, the function creates the file as if dwCreationDistribution were CREATE_NEW.

## OPEN_EXISTING
 **const win32file.OPEN_EXISTING;** 
Opens the file. The function fails if the file does not exist.

## OVERWRITE_HIDDEN
 **const win32file.OVERWRITE_HIDDEN;** 


## ObjectIdType
 **const win32file.ObjectIdType;** 


## [win32file](README.md#win32file).OpenEncryptedFileRaw

PyCObject = **OpenEncryptedFileRaw( *FileName*  *, Flags* ** )
Initiates a backup or restore operation on an encrypted file

#### Parameters


  -  *FileName* :[PyUNICODE](README.md#PyUNICODE)

    Name of file on which to operate

  -  *Flags* : int

    CREATE_FOR_IMPORT, CREATE_FOR_DIR, OVERWRITE_HIDDEN, or 0 for export

#### Comments
Only available on Windows 2000 or later

#### Return Value
Returns a PyCObject containing an operation context that can be passed to[win32file::ReadEncryptedFileRaw](win32file.md#win32fileReadEncryptedFileRaw)or[win32file::WriteEncryptedFileRaw](win32file.md#win32fileWriteEncryptedFileRaw).  Context must be 

destroyed using[win32file::CloseEncryptedFileRaw](win32file.md#win32fileCloseEncryptedFileRaw).

## [win32file](README.md#win32file).OpenFileById

[PyHANDLE](README.md#PyHANDLE)= **OpenFileById( *File*  *, FileId*  *, DesiredAccess*  *, ShareMode*  *, Flags*  *, SecurityAttributes* ** )
Opens a file by File Id or Object Id

#### Parameters


  -  *File* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a file on the volume that contains the file to open

  -  *FileId* : int/[PyIID](README.md#PyIID)

    File Id or Object Id of the file to open

  -  *DesiredAccess* : int

    Access mode

  -  *ShareMode* : int

    Sharing mode (FILE_SHARE_*)

  -  *Flags* : int

    Combination of FILE_FLAG_* flags

  -  *SecurityAttributes=None* :[PySECURITY_ATTRIBUTES](PySECURITY.md#PySECURITYATTRIBUTES)

    Reserved, use only None

#### Comments
Available on Vista and later.
Accepts keyword args.

## PROGRESS_CANCEL
 **const win32file.PROGRESS_CANCEL;** 


## PROGRESS_CONTINUE
 **const win32file.PROGRESS_CONTINUE;** 


## PROGRESS_QUIET
 **const win32file.PROGRESS_QUIET;** 


## PROGRESS_STOP
 **const win32file.PROGRESS_STOP;** 


## PURGE_RXABORT
 **const win32file.PURGE_RXABORT;** 
Terminates all outstanding overlapped read operations and returns immediately, even if the read operations have not been completed.

## PURGE_RXCLEAR
 **const win32file.PURGE_RXCLEAR;** 
Clears the input buffer (if the device driver has one).

## PURGE_TXABORT
 **const win32file.PURGE_TXABORT;** 
Terminates all outstanding overlapped write operations and returns immediately, even if the write operations have not been completed.

## PURGE_TXCLEAR
 **const win32file.PURGE_TXCLEAR;** 
Clears the output buffer (if the device driver has one).

## [win32file](README.md#win32file).PostQueuedCompletionStatus

None = **PostQueuedCompletionStatus( *handle*  *, numberOfbytes*  *, completionKey*  *, overlapped* ** )
lets you post an I/O completion packet to an I/O completion port. The I/O completion packet will satisfy an outstanding call to the GetQueuedCompletionStatus function.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    handle to an I/O completion port

  -  *numberOfbytes=0* : int

    value to return via GetQueuedCompletionStatus' first result

  -  *completionKey=0* : int

    value to return via GetQueuedCompletionStatus' second result

  -  *overlapped=None* :[PyOVERLAPPED](README.md#PyOVERLAPPED)

    value to return via GetQueuedCompletionStatus' third result

#### Comments
Note that if you post overlapped objects, but your post is closed 

before all pending requests are processed, the overlapped objects 

(including its 'handle' and 'object' members) will leak. 

See MS KB article Q192800 for a summary of this.

## [win32file](README.md#win32file).PurgeComm

 **PurgeComm( *handle*  *, action* ** )
Discards all characters from the output or input buffer of a specified communications resource. It can also terminate pending read or write operations on the resource.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the communications device.

  -  *action* : int

    The action to perform.  This parameter can be one or more of the following values.


## [win32file](README.md#win32file).QueryDosDevice

string = **QueryDosDevice( *DeviceName* ** )
Returns the mapping for a device name, or all device names

#### Parameters


  -  *DeviceName* : string

    Name of device to query, or None to return all defined devices

#### Return Value
Returns a string containing substrings separated by NULLs with 2 terminating NULLs

## [win32file](README.md#win32file).QueryRecoveryAgentsOnEncryptedFile

([PySID](README.md#PySID),string,unicode) = **QueryRecoveryAgentsOnEncryptedFile( *FileName* ** )
Lists recovery agents for file as a tuple of tuples.

#### Parameters


  -  *FileName* : string/unicode

    file to query

#### Return Value
The result is a tuple of tuples - ((SID, certificate hash blob, display info),....)

## [win32file](README.md#win32file).QueryUsersOnEncryptedFile

([PySID](README.md#PySID),string,unicode) = **QueryUsersOnEncryptedFile( *FileName* ** )
Returns list of users for an encrypted file as tuples of (SID, certificate hash blob, display info)

#### Parameters


  -  *FileName* : string/unicode

    file to query

## REPLACEFILE_IGNORE_MERGE_ERRORS
 **const win32file.REPLACEFILE_IGNORE_MERGE_ERRORS;** 


## REPLACEFILE_WRITE_THROUGH
 **const win32file.REPLACEFILE_WRITE_THROUGH;** 


## RTS_CONTROL_DISABLE
 **const win32file.RTS_CONTROL_DISABLE;** 
Disables the RTS line when the device is opened and leaves it disabled.

## RTS_CONTROL_ENABLE
 **const win32file.RTS_CONTROL_ENABLE;** 
Enables the RTS line when the device is opened and leaves it on.

## RTS_CONTROL_HANDSHAKE
 **const win32file.RTS_CONTROL_HANDSHAKE;** 
Enables RTS handshaking. The driver raises the RTS line when the "type-ahead" (input) buffer is less than one-half full and lowers the RTS line when the buffer is more than three-quarters full. If handshaking is enabled, it is an error for the application to adjust the line by using the EscapeCommFunction function.

## RTS_CONTROL_TOGGLE
 **const win32file.RTS_CONTROL_TOGGLE;** 
Specifies that the RTS line will be high if bytes are available for transmission. After all buffered bytes have been sent, the RTS line will be low.

## [win32file](README.md#win32file).ReOpenFile

[PyHANDLE](README.md#PyHANDLE)= **ReOpenFile( *OriginalFile*  *, DesiredAccess*  *, ShareMode*  *, Flags* ** )
Creates a new handle to an open file

#### Parameters


  -  *OriginalFile* :[PyHANDLE](README.md#PyHANDLE)

    An open file handle

  -  *DesiredAccess* : int

    Access mode, cannot conflict with original access mode

  -  *ShareMode* : int

    Sharing mode (FILE_SHARE_*), cannot conflict with original share mode

  -  *Flags* : int

    Combination of FILE_FLAG_* flags

#### Comments
Available on Vista and later.
Accepts keyword args.

## [win32file](README.md#win32file).ReadDirectoryChangesW

 **ReadDirectoryChangesW( *handle*  *, size*  *, bWatchSubtree*  *, dwNotifyFilter*  *, overlapped* ** )
retrieves information describing the changes occurring within a directory.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    Handle to the directory to be monitored. This directory must be opened with the FILE_LIST_DIRECTORY access right.

  -  *size* : int

    Size of the buffer to allocate for the results.

  -  *bWatchSubtree* : int

    Specifies whether the ReadDirectoryChangesW function will monitor the directory or the directory tree. If TRUE is specified, the function monitors the directory tree rooted at the specified directory. If FALSE is specified, the function monitors only the directory specified by the hDirectory parameter.

  -  *dwNotifyFilter* : int

    Specifies filter criteria the function checks to determine if the wait operation has completed. This parameter can be one or more of the FILE_NOTIFY_CHANGE_* values.

  -  *overlapped=None* :[PyOVERLAPPED](README.md#PyOVERLAPPED)

    An overlapped object.  The directory must also be opened with FILE_FLAG_OVERLAPPED.

#### Comments
If you pass an overlapped object, you almost certainly 

must pass a buffer object for the asynchronous results - failure 

to do so may crash Python as the asynchronous result writes to 

invalid memory.
The FILE_NOTIFY_INFORMATION structure used by this function 

is variable length, depending on the length of the filename. 

The size of the buffer must be at least 6 bytes long + the length 

of the filenames returned.  The number of notifications that can be 

returned for a given buffer size depends on the filename lengths.

#### Return Value
If a buffer size is passed, the result is a list of (action, filename)
If a buffer is passed, the result is None - you must use the overlapped 

object to determine when the information is available and how much is valid. 

The buffer can then be passed to[win32file::FILE_NOTIFY_INFORMATION](win32file.md#win32fileFILE_NOTIFY_INFORMATION)

## [win32file](README.md#win32file).ReadEncryptedFileRaw

 **ReadEncryptedFileRaw( *ExportCallback*  *, CallbackContext*  *, Context* ** )
Reads the encrypted bytes of a file for backup and restore purposes

#### Parameters


  -  *ExportCallback* :[ExportCallBack](README.md#ExportCallBack)

    Python function that receives chunks of data as it is read

  -  *CallbackContext* : object

    Arbitrary Python object to be passed to callback function

  -  *Context* : PyCObject

    Context object returned from[win32file::OpenEncryptedFileRaw](win32file.md#win32fileOpenEncryptedFileRaw)

#### Comments
Only available on Windows 2000 or later

## [win32file](README.md#win32file).ReadFile

(int, string) = **ReadFile( *hFile*  *, buffer/bufSize*  *, overlapped* ** )
Reads a string from a file

#### Parameters


  -  *hFile* :[PyHANDLE](README.md#PyHANDLE)/int

    Handle to the file

  -  *buffer/bufSize* :[PyOVERLAPPEDReadBuffer](README.md#PyOVERLAPPEDReadBuffer)/int

    Size of the buffer to create for the result, 

or a buffer to fill with the result. If a buffer object and overlapped is passed, the result is 

the buffer itself.  If a buffer but no overlapped is passed, the result is a new string object, 

built from the buffer, but with a length that reflects the data actually read.

  -  *overlapped=None* :[PyOVERLAPPED](README.md#PyOVERLAPPED)

    An overlapped structure

#### Comments
in a multi-threaded overlapped environment, it is likely to be necessary to pre-allocate the read buffer using the[win32file::AllocateReadBuffer](win32file.md#win32fileAllocateReadBuffer)method, otherwise the I/O operation may complete before you can assign to the resulting buffer.

#### Return Value
The result is a tuple of (hr, string/[PyOVERLAPPEDReadBuffer](README.md#PyOVERLAPPEDReadBuffer)), where hr may be 

0, ERROR_MORE_DATA or ERROR_IO_PENDING. 

If the overlapped param is not None, then the result is a[PyOVERLAPPEDReadBuffer](README.md#PyOVERLAPPEDReadBuffer).  Once the overlapped IO operation 

has completed, you can convert this to a string (str(object)) [py2k] or (bytes(object)) [py3k] to obtain the data. 

While the operation is in progress, you can use the slice operations (object[:end]) to 

obtain the data read so far. 

You must use the OVERLAPPED API functions to determine how much of the data is valid.

## [win32file](README.md#win32file).RemoveDirectory

 **RemoveDirectory( *PathName*  *, Transaction* ** )
Removes an existing directory

#### Parameters


  -  *PathName* :[PyUnicode](README.md#PyUnicode)

    Name of directory to be removed

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a transaction (optional). See[win32transaction::CreateTransaction](win32transaction.md#win32transactionCreateTransaction).

#### Comments
If a transaction handle is passed in, RemoveDirectoryTransacted will be called (requires Vista or later)
Accepts keyword arguments.  Implemented only as Unicode.

#### Win32 API References


  - Search for *RemoveDirectory* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RemoveDirectory),[google](README.md#http://www.google.com/search?q=RemoveDirectory)or[google groups](README.md#http://groups.google.com/groups?q=RemoveDirectory).

  - Search for *RemoveDirectoryTransacted* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RemoveDirectoryTransacted),[google](README.md#http://www.google.com/search?q=RemoveDirectoryTransacted)or[google groups](README.md#http://groups.google.com/groups?q=RemoveDirectoryTransacted).

## [win32file](README.md#win32file).RemoveUsersFromEncryptedFile

 **RemoveUsersFromEncryptedFile( *FileName*  *, pHashes* ** )
Removes specified certificates from file - if certificate is not found, it is ignored

#### Parameters


  -  *FileName* : string/unicode

    File from which to remove users

  -  *pHashes* : (([PySID](README.md#PySID),string,unicode),...)

    Sequence representing an ENCRYPTION_CERTIFICATE_HASH_LIST structure, as returned by QueryUsersOnEncryptedFile

## [win32file](README.md#win32file).ReplaceFile

 **ReplaceFile( *ReplacedFileName*  *, ReplacementFileName*  *, BackupFileName*  *, ReplaceFlags*  *, Exclude*  *, Reserved* ** )
Replaces one file with another

#### Parameters


  -  *ReplacedFileName* :[PyUNICODE](README.md#PyUNICODE)

    File to be replaced

  -  *ReplacementFileName* :[PyUNICODE](README.md#PyUNICODE)

    File that will replace it

  -  *BackupFileName=None* :[PyUNICODE](README.md#PyUNICODE)

    Place at which to create a backup of the replaced file, can be None

  -  *ReplaceFlags=0* : int

    Combination of REPLACEFILE_* flags

  -  *Exclude=None* : None

    Reserved, use None if passed in

  -  *Reserved=None* : None

    Reserved, use None if passed in

#### Comments
Only available on Windows 2000 or later

## SCS_32BIT_BINARY
 **const win32file.SCS_32BIT_BINARY;** 
A Win32-based application

## SCS_DOS_BINARY
 **const win32file.SCS_DOS_BINARY;** 
An MS-DOS - based application

## SCS_OS216_BINARY
 **const win32file.SCS_OS216_BINARY;** 
A 16-bit OS/2-based application

## SCS_PIF_BINARY
 **const win32file.SCS_PIF_BINARY;** 
A PIF file that executes an MS-DOS - based application

## SCS_POSIX_BINARY
 **const win32file.SCS_POSIX_BINARY;** 
A POSIX - based application

## SCS_WOW_BINARY
 **const win32file.SCS_WOW_BINARY;** 
A 16-bit Windows-based application

## SECURITY_ANONYMOUS
 **const win32file.SECURITY_ANONYMOUS;** 
Specifies to impersonate the client at the Anonymous impersonation level.

## SECURITY_CONTEXT_TRACKING
 **const win32file.SECURITY_CONTEXT_TRACKING;** 
Specifies that the security tracking mode is dynamic. If this flag is not specified, Security Tracking Mode is static.

## SECURITY_DELEGATION
 **const win32file.SECURITY_DELEGATION;** 
Specifies to impersonate the client at the Delegation impersonation level.

## SECURITY_EFFECTIVE_ONLY
 **const win32file.SECURITY_EFFECTIVE_ONLY;** 
Specifies that only the enabled aspects

## SECURITY_IDENTIFICATION
 **const win32file.SECURITY_IDENTIFICATION;** 
Specifies to impersonate the client at the Identification impersonation level.

## SECURITY_IMPERSONATION
 **const win32file.SECURITY_IMPERSONATION;** 
Specifies to impersonate the client at the Impersonation impersonation level.

## SETBREAK
 **const win32file.SETBREAK;** 
Suspends character transmission and places the transmission line in a break state until the ClearCommBreak function is called (or EscapeCommFunction is called with the CLRBREAK extended function code). The SETBREAK extended function code is identical to the SetCommBreak function. Note that this extended function does not flush data that has not been transmitted.

## SETDTR
 **const win32file.SETDTR;** 
Sends the DTR (data-terminal-ready) signal.

## SETRTS
 **const win32file.SETRTS;** 
Sends the RTS (request-to-send) signal.

## SETXOFF
 **const win32file.SETXOFF;** 
Causes transmission to act as if an XOFF character has been received.

## SETXON
 **const win32file.SETXON;** 
Causes transmission to act as if an XON character has been received.

## SO_CONNECT_TIME
 **const win32file.SO_CONNECT_TIME;** 


## SO_UPDATE_ACCEPT_CONTEXT
 **const win32file.SO_UPDATE_ACCEPT_CONTEXT;** 


## SO_UPDATE_CONNECT_CONTEXT
 **const win32file.SO_UPDATE_CONNECT_CONTEXT;** 


## SPACEPARITY
 **const win32file.SPACEPARITY;** 


## SYMBOLIC_LINK_FLAG_DIRECTORY
 **const win32file.SYMBOLIC_LINK_FLAG_DIRECTORY;** 


## [win32file](README.md#win32file).SetCommBreak

 **SetCommBreak( *handle* ** )
Suspends character transmission for a specified communications device and places the transmission line in a break state until the[win32file::ClearCommBreak](win32file.md#win32fileClearCommBreak)function is called.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the communications device.

## [win32file](README.md#win32file).SetCommMask

int = **SetCommMask( *handle*  *, val* ** )
Sets the value of the event mask for a specified communications device.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the communications device.

  -  *val* : int

    The new mask value.

## [win32file](README.md#win32file).SetCommState

 **SetCommState( *handle*  *, dcb* ** )
Configures a communications device according to the specifications in a device-control block. 

The function reinitializes all hardware and control settings, but it does not empty output or input queues.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the communications device.

  -  *dcb* :[PyDCB](README.md#PyDCB)

    The control settings.

## [win32file](README.md#win32file).SetCommTimeouts

int = **SetCommTimeouts( *handle*  *, val* ** )
Sets the time-out parameters for all read and write operations on a specified communications device.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the communications device.

  -  *val* : **PyCOMMTIMEOUTS** 

    The new time-out parameters.

## [win32file](README.md#win32file).SetCurrentDirectory

 **SetCurrentDirectory( *lpPathName* ** )
Sets the current directory.

#### Parameters


  -  *lpPathName* : str/[PyUnicode](README.md#PyUnicode)

    Name of the path to set current.

## [win32file](README.md#win32file).SetEndOfFile

 **SetEndOfFile( *hFile* ** )
Moves the end-of-file (EOF) position for the specified file to the current position of the file pointer.

#### Parameters


  -  *hFile* :[PyHANDLE](README.md#PyHANDLE)

    handle of file whose EOF is to be set

## [win32file](README.md#win32file).SetFileApisToANSI

 **SetFileApisToANSI(** )
Causes a set of Win32 file functions to use the ANSI character set code page. This function is useful for 8-bit console input and output operations.

## [win32file](README.md#win32file).SetFileApisToOEM

 **SetFileApisToOEM(** )
Causes a set of Win32 file functions to use the OEM character set code page. This function is useful for 8-bit console input and output operations.

## [win32file](README.md#win32file).SetFileAttributes

 **SetFileAttributes( *filename*  *, newAttributes* ** )
Changes a file's attributes.

#### Parameters


  -  *filename* :[PyUnicode](README.md#PyUnicode)

    filename

  -  *newAttributes* : int

    attributes to set

## [win32file](README.md#win32file).SetFileAttributesW

 **SetFileAttributesW( *FileName*  *, FileAttributes*  *, Transaction* ** )
Sets a file's attributes

#### Parameters


  -  *FileName* :[PyUNICODE](README.md#PyUNICODE)

    File or directory whose attributes are to be changed

  -  *FileAttributes* : int

    Combination of FILE_ATTRIBUTE_* flags

  -  *Transaction=None* :[PyHANDLE](README.md#PyHANDLE)

    Handle to the transaction.  See[win32transaction::CreateTransaction](win32transaction.md#win32transactionCreateTransaction).

#### Comments
If Transaction is not None, SetFileAttributesTransacted will be called (requires Vista or later)
Accepts keyword arguments.

#### Win32 API References


  - Search for *SetFileAttributes* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetFileAttributes),[google](README.md#http://www.google.com/search?q=SetFileAttributes)or[google groups](README.md#http://groups.google.com/groups?q=SetFileAttributes).

  - Search for *SetFileAttributesTransacted* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetFileAttributesTransacted),[google](README.md#http://www.google.com/search?q=SetFileAttributesTransacted)or[google groups](README.md#http://groups.google.com/groups?q=SetFileAttributesTransacted).

## [win32file](README.md#win32file).SetFileInformationByHandle

 **SetFileInformationByHandle( *File*  *, FileInformationClass*  *, Information* ** )
Changes file characteristics by file handle

#### Parameters


  -  *File* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a file or directory.  Do not pass a pipe handle.

  -  *FileInformationClass* : int

    Type of data, one of win32file.File*Info values

  -  *Information* : object

    Type is dependent on the class to be changed

 **Class**  **Type of input** FileBasicInfoDict representing a FILE_BASIC_INFO struct, containing 

{"CreationTime":[PyTime](README.md#PyTime), "LastAccessTime":[PyTime](README.md#PyTime),  "LastWriteTime":[PyTime](README.md#PyTime), 

"ChangeTime":[PyTime](README.md#PyTime), "FileAttributes":int}FileRenameInfoDict representing a FILE_RENAME_INFO struct, containing 

{"ReplaceIfExists":boolean, "RootDirectory":[PyHANDLE](README.md#PyHANDLE), "FileName":str} 

MSDN says the RootDirectory is "A handle to the root directory in which the file to be renamed is located". 

However, this is actually the destination dir, can be None to stay in same dir.FileDispositionInfoBoolean indicating if file should be deleted when handle is closedFileAllocationInfoInt giving the allocation size.FileEndOfFileInfoInt giving the EOF position, cannot be greater than allocated size.FileIoPriorityHintInfoInt containing the IO priority (IoPriorityHint*)
#### Comments
Available on Vista and later.
Accepts keyword args.

## [win32file](README.md#win32file).SetFilePointer

 **SetFilePointer( *handle*  *, offset*  *, moveMethod* ** )
Moves the file pointer of an open file.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The file to perform the operation on.

  -  *offset* : **Py_LARGEINTEGER** 

    Offset to move the file pointer.

  -  *moveMethod* : int

    Starting point for the file pointer move. This parameter can be one of the following values.


## [win32file](README.md#win32file).SetFileShortName

 **SetFileShortName( *hFile*  *, ShortName* ** )
Set the 8.3 name of a file

#### Parameters


  -  *hFile* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a file or directory

  -  *ShortName* :[PyUNICODE](README.md#PyUNICODE)

    The 8.3 name to be applied to the file

#### Comments
This function is only available on WinXP and later
File handle must be opened with FILE_FLAG_BACKUP_SEMANTICS, and SE_RESTORE_NAME privilege must be enabled

## [win32file](README.md#win32file).SetFileTime

 **SetFileTime( *File*  *, CreationTime*  *, LastAccessTime*  *, LastWriteTime*  *, UTCTimes* ** )
Sets the date and time that a file was created, last accessed, or last modified.

#### Parameters


  -  *File* :[PyHANDLE](README.md#PyHANDLE)

    Previously opened handle (opened with FILE_WRITE_ATTRIBUTES access).

  -  *CreationTime=None* :[PyTime](README.md#PyTime)

    File created time. None for no change.

  -  *LastAccessTime=None* :[PyTime](README.md#PyTime)

    File access time. None for no change.

  -  *LastWriteTime=None* :[PyTime](README.md#PyTime)

    File written time. None for no change.

  -  *UTCTimes=False* : boolean

    If True, input times are treated as UTC and no conversion is done, 

otherwise they are treated as local times.  Defaults to False for backward compatibility.

## [win32file](README.md#win32file).SetMailslotInfo

 **SetMailslotInfo( *Mailslot*  *, ReadTimeout* ** )
Sets a mailslot's timeout

#### Parameters


  -  *Mailslot* :[PyHANDLE](README.md#PyHANDLE)

    Handle to a mailslot

  -  *ReadTimeout* : int

    Timeout in milliseconds, use -1 for no timeout

#### Win32 API References


  - Search for *SetMailslotInfo* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetMailslotInfo),[google](README.md#http://www.google.com/search?q=SetMailslotInfo)or[google groups](README.md#http://groups.google.com/groups?q=SetMailslotInfo).

## [win32file](README.md#win32file).SetVolumeLabel

 **SetVolumeLabel( *rootPathName*  *, volumeName* ** )
Sets a volume label for a disk drive.

#### Parameters


  -  *rootPathName* :[PyUnicode](README.md#PyUnicode)

    address of name of root directory for volume

  -  *volumeName* :[PyUnicode](README.md#PyUnicode)

    name for the volume

## [win32file](README.md#win32file).SetVolumeMountPoint

[PyUnicode](README.md#PyUnicode)= **SetVolumeMountPoint( *VolumeMountPoint*  *, VolumeName* ** )
Mounts the specified volume at the specified volume mount point.

#### Parameters


  -  *VolumeMountPoint* :[PyUnicode](README.md#PyUnicode)

    The mount point - must be an existing empty directory on an NTFS volume

  -  *VolumeName* :[PyUnicode](README.md#PyUnicode)

    The volume to&#09mount there

#### Comments
Accepts keyword args.
Note that both&#09parameters must&#09have trailing backslashes.
This method exists only on Windows 2000 or later.  On earlier platforms, NotImplementedError will be raised.

#### Example
Usage
SetVolumeMountPoint('h:\\tmp\\','c:\\')
#### Return Value
The result is&#09the&#09GUID of&#09the&#09volume mounted,&#09as a string.

## [win32file](README.md#win32file).SetupComm

 **SetupComm( *handle*  *, dwInQueue*  *, dwOutQueue* ** )
Initializes the communications parameters for a specified communications device.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the communications device.

  -  *dwInQueue* : int

    Specifies the recommended size, in bytes, of the device's internal input buffer.

  -  *dwOutQueue* : int

    Specifies the recommended size, in bytes, of the device's internal output buffer.

## [win32file](README.md#win32file).SfcGetNextProtectedFile

[[PyUnicode](README.md#PyUnicode),...] = **SfcGetNextProtectedFile(** )
Returns list of protected operating system files

#### Win32 API References


  - Search for *SfcGetNextProtectedFile* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SfcGetNextProtectedFile),[google](README.md#http://www.google.com/search?q=SfcGetNextProtectedFile)or[google groups](README.md#http://groups.google.com/groups?q=SfcGetNextProtectedFile).

## [win32file](README.md#win32file).SfcIsFileProtected

boolean = **SfcIsFileProtected( *ProtFileName* ** )
Checks if a file is protected

#### Parameters


  -  *ProtFileName* :[PyUnicode](README.md#PyUnicode)

    Name of file to be checked

## TF_DISCONNECT
 **const win32file.TF_DISCONNECT;** 


## TF_REUSE_SOCKET
 **const win32file.TF_REUSE_SOCKET;** 


## TF_USE_DEFAULT_WORKER
 **const win32file.TF_USE_DEFAULT_WORKER;** 


## TF_USE_KERNEL_APC
 **const win32file.TF_USE_KERNEL_APC;** 


## TF_USE_SYSTEM_THREAD
 **const win32file.TF_USE_SYSTEM_THREAD;** 


## TF_WRITE_BEHIND
 **const win32file.TF_WRITE_BEHIND;** 


## TRUNCATE_EXISTING
 **const win32file.TRUNCATE_EXISTING;** 
Opens the file. Once opened, the file is truncated so that its size is zero bytes. The calling process must open the file with at least GENERIC_WRITE access. The function fails if the file does not exist.

## TWOSTOPBITS
 **const win32file.TWOSTOPBITS;** 


## [win32file](README.md#win32file).TransmitCommChar

 **TransmitCommChar( *handle*  *, cChar* ** )
Transmits a specified character ahead of any pending data in the output buffer of the specified communications device.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the communications device.

  -  *cChar* : char

    The character to transmit.

#### Comments
The TransmitCommChar function is useful for sending an interrupt character (such as a CTRL+C) to a host system.
If the device is not transmitting, TransmitCommChar cannot be called repeatedly. Once TransmitCommChar places a character in the output buffer, the character must be transmitted before the function can be called again. If the previous character has not yet been sent, TransmitCommChar returns an error.

## [win32file](README.md#win32file).TransmitFile

 **TransmitFile( *Socket*  *, File*  *, NumberOfBytesToWrite*  *, NumberOfBytesPerSend*  *, Overlapped*  *, Flags*  *, Head*  *, Tail* ** )
Transmits a file over a socket 

TransmitFile(sock, filehandle, bytes_to_write, bytes_per_send, overlap, flags [, (prepend_buf, postpend_buf)])

#### Parameters


  -  *Socket* : **PySocket** /int

    Socket that will be used to send the file

  -  *File* :[PyHANDLE](README.md#PyHANDLE)/int

    Handle to the file

  -  *NumberOfBytesToWrite* : int

    The number of bytes in the file to transmit, use 0 for entire file.

  -  *NumberOfBytesPerSend* : int

    The size, in bytes, of each block of data sent in each send operation.

  -  *Overlapped* :[PyOVERLAPPED](README.md#PyOVERLAPPED)

    An overlapped structure, can be None.

  -  *Flags* : int

    A set of flags used to modify the behavior of the TransmitFile function call. (win32file.TF_*)

  -  *Head=None* : buffer

    Buffer to send on the socket before the file

  -  *Tail=None* : buffer

    Buffer to send on the socket after the file

#### Return Value
Returns 0 on completion, or ERROR_IO_PENDING if an overlapped operation has been queued

## [win32file](README.md#win32file).UnlockFile

 **UnlockFile( *hFile*  *, offsetLow*  *, offsetHigh*  *, nNumberOfBytesToUnlockLow*  *, nNumberOfBytesToUnlockHigh* ** )
Unlocks a region of a file locked by[win32file::LockFile](win32file.md#win32fileLockFile)or[win32file::LockFileEx](win32file.md#win32fileLockFileEx)

#### Parameters


  -  *hFile* :[PyHANDLE](README.md#PyHANDLE)

    handle of file to unlock

  -  *offsetLow* : int

    low-order word of lock region offset

  -  *offsetHigh* : int

    high-order word of lock region offset

  -  *nNumberOfBytesToUnlockLow* : int

    low-order word of length to unlock

  -  *nNumberOfBytesToUnlockHigh* : int

    high-order word of length to unlock

## [win32file](README.md#win32file).UnlockFileEx

 **UnlockFileEx( *hFile*  *, int*  *, int*  *, ol* ** )
Unlocks a file. Wrapper for UnlockFileEx win32 API.

#### Parameters


  -  *hFile* :[PyHANDLE](README.md#PyHANDLE)/int

    Handle to the file

  -  *int* : nbytesLow

    low-order part of number of 

bytes to lock

  -  *int* : nbytesLow

    high-order part of number of 

bytes to lock

  -  *ol=None* :[PyOVERLAPPED](README.md#PyOVERLAPPED)

    An overlapped structure

## [win32file](README.md#win32file).WSAAsyncSelect

 **WSAAsyncSelect( *socket*  *, hwnd*  *, int*  *, networkEvents* ** )
Request windows message notification for the supplied set of FD_XXXX network events.

#### Parameters


  -  *socket* : **PySocket** 

    socket to attach to the event

  -  *hwnd* : **hwnd** 

    Window handle for the socket to become attached to.

  -  *int* : **int** 

    Window message that will be posted.

  -  *networkEvents* : int

    A bitmask of network events that will cause wMsg to be posted. e.g. (FD_CLOSE | FD_READ)

## WSAECONNABORTED
 **const win32file.WSAECONNABORTED;** 


## WSAECONNRESET
 **const win32file.WSAECONNRESET;** 


## WSAEDISCON
 **const win32file.WSAEDISCON;** 


## WSAEFAULT
 **const win32file.WSAEFAULT;** 


## WSAEINPROGRESS
 **const win32file.WSAEINPROGRESS;** 


## WSAEINTR
 **const win32file.WSAEINTR;** 


## WSAEINVAL
 **const win32file.WSAEINVAL;** 


## WSAEMSGSIZE
 **const win32file.WSAEMSGSIZE;** 


## WSAENETDOWN
 **const win32file.WSAENETDOWN;** 


## WSAENETRESET
 **const win32file.WSAENETRESET;** 


## WSAENOBUFS
 **const win32file.WSAENOBUFS;** 


## WSAENOTCONN
 **const win32file.WSAENOTCONN;** 


## WSAENOTSOCK
 **const win32file.WSAENOTSOCK;** 


## WSAEOPNOTSUPP
 **const win32file.WSAEOPNOTSUPP;** 


## WSAESHUTDOWN
 **const win32file.WSAESHUTDOWN;** 


## WSAEWOULDBLOCK
 **const win32file.WSAEWOULDBLOCK;** 


## [win32file](README.md#win32file).WSAEnumNetworkEvents

dict = **WSAEnumNetworkEvents( *s*  *, hEvent* ** )
Return network events that caused the event associated with the socket to be signaled.

#### Parameters


  -  *s* : **PySocket** 

    Socket to check for netork events, previously registered for network event notification with WSAEventSelect.

  -  *hEvent* :[PyHANDLE](README.md#PyHANDLE)

    Optional handle to the event associated with socket s in the last call to WSAEventSelect. If specified, the event will be reset.

#### Return Value
A dictionary mapping network events that occured for the specified socket since the last call to this function (e.g. FD_READ, FD_WRITE) to their associated error code, or 0 if the event occured without an error. The events returned are a subset of events previously registered for this socket with WSAEventSelect.

## [win32file](README.md#win32file).WSAEventSelect

 **WSAEventSelect( *socket*  *, hEvent*  *, networkEvents* ** )
Specifies an event object to be associated with the supplied set of FD_XXXX network events.

#### Parameters


  -  *socket* : **PySocket** 

    socket to attach to the event

  -  *hEvent* :[PyHandle](README.md#PyHandle)

    Event handle for the socket to become attached to.

  -  *networkEvents* : int

    A bitmask of network events that will cause hEvent to be signaled. e.g. (FD_CLOSE | FD_READ)

## [win32file](README.md#win32file).WSARecv

(rc, cBytesRecvd) = **WSARecv( *s*  *, buffer*  *, ol*  *, dwFlags* ** )
Winsock recv() equivalent function for Overlapped I/O.

#### Parameters


  -  *s* : **PySocket** /int

    Socket to send data on.

  -  *buffer* : **buffer** 

    Buffer to send data from.

  -  *ol* :[PyOVERLAPPED](README.md#PyOVERLAPPED)

    An overlapped structure

  -  *dwFlags* : int

    Optional reception flags.

## [win32file](README.md#win32file).WSASend

(rc, cBytesSent) = **WSASend( *s*  *, buffer*  *, ol*  *, dwFlags* ** )
Winsock send() equivalent function for Overlapped I/O.

#### Parameters


  -  *s* : **PySocket** /int

    Socket to send data on.

  -  *buffer* : string/ **buffer** 

    Buffer to send data from.

  -  *ol* :[PyOVERLAPPED](README.md#PyOVERLAPPED)

    An overlapped structure

  -  *dwFlags* : int

    Optional send flags.

## WSA_IO_PENDING
 **const win32file.WSA_IO_PENDING;** 


## WSA_OPERATION_ABORTED
 **const win32file.WSA_OPERATION_ABORTED;** 


## [win32file](README.md#win32file).WaitCommEvent

 **WaitCommEvent( *handle*  *, overlapped* ** )
Waits for an event to occur for a specified communications device. The set of events that are monitored by this function is contained in the event mask associated with the device handle.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#PyHANDLE)

    The handle to the communications device.

  -  *overlapped* :[PyOVERLAPPED](README.md#PyOVERLAPPED)

    This structure is required if hFile was opened with FILE_FLAG_OVERLAPPED.
If hFile was opened with FILE_FLAG_OVERLAPPED, the lpOverlapped parameter must not be NULL. It must point to a valid OVERLAPPED structure. If hFile was opened with FILE_FLAG_OVERLAPPED and lpOverlapped is NULL, the function can incorrectly report that the operation is complete.
If hFile was opened with FILE_FLAG_OVERLAPPED and lpOverlapped is not NULL, WaitCommEvent is performed as an overlapped operation. In this case, the OVERLAPPED structure must contain a handle to a manual-reset event object (created by using the CreateEvent function).
If hFile was not opened with FILE_FLAG_OVERLAPPED, WaitCommEvent does not return until one of the specified events or an error occurs.

#### Comments
If an overlapped structure is passed, then the **PyOVERLAPPED::dword** address is passed to the Win32 API as the mask.  This means that once the 

overlapped operation has completed, this dword attribute can be used to 

determine the type of event that occurred.

#### Return Value
The result is a tuple of (rc, mask_val), where rc is zero for success, or 

the result of calling GetLastError() otherwise.  The mask_val is the new mask value 

once the function has returned, but if an Overlapped object is passed, this value 

will generally be meaningless.  See the comments for more details.

## [win32file](README.md#win32file).Wow64DisableWow64FsRedirection

int = **Wow64DisableWow64FsRedirection(** )
Disables file system redirection for 32-bit processes running on a 64-bit system

#### Comments
Requires 64-bit XP or later

#### Return Value
Returns a state value to be passed to[win32file::Wow64RevertWow64FsRedirection](win32file.md#win32fileWow64RevertWow64FsRedirection)

## [win32file](README.md#win32file).Wow64RevertWow64FsRedirection

 **Wow64RevertWow64FsRedirection( *OldValue* ** )
Reenables file system redirection for 32-bit processes running on a 64-bit system

#### Parameters


  -  *OldValue* : int

    State returned from Wow64DisableWow64FsRedirection

#### Comments
Requires 64-bit XP or later

## [win32file](README.md#win32file).WriteEncryptedFileRaw

 **WriteEncryptedFileRaw( *ImportCallback*  *, CallbackContext*  *, Context* ** )
Writes raw bytes to an encrypted file

#### Parameters


  -  *ImportCallback* :[ImportCallBack](README.md#ImportCallBack)

    Python function that supplies data to be written

  -  *CallbackContext* : object

    Arbitrary Python object to be passed to callback function

  -  *Context* : PyCObject

    Context object returned from[win32file::OpenEncryptedFileRaw](win32file.md#win32fileOpenEncryptedFileRaw)

#### Comments
Only available on Windows 2000 or later

## [win32file](README.md#win32file).WriteFile

int, int = **WriteFile( *hFile*  *, data*  *, ol* ** )
Writes a string to a file

#### Parameters


  -  *hFile* :[PyHANDLE](README.md#PyHANDLE)/int

    Handle to the file

  -  *data* : string/[PyOVERLAPPEDReadBuffer](README.md#PyOVERLAPPEDReadBuffer)

    The data to write.

  -  *ol=None* :[PyOVERLAPPED](README.md#PyOVERLAPPED)

    An overlapped structure

#### Comments
If you use an overlapped buffer, then it is your responsibility 

to ensure the string object passed remains valid until the operation 

completes.  If Python garbage collection reclaims the buffer before the 

win32 API has finished with it, the results are unpredictable.

#### Return Value
The result is a tuple of (errCode, nBytesWritten).  If errCode is not zero, 

it will be ERROR_IO_PENDING (ie, it is an overlapped request).
Any other error will raise an exception.

## [win32file](README.md#win32file)._get_osfhandle

long = **_get_osfhandle( *fd* ** )
Gets operating-system file handle associated with existing stream

#### Parameters


  -  *fd* : int

    File descriptor as returned by file.fileno()

## [win32file](README.md#win32file)._getmaxstdio

int = **_getmaxstdio(** )
Returns the maximum number of CRT io streams.

## [win32file](README.md#win32file)._open_osfhandle

int = **_open_osfhandle( *osfhandle*  *, flags* ** )
Associates a C run-time file handle with a existing operating-system file handle.

#### Parameters


  -  *osfhandle* :[PyHANDLE](README.md#PyHANDLE)

    An open file handle

  -  *flags* : int

    O_APPEND,O_RDONLY, or O_TEXT

## [win32file](README.md#win32file)._setmaxstdio

int = **_setmaxstdio( *newmax* ** )
Set the maximum allowed number of open stdio handles

#### Parameters


  -  *newmax* : int

    Maximum number of open stdio streams, 2048 max

#### Return Value
Returns the number that was set, or -1 on failure.