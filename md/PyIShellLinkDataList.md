# PyIShellLinkDataList


## PyIShellLinkDataList Object

Interface to a link's extra data blocks\. Can be obtained from [PyIShellLink](PyIShellLink.md) 

by calling QueryInterface with IID\_IShellLinkDataList

#### Methods

  - [AddDataBlock](PyIShellLinkDataList.md#pyishelllinkdatalistadddatablock)

    Inserts a data block into the link&nbsp;

  - [CopyDataBlock](PyIShellLinkDataList.md#pyishelllinkdatalistcopydatablock)

    Retrieves the specified data block from the link&nbsp;

  - [GetFlags](PyIShellLinkDataList.md#pyishelllinkdatalistgetflags)

    Retrieves the link's flags&nbsp;

  - [RemoveDataBlock](PyIShellLinkDataList.md#pyishelllinkdatalistremovedatablock)

    Deletes one of the link's data blocks&nbsp;

  - [SetFlags](PyIShellLinkDataList.md#pyishelllinkdatalistsetflags)

    Sets the flags indicating which data blocks are present&nbsp;


## [PyIShellLinkDataList](PyIShellLinkDataList.md#pyishelllinkdatalist)\.AddDataBlock

AddDataBlock\(DataBlock\)
Inserts a data block into the link

#### Parameters

  - DataBlock : dict

    Contents are dependent on type of data block being added

#### Comments

Input should be one of [NT\_CONSOLE\_PROPS](NT.md#ntconsole_props), [NT\_FE\_CONSOLE\_PROPS](NT.md#ntfe_console_props), [EXP\_SPECIAL\_FOLDER](EXP.md#expspecial_folder), 

[EXP\_DARWIN\_LINK](EXP.md#expdarwin_link), or [EXP\_SZ\_LINK](EXP.md#expsz_link)\.  Expected form is indicated by the Signature member\.


## [PyIShellLinkDataList](PyIShellLinkDataList.md#pyishelllinkdatalist)\.CopyDataBlock

dict = CopyDataBlock\(Sig\)
Retrieves the specified data block from the link

#### Parameters

  - Sig : int

    The type of data block to retrieve, one of the shellcon\.\*\_SIG constants

#### Return Value
The returned dictionary will contain different information depending on the value passed in


## [PyIShellLinkDataList](PyIShellLinkDataList.md#pyishelllinkdatalist)\.GetFlags

int = GetFlags\(\)
Retrieves the link's flags

#### Return Value
Returns combination of shellcon\.SLDF\_\* flags


## [PyIShellLinkDataList](PyIShellLinkDataList.md#pyishelllinkdatalist)\.RemoveDataBlock

RemoveDataBlock\(Sig\)
Deletes one of the link's data blocks

#### Parameters

  - Sig : int

    Identifies which block is to be removed, one of shellcon\.\*\_SIG constants


## [PyIShellLinkDataList](PyIShellLinkDataList.md#pyishelllinkdatalist)\.SetFlags

SetFlags\(Flags\)
Sets the flags indicating which data blocks are present

#### Parameters

  - Flags : int

    Combination of shellcon\.SLDF\_\* flags