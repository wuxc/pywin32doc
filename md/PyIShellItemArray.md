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

## [PyIShellItemArray](#pyishellitemarray)\.BindToHandler

interface \= **BindToHandler\( *pbc*  *, rbhid*  *, riid* ** \)
Creates an instance of a handler for the items in the container

#### Parameters


  -  *pbc* :[PyIBindCtx](#pyibindctx)

    Bind context, can be None

  -  *rbhid* :[PyIID](#pyiid)

    Bind handler GUID \(shell\.BHID\_\*\)

  -  *riid* :[PyIID](#pyiid)

    The interface to return

## [PyIShellItemArray](#pyishellitemarray)\.EnumItems

[PyIEnumShellItems](#pyienumshellitems)\= **EnumItems\(** \)
Returns an enumeration interface to list contained items

## [PyIShellItemArray](#pyishellitemarray)\.GetAttributes

int \= **GetAttributes\( *AttribFlags*  *, Mask* ** \)
Retrieves shell attributes of contained items

#### Parameters


  -  *AttribFlags* : int

    SIATTRIBFLAGS value \(shellcon\.SIATTRIBFLAGS\_\*\) specifying how to combine attributes of multiple items

  -  *Mask* : int

    Combination of SFGAOF flags \(shellcon\.SFGAO\_\*\) specifying which attributes to return

## [PyIShellItemArray](#pyishellitemarray)\.GetCount

int \= **GetCount\(** \)
Returns the number of items in the container

## [PyIShellItemArray](#pyishellitemarray)\.GetItemAt

[PyIShellItem](#pyishellitem)\= **GetItemAt\( *dwIndex* ** \)
Retrieves an item by index

#### Parameters


  -  *dwIndex* : int

    Zero-based index of item to retrieve

## [PyIShellItemArray](#pyishellitemarray)\.GetPropertyDescriptionList

[PyIPropertyDescriptionList](#pyipropertydescriptionlist)\= **GetPropertyDescriptionList\( *Type*  *, riid* ** \)
Retrieves descriptions for a defined group of properties

#### Parameters


  -  *Type* :[PyPROPERTYKEY](#pypropertykey)

    Property list identifier \(pscon\.PKEY\_PropList\_\*\)

  -  *riid\=IID\_IPropertyDescriptionList* :[PyIID](#pyiid)

    The interface to return

## [PyIShellItemArray](#pyishellitemarray)\.GetPropertyStore

[PyIPropertyStore](#pyipropertystore)\= **GetPropertyStore\( *flags*  *, riid* ** \)
Retrieves a store containing consolidated properties of items in container

#### Parameters


  -  *flags\=GPS\_DEFAULT* : int

    Flags indicating how the properties are retrieved \(shellcon\.GPS\_\*\)

  -  *riid\=IID\_\_IPropertyStore* :[PyIID](#pyiid)

    The interface to return, IID\_IPropertyStore or related interface