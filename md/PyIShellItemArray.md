# PyIShellItemArray

## PyIShellItemArray Object

Container for a number of shell items

#### Comments
Can be used as an iterator to enumerate the contained items

#### Methods


  - [BindToHandler](PyIShellItemArray.md#pyishellitemarraybindtohandler)

    Creates an instance of a handler for the items in the container&nbsp;

  - [GetPropertyStore](PyIShellItemArray.md#pyishellitemarraygetpropertystore)

    Retrieves a store containing consolidated properties of items in container&nbsp;

  - [GetPropertyDescriptionList](PyIShellItemArray.md#pyishellitemarraygetpropertydescriptionlist)

    Retrieves descriptions for a defined group of properties&nbsp;

  - [GetAttributes](PyIShellItemArray.md#pyishellitemarraygetattributes)

    Retrieves shell attributes of contained items&nbsp;

  - [GetCount](PyIShellItemArray.md#pyishellitemarraygetcount)

    Returns the number of items in the container&nbsp;

  - [GetItemAt](PyIShellItemArray.md#pyishellitemarraygetitemat)

    Retrieves an item by index&nbsp;

  - [EnumItems](PyIShellItemArray.md#pyishellitemarrayenumitems)

    Returns an enumeration interface to list contained items&nbsp;

## [PyIShellItemArray](#pyishellitemarray).BindToHandler

interface = __BindToHandler( *pbc*  *, rbhid*  *, riid* __ )
Creates an instance of a handler for the items in the container

#### Parameters


  -  *pbc* :[PyIBindCtx](#pyibindctx)

    Bind context, can be None

  -  *rbhid* :[PyIID](#pyiid)

    Bind handler GUID (shell.BHID_*)

  -  *riid* :[PyIID](#pyiid)

    The interface to return

## [PyIShellItemArray](#pyishellitemarray).EnumItems

[PyIEnumShellItems](#pyienumshellitems)= __EnumItems(__ )
Returns an enumeration interface to list contained items

## [PyIShellItemArray](#pyishellitemarray).GetAttributes

int = __GetAttributes( *AttribFlags*  *, Mask* __ )
Retrieves shell attributes of contained items

#### Parameters


  -  *AttribFlags* : int

    SIATTRIBFLAGS value (shellcon.SIATTRIBFLAGS_*) specifying how to combine attributes of multiple items

  -  *Mask* : int

    Combination of SFGAOF flags (shellcon.SFGAO_*) specifying which attributes to return

## [PyIShellItemArray](#pyishellitemarray).GetCount

int = __GetCount(__ )
Returns the number of items in the container

## [PyIShellItemArray](#pyishellitemarray).GetItemAt

[PyIShellItem](#pyishellitem)= __GetItemAt( *dwIndex* __ )
Retrieves an item by index

#### Parameters


  -  *dwIndex* : int

    Zero-based index of item to retrieve

## [PyIShellItemArray](#pyishellitemarray).GetPropertyDescriptionList

[PyIPropertyDescriptionList](#pyipropertydescriptionlist)= __GetPropertyDescriptionList( *Type*  *, riid* __ )
Retrieves descriptions for a defined group of properties

#### Parameters


  -  *Type* :[PyPROPERTYKEY](#pypropertykey)

    Property list identifier (pscon.PKEY_PropList_*)

  -  *riid=IID_IPropertyDescriptionList* :[PyIID](#pyiid)

    The interface to return

## [PyIShellItemArray](#pyishellitemarray).GetPropertyStore

[PyIPropertyStore](#pyipropertystore)= __GetPropertyStore( *flags*  *, riid* __ )
Retrieves a store containing consolidated properties of items in container

#### Parameters


  -  *flags=GPS_DEFAULT* : int

    Flags indicating how the properties are retrieved (shellcon.GPS_*)

  -  *riid=IID__IPropertyStore* :[PyIID](#pyiid)

    The interface to return, IID_IPropertyStore or related interface