# PyIMAPIFolder

## PyIMAPIFolder Object

An COM interface to MAPI
Derived from[PyIMAPIProp](#pyimapiprop)

#### Methods


  - [GetLastError](PyIMAPIFolder.md#pyimapifoldergetlasterror)

    Returns the last error associated with this object&nbsp;

  - [CreateFolder](PyIMAPIFolder.md#pyimapifoldercreatefolder)

    Creates a folder object.&nbsp;

  - [CreateMessage](PyIMAPIFolder.md#pyimapifoldercreatemessage)

    Creates a message in a folder&nbsp;

  - [CopyMessages](PyIMAPIFolder.md#pyimapifoldercopymessages)

    Copies the specified messages&nbsp;

  - [DeleteFolder](PyIMAPIFolder.md#pyimapifolderdeletefolder)

    Deletes a subfolder.&nbsp;

  - [DeleteMessages](PyIMAPIFolder.md#pyimapifolderdeletemessages)

    Deletes the specified messages.&nbsp;

  - [EmptyFolder](PyIMAPIFolder.md#pyimapifolderemptyfolder)

    deletes all messages and subfolders from a folder without deleting the folder itself.&nbsp;

## [PyIMAPIFolder](#pyimapifolder).CopyMessages

 __CopyMessages( *msgs*  *, iid*  *, folder*  *, ulUIParam*  *, progress*  *, flags* __ )
Copies the specified messages

#### Parameters


  -  *msgs* :[PySBinaryArray](#pysbinaryarray)

    

  -  *iid* :[PyIID](#pyiid)

    IID representing the interface to be used to access the destination folder.  Should usually be None.

  -  *folder* :[PyIMAPIFolder](#pyimapifolder)

    The destination folder

  -  *ulUIParam* : long

    Handle of the parent window for any dialog boxes or windows this method displays.

  -  *progress* : __PyIMAPIProgress__ 

    A progress object, or None

  -  *flags* : int

    A bitmask of


## [PyIMAPIFolder](#pyimapifolder).CreateFolder

[PyIMAPIFolder](#pyimapifolder)= __CreateFolder( *folderType*  *, folderName*  *, folderComment*  *, iid*  *, flags* __ )
Creates a folder object.

#### Parameters


  -  *folderType* : int

    The type of folder to create

  -  *folderName* : string

    The name of the folder.

  -  *folderComment* : string

    A comment for the folder or None

  -  *iid* :[PyIID](#pyiid)

    The IID of the object to return.  Should usually be None.

  -  *flags* : int

    

## [PyIMAPIFolder](#pyimapifolder).CreateMessage

[PyIMessage](#pyimessage)= __CreateMessage( *iid*  *, flags* __ )
Creates a message in a folder

#### Parameters


  -  *iid* :[PyIID](#pyiid)

    The IID of the object to return.  Should usually be None.

  -  *flags* : int

    

## [PyIMAPIFolder](#pyimapifolder).DeleteFolder

 __DeleteFolder( *entryId*  *, uiParam*  *, progress* __ )
Deletes a subfolder.

#### Parameters


  -  *entryId* : string

    The EntryID of the subfolder to delete.

  -  *uiParam* : long

    Handle of the parent window of the progress indicator.

  -  *progress* : __PyIMAPIProgress__ 

    A progress object, or None

## [PyIMAPIFolder](#pyimapifolder).DeleteMessages

 __DeleteMessages( *msgs*  *, uiParam*  *, progress*  *, flags* __ )
Deletes the specified messages.

#### Parameters


  -  *msgs* :[PySBinaryArray](#pysbinaryarray)

    

  -  *uiParam* : int

    A HWND for the progress

  -  *progress* : __PyIMAPIProgress__ 

    A progress object, or None

  -  *flags* : int

    

## [PyIMAPIFolder](#pyimapifolder).EmptyFolder

 __EmptyFolder( *uiParam*  *, progress*  *, flags* __ )
deletes all messages and subfolders from a folder without deleting the folder itself.

#### Parameters


  -  *uiParam* : int

    A HWND for the progress

  -  *progress* : __PyIMAPIProgress__ 

    A progress object, or None

  -  *flags* : int

    

## [PyIMAPIFolder](#pyimapifolder).GetLastError

 __PyMAPIError__ = __GetLastError( *hr*  *, flags* __ )
Returns the last error associated with this object

#### Parameters


  -  *hr* : int

    The HRESULT

  -  *flags* : int

    