# COMPONENT

## COMPONENT Object

A dictionary containing data to fill a COMPPOS struct

#### Properties

  -  __int ID__ 
    Id of component, ignored when adding a new component

  -  __int ComponentType__ 
    One of shellcon.COMP_TYPE_* values

  -  __bool Checked__ 
    True indicates item is currently displayed

  -  __bool fDirty__ 
    Indicates if unsaved changes exist

  -  __bool NoScroll__ 
    True disables scrolling

  -  __dict Pos__ 
    [COMPPOS](#comppos)dictionary determining window size and placement

  -  __[PyUNICODE](#pyunicode)FriendlyName__ 
    String of at most MAX_PATH-1 characters, truncated if longer

  -  __[PyUNICODE](#pyunicode)Source__ 
    String of at most INTERNET_MAX_URL_LENGTH-1 characters

  -  __[PyUNICODE](#pyunicode)SubscribedURL__ 
    String of at most INTERNET_MAX_URL_LENGTH-1 characters

  -  __int CurItemState__ 
    One of shellcon.IS_* flags

  -  __dict Original__ 
    [COMPSTATEINFO](#compstateinfo)dictionary

  -  __dict Restored__ 
    [COMPSTATEINFO](#compstateinfo)dictionary

  -  __int Size__ 
    Size of structure, ignored on input