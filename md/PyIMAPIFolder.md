# PyIMAPIFolder


## PyIMAPIFolder Object

An COM interface to MAPI 

Derived from [PyIMAPIProp](PyIMAPIProp.md)

#### Methods

  - [GetLastError](PyIMAPIFolder.md#pyimapifoldergetlasterror)

    Returns the last error associated with this object&nbsp;

  - [CreateFolder](PyIMAPIFolder.md#pyimapifoldercreatefolder)

    Creates a folder object\.&nbsp;

  - [CreateMessage](PyIMAPIFolder.md#pyimapifoldercreatemessage)

    Creates a message in a folder&nbsp;

  - [CopyMessages](PyIMAPIFolder.md#pyimapifoldercopymessages)

    Copies the specified messages&nbsp;

  - [DeleteFolder](PyIMAPIFolder.md#pyimapifolderdeletefolder)

    Deletes a subfolder\.&nbsp;

  - [DeleteMessages](PyIMAPIFolder.md#pyimapifolderdeletemessages)

    Deletes the specified messages\.&nbsp;

  - [EmptyFolder](PyIMAPIFolder.md#pyimapifolderemptyfolder)

    deletes all messages and subfolders from a folder without deleting the folder itself\.&nbsp;


## [PyIMAPIFolder](PyIMAPIFolder.md#pyimapifolder)\.CopyMessages

CopyMessages\(msgs, iid, folder, ulUIParam, progress, flags\)
Copies the specified messages

#### Parameters

  - msgs : [PySBinaryArray](PySBinaryArray.md)

    

  - iid : [PyIID](PyIID.md)

    IID representing the interface to be used to access the destination folder\.  Should usually be None\.

  - folder : [PyIMAPIFolder](PyIMAPIFolder.md#pyimapifolder)

    The destination folder

  - ulUIParam : long

    Handle of the parent window for any dialog boxes or windows this method displays\.

  - progress : PyIMAPIProgress

    A progress object, or None

  - flags : int

    A bitmask of



## [PyIMAPIFolder](PyIMAPIFolder.md#pyimapifolder)\.CreateFolder

[PyIMAPIFolder](PyIMAPIFolder.md#pyimapifolder) = CreateFolder\(folderType, folderName

, folderComment

, iid

, flags

\)
Creates a folder object\.

#### Parameters

  - folderType : int

    The type of folder to create

  - folderName : string

    The name of the folder\.

  - folderComment : string

    A comment for the folder or None

  - iid : [PyIID](PyIID.md)

    The IID of the object to return\.  Should usually be None\.

  - flags : int

    


## [PyIMAPIFolder](PyIMAPIFolder.md#pyimapifolder)\.CreateMessage

[PyIMessage](PyIMessage.md) = CreateMessage\(iid, flags

\)
Creates a message in a folder

#### Parameters

  - iid : [PyIID](PyIID.md)

    The IID of the object to return\.  Should usually be None\.

  - flags : int

    


## [PyIMAPIFolder](PyIMAPIFolder.md#pyimapifolder)\.DeleteFolder

DeleteFolder\(entryId, uiParam, progress\)
Deletes a subfolder\.

#### Parameters

  - entryId : string

    The EntryID of the subfolder to delete\.

  - uiParam : long

    Handle of the parent window of the progress indicator\.

  - progress : PyIMAPIProgress

    A progress object, or None


## [PyIMAPIFolder](PyIMAPIFolder.md#pyimapifolder)\.DeleteMessages

DeleteMessages\(msgs, uiParam, progress, flags\)
Deletes the specified messages\.

#### Parameters

  - msgs : [PySBinaryArray](PySBinaryArray.md)

    

  - uiParam : int

    A HWND for the progress

  - progress : PyIMAPIProgress

    A progress object, or None

  - flags : int

    


## [PyIMAPIFolder](PyIMAPIFolder.md#pyimapifolder)\.EmptyFolder

EmptyFolder\(uiParam, progress, flags\)
deletes all messages and subfolders from a folder without deleting the folder itself\.

#### Parameters

  - uiParam : int

    A HWND for the progress

  - progress : PyIMAPIProgress

    A progress object, or None

  - flags : int

    


## [PyIMAPIFolder](PyIMAPIFolder.md#pyimapifolder)\.GetLastError

PyMAPIError

 = GetLastError\(hr, flags

\)
Returns the last error associated with this object

#### Parameters

  - hr : int

    The HRESULT

  - flags : int

    