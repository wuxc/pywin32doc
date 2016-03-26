# win32file

## Module win32file

An interface to the win32 File API's
This module includes the tranactional NTFS operations introduced with 

Vista.  The transacted functions are not wrapped separately, but are invoked by 

passing a transaction handle to the corresponding Unicode API function. 

This makes it simple to convert a set of file operations into a transaction by 

simply adding Transaction=[PyHANDLE](#pyhandle)to the passed arguments. 

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


  - [AreFileApisANSI](win32file.md#win32filearefileapisansi)

    Determines whether a set of Win32 file functions is using the ANSI or OEM character set code page. This function is useful for 8-bit console input and output operations.&nbsp;

  - [CancelIo](win32file.md#win32filecancelio)

    Cancels pending IO requests for the object.&nbsp;

  - [CopyFile](win32file.md#win32filecopyfile)

    Copies a file&nbsp;

  - [CopyFileW](win32file.md#win32filecopyfilew)

    Copies a file (NT/2000 Unicode specific version)&nbsp;

  - [CreateDirectory](win32file.md#win32filecreatedirectory)

    Creates a directory&nbsp;

  - [CreateDirectoryW](win32file.md#win32filecreatedirectoryw)

    Creates a directory (NT/2000 Unicode specific version)&nbsp;

  - [CreateDirectoryEx](win32file.md#win32filecreatedirectoryex)

    Creates a directory&nbsp;

  - [CreateFile](win32file.md#win32filecreatefile)

    Creates or opens the a file or other object and returns a handle that can be used to access the object.&nbsp;

  - [CreateIoCompletionPort](win32file.md#win32filecreateiocompletionport)

    Can associate an instance of an opened file with a newly created or an existing input/output (I/O) completion port; or it can create an I/O completion port without associating it with a file.&nbsp;

  - [CreateMailslot](win32file.md#win32filecreatemailslot)

    Creates a mailslot on the local machine&nbsp;

  - [GetMailslotInfo](win32file.md#win32filegetmailslotinfo)

    Retrieves information about a mailslot&nbsp;

  - [SetMailslotInfo](win32file.md#win32filesetmailslotinfo)

    Sets a mailslot's timeout&nbsp;

  - [DefineDosDevice](win32file.md#win32filedefinedosdevice)

    Lets an application define, redefine, or delete MS-DOS device names.&nbsp;

  - [DefineDosDeviceW](win32file.md#win32filedefinedosdevicew)

    Lets an application define, redefine, or delete MS-DOS device names. (NT/2000 Unicode specific version)&nbsp;

  - [DeleteFile](win32file.md#win32filedeletefile)

    Deletes a file.&nbsp;

  - [DeviceIoControl](win32file.md#win32filedeviceiocontrol)

    Sends a control code to a device or file system driver&nbsp;

  - [FindClose](win32file.md#win32filefindclose)

    Closes a find handle.&nbsp;

  - [FindCloseChangeNotification](win32file.md#win32filefindclosechangenotification)

    Closes a handle.&nbsp;

  - [FindFirstChangeNotification](win32file.md#win32filefindfirstchangenotification)

    Creates a change notification handle and sets up initial change notification filter conditions. A wait on a notification handle succeeds when a change matching the filter conditions occurs in the specified directory or subtree.&nbsp;

  - [FindNextChangeNotification](win32file.md#win32filefindnextchangenotification)

    Requests that the operating system signal a change notification handle the next time it detects an appropriate change,&nbsp;

  - [FlushFileBuffers](win32file.md#win32fileflushfilebuffers)

    Clears the buffers for the specified file and causes all buffered data to be written to the file.&nbsp;

  - [GetBinaryType](win32file.md#win32filegetbinarytype)

    Determines whether a file is executable, and if so, what type of executable file it is. That last property determines which subsystem an executable file runs under.&nbsp;

  - [GetDiskFreeSpace](win32file.md#win32filegetdiskfreespace)

    Determines the free space on a device.&nbsp;

  - [GetDiskFreeSpaceEx](win32file.md#win32filegetdiskfreespaceex)

    Determines the free space on a device.&nbsp;

  - [GetDriveType](win32file.md#win32filegetdrivetype)

    Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive.&nbsp;

  - [GetDriveTypeW](win32file.md#win32filegetdrivetypew)

    Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive. (NT/2000 Unicode specific version).&nbsp;

  - [GetFileAttributes](win32file.md#win32filegetfileattributes)

    Determines a files attributes.&nbsp;

  - [GetFileAttributesW](win32file.md#win32filegetfileattributesw)

    Determines a files attributes (NT/2000 Unicode specific version).&nbsp;

  - [GetFileTime](win32file.md#win32filegetfiletime)

    Returns a file's creation, last access, and modification times.&nbsp;

  - [SetFileTime](win32file.md#win32filesetfiletime)

    Sets the date and time that a file was created, last accessed, or last modified.&nbsp;

  - [GetFileInformationByHandle](win32file.md#win32filegetfileinformationbyhandle)

    Retrieves file information for a specified file.&nbsp;

  - [GetCompressedFileSize](win32file.md#win32filegetcompressedfilesize)

    Determines the compressed size of a file.&nbsp;

  - [GetFileSize](win32file.md#win32filegetfilesize)

    Determines the size of a file.&nbsp;

  - [AllocateReadBuffer](win32file.md#win32fileallocatereadbuffer)

    Allocates a buffer which can be used with an overlapped Read operation using[win32file::ReadFile](win32file.md#win32filereadfile)&nbsp;

  - [ReadFile](win32file.md#win32filereadfile)

    Reads a string from a file&nbsp;

  - [WriteFile](win32file.md#win32filewritefile)

    Writes a string to a file&nbsp;

  - [CloseHandle](win32file.md#win32fileclosehandle)

    Closes an open handle.&nbsp;

  - [LockFileEx](win32file.md#win32filelockfileex)

    Locks a file. Wrapper for LockFileEx win32 API.&nbsp;

  - [UnlockFileEx](win32file.md#win32fileunlockfileex)

    Unlocks a file. Wrapper for UnlockFileEx win32 API.&nbsp;

  - [GetQueuedCompletionStatus](win32file.md#win32filegetqueuedcompletionstatus)

    Attempts to dequeue an I/O completion packet from a specified input/output completion port.&nbsp;

  - [PostQueuedCompletionStatus](win32file.md#win32filepostqueuedcompletionstatus)

    lets you post an I/O completion packet to an I/O completion port. The I/O completion packet will satisfy an outstanding call to the GetQueuedCompletionStatus function.&nbsp;

  - [GetFileType](win32file.md#win32filegetfiletype)

    Determines the type of a file.&nbsp;

  - [GetLogicalDrives](win32file.md#win32filegetlogicaldrives)

    Returns a bitmaks of the logical drives installed.&nbsp;

  - [GetOverlappedResult](win32file.md#win32filegetoverlappedresult)

    Determines the result of the most recent call with an OVERLAPPED object.&nbsp;

  - [LockFile](win32file.md#win32filelockfile)

    Locks a specified file for exclusive access by the calling process.&nbsp;

  - [MoveFile](win32file.md#win32filemovefile)

    Renames an existing file or a directory (including all its children).&nbsp;

  - [MoveFileW](win32file.md#win32filemovefilew)

    Renames an existing file or a directory (including all its children). (NT/2000 Unicode specific version).&nbsp;

  - [MoveFileEx](win32file.md#win32filemovefileex)

    Renames an existing file or a directory (including all its children).&nbsp;

  - [MoveFileExW](win32file.md#win32filemovefileexw)

    Renames an existing file or a directory (including all its children). (NT/2000 Unicode specific version).&nbsp;

  - [QueryDosDevice](win32file.md#win32filequerydosdevice)

    Returns the mapping for a device name, or all device names&nbsp;

  - [ReadDirectoryChangesW](win32file.md#win32filereaddirectorychangesw)

    retrieves information describing the changes occurring within a directory.&nbsp;

  - [FILE_NOTIFY_INFORMATION](win32file.md#win32filefile_notify_information)

    Decodes a PyFILE_NOTIFY_INFORMATION buffer.&nbsp;

  - [SetCurrentDirectory](win32file.md#win32filesetcurrentdirectory)

    Sets the current directory.&nbsp;

  - [SetEndOfFile](win32file.md#win32filesetendoffile)

    Moves the end-of-file (EOF) position for the specified file to the current position of the file pointer.&nbsp;

  - [SetFileApisToANSI](win32file.md#win32filesetfileapistoansi)

    Causes a set of Win32 file functions to use the ANSI character set code page. This function is useful for 8-bit console input and output operations.&nbsp;

  - [SetFileApisToOEM](win32file.md#win32filesetfileapistooem)

    Causes a set of Win32 file functions to use the OEM character set code page. This function is useful for 8-bit console input and output operations.&nbsp;

  - [SetFileAttributes](win32file.md#win32filesetfileattributes)

    Changes a file's attributes.&nbsp;

  - [SetFilePointer](win32file.md#win32filesetfilepointer)

    Moves the file pointer of an open file.&nbsp;

  - [SetVolumeLabel](win32file.md#win32filesetvolumelabel)

    Sets a volume label for a disk drive.&nbsp;

  - [UnlockFile](win32file.md#win32fileunlockfile)

    Unlocks a region of a file locked by[win32file::LockFile](win32file.md#win32filelockfile)or[win32file::LockFileEx](win32file.md#win32filelockfileex)&nbsp;

  - [_get_osfhandle](win32file.md#win32file_get_osfhandle)

    Gets operating-system file handle associated with existing stream&nbsp;

  - [_open_osfhandle](win32file.md#win32file_open_osfhandle)

    Associates a C run-time file handle with a existing operating-system file handle.&nbsp;

  - [_setmaxstdio](win32file.md#win32file_setmaxstdio)

    Set the maximum allowed number of open stdio handles&nbsp;

  - [_getmaxstdio](win32file.md#win32file_getmaxstdio)

    Returns the maximum number of CRT io streams.&nbsp;

  - [TransmitFile](win32file.md#win32filetransmitfile)

    Transmits a file over a socket 

TransmitFile(sock, filehandle, bytes_to_write, bytes_per_send, overlap, flags [, (prepend_buf, postpend_buf)])&nbsp;

  - [ConnectEx](win32file.md#win32fileconnectex)

    Version of connect that uses Overlapped I/O 

ConnectEx(sock, (addr, port), buf, overlap)&nbsp;

  - [AcceptEx](win32file.md#win32fileacceptex)

    Version of accept that uses Overlapped I/O&nbsp;

  - [CalculateSocketEndPointSize](win32file.md#win32filecalculatesocketendpointsize)

    Calculate how many bytes are needed for the connection endpoints data for a socket.&nbsp;

  - [GetAcceptExSockaddrs](win32file.md#win32filegetacceptexsockaddrs)

    Parses the connection endpoints from the buffer passed into AcceptEx&nbsp;

  - [WSAEventSelect](win32file.md#win32filewsaeventselect)

    Specifies an event object to be associated with the supplied set of FD_XXXX network events.&nbsp;

  - [WSAEnumNetworkEvents](win32file.md#win32filewsaenumnetworkevents)

    Return network events that caused the event associated with the socket to be signaled.&nbsp;

  - [WSAAsyncSelect](win32file.md#win32filewsaasyncselect)

    Request windows message notification for the supplied set of FD_XXXX network events.&nbsp;

  - [WSASend](win32file.md#win32filewsasend)

    Winsock send() equivalent function for Overlapped I/O.&nbsp;

  - [WSARecv](win32file.md#win32filewsarecv)

    Winsock recv() equivalent function for Overlapped I/O.&nbsp;

  - [BuildCommDCB](win32file.md#win32filebuildcommdcb)

    Fills the specified DCB structure with values specified in a device-control string. The device-control string uses the syntax of the mode command&nbsp;

  - [ClearCommError](win32file.md#win32fileclearcommerror)

    retrieves information about a communications error and reports the current status of a communications device.&nbsp;

  - [EscapeCommFunction](win32file.md#win32fileescapecommfunction)

    directs a specified communications device to perform an extended function.&nbsp;

  - [GetCommState](win32file.md#win32filegetcommstate)

    Returns a device-control block (a DCB structure) with the current control settings for a specified communications device.&nbsp;

  - [SetCommState](win32file.md#win32filesetcommstate)

    Configures a communications device according to the specifications in a device-control block. 

The function reinitializes all hardware and control settings, but it does not empty output or input queues.&nbsp;

  - [ClearCommBreak](win32file.md#win32fileclearcommbreak)

    Restores character transmission for a specified communications device and places the transmission line in a nonbreak state&nbsp;

  - [GetCommMask](win32file.md#win32filegetcommmask)

    Retrieves the value of the event mask for a specified communications device.&nbsp;

  - [SetCommMask](win32file.md#win32filesetcommmask)

    Sets the value of the event mask for a specified communications device.&nbsp;

  - [GetCommModemStatus](win32file.md#win32filegetcommmodemstatus)

    Retrieves modem control-register values.&nbsp;

  - [GetCommTimeouts](win32file.md#win32filegetcommtimeouts)

    Retrieves the time-out parameters for all read and write operations on a specified communications device.&nbsp;

  - [SetCommTimeouts](win32file.md#win32filesetcommtimeouts)

    Sets the time-out parameters for all read and write operations on a specified communications device.&nbsp;

  - [PurgeComm](win32file.md#win32filepurgecomm)

    Discards all characters from the output or input buffer of a specified communications resource. It can also terminate pending read or write operations on the resource.&nbsp;

  - [SetCommBreak](win32file.md#win32filesetcommbreak)

    Suspends character transmission for a specified communications device and places the transmission line in a break state until the[win32file::ClearCommBreak](win32file.md#win32fileclearcommbreak)function is called.&nbsp;

  - [SetupComm](win32file.md#win32filesetupcomm)

    Initializes the communications parameters for a specified communications device.&nbsp;

  - [TransmitCommChar](win32file.md#win32filetransmitcommchar)

    Transmits a specified character ahead of any pending data in the output buffer of the specified communications device.&nbsp;

  - [WaitCommEvent](win32file.md#win32filewaitcommevent)

    Waits for an event to occur for a specified communications device. The set of events that are monitored by this function is contained in the event mask associated with the device handle.&nbsp;

  - [SetVolumeMountPoint](win32file.md#win32filesetvolumemountpoint)

    Mounts the specified volume at the specified volume mount point.&nbsp;

  - [DeleteVolumeMountPoint](win32file.md#win32filedeletevolumemountpoint)

    Unmounts the volume from the specified volume mount point.&nbsp;

  - [GetVolumeNameForVolumeMountPoint](win32file.md#win32filegetvolumenameforvolumemountpoint)

    Returns unique volume name.&nbsp;

  - [GetVolumePathName](win32file.md#win32filegetvolumepathname)

    Returns volume mount point for a path&nbsp;

  - [GetVolumePathNamesForVolumeName](win32file.md#win32filegetvolumepathnamesforvolumename)

    Returns mounted paths for a volume&nbsp;

  - [CreateHardLink](win32file.md#win32filecreatehardlink)

    Establishes an NTFS hard link between an existing file and a new file.&nbsp;

  - [CreateSymbolicLink](win32file.md#win32filecreatesymboliclink)

    Creates a symbolic link (reparse point)&nbsp;

  - [EncryptFile](win32file.md#win32fileencryptfile)

    Encrypts specified file (requires Win2k or higher and NTFS)&nbsp;

  - [DecryptFile](win32file.md#win32filedecryptfile)

    Decrypts specified file (requires Win2k or higher and NTFS)&nbsp;

  - [EncryptionDisable](win32file.md#win32fileencryptiondisable)

    Enables/disables encryption for a directory (requires Win2k or higher and NTFS)&nbsp;

  - [FileEncryptionStatus](win32file.md#win32filefileencryptionstatus)

    retrieves the encryption status of the specified file.&nbsp;

  - [QueryUsersOnEncryptedFile](win32file.md#win32filequeryusersonencryptedfile)

    Returns list of users for an encrypted file as tuples of (SID, certificate hash blob, display info)&nbsp;

  - [QueryRecoveryAgentsOnEncryptedFile](win32file.md#win32filequeryrecoveryagentsonencryptedfile)

    Lists recovery agents for file as a tuple of tuples.&nbsp;

  - [RemoveUsersFromEncryptedFile](win32file.md#win32fileremoveusersfromencryptedfile)

    Removes specified certificates from file - if certificate is not found, it is ignored&nbsp;

  - [AddUsersToEncryptedFile](win32file.md#win32fileadduserstoencryptedfile)

    Allows user identified by SID and EFS certificate access to decrypt specified file&nbsp;

  - [DuplicateEncryptionInfoFile](win32file.md#win32fileduplicateencryptioninfofile)

    Duplicates EFS encryption from one file to another&nbsp;

  - [BackupRead](win32file.md#win32filebackupread)

    Reads streams of data from a file&nbsp;

  - [BackupSeek](win32file.md#win32filebackupseek)

    Seeks forward in a file stream&nbsp;

  - [BackupWrite](win32file.md#win32filebackupwrite)

    Restores file data&nbsp;

  - [SetFileShortName](win32file.md#win32filesetfileshortname)

    Set the 8.3 name of a file&nbsp;

  - [CopyFileEx](win32file.md#win32filecopyfileex)

    Restartable file copy with optional progress routine&nbsp;

  - [MoveFileWithProgress](win32file.md#win32filemovefilewithprogress)

    Moves a file, and reports progress to a callback function&nbsp;

  - [ReplaceFile](win32file.md#win32filereplacefile)

    Replaces one file with another&nbsp;

  - [OpenEncryptedFileRaw](win32file.md#win32fileopenencryptedfileraw)

    Initiates a backup or restore operation on an encrypted file&nbsp;

  - [ReadEncryptedFileRaw](win32file.md#win32filereadencryptedfileraw)

    Reads the encrypted bytes of a file for backup and restore purposes&nbsp;

  - [WriteEncryptedFileRaw](win32file.md#win32filewriteencryptedfileraw)

    Writes raw bytes to an encrypted file&nbsp;

  - [CloseEncryptedFileRaw](win32file.md#win32filecloseencryptedfileraw)

    Frees a context created by[win32file::OpenEncryptedFileRaw](win32file.md#win32fileopenencryptedfileraw)&nbsp;

  - [CreateFileW](win32file.md#win32filecreatefilew)

    Unicode version of CreateFile - see[win32file::CreateFile](win32file.md#win32filecreatefile)for more information.&nbsp;

  - [DeleteFileW](win32file.md#win32filedeletefilew)

    Deletes a file (Unicode version)&nbsp;

  - [GetFileAttributesEx](win32file.md#win32filegetfileattributesex)

    Retrieves attributes for a specified file or directory.&nbsp;

  - [SetFileAttributesW](win32file.md#win32filesetfileattributesw)

    Sets a file's attributes&nbsp;

  - [CreateDirectoryExW](win32file.md#win32filecreatedirectoryexw)

    Creates a directory (Unicode version)&nbsp;

  - [RemoveDirectory](win32file.md#win32fileremovedirectory)

    Removes an existing directory&nbsp;

  - [FindFilesW](win32file.md#win32filefindfilesw)

    Retrieves a list of matching filenames, using the Windows Unicode API.  An interface to the API FindFirstFileW/FindNextFileW/Find close functions.&nbsp;

  - [FindFilesIterator](win32file.md#win32filefindfilesiterator)

    Returns an interator based on 

FindFirstFile/FindNextFile. Similar to __win32file::FindFiles__ , but 

avoids the creation of the list for huge directories.&nbsp;

  - [FindStreams](win32file.md#win32filefindstreams)

    List the data streams for a file&nbsp;

  - [FindFileNames](win32file.md#win32filefindfilenames)

    Enumerates hard links that point to specified file&nbsp;

  - [GetFinalPathNameByHandle](win32file.md#win32filegetfinalpathnamebyhandle)

    Returns the file name for an open file handle&nbsp;

  - [SfcGetNextProtectedFile](win32file.md#win32filesfcgetnextprotectedfile)

    Returns list of protected operating system files&nbsp;

  - [SfcIsFileProtected](win32file.md#win32filesfcisfileprotected)

    Checks if a file is protected&nbsp;

  - [GetLongPathName](win32file.md#win32filegetlongpathname)

    Retrieves the long path for a short path (8.3 filename)&nbsp;

  - [GetFullPathName](win32file.md#win32filegetfullpathname)

    Returns full path for path passed in&nbsp;

  - [Wow64DisableWow64FsRedirection](win32file.md#win32filewow64disablewow64fsredirection)

    Disables file system redirection for 32-bit processes running on a 64-bit system&nbsp;

  - [Wow64RevertWow64FsRedirection](win32file.md#win32filewow64revertwow64fsredirection)

    Reenables file system redirection for 32-bit processes running on a 64-bit system&nbsp;

  - [GetFileInformationByHandleEx](win32file.md#win32filegetfileinformationbyhandleex)

    Retrieves extended file information for an open file handle.&nbsp;

  - [SetFileInformationByHandle](win32file.md#win32filesetfileinformationbyhandle)

    Changes file characteristics by file handle&nbsp;

  - [ReOpenFile](win32file.md#win32filereopenfile)

    Creates a new handle to an open file&nbsp;

  - [OpenFileById](win32file.md#win32fileopenfilebyid)

    Opens a file by File Id or Object Id&nbsp;

## [win32file](#win32file).AcceptEx

 __AcceptEx( *sListening*  *, sAccepting*  *, buffer*  *, ol* __ )
Version of accept that uses Overlapped I/O

#### Parameters


  -  *sListening* : __PySocket__ /int

    Socket that had listen() called on.

  -  *sAccepting* : __PySocket__ /int

    Socket that will be used as the incoming connection.

  -  *buffer* : __buffer__ 

    Buffer to read incoming data and connection point information into. This buffer MUST be big enough to recieve your connection endpoints... AF_INET sockets need to be at least 64 bytes. The correct minimum of the buffer is determined by the protocol family that the listening socket is using.

  -  *ol* :[PyOVERLAPPED](#pyoverlapped)

    An overlapped structure

#### Comments
In order to make sure the connection has been accepted, either use the hEvent in PyOVERLAPPED, GetOverlappedResult, or GetQueuedCompletionStatus.
To use this with I/O completion ports, don't forget to attach sAccepting to your completion port.
Pass a buffer of exactly the size returned by[win32file::CalculateSocketEndPointSize](win32file.md#win32filecalculatesocketendpointsize)to have AcceptEx return without reading any bytes from the remote connection.

#### Example
To have sAccepting inherit the properties of sListening, you need to do the following after a connection is successfully accepted
import struct

sAccepting.setsockopt(socket.SOL_SOCKET, win32file.SO_UPDATE_ACCEPT_CONTEXT, struct.pack("I", sListening.fileno()))
#### Return Value
The result is 0 or ERROR_IO_PENDING.  All other values will raise 

win32file.error.  Specifically: if the win32 function returns FALSE, 

WSAGetLastError() is checked for ERROR_IO_PENDING.

## [win32file](#win32file).AddUsersToEncryptedFile

 __AddUsersToEncryptedFile( *FileName*  *, pUsers* __ )
Allows user identified by SID and EFS certificate access to decrypt specified file

#### Parameters


  -  *FileName* : string/unicode

    File that additional users will be allowed to decrypt

  -  *pUsers* : (([PySID](#pysid),string,int),...)

    Sequence representing 

ENCRYPTION_CERTIFICATE_LIST - elements are sequences consisting of 

users' Sid, encoded EFS certficate (user must export a .cer to obtain 

this data), and encoding type (usually 1 for X509_ASN_ENCODING)

## [win32file](#win32file).AllocateReadBuffer

[PyOVERLAPPEDReadBuffer](#pyoverlappedreadbuffer)= __AllocateReadBuffer( *bufSize* __ )
Allocates a buffer which can be used with an overlapped Read operation using[win32file::ReadFile](win32file.md#win32filereadfile)

#### Parameters


  -  *bufSize* : int

    The size of the buffer to allocate.

## [win32file](#win32file).AreFileApisANSI

int = __AreFileApisANSI(__ )
Determines whether a set of Win32 file functions is using the ANSI or OEM character set code page. This function is useful for 8-bit console input and output operations.

## [win32file](#win32file).BackupRead

(int, buffer, int) = __BackupRead( *hFile*  *, NumberOfBytesToRead*  *, Buffer*  *, bAbort*  *, bProcessSecurity*  *, lpContext* __ )
Reads streams of data from a file

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)

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

## [win32file](#win32file).BackupSeek

long = __BackupSeek( *hFile*  *, NumberOfBytesToSeek*  *, lpContext* __ )
Seeks forward in a file stream

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)

    File handle used by a BackupRead operation

  -  *NumberOfBytesToSeek* : long

    Number of bytes to move forward in current stream

  -  *lpContext* : int

    Context pointer returned from a BackupRead operation

#### Comments
Function will only seek to end of current stream, used to seek past bad data 

or find beginning position for read of next stream 

Returns number of bytes actually moved

## [win32file](#win32file).BackupWrite

(int,int) = __BackupWrite( *hFile*  *, NumberOfBytesToWrite*  *, Buffer*  *, bAbort*  *, bProcessSecurity*  *, lpContext* __ )
Restores file data

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)

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

## [win32file](#win32file).BuildCommDCB

[PyDCB](#pydcb)= __BuildCommDCB( *def*  *, dcb* __ )
Fills the specified DCB structure with values specified in a device-control string. The device-control string uses the syntax of the mode command

#### Parameters


  -  *def* : string

    device-control string

  -  *dcb* :[PyDCB](#pydcb)

    The device-control block

## CALLBACK_CHUNK_FINISHED
 __const win32file.CALLBACK_CHUNK_FINISHED;__ 


## CALLBACK_STREAM_SWITCH
 __const win32file.CALLBACK_STREAM_SWITCH;__ 


## CBR_110
 __const win32file.CBR_110;__ 


## CBR_115200
 __const win32file.CBR_115200;__ 


## CBR_1200
 __const win32file.CBR_1200;__ 


## CBR_128000
 __const win32file.CBR_128000;__ 


## CBR_14400
 __const win32file.CBR_14400;__ 


## CBR_19200
 __const win32file.CBR_19200;__ 


## CBR_2400
 __const win32file.CBR_2400;__ 


## CBR_256000
 __const win32file.CBR_256000;__ 


## CBR_300
 __const win32file.CBR_300;__ 


## CBR_38400
 __const win32file.CBR_38400;__ 


## CBR_4800
 __const win32file.CBR_4800;__ 


## CBR_56000
 __const win32file.CBR_56000;__ 


## CBR_57600
 __const win32file.CBR_57600;__ 


## CBR_600
 __const win32file.CBR_600;__ 


## CBR_9600
 __const win32file.CBR_9600;__ 


## CLRBREAK
 __const win32file.CLRBREAK;__ 
Restores character transmission and places the transmission line in a nonbreak state. The CLRBREAK extended function code is identical to the ClearCommBreak function.

## CLRDTR
 __const win32file.CLRDTR;__ 
Clears the DTR (data-terminal-ready) signal.

## CLRRTS
 __const win32file.CLRRTS;__ 
Clears the RTS (request-to-send) signal.

## [win32file](#win32file).COMSTAT

[PyCOMSTAT](#pycomstat)= __COMSTAT(__ )
Creates a new COMSTAT object

## COPY_FILE_ALLOW_DECRYPTED_DESTINATION
 __const win32file.COPY_FILE_ALLOW_DECRYPTED_DESTINATION;__ 


## COPY_FILE_COPY_SYMLINK
 __const win32file.COPY_FILE_COPY_SYMLINK;__ 


## COPY_FILE_FAIL_IF_EXISTS
 __const win32file.COPY_FILE_FAIL_IF_EXISTS;__ 


## COPY_FILE_OPEN_SOURCE_FOR_WRITE
 __const win32file.COPY_FILE_OPEN_SOURCE_FOR_WRITE;__ 


## COPY_FILE_RESTARTABLE
 __const win32file.COPY_FILE_RESTARTABLE;__ 


## CREATE_ALWAYS
 __const win32file.CREATE_ALWAYS;__ 
Creates a new file. The function overwrites the file if it exists.

## CREATE_FOR_DIR
 __const win32file.CREATE_FOR_DIR;__ 


## CREATE_FOR_IMPORT
 __const win32file.CREATE_FOR_IMPORT;__ 


## CREATE_NEW
 __const win32file.CREATE_NEW;__ 
Creates a new file. The function fails if the specified file already exists.

## [win32file](#win32file).CalculateSocketEndPointSize

int = __CalculateSocketEndPointSize( *socket* __ )
Calculate how many bytes are needed for the connection endpoints data for a socket.

#### Parameters


  -  *socket* : __PySocket__ /int

    The socket for which to determine the size.

#### Comments
This function allows you to determine the minumum buffer size 

which can be passed to[win32file::AcceptEx](win32file.md#win32fileacceptex)

## [win32file](#win32file).CancelIo

 __CancelIo( *handle* __ )
Cancels pending IO requests for the object.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle being cancelled.

## [win32file](#win32file).ClearCommBreak

 __ClearCommBreak( *handle* __ )
Restores character transmission for a specified communications device and places the transmission line in a nonbreak state

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the communications device.

## [win32file](#win32file).ClearCommError

int,[PyCOMSTAT](#pycomstat)= __ClearCommError( *[PyHANDLE](#pyhandle)* __ )
retrieves information about a communications error and reports the current status of a communications device.

#### Parameters


  -  *[PyHANDLE](#pyhandle)* : handle

    A handle to the device.

## [win32file](#win32file).CloseEncryptedFileRaw

 __CloseEncryptedFileRaw( *Context* __ )
Frees a context created by[win32file::OpenEncryptedFileRaw](win32file.md#win32fileopenencryptedfileraw)

#### Parameters


  -  *Context* : PyCObject

    Context object returned from[win32file::OpenEncryptedFileRaw](win32file.md#win32fileopenencryptedfileraw)

#### Comments
Only available on Windows 2000 or later

## [win32file](#win32file).CloseHandle

 __CloseHandle( *handle* __ )
Closes an open handle.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)/int

    A previously opened handle.

## [win32file](#win32file).ConnectEx

(int, int) = __ConnectEx( *s*  *, name*  *, Overlapped*  *, SendBuffer* __ )
Version of connect that uses Overlapped I/O 

ConnectEx(sock, (addr, port), buf, overlap)

#### Parameters


  -  *s* : __PySocket__ /int

    A bound, unconnected socket that will be used to connect

  -  *name* : tuple

    Address to connect to (host, port)

  -  *Overlapped* :[PyOVERLAPPED](#pyoverlapped)

    An overlapped structure

  -  *SendBuffer=None* : buffer

    Buffer to send on the socket after connect

#### Return Value
Returns the completion code and number of bytes sent. 

The completion code will be 0 for a completed operation, or ERROR_IO_PENDING for a pending overlapped operation.
If the platform does not support ConnectEx (eg, Windows 2000), an 

exception will be thrown indicating the WSAIoctl function (which is used to 

fetch the function pointer) failed with error code WSAEINVAL (10022).

## [win32file](#win32file).CopyFile

 __CopyFile( *from*  *, to*  *, bFailIfExists* __ )
Copies a file

#### Parameters


  -  *from* :[PyUnicode](#pyunicode)

    The name of the file to copy from

  -  *to* :[PyUnicode](#pyunicode)

    The name of the file to copy to

  -  *bFailIfExists* : int

    Indicates if the operation should fail if the file exists.

## [win32file](#win32file).CopyFileEx

 __CopyFileEx( *ExistingFileName*  *, NewFileName*  *, ProgressRoutine*  *, Data*  *, Cancel*  *, CopyFlags*  *, Transaction* __ )
Restartable file copy with optional progress routine

#### Parameters


  -  *ExistingFileName* :[PyUNICODE](#pyunicode)

    File to be copied

  -  *NewFileName* :[PyUNICODE](#pyunicode)

    Place to which it will be copied

  -  *ProgressRoutine=None* :[CopyProgressRoutine](#copyprogressroutine)

    A python function that receives progress updates, can be None

  -  *Data=None* : object

    An arbitrary object to be passed to the callback function

  -  *Cancel=False* : boolean

    Pass True to cancel a restartable copy that was previously interrupted

  -  *CopyFlags=0* : int

    Combination of COPY_FILE_* flags

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Handle to a transaction as returned by[win32transaction::CreateTransaction](win32transaction.md#win32transactioncreatetransaction)

#### Comments
Accepts keyword args.
On Vista and later, the Transaction arg can be passed to invoke CopyFileTransacted

#### Win32 API References


  - Search for *CopyFileEx* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=copyfileex),[google](#http://www.google.com/search?q=copyfileex)or[google groups](#http://groups.google.com/groups?q=copyfileex).

  - Search for *CopyFileTransacted* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=copyfiletransacted),[google](#http://www.google.com/search?q=copyfiletransacted)or[google groups](#http://groups.google.com/groups?q=copyfiletransacted).

## [win32file](#win32file).CopyFileW

 __CopyFileW( *from*  *, to*  *, bFailIfExists* __ )
Copies a file (NT/2000 Unicode specific version)

#### Parameters


  -  *from* :[PyUnicode](#pyunicode)

    The name of the file to copy from

  -  *to* :[PyUnicode](#pyunicode)

    The name of the file to copy to

  -  *bFailIfExists* : int

    Indicates if the operation should fail if the file exists.

## [win32file](#win32file).CreateDirectory

 __CreateDirectory( *name*  *, sa* __ )
Creates a directory

#### Parameters


  -  *name* :[PyUnicode](#pyunicode)

    The name of the directory to create

  -  *sa* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    The security attributes, or None

## [win32file](#win32file).CreateDirectoryEx

 __CreateDirectoryEx( *templateName*  *, newDirectory*  *, sa* __ )
Creates a directory

#### Parameters


  -  *templateName* :[PyUnicode](#pyunicode)

    Specifies the path of the directory to use as a template when creating the new directory.

  -  *newDirectory* :[PyUnicode](#pyunicode)

    Specifies the name of the new directory

  -  *sa* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    The security attributes, or None

## [win32file](#win32file).CreateDirectoryExW

 __CreateDirectoryExW( *TemplateDirectory*  *, NewDirectory*  *, SecurityAttributes*  *, Transaction* __ )
Creates a directory (Unicode version)

#### Parameters


  -  *TemplateDirectory* :[PyUnicode](#pyunicode)

    Directory to use as a template, can be None

  -  *NewDirectory* :[PyUnicode](#pyunicode)

    Name of directory to be created

  -  *SecurityAttributes=None* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Security for new directory (optional)

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Handle to a transaction (optional).  See[win32transaction::CreateTransaction](win32transaction.md#win32transactioncreatetransaction).

#### Comments
If a transaction handle is passed, CreateDirectoryTransacted will be called (requires Vista or later).
Accepts keyword arguments.

#### Win32 API References


  - Search for *CreateDirectoryEx* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createdirectoryex),[google](#http://www.google.com/search?q=createdirectoryex)or[google groups](#http://groups.google.com/groups?q=createdirectoryex).

  - Search for *CreateDirectoryTransacted* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createdirectorytransacted),[google](#http://www.google.com/search?q=createdirectorytransacted)or[google groups](#http://groups.google.com/groups?q=createdirectorytransacted).

## [win32file](#win32file).CreateDirectoryW

 __CreateDirectoryW( *name*  *, sa* __ )
Creates a directory (NT/2000 Unicode specific version)

#### Parameters


  -  *name* :[PyUnicode](#pyunicode)

    The name of the directory to create

  -  *sa* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    The security attributes, or None

## [win32file](#win32file).CreateFile

[PyHANDLE](#pyhandle)= __CreateFile( *fileName*  *, desiredAccess*  *, shareMode*  *, attributes*  *, CreationDisposition*  *, flagsAndAttributes*  *, hTemplateFile* __ )
Creates or opens the a file or other object and returns a handle that can be used to access the object.

#### Parameters


  -  *fileName* :[PyUnicode](#pyunicode)

    The name of the file

  -  *desiredAccess* : int

    access (read-write) mode 

Specifies the type of access to the object. An application can obtain read access, write access, read-write access, or device query access. This parameter can be any combination of the following values.

 __Value__  __Meaning__ 0Specifies device query access to the object. An application can query device attributes without accessing the device.GENERIC_READSpecifies read access to the object. Data can be read from the file and the file pointer can be moved. Combine with GENERIC_WRITE for read-write access.GENERIC_WRITESpecifies write access to the object. Data can be written to the file and the file pointer can be moved. Combine with GENERIC_READ for read-write access.
  -  *shareMode* : int

    Set of bit flags that specifies how the object can be shared. If dwShareMode is 0, the object cannot be shared. Subsequent open operations on the object will fail, until the handle is closed. 

To share the object, use a combination of one or more of the following values:

 __Value__  __Meaning__ FILE_SHARE_DELETEWindows NT: Subsequent open operations on the object will succeed only if delete access is requested.FILE_SHARE_READSubsequent open operations on the object will succeed only if read access is requested.FILE_SHARE_WRITESubsequent open operations on the object will succeed only if write access is requested.
  -  *attributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    The security attributes, or None

  -  *CreationDisposition* : int

    Specifies which action to take on files that exist, and which action to take when files do not exist. For more information about this parameter, see the Remarks section. This parameter must be one of the following values:

 __Value__  __Meaning__ CREATE_NEWCreates a new file. The function fails if the specified file already exists.CREATE_ALWAYSCreates a new file. If the file exists, the function overwrites the file and clears the existing attributes.OPEN_EXISTINGOpens the file. The function fails if the file does not exist. 

See the Remarks section for a discussion of why you should use the OPEN_EXISTING flag if you are using the CreateFile function for devices, including the console.OPEN_ALWAYSOpens the file, if it exists. If the file does not exist, the function creates the file as if dwCreationDisposition were CREATE_NEW.TRUNCATE_EXISTINGOpens the file. Once opened, the file is truncated so that its size is zero bytes. The calling process must open the file with at least GENERIC_WRITE access. The function fails if the file does not exist.
  -  *flagsAndAttributes* : int

    file attributes

  -  *hTemplateFile* :[PyHANDLE](#pyhandle)

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

## [win32file](#win32file).CreateFileW

[PyHANDLE](#pyhandle)= __CreateFileW( *FileName*  *, DesiredAccess*  *, ShareMode*  *, SecurityAttributes*  *, CreationDisposition*  *, FlagsAndAttributes*  *, TemplateFile*  *, Transaction*  *, MiniVersion*  *, ExtendedParameter* __ )
Unicode version of CreateFile - see[win32file::CreateFile](win32file.md#win32filecreatefile)for more information.

#### Parameters


  -  *FileName* :[PyUnicode](#pyunicode)

    Name of file

  -  *DesiredAccess* : int

    Combination of access mode flags.  See MSDN docs.

  -  *ShareMode* : int

    Combination of FILE_SHARE_READ, FILE_SHARE_WRITE, FILE_SHARE_DELETE

  -  *SecurityAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies security descriptor and handle inheritance, can be None

  -  *CreationDisposition* : int

    One of CREATE_ALWAYS,CREATE_NEW,OPEN_ALWAYS,OPEN_EXISTING or TRUNCATE_EXISTING

  -  *FlagsAndAttributes* : int

    Combination of FILE_ATTRIBUTE_* and FILE_FLAG_* flags

  -  *TemplateFile=None* :[PyHANDLE](#pyhandle)

    Handle to file to be used as template, can be None

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Handle to the transaction as returned by[win32transaction::CreateTransaction](win32transaction.md#win32transactioncreatetransaction)

  -  *MiniVersion=None* : int

    Transacted version of file to open, can be None

  -  *ExtendedParameter=None* : None

    Reserved, use only None

#### Comments
If Transaction is specified, CreateFileTransacted will be called (requires Vista or later)
Accepts keyword arguments.

#### Win32 API References


  - Search for *CreateFile* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createfile),[google](#http://www.google.com/search?q=createfile)or[google groups](#http://groups.google.com/groups?q=createfile).

  - Search for *CreateFileTransacted* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createfiletransacted),[google](#http://www.google.com/search?q=createfiletransacted)or[google groups](#http://groups.google.com/groups?q=createfiletransacted).

## [win32file](#win32file).CreateHardLink

 __CreateHardLink( *FileName*  *, ExistingFileName*  *, SecurityAttributes*  *, Transaction* __ )
Establishes an NTFS hard link between an existing file and a new file.

#### Parameters


  -  *FileName* :[PyUnicode](#pyunicode)

    The name of the new directory entry to be created.

  -  *ExistingFileName* :[PyUnicode](#pyunicode)

    The name of the existing file to which the new link will point.

  -  *SecurityAttributes=None* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Optional SECURITY_ATTRIBUTES object. MSDN describes this parameter as reserved, so use only None

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Handle to a transaction, as returned by[win32transaction::CreateTransaction](win32transaction.md#win32transactioncreatetransaction)

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

## [win32file](#win32file).CreateIoCompletionPort

[PyHANDLE](#pyhandle)= __CreateIoCompletionPort( *handle*  *, existing*  *, completionKey*  *, numThreads* __ )
Can associate an instance of an opened file with a newly created or an existing input/output (I/O) completion port; or it can create an I/O completion port without associating it with a file.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    file handle to associate with the I/O completion port

  -  *existing* :[PyHANDLE](#pyhandle)

    handle to the I/O completion port

  -  *completionKey* : int

    per-file completion key for I/O completion packets

  -  *numThreads* : int

    number of threads allowed to execute concurrently

#### Return Value
If an existing handle to a completion port is passed, the result 

of this function will be that same handle.  See MSDN for more details.

## [win32file](#win32file).CreateMailslot

[PyHANDLE](#pyhandle)= __CreateMailslot( *Name*  *, MaxMessageSize*  *, ReadTimeout*  *, SecurityAttributes* __ )
Creates a mailslot on the local machine

#### Parameters


  -  *Name* : str

    Name of the mailslot, of the form \\.\\mailslot\\[path]name

  -  *MaxMessageSize* : int

    Largest message size.  Use 0 for unlimited.

  -  *ReadTimeout* : int

    Timeout in milliseconds.  Use -1 for no timeout.

  -  *SecurityAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Determines if returned handle is inheritable, can be None

#### Win32 API References


  - Search for *CreateMailslot* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createmailslot),[google](#http://www.google.com/search?q=createmailslot)or[google groups](#http://groups.google.com/groups?q=createmailslot).

## [win32file](#win32file).CreateSymbolicLink

 __CreateSymbolicLink( *SymlinkFileName*  *, TargetFileName*  *, Flags*  *, Transaction* __ )
Creates a symbolic link (reparse point)

#### Parameters


  -  *SymlinkFileName* :[PyUnicode](#pyunicode)

    Path of the symbolic link to be created

  -  *TargetFileName* :[PyUnicode](#pyunicode)

    The name of file to which link will point

  -  *Flags=0* : int

    SYMBOLIC_LINK_FLAG_DIRECTORY is only defined flag

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Handle to a transaction, as returned by[win32transaction::CreateTransaction](win32transaction.md#win32transactioncreatetransaction)

#### Comments
This method only exists on Vista and later.
Accepts keyword args.
Requires SeCreateSymbolicLink priv.
If the Transaction parameter is passed in, CreateSymbolicLinkTransacted will be called

## [win32file](#win32file).DCB

[PyDCB](#pydcb)= __DCB(__ )
Creates a new DCB object

## DRIVE_CDROM
 __const win32file.DRIVE_CDROM;__ 
The drive is a CD-ROM drive.

## DRIVE_FIXED
 __const win32file.DRIVE_FIXED;__ 
The disk cannot be removed from the drive.

## DRIVE_NO_ROOT_DIR
 __const win32file.DRIVE_NO_ROOT_DIR;__ 
The root directory does not exist.

## DRIVE_RAMDISK
 __const win32file.DRIVE_RAMDISK;__ 
The drive is a RAM disk.

## DRIVE_REMOTE
 __const win32file.DRIVE_REMOTE;__ 
The drive is a remote (network) drive.

## DRIVE_REMOVABLE
 __const win32file.DRIVE_REMOVABLE;__ 
The disk can be removed from the drive.

## DRIVE_UNKNOWN
 __const win32file.DRIVE_UNKNOWN;__ 
The drive type cannot be determined.

## DTR_CONTROL_DISABLE
 __const win32file.DTR_CONTROL_DISABLE;__ 
Disables the DTR line when the device is opened and leaves it disabled.

## DTR_CONTROL_ENABLE
 __const win32file.DTR_CONTROL_ENABLE;__ 
Enables the DTR line when the device is opened and leaves it on.

## DTR_CONTROL_HANDSHAKE
 __const win32file.DTR_CONTROL_HANDSHAKE;__ 
Enables DTR handshaking. If handshaking is enabled, it is an error for the application to adjust the line by using the EscapeCommFunction function.

## [win32file](#win32file).DecryptFile

 __DecryptFile( *filename* __ )
Decrypts specified file (requires Win2k or higher and NTFS)

#### Parameters


  -  *filename* : string/unicode

    File to decrypt

## [win32file](#win32file).DefineDosDevice

 __DefineDosDevice( *flags*  *, deviceName*  *, targetPath* __ )
Lets an application define, redefine, or delete MS-DOS device names.

#### Parameters


  -  *flags* : int

    flags specifying aspects of device definition

  -  *deviceName* :[PyUnicode](#pyunicode)

    MS-DOS device name string

  -  *targetPath* :[PyUnicode](#pyunicode)

    MS-DOS or path string for 32-bit Windows.

## [win32file](#win32file).DefineDosDeviceW

 __DefineDosDeviceW( *flags*  *, deviceName*  *, targetPath* __ )
Lets an application define, redefine, or delete MS-DOS device names. (NT/2000 Unicode specific version)

#### Parameters


  -  *flags* : int

    flags specifying aspects of device definition

  -  *deviceName* :[PyUnicode](#pyunicode)

    MS-DOS device name string

  -  *targetPath* :[PyUnicode](#pyunicode)

    MS-DOS or path string for 32-bit Windows.

## [win32file](#win32file).DeleteFile

 __DeleteFile( *fileName* __ )
Deletes a file.

#### Parameters


  -  *fileName* :[PyUnicode](#pyunicode)

    The filename to delete

## [win32file](#win32file).DeleteFileW

 __DeleteFileW( *FileName*  *, Transaction* __ )
Deletes a file (Unicode version)

#### Parameters


  -  *FileName* :[PyUnicode](#pyunicode)

    Name of file to be deleted

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Transaction handle as returned by[win32transaction::CreateTransaction](win32transaction.md#win32transactioncreatetransaction)

#### Comments
If a transaction handle is passed in, DeleteFileTransacted will be called (requires Windows Vista).
Accepts keyword arguments.

#### Win32 API References


  - Search for *DeleteFile* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=deletefile),[google](#http://www.google.com/search?q=deletefile)or[google groups](#http://groups.google.com/groups?q=deletefile).

  - Search for *DeleteFileTransacted* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=deletefiletransacted),[google](#http://www.google.com/search?q=deletefiletransacted)or[google groups](#http://groups.google.com/groups?q=deletefiletransacted).

## [win32file](#win32file).DeleteVolumeMountPoint

 __DeleteVolumeMountPoint( *VolumeMountPoint* __ )
Unmounts the volume from the specified volume mount point.

#### Parameters


  -  *VolumeMountPoint* :[PyUnicode](#pyunicode)

    The mount point to delete - must have a trailing backslash.

#### Comments
Accepts keyword args.
Throws&#09an error if&#09it is not a&#09valid mount&#09point, returns None&#09on success.
Use carefully - will&#09remove drive letter&#09assignment if no directory specified
This method requires Windows 2000 or later.  On earlier platforms, NotImplementedError will be raised.

#### Example
Usage

## [win32file](#win32file).DeviceIoControl

str/buffer = __DeviceIoControl( *Device*  *, IoControlCode*  *, InBuffer*  *, OutBuffer*  *, Overlapped* __ )
Sends a control code to a device or file system driver

#### Parameters


  -  *Device* :[PyHANDLE](#pyhandle)

    Handle to a file, device, or volume

  -  *IoControlCode* : int

    IOControl Code to use, from winioctlcon

  -  *InBuffer* : str/buffer

    The input data for the operation, can be None for some operations.

  -  *OutBuffer* : int/buffer

    Size of the buffer to allocate for output, or a writeable buffer 

as returned by[win32file::AllocateReadBuffer](win32file.md#win32fileallocatereadbuffer).

  -  *Overlapped=None* :[PyOVERLAPPED](#pyoverlapped)

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

## [win32file](#win32file).DuplicateEncryptionInfoFile

 __DuplicateEncryptionInfoFile( *SrcFileName*  *, DstFileName*  *, CreationDisposition*  *, Attributes*  *, SecurityAttributes* __ )
Duplicates EFS encryption from one file to another

#### Parameters


  -  *SrcFileName* :[PyUnicode](#pyunicode)

    Encrypted file to read EFS metadata from

  -  *DstFileName* :[PyUnicode](#pyunicode)

    File to be encrypted using EFS data from source file

  -  *CreationDisposition* : int

    Specifies whether an existing file should be overwritten (CREATE_NEW or CREATE_ALWAYS)

  -  *Attributes* : int

    File attributes

  -  *SecurityAttributes=None* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies security for destination file

#### Comments
Requires Windows XP or later
Accepts keyword arguments.

#### Win32 API References


  - Search for *DuplicateEncryptionInfoFile* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=duplicateencryptioninfofile),[google](#http://www.google.com/search?q=duplicateencryptioninfofile)or[google groups](#http://groups.google.com/groups?q=duplicateencryptioninfofile).

## EVENPARITY
 __const win32file.EVENPARITY;__ 


## EV_BREAK
 __const win32file.EV_BREAK;__ 
A break was detected on input.

## EV_CTS
 __const win32file.EV_CTS;__ 
The CTS (clear-to-send) signal changed state.

## EV_DSR
 __const win32file.EV_DSR;__ 
The DSR (data-set-ready) signal changed state.

## EV_ERR
 __const win32file.EV_ERR;__ 
A line-status error occurred. Line-status errors are CE_FRAME, CE_OVERRUN, and CE_RXPARITY.

## EV_RING
 __const win32file.EV_RING;__ 
A ring indicator was detected.

## EV_RLSD
 __const win32file.EV_RLSD;__ 
The RLSD (receive-line-signal-detect) signal changed state.

## EV_RXCHAR
 __const win32file.EV_RXCHAR;__ 
A character was received and placed in the input buffer.

## EV_RXFLAG
 __const win32file.EV_RXFLAG;__ 
The event character was received and placed in the input buffer. The event character is specified in the device's DCB structure, which is applied to a serial port by using the SetCommState function.

## EV_TXEMPTY
 __const win32file.EV_TXEMPTY;__ 
The last character in the output buffer was sent.

## [win32file](#win32file).EncryptFile

 __EncryptFile( *filename* __ )
Encrypts specified file (requires Win2k or higher and NTFS)

#### Parameters


  -  *filename* : string/unicode

    File to encrypt

## [win32file](#win32file).EncryptionDisable

 __EncryptionDisable( *DirName*  *, Disable* __ )
Enables/disables encryption for a directory (requires Win2k or higher and NTFS)

#### Parameters


  -  *DirName* : string/unicode

    Directory to enable or disable

  -  *Disable* : boolean

    Set to False to enable encryption

## [win32file](#win32file).EscapeCommFunction

 __EscapeCommFunction( *handle* __ )
directs a specified communications device to perform an extended function.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the communications device.


## FD_ACCEPT
 __const win32file.FD_ACCEPT;__ 


## FD_ADDRESS_LIST_CHANGE
 __const win32file.FD_ADDRESS_LIST_CHANGE;__ 


## FD_CLOSE
 __const win32file.FD_CLOSE;__ 


## FD_CONNECT
 __const win32file.FD_CONNECT;__ 


## FD_GROUP_QOS
 __const win32file.FD_GROUP_QOS;__ 


## FD_OOB
 __const win32file.FD_OOB;__ 


## FD_QOS
 __const win32file.FD_QOS;__ 


## FD_READ
 __const win32file.FD_READ;__ 


## FD_ROUTING_INTERFACE_CHANGE
 __const win32file.FD_ROUTING_INTERFACE_CHANGE;__ 


## FD_WRITE
 __const win32file.FD_WRITE;__ 


## FILE_ALL_ACCESS
 __const win32file.FILE_ALL_ACCESS;__ 


## FILE_ATTRIBUTE_ARCHIVE
 __const win32file.FILE_ATTRIBUTE_ARCHIVE;__ 
The file should be archived. Applications use this attribute to mark files for backup or removal.

## FILE_ATTRIBUTE_COMPRESSED
 __const win32file.FILE_ATTRIBUTE_COMPRESSED;__ 
The file or directory is compressed. For a file, this means that all of the data in the file is compressed. For a directory, this means that compression is the default for newly created files and subdirectories.

## FILE_ATTRIBUTE_DIRECTORY
 __const win32file.FILE_ATTRIBUTE_DIRECTORY;__ 
The file is a directory

## FILE_ATTRIBUTE_HIDDEN
 __const win32file.FILE_ATTRIBUTE_HIDDEN;__ 
The file is hidden. It is not to be included in an ordinary directory listing.

## FILE_ATTRIBUTE_NORMAL
 __const win32file.FILE_ATTRIBUTE_NORMAL;__ 
The file has no other attributes set. This attribute is valid only if used alone.

## FILE_ATTRIBUTE_OFFLINE
 __const win32file.FILE_ATTRIBUTE_OFFLINE;__ 
The data of the file is not immediately available. Indicates that the file data has been physically moved to offline storage.

## FILE_ATTRIBUTE_READONLY
 __const win32file.FILE_ATTRIBUTE_READONLY;__ 
The file is read only. Applications can read the file but cannot write to it or delete it.

## FILE_ATTRIBUTE_SYSTEM
 __const win32file.FILE_ATTRIBUTE_SYSTEM;__ 
The file is part of or is used exclusively by the operating system.

## FILE_ATTRIBUTE_TEMPORARY
 __const win32file.FILE_ATTRIBUTE_TEMPORARY;__ 
The file is being used for temporary storage. File systems attempt to keep all of the data in memory for quicker access rather than flushing the data back to mass storage. A temporary file should be deleted by the application as soon as it is no longer needed.

## FILE_BEGIN
 __const win32file.FILE_BEGIN;__ 


## FILE_CURRENT
 __const win32file.FILE_CURRENT;__ 


## FILE_ENCRYPTABLE
 __const win32file.FILE_ENCRYPTABLE;__ 


## FILE_END
 __const win32file.FILE_END;__ 


## FILE_FLAG_BACKUP_SEMANTICS
 __const win32file.FILE_FLAG_BACKUP_SEMANTICS;__ 
Windows NT only: Indicates that the file is being opened or created for a backup or restore operation. 

The operating system ensures that the calling process overrides file security checks, provided it has the necessary permission to do so. The relevant permissions are SE_BACKUP_NAME and SE_RESTORE_NAME. 

You can also set this flag to obtain a handle to a directory. A directory handle can be passed to some Win32 functions in place of a file handle.

## FILE_FLAG_DELETE_ON_CLOSE
 __const win32file.FILE_FLAG_DELETE_ON_CLOSE;__ 
Indicates that the operating system is to delete the file immediately after all of its handles have been closed, 

not just the handle for which you specified FILE_FLAG_DELETE_ON_CLOSE. Subsequent open requests for the file will fail, unless FILE_SHARE_DELETE is used.

## FILE_FLAG_NO_BUFFERING
 __const win32file.FILE_FLAG_NO_BUFFERING;__ 
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
 __const win32file.FILE_FLAG_OPEN_REPARSE_POINT;__ 
used to open a handle for use with DeviceIoControl and FSCTL_GET_REPARSE_POINT/FSCTL_SET_REPARSE_POINT)

## FILE_FLAG_OVERLAPPED
 __const win32file.FILE_FLAG_OVERLAPPED;__ 
Instructs the system to initialize the object, so that operations that take a significant amount of time to process return ERROR_IO_PENDING. When the operation is finished, the specified event is set to the signaled state. 

When you specify FILE_FLAG_OVERLAPPED, the ReadFile and WriteFile functions must specify an OVERLAPPED structure. That is, when FILE_FLAG_OVERLAPPED is specified, an application must perform overlapped reading and writing. 

When FILE_FLAG_OVERLAPPED is specified, the system does not maintain the file pointer. The file position must be passed as part of the lpOverlapped parameter (pointing to an OVERLAPPED structure) to the ReadFile and WriteFile functions. 

This flag also enables more than one operation to be performed simultaneously with the handle (a simultaneous read and write operation, for example).

## FILE_FLAG_POSIX_SEMANTICS
 __const win32file.FILE_FLAG_POSIX_SEMANTICS;__ 
Indicates that the file is to be accessed according to POSIX rules. 

This includes allowing multiple files with names, differing only in case, for file systems that support such naming. 

Use care when using this option because files created with this flag may not be accessible by applications written for MS-DOS or Windows.

## FILE_FLAG_RANDOM_ACCESS
 __const win32file.FILE_FLAG_RANDOM_ACCESS;__ 
Indicates that the file is accessed randomly. The system can use this as a hint to optimize file caching.

## FILE_FLAG_SEQUENTIAL_SCAN
 __const win32file.FILE_FLAG_SEQUENTIAL_SCAN;__ 
Indicates that the file is to be accessed sequentially from beginning to end. The system can use this as a hint to optimize file caching. 

If an application moves the file pointer for random access, optimum caching may not occur; however, correct operation is still guaranteed. 

Specifying this flag can increase performance for applications that read large files using sequential access. 

Performance gains can be even more noticeable for applications that read large files mostly sequentially, but occasionally skip over small ranges of bytes.

## FILE_FLAG_WRITE_THROUGH
 __const win32file.FILE_FLAG_WRITE_THROUGH;__ 
Instructs the system to write through any intermediate cache and go directly to disk. Windows can still cache write operations, but cannot lazily flush them.

## FILE_GENERIC_READ
 __const win32file.FILE_GENERIC_READ;__ 


## FILE_GENERIC_WRITE
 __const win32file.FILE_GENERIC_WRITE;__ 


## FILE_IS_ENCRYPTED
 __const win32file.FILE_IS_ENCRYPTED;__ 


## [win32file](#win32file).FILE_NOTIFY_INFORMATION

[(action, filename), ... = __FILE_NOTIFY_INFORMATION( *buffer*  *, size* __ )
Decodes a PyFILE_NOTIFY_INFORMATION buffer.

#### Parameters


  -  *buffer* : string

    The buffer to decode.

  -  *size* : int

    The number of bytes to refer to.  Generally this 

will be smaller than the size of the buffer (and certainly never greater!)

#### Comments
See[win32file::ReadDirectoryChangesW](win32file.md#win32filereaddirectorychangesw)for more information.

## FILE_READ_ONLY
 __const win32file.FILE_READ_ONLY;__ 


## FILE_ROOT_DIR
 __const win32file.FILE_ROOT_DIR;__ 


## FILE_SHARE_DELETE
 __const win32file.FILE_SHARE_DELETE;__ 
Windows NT only: Subsequent open operations on the object will succeed only if delete access is requested.

## FILE_SHARE_READ
 __const win32file.FILE_SHARE_READ;__ 
Subsequent open operations on the object will succeed only if read access is requested.

## FILE_SHARE_WRITE
 __const win32file.FILE_SHARE_WRITE;__ 
Subsequent open operations on the object will succeed only if write access is requested.

## FILE_SYSTEM_ATTR
 __const win32file.FILE_SYSTEM_ATTR;__ 


## FILE_SYSTEM_DIR
 __const win32file.FILE_SYSTEM_DIR;__ 


## FILE_SYSTEM_NOT_SUPPORT
 __const win32file.FILE_SYSTEM_NOT_SUPPORT;__ 


## FILE_TYPE_CHAR
 __const win32file.FILE_TYPE_CHAR;__ 
The specified file is a character file, typically an LPT device or a console.

## FILE_TYPE_DISK
 __const win32file.FILE_TYPE_DISK;__ 
The specified file is a disk file.

## FILE_TYPE_PIPE
 __const win32file.FILE_TYPE_PIPE;__ 
The specified file is either a named or anonymous pipe.

## FILE_TYPE_UNKNOWN
 __const win32file.FILE_TYPE_UNKNOWN;__ 
The type of the specified file is unknown.

## FILE_UNKNOWN
 __const win32file.FILE_UNKNOWN;__ 


## FILE_USER_DISALLOWED
 __const win32file.FILE_USER_DISALLOWED;__ 


## FileAllocationInfo
 __const win32file.FileAllocationInfo;__ 


## FileAttributeTagInfo
 __const win32file.FileAttributeTagInfo;__ 


## FileBasicInfo
 __const win32file.FileBasicInfo;__ 


## FileCompressionInfo
 __const win32file.FileCompressionInfo;__ 


## FileDispositionInfo
 __const win32file.FileDispositionInfo;__ 


## [win32file](#win32file).FileEncryptionStatus

int = __FileEncryptionStatus( *FileName* __ )
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
 __const win32file.FileEndOfFileInfo;__ 


## FileIdBothDirectoryInfo
 __const win32file.FileIdBothDirectoryInfo;__ 


## FileIdBothDirectoryRestartInfo
 __const win32file.FileIdBothDirectoryRestartInfo;__ 


## FileIdType
 __const win32file.FileIdType;__ 


## FileIoPriorityHintInfo
 __const win32file.FileIoPriorityHintInfo;__ 


## FileNameInfo
 __const win32file.FileNameInfo;__ 


## FileRenameInfo
 __const win32file.FileRenameInfo;__ 


## FileStandardInfo
 __const win32file.FileStandardInfo;__ 


## FileStreamInfo
 __const win32file.FileStreamInfo;__ 


## [win32file](#win32file).FindClose

 __FindClose( *hFindFile* __ )
Closes a find handle.

#### Parameters


  -  *hFindFile* : int

    file search handle

## [win32file](#win32file).FindCloseChangeNotification

 __FindCloseChangeNotification( *hChangeHandle* __ )
Closes a handle.

#### Parameters


  -  *hChangeHandle* : int

    handle to change notification to close

## [win32file](#win32file).FindFileNames

[[PyUnicode](#pyunicode),...] = __FindFileNames( *FileName*  *, Transaction* __ )
Enumerates hard links that point to specified file

#### Parameters


  -  *FileName* :[PyUnicode](#pyunicode)

    Name of file for which to find links

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Handle to a transaction, can be None

#### Comments
This uses the API functions FindFirstFileNameW, FindNextFileNameW and FindClose
Available on Vista and later
If Transaction is specified, a transacted search is performed using FindFirstFileNameTransacted

## [win32file](#win32file).FindFilesIterator

iterator = __FindFilesIterator( *FileName*  *, Transaction* __ )
Returns an interator based on 

FindFirstFile/FindNextFile. Similar to __win32file::FindFiles__ , but 

avoids the creation of the list for huge directories.

#### Parameters


  -  *FileName* : string

    A string that specifies a valid directory or path and filename, which can contain wildcard characters (* and ?).

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Handle to a transaction, can be None. 

If this parameter is not None, FindFirstFileTransacted will be called to perform a transacted search

#### Comments
Accepts keyword args.
FindFirstFileTransacted will be called if a transaction handle is passed in.

#### Return Value
The result is a Python iterator, with each next() method 

returning a[WIN32_FIND_DATA](WIN32.md#win32find_data)tuple.

## [win32file](#win32file).FindFilesW

list = __FindFilesW( *FileName*  *, Transaction* __ )
Retrieves a list of matching filenames, using the Windows Unicode API.  An interface to the API FindFirstFileW/FindNextFileW/Find close functions.

#### Parameters


  -  *FileName* : string

    A string that specifies a valid directory or path and filename, which can contain wildcard characters (* and ?).

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Transaction handle as returned by[win32transaction::CreateTransaction](win32transaction.md#win32transactioncreatetransaction).  Can be None. 

If this parameter is not None, FindFirstFileTransacted will be called to perform a transacted search

#### Comments
Accepts keyword args.
FindFirstFileTransacted will be called if a transaction handle is passed in.

#### Win32 API References


  - Search for *FindFirstFile* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=findfirstfile),[google](#http://www.google.com/search?q=findfirstfile)or[google groups](#http://groups.google.com/groups?q=findfirstfile).

  - Search for *FindFirstFileTransacted* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=findfirstfiletransacted),[google](#http://www.google.com/search?q=findfirstfiletransacted)or[google groups](#http://groups.google.com/groups?q=findfirstfiletransacted).

  - Search for *FindNextFile* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=findnextfile),[google](#http://www.google.com/search?q=findnextfile)or[google groups](#http://groups.google.com/groups?q=findnextfile).

  - Search for *FindClose* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=findclose),[google](#http://www.google.com/search?q=findclose)or[google groups](#http://groups.google.com/groups?q=findclose).

#### Return Value
The return value is a list of[WIN32_FIND_DATA](WIN32.md#win32find_data)tuples.

## [win32file](#win32file).FindFirstChangeNotification

int = __FindFirstChangeNotification( *pathName*  *, bWatchSubtree*  *, notifyFilter* __ )
Creates a change notification handle and sets up initial change notification filter conditions. A wait on a notification handle succeeds when a change matching the filter conditions occurs in the specified directory or subtree.

#### Parameters


  -  *pathName* :[PyUnicode](#pyunicode)

    Name of directory to watch

  -  *bWatchSubtree* : int

    flag for monitoring directory or directory tree

  -  *notifyFilter* : int

    filter conditions to watch for.  See[win32api::FindFirstChangeNotification](win32api.md#win32apifindfirstchangenotification)for details.

## [win32file](#win32file).FindNextChangeNotification

int = __FindNextChangeNotification( *hChangeHandle* __ )
Requests that the operating system signal a change notification handle the next time it detects an appropriate change,

#### Parameters


  -  *hChangeHandle* : int

    handle to change notification to signal

## [win32file](#win32file).FindStreams

[(long,[PyUnicode](#pyunicode)),...] = __FindStreams( *FileName*  *, Transaction* __ )
List the data streams for a file

#### Parameters


  -  *FileName* :[PyUnicode](#pyunicode)

    Name of file (or directory) to operate on

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Handle to a transaction, can be None

#### Comments
This uses the API functions FindFirstStreamW, FindNextStreamW and FindClose
Available on Windows Server 2003 and Vista
If the Transaction arg is not None, FindFirstStreamTransacted will be called in place of FindFirstStreamW

#### Return Value
Returns a list of tuples containing each stream's size and name

## [win32file](#win32file).FlushFileBuffers

 __FlushFileBuffers( *hFile* __ )
Clears the buffers for the specified file and causes all buffered data to be written to the file.

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)

    open handle to file whose buffers are to be flushed

## GENERIC_EXECUTE
 __const win32file.GENERIC_EXECUTE;__ 
Specifies execute access.

## GENERIC_READ
 __const win32file.GENERIC_READ;__ 
Specifies read access to the object. Data can be read from the file and the file pointer can be moved. Combine with GENERIC_WRITE for read-write access.

## GENERIC_WRITE
 __const win32file.GENERIC_WRITE;__ 
Specifies write access to the object. Data can be written to the file and the file pointer can be moved. Combine with GENERIC_READ for read-write access.

## [win32file](#win32file).GetAcceptExSockaddrs

(iFamily, __LocalSockAddr__ , __RemoteSockAddr__ ) = __GetAcceptExSockaddrs( *sAccepting*  *, buffer* __ )
Parses the connection endpoints from the buffer passed into AcceptEx

#### Parameters


  -  *sAccepting* : __PySocket__ /int

    Socket that was passed into the sAccepting parameter of AcceptEx

  -  *buffer* :[PyOVERLAPPEDReadBuffer](#pyoverlappedreadbuffer)

    Buffer you passed into AcceptEx

#### Comments
LocalSockAddr and RemoteSockAddr are ("xx.xx.xx.xx", port#) if iFamily == AF_INET
otherwise LocalSockAddr and RemoteSockAddr are just binary strings
and they should be unpacked with the struct module.

## [win32file](#win32file).GetBinaryType

int = __GetBinaryType( *appName* __ )
Determines whether a file is executable, and if so, what type of executable file it is. That last property determines which subsystem an executable file runs under.

#### Parameters


  -  *appName* :[PyUnicode](#pyunicode)

    Fully qualified path of file to test

## [win32file](#win32file).GetCommMask

int = __GetCommMask( *handle* __ )
Retrieves the value of the event mask for a specified communications device.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the communications device.

## [win32file](#win32file).GetCommModemStatus

int = __GetCommModemStatus( *handle* __ )
Retrieves modem control-register values.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the communications device.

## [win32file](#win32file).GetCommState

[PyDCB](#pydcb)= __GetCommState( *handle* __ )
Returns a device-control block (a DCB structure) with the current control settings for a specified communications device.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the communications device.

## [win32file](#win32file).GetCommTimeouts

 __PyCOMMTIMEOUTS__ = __GetCommTimeouts( *handle* __ )
Retrieves the time-out parameters for all read and write operations on a specified communications device.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the communications device.

## [win32file](#win32file).GetCompressedFileSize

long = __GetCompressedFileSize(__ )
Determines the compressed size of a file.

## [win32file](#win32file).GetDiskFreeSpace

(int, int, int, int) = __GetDiskFreeSpace( *rootPathName* __ )
Determines the free space on a device.

#### Parameters


  -  *rootPathName* :[PyUnicode](#pyunicode)

    address of root path

#### Return Value
The result is a tuple of integers representing (sectors per cluster, bytes per sector, number of free clusters, total number of clusters)

## [win32file](#win32file).GetDiskFreeSpaceEx

long, long, long = __GetDiskFreeSpaceEx( *rootPathName* __ )
Determines the free space on a device.

#### Parameters


  -  *rootPathName* :[PyUnicode](#pyunicode)

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

## [win32file](#win32file).GetDriveType

int = __GetDriveType( *rootPathName* __ )
Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive.

#### Parameters


  -  *rootPathName* : string

    

#### Return Value
The result is one of the DRIVE_* constants.

## [win32file](#win32file).GetDriveTypeW

int = __GetDriveTypeW( *rootPathName* __ )
Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive. (NT/2000 Unicode specific version).

#### Parameters


  -  *rootPathName* : string

    

#### Return Value
The result is one of the DRIVE_* constants.

## [win32file](#win32file).GetFileAttributes

int = __GetFileAttributes( *fileName* __ )
Determines a files attributes.

#### Parameters


  -  *fileName* :[PyUnicode](#pyunicode)

    Name of the file to retrieve attributes for.

#### Comments
The win32file module exposes[win32file::GetFileAttributes](win32file.md#win32filegetfileattributes)and[win32file::GetFileAttributesW](win32file.md#win32filegetfileattributesw)separately - both functions will accept 

either strings or Unicode objects but will always call the named function. 

This is different than[win32api::GetFileAttributes](win32api.md#win32apigetfileattributes), which only exposes 

one Python function and automatically calls the appropriate win32 function 

based on the type of the filename param.

## [win32file](#win32file).GetFileAttributesEx

tuple = __GetFileAttributesEx( *FileName*  *, InfoLevelId*  *, Transaction* __ )
Retrieves attributes for a specified file or directory.

#### Parameters


  -  *FileName* :[PyUnicode](#pyunicode)

    File or directory for which to retrieve information 

In the ANSI version of this function, the name is limited to 

MAX_PATH characters. To extend this limit to nearly 32,000 wide characters, 

call the Unicode version of the function ( __win32file::GetFileAttributesExW__ ) and prepend 

r"\\?\\" to the path.

  -  *InfoLevelId=GetFileExInfoStandard* : int

    An integer that gives the set of attribute information to obtain. 

See the Win32 SDK documentation for more information.

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Handle to a transaction (optional).  See[win32transaction::CreateTransaction](win32transaction.md#win32transactioncreatetransaction). 

If this parameter is specified, GetFileAttributesTransacted will be called (requires Vista or later).

#### Comments
Not all file systems can record creation and last access time and not all file systems record 

them in the same manner. For example, on Windows NT FAT, create time has a resolution of 

10 milliseconds, write time has a resolution of 2 seconds, and access time has a resolution 

of 1 day (really, the access date). On NTFS, access time has a resolution of 1 hour. 

Furthermore, FAT records times on disk in local time, while NTFS records times on disk in UTC, 

so it is not affected by changes in time zone or daylight saving time.
Accepts keyword arguments.

 __InfoLevelId__  __Information returned__ GetFileExInfoStandardTuple representing a WIN32_FILE_ATTRIBUTE_DATA struc
#### Win32 API References


  - Search for *GetFileAttributesEx* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=getfileattributesex),[google](#http://www.google.com/search?q=getfileattributesex)or[google groups](#http://groups.google.com/groups?q=getfileattributesex).

  - Search for *GetFileAttributesTransacted* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=getfileattributestransacted),[google](#http://www.google.com/search?q=getfileattributestransacted)or[google groups](#http://groups.google.com/groups?q=getfileattributestransacted).

#### Return Value
The result is a tuple of:

#### Items


  - [0] *int* : attributes

    File Attributes.  A combination of the win32com.FILE_ATTRIBUTE_* flags.

  - [1] *[PyTime](#pytime)* : creationTime

    Specifies when the file or directory was created.

  - [2] *[PyTime](#pytime)* : lastAccessTime

    For a file, specifies when the file was last read from 

or written to. For a directory, the structure specifies when the directory was created. For 

both files and directories, the specified date will be correct, but the time of day will 

always be set to midnight.

  - [3] *[PyTime](#pytime)* : lastWriteTime

    For a file, the structure specifies when the file was last 

written to. For a directory, the structure specifies when the directory was created.

  - [4] *int/long* : fileSize

    The size of the file. This member has no meaning for directories.

## [win32file](#win32file).GetFileAttributesW

int = __GetFileAttributesW( *fileName* __ )
Determines a files attributes (NT/2000 Unicode specific version).

#### Parameters


  -  *fileName* :[PyUnicode](#pyunicode)

    Name of the file to retrieve attributes for.

#### Comments
Note that[win32api::GetFileAttributes](win32api.md#win32apigetfileattributes)will automatically call 

GetFileAttributesW when passed a unicode filename param.  See[win32file::GetFileAttributes](win32file.md#win32filegetfileattributes)and[win32api::GetFileAttributes](win32api.md#win32apigetfileattributes)for more.

## GetFileExInfoStandard
 __const win32file.GetFileExInfoStandard;__ 


## [win32file](#win32file).GetFileInformationByHandle

tuple = __GetFileInformationByHandle( *handle* __ )
Retrieves file information for a specified file.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)/int

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

    

  - [1] *[PyTime](#pytime)* : ftCreationTime

    

  - [2] *[PyTime](#pytime)* : ftLastAccessTime

    

  - [3] *[PyTime](#pytime)* : ftLastWriteTime

    

  - [4] *int* : dwVolumeSerialNumber

    

  - [5] *int* : nFileSizeHigh

    

  - [6] *int* : nFileSizeLow

    

  - [7] *int* : nNumberOfLinks

    

  - [8] *int* : nFileIndexHigh

    

  - [9] *int* : nFileIndexLow

    

## [win32file](#win32file).GetFileInformationByHandleEx

object = __GetFileInformationByHandleEx( *File*  *, FileInformationClass* __ )
Retrieves extended file information for an open file handle.

#### Parameters


  -  *File* :[PyHANDLE](#pyhandle)

    Handle to a file or directory.  Do not pass a pipe handle.

  -  *FileInformationClass* : int

    Type of data to return, one of win32file.File*Info values

#### Comments
Available on Vista and later.
Accepts keyword args.

#### Return Value
Type of returned object is determined by the requested information class


## [win32file](#win32file).GetFileSize

long = __GetFileSize(__ )
Determines the size of a file.

## [win32file](#win32file).GetFileTime

([PyTime](#pytime),[PyTime](#pytime),[PyTime](#pytime)) = __GetFileTime( *handle*  *, creationTime*  *, accessTime*  *, writeTime* __ )
Returns a file's creation, last access, and modification times.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    Handle to the file.

  -  *creationTime* :[PyTime](#pytime)

    

  -  *accessTime* :[PyTime](#pytime)

    

  -  *writeTime* :[PyTime](#pytime)

    

#### Comments
Times are returned in UTC time.

## [win32file](#win32file).GetFileType

int = __GetFileType( *hFile* __ )
Determines the type of a file.

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)

    The handle to the file.

## [win32file](#win32file).GetFinalPathNameByHandle

[PyUnicode](#pyunicode)= __GetFinalPathNameByHandle( *File*  *, Flags* __ )
Returns the file name for an open file handle

#### Parameters


  -  *File* :[PyHANDLE](#pyhandle)

    An open file handle

  -  *Flags* : int

    Specifies type of path to return. (win32con.FILE_NAME_NORMALIZED,FILE_NAME_OPENED,VOLUME_NAME_DOS,VOLUME_NAME_GUID,VOLUME_NAME_NONE,VOLUME_NAME_NT)

#### Comments
Exists on Windows Vista or later.
Accepts keyword arguments.

#### Win32 API References


  - Search for *GetFinalPathNameByHandle* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=getfinalpathnamebyhandle),[google](#http://www.google.com/search?q=getfinalpathnamebyhandle)or[google groups](#http://groups.google.com/groups?q=getfinalpathnamebyhandle).

## [win32file](#win32file).GetFullPathName

str/unicode = __GetFullPathName( *FileName*  *, Transaction* __ )
Returns full path for path passed in

#### Parameters


  -  *FileName* : str/unicode

    Path on which to operate

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Handle to a transaction as returned by[win32transaction::CreateTransaction](win32transaction.md#win32transactioncreatetransaction)

#### Comments
This function takes either a plain string or a unicode string, and returns the same type 

If unicode is passed in, GetFullPathNameW is called, which supports filenames longer than MAX_PATH
If Transaction parameter is specified, GetFullPathNameTransacted is called (requires Vista or later)

## [win32file](#win32file).GetLogicalDrives

int = __GetLogicalDrives(__ )
Returns a bitmaks of the logical drives installed.

## [win32file](#win32file).GetLongPathName

[PyUnicode](#pyunicode)= __GetLongPathName( *ShortPath*  *, Transaction* __ )
Retrieves the long path for a short path (8.3 filename)

#### Parameters


  -  *ShortPath* :[PyUnicode](#pyunicode)

    8.3 path to be expanded

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Handle to a transaction.  If specified, GetLongPathNameTransacted will be called.

#### Comments
Accepts keyword args

## [win32file](#win32file).GetMailslotInfo

(int,int,int,int) = __GetMailslotInfo( *Mailslot* __ )
Retrieves information about a mailslot

#### Parameters


  -  *Mailslot* :[PyHANDLE](#pyhandle)

    Handle to a mailslot

#### Win32 API References


  - Search for *GetMailslotInfo* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=getmailslotinfo),[google](#http://www.google.com/search?q=getmailslotinfo)or[google groups](#http://groups.google.com/groups?q=getmailslotinfo).

#### Return Value
Returns (maximum message size, next message size, message count, timeout)

## [win32file](#win32file).GetOverlappedResult

int = __GetOverlappedResult( *hFile*  *, overlapped*  *, bWait* __ )
Determines the result of the most recent call with an OVERLAPPED object.

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)

    The handle to the pipe or file

  -  *overlapped* :[PyOVERLAPPED](#pyoverlapped)

    The overlapped object to check.

  -  *bWait* : int

    Indicates if the function should wait for data to become available.

#### Comments
The result is the number of bytes transferred.  The overlapped object's attributes will be changed during this call.

## [win32file](#win32file).GetQueuedCompletionStatus

(int, int, int,[PyOVERLAPPED](#pyoverlapped)) = __GetQueuedCompletionStatus( *hPort*  *, timeOut* __ )
Attempts to dequeue an I/O completion packet from a specified input/output completion port.

#### Parameters


  -  *hPort* :[PyHANDLE](#pyhandle)

    The handle to the completion port.

  -  *timeOut* : int

    Timeout in milli-seconds.

#### Comments
This method never throws an API error.
The result is a tuple of (rc, numberOfBytesTransferred, completionKey, overlapped)
If the function succeeds, rc will be set to 0, otherwise it will be set to the win32 error code.

## [win32file](#win32file).GetVolumeNameForVolumeMountPoint

[PyUnicode](#pyunicode)= __GetVolumeNameForVolumeMountPoint( *VolumeMountPoint* __ )
Returns unique volume name.

#### Parameters


  -  *VolumeMountPoint* :[PyUnicode](#pyunicode)

    Volume mount point or root drive - trailing backslash required

#### Comments
Requires Win2K or later.
Accepts keyword args.

## [win32file](#win32file).GetVolumePathName

[PyUnicode](#pyunicode)= __GetVolumePathName( *FileName*  *, BufferLength* __ )
Returns volume mount point for a path

#### Parameters


  -  *FileName* :[PyUnicode](#pyunicode)

    File/dir for which to return volume mount point

  -  *BufferLength=0* : int

    Optional parm to allocate extra space for returned string

#### Comments
Api gives no indication of how much memory is needed, so function assumes returned path 

will not be longer that length of input path + 1. 

Use GetFullPathName first for relative paths, or GetLongPathName for 8.3 paths. 

Optional second parm can also be used to override the buffer size for returned path
Accepts keyword args.

## [win32file](#win32file).GetVolumePathNamesForVolumeName

[[PyUnicode](#pyunicode),...] = __GetVolumePathNamesForVolumeName( *VolumeName* __ )
Returns mounted paths for a volume

#### Parameters


  -  *VolumeName* :[PyUnicode](#pyunicode)

    Name of a volume as returned by[win32file::GetVolumeNameForVolumeMountPoint](win32file.md#win32filegetvolumenameforvolumemountpoint)

#### Comments
Requires WinXP or later
Accepts keyword args

## IoPriorityHintLow
 __const win32file.IoPriorityHintLow;__ 


## IoPriorityHintNormal
 __const win32file.IoPriorityHintNormal;__ 


## IoPriorityHintVeryLow
 __const win32file.IoPriorityHintVeryLow;__ 


## [win32file](#win32file).LockFile

 __LockFile( *hFile*  *, offsetLow*  *, offsetHigh*  *, nNumberOfBytesToLockLow*  *, nNumberOfBytesToLockHigh* __ )
Locks a specified file for exclusive access by the calling process.

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)

    handle of file to lock

  -  *offsetLow* : int

    low-order word of lock region offset

  -  *offsetHigh* : int

    high-order word of lock region offset

  -  *nNumberOfBytesToLockLow* : int

    low-order word of length to lock

  -  *nNumberOfBytesToLockHigh* : int

    high-order word of length to lock

## [win32file](#win32file).LockFileEx

 __LockFileEx( *hFile*  *, int*  *, int*  *, int*  *, ol* __ )
Locks a file. Wrapper for LockFileEx win32 API.

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)/int

    Handle to the file

  -  *int* : dwFlags

    Flags that specify exclusive/shared and blocking/non-blocking mode

  -  *int* : nbytesLow

    low-order part of number of bytes to lock

  -  *int* : nbytesHigh

    high-order part of number of bytes to lock

  -  *ol=None* :[PyOVERLAPPED](#pyoverlapped)

    An overlapped structure

## MARKPARITY
 __const win32file.MARKPARITY;__ 


## MOVEFILE_COPY_ALLOWED
 __const win32file.MOVEFILE_COPY_ALLOWED;__ 
If the file is to be moved to a different volume, the function simulates the move by using the CopyFile and DeleteFile functions. Cannot be combined with the MOVEFILE_DELAY_UNTIL_REBOOT flag.

## MOVEFILE_CREATE_HARDLINK
 __const win32file.MOVEFILE_CREATE_HARDLINK;__ 


## MOVEFILE_DELAY_UNTIL_REBOOT
 __const win32file.MOVEFILE_DELAY_UNTIL_REBOOT;__ 
Windows NT only: The function does not move the file until the operating system is restarted. The system moves the file immediately after AUTOCHK is executed, but before creating any paging files. Consequently, this parameter enables the function to delete paging files from previous startups.

## MOVEFILE_FAIL_IF_NOT_TRACKABLE
 __const win32file.MOVEFILE_FAIL_IF_NOT_TRACKABLE;__ 


## MOVEFILE_REPLACE_EXISTING
 __const win32file.MOVEFILE_REPLACE_EXISTING;__ 
If a file of the name specified by lpNewFileName already exists, the function replaces its contents with those specified by lpExistingFileName.

## MOVEFILE_WRITE_THROUGH
 __const win32file.MOVEFILE_WRITE_THROUGH;__ 
Windows NT only: The function does not return until the file has actually been moved on the disk. Setting this flag guarantees that a move perfomed as a copy and delete operation is flushed to disk before the function returns. The flush occurs at the end of the copy operation.
This flag has no effect if the MOVEFILE_DELAY_UNTIL_REBOOT flag is set.

## [win32file](#win32file).MoveFile

 __MoveFile( *existingFileName*  *, newFileName* __ )
Renames an existing file or a directory (including all its children).

#### Parameters


  -  *existingFileName* :[PyUnicode](#pyunicode)

    Name of the existing file

  -  *newFileName* :[PyUnicode](#pyunicode)

    New name for the file

## [win32file](#win32file).MoveFileEx

 __MoveFileEx( *existingFileName*  *, newFileName*  *, flags* __ )
Renames an existing file or a directory (including all its children).

#### Parameters


  -  *existingFileName* :[PyUnicode](#pyunicode)

    Name of the existing file

  -  *newFileName* :[PyUnicode](#pyunicode)

    New name for the file, can be None for delayed delete operation

  -  *flags* : int

    flag to determine how to move file (win32file.MOVEFILE_*)

## [win32file](#win32file).MoveFileExW

 __MoveFileExW( *existingFileName*  *, newFileName*  *, flags* __ )
Renames an existing file or a directory (including all its children). (NT/2000 Unicode specific version).

#### Parameters


  -  *existingFileName* :[PyUnicode](#pyunicode)

    Name of the existing file

  -  *newFileName* :[PyUnicode](#pyunicode)

    New name for the file, can be None for delayed delete operation

  -  *flags* : int

    flag to determine how to move file (win32file.MOVEFILE_*)

## [win32file](#win32file).MoveFileW

 __MoveFileW( *existingFileName*  *, newFileName* __ )
Renames an existing file or a directory (including all its children). (NT/2000 Unicode specific version).

#### Parameters


  -  *existingFileName* :[PyUnicode](#pyunicode)

    Name of the existing file

  -  *newFileName* :[PyUnicode](#pyunicode)

    New name for the file

## [win32file](#win32file).MoveFileWithProgress

 __MoveFileWithProgress( *ExistingFileName*  *, NewFileName*  *, ProgressRoutine*  *, Data*  *, Flags*  *, Transaction* __ )
Moves a file, and reports progress to a callback function

#### Parameters


  -  *ExistingFileName* :[PyUNICODE](#pyunicode)

    File or directory to be moved

  -  *NewFileName* :[PyUNICODE](#pyunicode)

    Destination, can be None if flags contain MOVEFILE_DELAY_UNTIL_REBOOT

  -  *ProgressRoutine=None* :[CopyProgressRoutine](#copyprogressroutine)

    A python function that receives progress updates, can be None

  -  *Data=None* : object

    An arbitrary object to be passed to the callback function

  -  *Flags=0* : int

    Combination of MOVEFILE_* flags

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Handle to a transaction (optional).  See[win32transaction::CreateTransaction](win32transaction.md#win32transactioncreatetransaction).

#### Comments
Only available on Windows 2000 or later
Accepts keyword arguments.
On Vista and later, the Transaction arg can be passed to invoke MoveFileTransacted

## NOPARITY
 __const win32file.NOPARITY;__ 


## ODDPARITY
 __const win32file.ODDPARITY;__ 


## ONE5STOPBITS
 __const win32file.ONE5STOPBITS;__ 


## ONESTOPBIT
 __const win32file.ONESTOPBIT;__ 


## OPEN_ALWAYS
 __const win32file.OPEN_ALWAYS;__ 
Opens the file, if it exists. If the file does not exist, the function creates the file as if dwCreationDistribution were CREATE_NEW.

## OPEN_EXISTING
 __const win32file.OPEN_EXISTING;__ 
Opens the file. The function fails if the file does not exist.

## OVERWRITE_HIDDEN
 __const win32file.OVERWRITE_HIDDEN;__ 


## ObjectIdType
 __const win32file.ObjectIdType;__ 


## [win32file](#win32file).OpenEncryptedFileRaw

PyCObject = __OpenEncryptedFileRaw( *FileName*  *, Flags* __ )
Initiates a backup or restore operation on an encrypted file

#### Parameters


  -  *FileName* :[PyUNICODE](#pyunicode)

    Name of file on which to operate

  -  *Flags* : int

    CREATE_FOR_IMPORT, CREATE_FOR_DIR, OVERWRITE_HIDDEN, or 0 for export

#### Comments
Only available on Windows 2000 or later

#### Return Value
Returns a PyCObject containing an operation context that can be passed to[win32file::ReadEncryptedFileRaw](win32file.md#win32filereadencryptedfileraw)or[win32file::WriteEncryptedFileRaw](win32file.md#win32filewriteencryptedfileraw).  Context must be 

destroyed using[win32file::CloseEncryptedFileRaw](win32file.md#win32filecloseencryptedfileraw).

## [win32file](#win32file).OpenFileById

[PyHANDLE](#pyhandle)= __OpenFileById( *File*  *, FileId*  *, DesiredAccess*  *, ShareMode*  *, Flags*  *, SecurityAttributes* __ )
Opens a file by File Id or Object Id

#### Parameters


  -  *File* :[PyHANDLE](#pyhandle)

    Handle to a file on the volume that contains the file to open

  -  *FileId* : int/[PyIID](#pyiid)

    File Id or Object Id of the file to open

  -  *DesiredAccess* : int

    Access mode

  -  *ShareMode* : int

    Sharing mode (FILE_SHARE_*)

  -  *Flags* : int

    Combination of FILE_FLAG_* flags

  -  *SecurityAttributes=None* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Reserved, use only None

#### Comments
Available on Vista and later.
Accepts keyword args.

## PROGRESS_CANCEL
 __const win32file.PROGRESS_CANCEL;__ 


## PROGRESS_CONTINUE
 __const win32file.PROGRESS_CONTINUE;__ 


## PROGRESS_QUIET
 __const win32file.PROGRESS_QUIET;__ 


## PROGRESS_STOP
 __const win32file.PROGRESS_STOP;__ 


## PURGE_RXABORT
 __const win32file.PURGE_RXABORT;__ 
Terminates all outstanding overlapped read operations and returns immediately, even if the read operations have not been completed.

## PURGE_RXCLEAR
 __const win32file.PURGE_RXCLEAR;__ 
Clears the input buffer (if the device driver has one).

## PURGE_TXABORT
 __const win32file.PURGE_TXABORT;__ 
Terminates all outstanding overlapped write operations and returns immediately, even if the write operations have not been completed.

## PURGE_TXCLEAR
 __const win32file.PURGE_TXCLEAR;__ 
Clears the output buffer (if the device driver has one).

## [win32file](#win32file).PostQueuedCompletionStatus

None = __PostQueuedCompletionStatus( *handle*  *, numberOfbytes*  *, completionKey*  *, overlapped* __ )
lets you post an I/O completion packet to an I/O completion port. The I/O completion packet will satisfy an outstanding call to the GetQueuedCompletionStatus function.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    handle to an I/O completion port

  -  *numberOfbytes=0* : int

    value to return via GetQueuedCompletionStatus' first result

  -  *completionKey=0* : int

    value to return via GetQueuedCompletionStatus' second result

  -  *overlapped=None* :[PyOVERLAPPED](#pyoverlapped)

    value to return via GetQueuedCompletionStatus' third result

#### Comments
Note that if you post overlapped objects, but your post is closed 

before all pending requests are processed, the overlapped objects 

(including its 'handle' and 'object' members) will leak. 

See MS KB article Q192800 for a summary of this.

## [win32file](#win32file).PurgeComm

 __PurgeComm( *handle*  *, action* __ )
Discards all characters from the output or input buffer of a specified communications resource. It can also terminate pending read or write operations on the resource.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the communications device.

  -  *action* : int

    The action to perform.  This parameter can be one or more of the following values.


## [win32file](#win32file).QueryDosDevice

string = __QueryDosDevice( *DeviceName* __ )
Returns the mapping for a device name, or all device names

#### Parameters


  -  *DeviceName* : string

    Name of device to query, or None to return all defined devices

#### Return Value
Returns a string containing substrings separated by NULLs with 2 terminating NULLs

## [win32file](#win32file).QueryRecoveryAgentsOnEncryptedFile

([PySID](#pysid),string,unicode) = __QueryRecoveryAgentsOnEncryptedFile( *FileName* __ )
Lists recovery agents for file as a tuple of tuples.

#### Parameters


  -  *FileName* : string/unicode

    file to query

#### Return Value
The result is a tuple of tuples - ((SID, certificate hash blob, display info),....)

## [win32file](#win32file).QueryUsersOnEncryptedFile

([PySID](#pysid),string,unicode) = __QueryUsersOnEncryptedFile( *FileName* __ )
Returns list of users for an encrypted file as tuples of (SID, certificate hash blob, display info)

#### Parameters


  -  *FileName* : string/unicode

    file to query

## REPLACEFILE_IGNORE_MERGE_ERRORS
 __const win32file.REPLACEFILE_IGNORE_MERGE_ERRORS;__ 


## REPLACEFILE_WRITE_THROUGH
 __const win32file.REPLACEFILE_WRITE_THROUGH;__ 


## RTS_CONTROL_DISABLE
 __const win32file.RTS_CONTROL_DISABLE;__ 
Disables the RTS line when the device is opened and leaves it disabled.

## RTS_CONTROL_ENABLE
 __const win32file.RTS_CONTROL_ENABLE;__ 
Enables the RTS line when the device is opened and leaves it on.

## RTS_CONTROL_HANDSHAKE
 __const win32file.RTS_CONTROL_HANDSHAKE;__ 
Enables RTS handshaking. The driver raises the RTS line when the "type-ahead" (input) buffer is less than one-half full and lowers the RTS line when the buffer is more than three-quarters full. If handshaking is enabled, it is an error for the application to adjust the line by using the EscapeCommFunction function.

## RTS_CONTROL_TOGGLE
 __const win32file.RTS_CONTROL_TOGGLE;__ 
Specifies that the RTS line will be high if bytes are available for transmission. After all buffered bytes have been sent, the RTS line will be low.

## [win32file](#win32file).ReOpenFile

[PyHANDLE](#pyhandle)= __ReOpenFile( *OriginalFile*  *, DesiredAccess*  *, ShareMode*  *, Flags* __ )
Creates a new handle to an open file

#### Parameters


  -  *OriginalFile* :[PyHANDLE](#pyhandle)

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

## [win32file](#win32file).ReadDirectoryChangesW

 __ReadDirectoryChangesW( *handle*  *, size*  *, bWatchSubtree*  *, dwNotifyFilter*  *, overlapped* __ )
retrieves information describing the changes occurring within a directory.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    Handle to the directory to be monitored. This directory must be opened with the FILE_LIST_DIRECTORY access right.

  -  *size* : int

    Size of the buffer to allocate for the results.

  -  *bWatchSubtree* : int

    Specifies whether the ReadDirectoryChangesW function will monitor the directory or the directory tree. If TRUE is specified, the function monitors the directory tree rooted at the specified directory. If FALSE is specified, the function monitors only the directory specified by the hDirectory parameter.

  -  *dwNotifyFilter* : int

    Specifies filter criteria the function checks to determine if the wait operation has completed. This parameter can be one or more of the FILE_NOTIFY_CHANGE_* values.

  -  *overlapped=None* :[PyOVERLAPPED](#pyoverlapped)

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

The buffer can then be passed to[win32file::FILE_NOTIFY_INFORMATION](win32file.md#win32filefile_notify_information)

## [win32file](#win32file).ReadEncryptedFileRaw

 __ReadEncryptedFileRaw( *ExportCallback*  *, CallbackContext*  *, Context* __ )
Reads the encrypted bytes of a file for backup and restore purposes

#### Parameters


  -  *ExportCallback* :[ExportCallBack](#exportcallback)

    Python function that receives chunks of data as it is read

  -  *CallbackContext* : object

    Arbitrary Python object to be passed to callback function

  -  *Context* : PyCObject

    Context object returned from[win32file::OpenEncryptedFileRaw](win32file.md#win32fileopenencryptedfileraw)

#### Comments
Only available on Windows 2000 or later

## [win32file](#win32file).ReadFile

(int, string) = __ReadFile( *hFile*  *, buffer/bufSize*  *, overlapped* __ )
Reads a string from a file

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)/int

    Handle to the file

  -  *buffer/bufSize* :[PyOVERLAPPEDReadBuffer](#pyoverlappedreadbuffer)/int

    Size of the buffer to create for the result, 

or a buffer to fill with the result. If a buffer object and overlapped is passed, the result is 

the buffer itself.  If a buffer but no overlapped is passed, the result is a new string object, 

built from the buffer, but with a length that reflects the data actually read.

  -  *overlapped=None* :[PyOVERLAPPED](#pyoverlapped)

    An overlapped structure

#### Comments
in a multi-threaded overlapped environment, it is likely to be necessary to pre-allocate the read buffer using the[win32file::AllocateReadBuffer](win32file.md#win32fileallocatereadbuffer)method, otherwise the I/O operation may complete before you can assign to the resulting buffer.

#### Return Value
The result is a tuple of (hr, string/[PyOVERLAPPEDReadBuffer](#pyoverlappedreadbuffer)), where hr may be 

0, ERROR_MORE_DATA or ERROR_IO_PENDING. 

If the overlapped param is not None, then the result is a[PyOVERLAPPEDReadBuffer](#pyoverlappedreadbuffer).  Once the overlapped IO operation 

has completed, you can convert this to a string (str(object)) [py2k] or (bytes(object)) [py3k] to obtain the data. 

While the operation is in progress, you can use the slice operations (object[:end]) to 

obtain the data read so far. 

You must use the OVERLAPPED API functions to determine how much of the data is valid.

## [win32file](#win32file).RemoveDirectory

 __RemoveDirectory( *PathName*  *, Transaction* __ )
Removes an existing directory

#### Parameters


  -  *PathName* :[PyUnicode](#pyunicode)

    Name of directory to be removed

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Handle to a transaction (optional). See[win32transaction::CreateTransaction](win32transaction.md#win32transactioncreatetransaction).

#### Comments
If a transaction handle is passed in, RemoveDirectoryTransacted will be called (requires Vista or later)
Accepts keyword arguments.  Implemented only as Unicode.

#### Win32 API References


  - Search for *RemoveDirectory* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=removedirectory),[google](#http://www.google.com/search?q=removedirectory)or[google groups](#http://groups.google.com/groups?q=removedirectory).

  - Search for *RemoveDirectoryTransacted* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=removedirectorytransacted),[google](#http://www.google.com/search?q=removedirectorytransacted)or[google groups](#http://groups.google.com/groups?q=removedirectorytransacted).

## [win32file](#win32file).RemoveUsersFromEncryptedFile

 __RemoveUsersFromEncryptedFile( *FileName*  *, pHashes* __ )
Removes specified certificates from file - if certificate is not found, it is ignored

#### Parameters


  -  *FileName* : string/unicode

    File from which to remove users

  -  *pHashes* : (([PySID](#pysid),string,unicode),...)

    Sequence representing an ENCRYPTION_CERTIFICATE_HASH_LIST structure, as returned by QueryUsersOnEncryptedFile

## [win32file](#win32file).ReplaceFile

 __ReplaceFile( *ReplacedFileName*  *, ReplacementFileName*  *, BackupFileName*  *, ReplaceFlags*  *, Exclude*  *, Reserved* __ )
Replaces one file with another

#### Parameters


  -  *ReplacedFileName* :[PyUNICODE](#pyunicode)

    File to be replaced

  -  *ReplacementFileName* :[PyUNICODE](#pyunicode)

    File that will replace it

  -  *BackupFileName=None* :[PyUNICODE](#pyunicode)

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
 __const win32file.SCS_32BIT_BINARY;__ 
A Win32-based application

## SCS_DOS_BINARY
 __const win32file.SCS_DOS_BINARY;__ 
An MS-DOS - based application

## SCS_OS216_BINARY
 __const win32file.SCS_OS216_BINARY;__ 
A 16-bit OS/2-based application

## SCS_PIF_BINARY
 __const win32file.SCS_PIF_BINARY;__ 
A PIF file that executes an MS-DOS - based application

## SCS_POSIX_BINARY
 __const win32file.SCS_POSIX_BINARY;__ 
A POSIX - based application

## SCS_WOW_BINARY
 __const win32file.SCS_WOW_BINARY;__ 
A 16-bit Windows-based application

## SECURITY_ANONYMOUS
 __const win32file.SECURITY_ANONYMOUS;__ 
Specifies to impersonate the client at the Anonymous impersonation level.

## SECURITY_CONTEXT_TRACKING
 __const win32file.SECURITY_CONTEXT_TRACKING;__ 
Specifies that the security tracking mode is dynamic. If this flag is not specified, Security Tracking Mode is static.

## SECURITY_DELEGATION
 __const win32file.SECURITY_DELEGATION;__ 
Specifies to impersonate the client at the Delegation impersonation level.

## SECURITY_EFFECTIVE_ONLY
 __const win32file.SECURITY_EFFECTIVE_ONLY;__ 
Specifies that only the enabled aspects

## SECURITY_IDENTIFICATION
 __const win32file.SECURITY_IDENTIFICATION;__ 
Specifies to impersonate the client at the Identification impersonation level.

## SECURITY_IMPERSONATION
 __const win32file.SECURITY_IMPERSONATION;__ 
Specifies to impersonate the client at the Impersonation impersonation level.

## SETBREAK
 __const win32file.SETBREAK;__ 
Suspends character transmission and places the transmission line in a break state until the ClearCommBreak function is called (or EscapeCommFunction is called with the CLRBREAK extended function code). The SETBREAK extended function code is identical to the SetCommBreak function. Note that this extended function does not flush data that has not been transmitted.

## SETDTR
 __const win32file.SETDTR;__ 
Sends the DTR (data-terminal-ready) signal.

## SETRTS
 __const win32file.SETRTS;__ 
Sends the RTS (request-to-send) signal.

## SETXOFF
 __const win32file.SETXOFF;__ 
Causes transmission to act as if an XOFF character has been received.

## SETXON
 __const win32file.SETXON;__ 
Causes transmission to act as if an XON character has been received.

## SO_CONNECT_TIME
 __const win32file.SO_CONNECT_TIME;__ 


## SO_UPDATE_ACCEPT_CONTEXT
 __const win32file.SO_UPDATE_ACCEPT_CONTEXT;__ 


## SO_UPDATE_CONNECT_CONTEXT
 __const win32file.SO_UPDATE_CONNECT_CONTEXT;__ 


## SPACEPARITY
 __const win32file.SPACEPARITY;__ 


## SYMBOLIC_LINK_FLAG_DIRECTORY
 __const win32file.SYMBOLIC_LINK_FLAG_DIRECTORY;__ 


## [win32file](#win32file).SetCommBreak

 __SetCommBreak( *handle* __ )
Suspends character transmission for a specified communications device and places the transmission line in a break state until the[win32file::ClearCommBreak](win32file.md#win32fileclearcommbreak)function is called.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the communications device.

## [win32file](#win32file).SetCommMask

int = __SetCommMask( *handle*  *, val* __ )
Sets the value of the event mask for a specified communications device.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the communications device.

  -  *val* : int

    The new mask value.

## [win32file](#win32file).SetCommState

 __SetCommState( *handle*  *, dcb* __ )
Configures a communications device according to the specifications in a device-control block. 

The function reinitializes all hardware and control settings, but it does not empty output or input queues.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the communications device.

  -  *dcb* :[PyDCB](#pydcb)

    The control settings.

## [win32file](#win32file).SetCommTimeouts

int = __SetCommTimeouts( *handle*  *, val* __ )
Sets the time-out parameters for all read and write operations on a specified communications device.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the communications device.

  -  *val* : __PyCOMMTIMEOUTS__ 

    The new time-out parameters.

## [win32file](#win32file).SetCurrentDirectory

 __SetCurrentDirectory( *lpPathName* __ )
Sets the current directory.

#### Parameters


  -  *lpPathName* : str/[PyUnicode](#pyunicode)

    Name of the path to set current.

## [win32file](#win32file).SetEndOfFile

 __SetEndOfFile( *hFile* __ )
Moves the end-of-file (EOF) position for the specified file to the current position of the file pointer.

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)

    handle of file whose EOF is to be set

## [win32file](#win32file).SetFileApisToANSI

 __SetFileApisToANSI(__ )
Causes a set of Win32 file functions to use the ANSI character set code page. This function is useful for 8-bit console input and output operations.

## [win32file](#win32file).SetFileApisToOEM

 __SetFileApisToOEM(__ )
Causes a set of Win32 file functions to use the OEM character set code page. This function is useful for 8-bit console input and output operations.

## [win32file](#win32file).SetFileAttributes

 __SetFileAttributes( *filename*  *, newAttributes* __ )
Changes a file's attributes.

#### Parameters


  -  *filename* :[PyUnicode](#pyunicode)

    filename

  -  *newAttributes* : int

    attributes to set

## [win32file](#win32file).SetFileAttributesW

 __SetFileAttributesW( *FileName*  *, FileAttributes*  *, Transaction* __ )
Sets a file's attributes

#### Parameters


  -  *FileName* :[PyUNICODE](#pyunicode)

    File or directory whose attributes are to be changed

  -  *FileAttributes* : int

    Combination of FILE_ATTRIBUTE_* flags

  -  *Transaction=None* :[PyHANDLE](#pyhandle)

    Handle to the transaction.  See[win32transaction::CreateTransaction](win32transaction.md#win32transactioncreatetransaction).

#### Comments
If Transaction is not None, SetFileAttributesTransacted will be called (requires Vista or later)
Accepts keyword arguments.

#### Win32 API References


  - Search for *SetFileAttributes* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=setfileattributes),[google](#http://www.google.com/search?q=setfileattributes)or[google groups](#http://groups.google.com/groups?q=setfileattributes).

  - Search for *SetFileAttributesTransacted* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=setfileattributestransacted),[google](#http://www.google.com/search?q=setfileattributestransacted)or[google groups](#http://groups.google.com/groups?q=setfileattributestransacted).

## [win32file](#win32file).SetFileInformationByHandle

 __SetFileInformationByHandle( *File*  *, FileInformationClass*  *, Information* __ )
Changes file characteristics by file handle

#### Parameters


  -  *File* :[PyHANDLE](#pyhandle)

    Handle to a file or directory.  Do not pass a pipe handle.

  -  *FileInformationClass* : int

    Type of data, one of win32file.File*Info values

  -  *Information* : object

    Type is dependent on the class to be changed

 __Class__  __Type of input__ FileBasicInfoDict representing a FILE_BASIC_INFO struct, containing 

{"CreationTime":[PyTime](#pytime), "LastAccessTime":[PyTime](#pytime),  "LastWriteTime":[PyTime](#pytime), 

"ChangeTime":[PyTime](#pytime), "FileAttributes":int}FileRenameInfoDict representing a FILE_RENAME_INFO struct, containing 

{"ReplaceIfExists":boolean, "RootDirectory":[PyHANDLE](#pyhandle), "FileName":str} 

MSDN says the RootDirectory is "A handle to the root directory in which the file to be renamed is located". 

However, this is actually the destination dir, can be None to stay in same dir.FileDispositionInfoBoolean indicating if file should be deleted when handle is closedFileAllocationInfoInt giving the allocation size.FileEndOfFileInfoInt giving the EOF position, cannot be greater than allocated size.FileIoPriorityHintInfoInt containing the IO priority (IoPriorityHint*)
#### Comments
Available on Vista and later.
Accepts keyword args.

## [win32file](#win32file).SetFilePointer

 __SetFilePointer( *handle*  *, offset*  *, moveMethod* __ )
Moves the file pointer of an open file.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The file to perform the operation on.

  -  *offset* : __Py_LARGEINTEGER__ 

    Offset to move the file pointer.

  -  *moveMethod* : int

    Starting point for the file pointer move. This parameter can be one of the following values.


## [win32file](#win32file).SetFileShortName

 __SetFileShortName( *hFile*  *, ShortName* __ )
Set the 8.3 name of a file

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)

    Handle to a file or directory

  -  *ShortName* :[PyUNICODE](#pyunicode)

    The 8.3 name to be applied to the file

#### Comments
This function is only available on WinXP and later
File handle must be opened with FILE_FLAG_BACKUP_SEMANTICS, and SE_RESTORE_NAME privilege must be enabled

## [win32file](#win32file).SetFileTime

 __SetFileTime( *File*  *, CreationTime*  *, LastAccessTime*  *, LastWriteTime*  *, UTCTimes* __ )
Sets the date and time that a file was created, last accessed, or last modified.

#### Parameters


  -  *File* :[PyHANDLE](#pyhandle)

    Previously opened handle (opened with FILE_WRITE_ATTRIBUTES access).

  -  *CreationTime=None* :[PyTime](#pytime)

    File created time. None for no change.

  -  *LastAccessTime=None* :[PyTime](#pytime)

    File access time. None for no change.

  -  *LastWriteTime=None* :[PyTime](#pytime)

    File written time. None for no change.

  -  *UTCTimes=False* : boolean

    If True, input times are treated as UTC and no conversion is done, 

otherwise they are treated as local times.  Defaults to False for backward compatibility.

## [win32file](#win32file).SetMailslotInfo

 __SetMailslotInfo( *Mailslot*  *, ReadTimeout* __ )
Sets a mailslot's timeout

#### Parameters


  -  *Mailslot* :[PyHANDLE](#pyhandle)

    Handle to a mailslot

  -  *ReadTimeout* : int

    Timeout in milliseconds, use -1 for no timeout

#### Win32 API References


  - Search for *SetMailslotInfo* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=setmailslotinfo),[google](#http://www.google.com/search?q=setmailslotinfo)or[google groups](#http://groups.google.com/groups?q=setmailslotinfo).

## [win32file](#win32file).SetVolumeLabel

 __SetVolumeLabel( *rootPathName*  *, volumeName* __ )
Sets a volume label for a disk drive.

#### Parameters


  -  *rootPathName* :[PyUnicode](#pyunicode)

    address of name of root directory for volume

  -  *volumeName* :[PyUnicode](#pyunicode)

    name for the volume

## [win32file](#win32file).SetVolumeMountPoint

[PyUnicode](#pyunicode)= __SetVolumeMountPoint( *VolumeMountPoint*  *, VolumeName* __ )
Mounts the specified volume at the specified volume mount point.

#### Parameters


  -  *VolumeMountPoint* :[PyUnicode](#pyunicode)

    The mount point - must be an existing empty directory on an NTFS volume

  -  *VolumeName* :[PyUnicode](#pyunicode)

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

## [win32file](#win32file).SetupComm

 __SetupComm( *handle*  *, dwInQueue*  *, dwOutQueue* __ )
Initializes the communications parameters for a specified communications device.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the communications device.

  -  *dwInQueue* : int

    Specifies the recommended size, in bytes, of the device's internal input buffer.

  -  *dwOutQueue* : int

    Specifies the recommended size, in bytes, of the device's internal output buffer.

## [win32file](#win32file).SfcGetNextProtectedFile

[[PyUnicode](#pyunicode),...] = __SfcGetNextProtectedFile(__ )
Returns list of protected operating system files

#### Win32 API References


  - Search for *SfcGetNextProtectedFile* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=sfcgetnextprotectedfile),[google](#http://www.google.com/search?q=sfcgetnextprotectedfile)or[google groups](#http://groups.google.com/groups?q=sfcgetnextprotectedfile).

## [win32file](#win32file).SfcIsFileProtected

boolean = __SfcIsFileProtected( *ProtFileName* __ )
Checks if a file is protected

#### Parameters


  -  *ProtFileName* :[PyUnicode](#pyunicode)

    Name of file to be checked

## TF_DISCONNECT
 __const win32file.TF_DISCONNECT;__ 


## TF_REUSE_SOCKET
 __const win32file.TF_REUSE_SOCKET;__ 


## TF_USE_DEFAULT_WORKER
 __const win32file.TF_USE_DEFAULT_WORKER;__ 


## TF_USE_KERNEL_APC
 __const win32file.TF_USE_KERNEL_APC;__ 


## TF_USE_SYSTEM_THREAD
 __const win32file.TF_USE_SYSTEM_THREAD;__ 


## TF_WRITE_BEHIND
 __const win32file.TF_WRITE_BEHIND;__ 


## TRUNCATE_EXISTING
 __const win32file.TRUNCATE_EXISTING;__ 
Opens the file. Once opened, the file is truncated so that its size is zero bytes. The calling process must open the file with at least GENERIC_WRITE access. The function fails if the file does not exist.

## TWOSTOPBITS
 __const win32file.TWOSTOPBITS;__ 


## [win32file](#win32file).TransmitCommChar

 __TransmitCommChar( *handle*  *, cChar* __ )
Transmits a specified character ahead of any pending data in the output buffer of the specified communications device.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the communications device.

  -  *cChar* : char

    The character to transmit.

#### Comments
The TransmitCommChar function is useful for sending an interrupt character (such as a CTRL+C) to a host system.
If the device is not transmitting, TransmitCommChar cannot be called repeatedly. Once TransmitCommChar places a character in the output buffer, the character must be transmitted before the function can be called again. If the previous character has not yet been sent, TransmitCommChar returns an error.

## [win32file](#win32file).TransmitFile

 __TransmitFile( *Socket*  *, File*  *, NumberOfBytesToWrite*  *, NumberOfBytesPerSend*  *, Overlapped*  *, Flags*  *, Head*  *, Tail* __ )
Transmits a file over a socket 

TransmitFile(sock, filehandle, bytes_to_write, bytes_per_send, overlap, flags [, (prepend_buf, postpend_buf)])

#### Parameters


  -  *Socket* : __PySocket__ /int

    Socket that will be used to send the file

  -  *File* :[PyHANDLE](#pyhandle)/int

    Handle to the file

  -  *NumberOfBytesToWrite* : int

    The number of bytes in the file to transmit, use 0 for entire file.

  -  *NumberOfBytesPerSend* : int

    The size, in bytes, of each block of data sent in each send operation.

  -  *Overlapped* :[PyOVERLAPPED](#pyoverlapped)

    An overlapped structure, can be None.

  -  *Flags* : int

    A set of flags used to modify the behavior of the TransmitFile function call. (win32file.TF_*)

  -  *Head=None* : buffer

    Buffer to send on the socket before the file

  -  *Tail=None* : buffer

    Buffer to send on the socket after the file

#### Return Value
Returns 0 on completion, or ERROR_IO_PENDING if an overlapped operation has been queued

## [win32file](#win32file).UnlockFile

 __UnlockFile( *hFile*  *, offsetLow*  *, offsetHigh*  *, nNumberOfBytesToUnlockLow*  *, nNumberOfBytesToUnlockHigh* __ )
Unlocks a region of a file locked by[win32file::LockFile](win32file.md#win32filelockfile)or[win32file::LockFileEx](win32file.md#win32filelockfileex)

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)

    handle of file to unlock

  -  *offsetLow* : int

    low-order word of lock region offset

  -  *offsetHigh* : int

    high-order word of lock region offset

  -  *nNumberOfBytesToUnlockLow* : int

    low-order word of length to unlock

  -  *nNumberOfBytesToUnlockHigh* : int

    high-order word of length to unlock

## [win32file](#win32file).UnlockFileEx

 __UnlockFileEx( *hFile*  *, int*  *, int*  *, ol* __ )
Unlocks a file. Wrapper for UnlockFileEx win32 API.

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)/int

    Handle to the file

  -  *int* : nbytesLow

    low-order part of number of 

bytes to lock

  -  *int* : nbytesLow

    high-order part of number of 

bytes to lock

  -  *ol=None* :[PyOVERLAPPED](#pyoverlapped)

    An overlapped structure

## [win32file](#win32file).WSAAsyncSelect

 __WSAAsyncSelect( *socket*  *, hwnd*  *, int*  *, networkEvents* __ )
Request windows message notification for the supplied set of FD_XXXX network events.

#### Parameters


  -  *socket* : __PySocket__ 

    socket to attach to the event

  -  *hwnd* : __hwnd__ 

    Window handle for the socket to become attached to.

  -  *int* : __int__ 

    Window message that will be posted.

  -  *networkEvents* : int

    A bitmask of network events that will cause wMsg to be posted. e.g. (FD_CLOSE | FD_READ)

## WSAECONNABORTED
 __const win32file.WSAECONNABORTED;__ 


## WSAECONNRESET
 __const win32file.WSAECONNRESET;__ 


## WSAEDISCON
 __const win32file.WSAEDISCON;__ 


## WSAEFAULT
 __const win32file.WSAEFAULT;__ 


## WSAEINPROGRESS
 __const win32file.WSAEINPROGRESS;__ 


## WSAEINTR
 __const win32file.WSAEINTR;__ 


## WSAEINVAL
 __const win32file.WSAEINVAL;__ 


## WSAEMSGSIZE
 __const win32file.WSAEMSGSIZE;__ 


## WSAENETDOWN
 __const win32file.WSAENETDOWN;__ 


## WSAENETRESET
 __const win32file.WSAENETRESET;__ 


## WSAENOBUFS
 __const win32file.WSAENOBUFS;__ 


## WSAENOTCONN
 __const win32file.WSAENOTCONN;__ 


## WSAENOTSOCK
 __const win32file.WSAENOTSOCK;__ 


## WSAEOPNOTSUPP
 __const win32file.WSAEOPNOTSUPP;__ 


## WSAESHUTDOWN
 __const win32file.WSAESHUTDOWN;__ 


## WSAEWOULDBLOCK
 __const win32file.WSAEWOULDBLOCK;__ 


## [win32file](#win32file).WSAEnumNetworkEvents

dict = __WSAEnumNetworkEvents( *s*  *, hEvent* __ )
Return network events that caused the event associated with the socket to be signaled.

#### Parameters


  -  *s* : __PySocket__ 

    Socket to check for netork events, previously registered for network event notification with WSAEventSelect.

  -  *hEvent* :[PyHANDLE](#pyhandle)

    Optional handle to the event associated with socket s in the last call to WSAEventSelect. If specified, the event will be reset.

#### Return Value
A dictionary mapping network events that occured for the specified socket since the last call to this function (e.g. FD_READ, FD_WRITE) to their associated error code, or 0 if the event occured without an error. The events returned are a subset of events previously registered for this socket with WSAEventSelect.

## [win32file](#win32file).WSAEventSelect

 __WSAEventSelect( *socket*  *, hEvent*  *, networkEvents* __ )
Specifies an event object to be associated with the supplied set of FD_XXXX network events.

#### Parameters


  -  *socket* : __PySocket__ 

    socket to attach to the event

  -  *hEvent* :[PyHandle](#pyhandle)

    Event handle for the socket to become attached to.

  -  *networkEvents* : int

    A bitmask of network events that will cause hEvent to be signaled. e.g. (FD_CLOSE | FD_READ)

## [win32file](#win32file).WSARecv

(rc, cBytesRecvd) = __WSARecv( *s*  *, buffer*  *, ol*  *, dwFlags* __ )
Winsock recv() equivalent function for Overlapped I/O.

#### Parameters


  -  *s* : __PySocket__ /int

    Socket to send data on.

  -  *buffer* : __buffer__ 

    Buffer to send data from.

  -  *ol* :[PyOVERLAPPED](#pyoverlapped)

    An overlapped structure

  -  *dwFlags* : int

    Optional reception flags.

## [win32file](#win32file).WSASend

(rc, cBytesSent) = __WSASend( *s*  *, buffer*  *, ol*  *, dwFlags* __ )
Winsock send() equivalent function for Overlapped I/O.

#### Parameters


  -  *s* : __PySocket__ /int

    Socket to send data on.

  -  *buffer* : string/ __buffer__ 

    Buffer to send data from.

  -  *ol* :[PyOVERLAPPED](#pyoverlapped)

    An overlapped structure

  -  *dwFlags* : int

    Optional send flags.

## WSA_IO_PENDING
 __const win32file.WSA_IO_PENDING;__ 


## WSA_OPERATION_ABORTED
 __const win32file.WSA_OPERATION_ABORTED;__ 


## [win32file](#win32file).WaitCommEvent

 __WaitCommEvent( *handle*  *, overlapped* __ )
Waits for an event to occur for a specified communications device. The set of events that are monitored by this function is contained in the event mask associated with the device handle.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the communications device.

  -  *overlapped* :[PyOVERLAPPED](#pyoverlapped)

    This structure is required if hFile was opened with FILE_FLAG_OVERLAPPED.
If hFile was opened with FILE_FLAG_OVERLAPPED, the lpOverlapped parameter must not be NULL. It must point to a valid OVERLAPPED structure. If hFile was opened with FILE_FLAG_OVERLAPPED and lpOverlapped is NULL, the function can incorrectly report that the operation is complete.
If hFile was opened with FILE_FLAG_OVERLAPPED and lpOverlapped is not NULL, WaitCommEvent is performed as an overlapped operation. In this case, the OVERLAPPED structure must contain a handle to a manual-reset event object (created by using the CreateEvent function).
If hFile was not opened with FILE_FLAG_OVERLAPPED, WaitCommEvent does not return until one of the specified events or an error occurs.

#### Comments
If an overlapped structure is passed, then the __PyOVERLAPPED::dword__ address is passed to the Win32 API as the mask.  This means that once the 

overlapped operation has completed, this dword attribute can be used to 

determine the type of event that occurred.

#### Return Value
The result is a tuple of (rc, mask_val), where rc is zero for success, or 

the result of calling GetLastError() otherwise.  The mask_val is the new mask value 

once the function has returned, but if an Overlapped object is passed, this value 

will generally be meaningless.  See the comments for more details.

## [win32file](#win32file).Wow64DisableWow64FsRedirection

int = __Wow64DisableWow64FsRedirection(__ )
Disables file system redirection for 32-bit processes running on a 64-bit system

#### Comments
Requires 64-bit XP or later

#### Return Value
Returns a state value to be passed to[win32file::Wow64RevertWow64FsRedirection](win32file.md#win32filewow64revertwow64fsredirection)

## [win32file](#win32file).Wow64RevertWow64FsRedirection

 __Wow64RevertWow64FsRedirection( *OldValue* __ )
Reenables file system redirection for 32-bit processes running on a 64-bit system

#### Parameters


  -  *OldValue* : int

    State returned from Wow64DisableWow64FsRedirection

#### Comments
Requires 64-bit XP or later

## [win32file](#win32file).WriteEncryptedFileRaw

 __WriteEncryptedFileRaw( *ImportCallback*  *, CallbackContext*  *, Context* __ )
Writes raw bytes to an encrypted file

#### Parameters


  -  *ImportCallback* :[ImportCallBack](#importcallback)

    Python function that supplies data to be written

  -  *CallbackContext* : object

    Arbitrary Python object to be passed to callback function

  -  *Context* : PyCObject

    Context object returned from[win32file::OpenEncryptedFileRaw](win32file.md#win32fileopenencryptedfileraw)

#### Comments
Only available on Windows 2000 or later

## [win32file](#win32file).WriteFile

int, int = __WriteFile( *hFile*  *, data*  *, ol* __ )
Writes a string to a file

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)/int

    Handle to the file

  -  *data* : string/[PyOVERLAPPEDReadBuffer](#pyoverlappedreadbuffer)

    The data to write.

  -  *ol=None* :[PyOVERLAPPED](#pyoverlapped)

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

## [win32file](#win32file)._get_osfhandle

long = ___get_osfhandle( *fd* __ )
Gets operating-system file handle associated with existing stream

#### Parameters


  -  *fd* : int

    File descriptor as returned by file.fileno()

## [win32file](#win32file)._getmaxstdio

int = ___getmaxstdio(__ )
Returns the maximum number of CRT io streams.

## [win32file](#win32file)._open_osfhandle

int = ___open_osfhandle( *osfhandle*  *, flags* __ )
Associates a C run-time file handle with a existing operating-system file handle.

#### Parameters


  -  *osfhandle* :[PyHANDLE](#pyhandle)

    An open file handle

  -  *flags* : int

    O_APPEND,O_RDONLY, or O_TEXT

## [win32file](#win32file)._setmaxstdio

int = ___setmaxstdio( *newmax* __ )
Set the maximum allowed number of open stdio handles

#### Parameters


  -  *newmax* : int

    Maximum number of open stdio streams, 2048 max

#### Return Value
Returns the number that was set, or -1 on failure.