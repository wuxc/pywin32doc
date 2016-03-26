# PyIShellLinkDataList

## PyIShellLinkDataList Object

Interface to a link's extra data blocks. Can be obtained from[PyIShellLink](#pyishelllink)by calling QueryInterface with IID_IShellLinkDataList

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

## [PyIShellLinkDataList](#pyishelllinkdatalist).AddDataBlock

 __AddDataBlock( *DataBlock* __ )
Inserts a data block into the link

#### Parameters


  -  *DataBlock* : dict

    Contents are dependent on type of data block being added

#### Comments
Input should be one of[NT_CONSOLE_PROPS](NT.md#ntconsole_props),[NT_FE_CONSOLE_PROPS](NT.md#ntfe_console_props),[EXP_SPECIAL_FOLDER](EXP.md#expspecial_folder),[EXP_DARWIN_LINK](EXP.md#expdarwin_link), or[EXP_SZ_LINK](EXP.md#expsz_link).  Expected form is indicated by the Signature member.

## [PyIShellLinkDataList](#pyishelllinkdatalist).CopyDataBlock

dict = __CopyDataBlock( *Sig* __ )
Retrieves the specified data block from the link

#### Parameters


  -  *Sig* : int

    The type of data block to retrieve, one of the shellcon.*_SIG constants

#### Return Value
The returned dictionary will contain different information depending on the value passed in

## [PyIShellLinkDataList](#pyishelllinkdatalist).GetFlags

int = __GetFlags(__ )
Retrieves the link's flags

#### Return Value
Returns combination of shellcon.SLDF_* flags

## [PyIShellLinkDataList](#pyishelllinkdatalist).RemoveDataBlock

 __RemoveDataBlock( *Sig* __ )
Deletes one of the link's data blocks

#### Parameters


  -  *Sig* : int

    Identifies which block is to be removed, one of shellcon.*_SIG constants

## [PyIShellLinkDataList](#pyishelllinkdatalist).SetFlags

 __SetFlags( *Flags* __ )
Sets the flags indicating which data blocks are present

#### Parameters


  -  *Flags* : int

    Combination of shellcon.SLDF_* flags