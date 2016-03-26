# EXP

## EXP_DARWIN_LINK Object

Dictionary containing information for a EXP_DARWIN_LINK struct

#### Properties

  -  __int Signature__ 
    The type of data block, one of shellcon.*_SIG values

  -  __str DarwinID__ 
    The Windows Installer id for the link

  -  __[PyUNICODE](#pyunicode)wDarwinID__ 
    The installer id as Unicode

  -  __int Size__ 
    Size of structure, ignored on input

## EXP_SPECIAL_FOLDER Object

Dictionary containing information for a EXP_SPECIAL_FOLDER struct

#### Properties

  -  __int Signature__ 
    The type of data block, one of shellcon.*_SIG values

  -  __int idSpecialFolder__ 
    The special folder id of the target (shellcon.CSIDL_*)

  -  __int Offset__ 
    Offset into the link's PIDL

  -  __int Size__ 
    Size of structure, ignored on input

## EXP_SZ_LINK Object

Dictionary containing information for an EXP_SZ_LINK or EXP_SZ_ICON struct

#### Properties

  -  __int Signature__ 
    The type of data block, one of shellcon.*_SIG values

  -  __str Target__ 
    The link's target or icon location

  -  __[PyUNICODE](#pyunicode)wTarget__ 
    The target in Unicode form

  -  __int Size__ 
    Size of structure, ignored on input