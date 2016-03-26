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


## [PyIShellItemArray](PyIShellItemArray.md#pyishellitemarray)\.BindToHandler

interface = BindToHandler\(pbc, rbhid

, riid

\)
Creates an instance of a handler for the items in the container

#### Parameters

  - pbc : [PyIBindCtx](PyIBindCtx.md)

    Bind context, can be None

  - rbhid : [PyIID](PyIID.md)

    Bind handler GUID \(shell\.BHID\_\*\)

  - riid : [PyIID](PyIID.md)

    The interface to return


## [PyIShellItemArray](PyIShellItemArray.md#pyishellitemarray)\.EnumItems

[PyIEnumShellItems](PyIEnumShellItems.md) = EnumItems\(\)
Returns an enumeration interface to list contained items


## [PyIShellItemArray](PyIShellItemArray.md#pyishellitemarray)\.GetAttributes

int = GetAttributes\(AttribFlags, Mask

\)
Retrieves shell attributes of contained items

#### Parameters

  - AttribFlags : int

    SIATTRIBFLAGS value \(shellcon\.SIATTRIBFLAGS\_\*\) specifying how to combine attributes of multiple items

  - Mask : int

    Combination of SFGAOF flags \(shellcon\.SFGAO\_\*\) specifying which attributes to return


## [PyIShellItemArray](PyIShellItemArray.md#pyishellitemarray)\.GetCount

int = GetCount\(\)
Returns the number of items in the container


## [PyIShellItemArray](PyIShellItemArray.md#pyishellitemarray)\.GetItemAt

[PyIShellItem](PyIShellItem.md) = GetItemAt\(dwIndex\)
Retrieves an item by index

#### Parameters

  - dwIndex : int

    Zero-based index of item to retrieve


## [PyIShellItemArray](PyIShellItemArray.md#pyishellitemarray)\.GetPropertyDescriptionList

[PyIPropertyDescriptionList](PyIPropertyDescriptionList.md) = GetPropertyDescriptionList\(Type, riid

\)
Retrieves descriptions for a defined group of properties

#### Parameters

  - Type : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    Property list identifier \(pscon\.PKEY\_PropList\_\*\)

  - riid=IID\_IPropertyDescriptionList : [PyIID](PyIID.md)

    The interface to return


## [PyIShellItemArray](PyIShellItemArray.md#pyishellitemarray)\.GetPropertyStore

[PyIPropertyStore](PyIPropertyStore.md) = GetPropertyStore\(flags, riid

\)
Retrieves a store containing consolidated properties of items in container

#### Parameters

  - flags=GPS\_DEFAULT : int

    Flags indicating how the properties are retrieved \(shellcon\.GPS\_\*\)

  - riid=IID\_\_IPropertyStore : [PyIID](PyIID.md)

    The interface to return, IID\_IPropertyStore or related interface