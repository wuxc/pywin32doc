# EXP

## EXP\_DARWIN\_LINK Object

Dictionary containing information for a EXP\_DARWIN\_LINK struct

#### Properties

  -  **int Signature** 
    The type of data block, one of shellcon\.\*\_SIG values

  -  **str DarwinID** 
    The Windows Installer id for the link

  -  **[PyUNICODE](#pyunicode)wDarwinID** 
    The installer id as Unicode

  -  **int Size** 
    Size of structure, ignored on input

## EXP\_SPECIAL\_FOLDER Object

Dictionary containing information for a EXP\_SPECIAL\_FOLDER struct

#### Properties

  -  **int Signature** 
    The type of data block, one of shellcon\.\*\_SIG values

  -  **int idSpecialFolder** 
    The special folder id of the target \(shellcon\.CSIDL\_\*\)

  -  **int Offset** 
    Offset into the link's PIDL

  -  **int Size** 
    Size of structure, ignored on input

## EXP\_SZ\_LINK Object

Dictionary containing information for an EXP\_SZ\_LINK or EXP\_SZ\_ICON struct

#### Properties

  -  **int Signature** 
    The type of data block, one of shellcon\.\*\_SIG values

  -  **str Target** 
    The link's target or icon location

  -  **[PyUNICODE](#pyunicode)wTarget** 
    The target in Unicode form

  -  **int Size** 
    Size of structure, ignored on input