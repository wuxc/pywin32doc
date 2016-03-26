# COMPONENT


## COMPONENT Object

A dictionary containing data to fill a COMPPOS struct

#### Properties

  - int ID

    Id of component, ignored when adding a new component

  - int ComponentType

    One of shellcon\.COMP\_TYPE\_\* values

  - bool Checked

    True indicates item is currently displayed

  - bool fDirty

    Indicates if unsaved changes exist

  - bool NoScroll

    True disables scrolling

  - dict Pos

    [COMPPOS](COMPPOS.md) dictionary determining window size and placement

  - [PyUNICODE](PyUNICODE.md) FriendlyName

    String of at most MAX\_PATH-1 characters, truncated if longer

  - [PyUNICODE](PyUNICODE.md) Source

    String of at most INTERNET\_MAX\_URL\_LENGTH-1 characters

  - [PyUNICODE](PyUNICODE.md) SubscribedURL

    String of at most INTERNET\_MAX\_URL\_LENGTH-1 characters

  - int CurItemState

    One of shellcon\.IS\_\* flags

  - dict Original

    [COMPSTATEINFO](COMPSTATEINFO.md) dictionary

  - dict Restored

    [COMPSTATEINFO](COMPSTATEINFO.md) dictionary

  - int Size

    Size of structure, ignored on input