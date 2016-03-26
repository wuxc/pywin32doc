# PyIMoniker

## PyIMoniker Object



A Python interface to IMoniker

#### Methods


  - [BindToObject](PyIMoniker.md#pyimonikerbindtoobject)

    Uses the moniker to bind to the object it identifies\.&nbsp;

  - [BindToStorage](PyIMoniker.md#pyimonikerbindtostorage)

    Retrieves an interface object to the storage that contains the object identified by the moniker\.&nbsp;

  - [GetDisplayName](PyIMoniker.md#pyimonikergetdisplayname)

    Gets the display name , which is a user-readable representation of this moniker\.&nbsp;

  - [ComposeWith](PyIMoniker.md#pyimonikercomposewith)

    Combines the current moniker with another moniker, creating a new composite moniker\.&nbsp;

  - [Enum](PyIMoniker.md#pyimonikerenum)

    Supplies an enumerator that can enumerate the components of a composite moniker\.&nbsp;

  - [IsEqual](PyIMoniker.md#pyimonikerisequal)

    Compares this moniker with a specified moniker and indicates whether they are identical\.&nbsp;

  - [IsSystemMoniker](PyIMoniker.md#pyimonikerissystemmoniker)

    Indicates whether this moniker is of one of the system-supplied moniker classes\.&nbsp;

  - [Hash](PyIMoniker.md#pyimonikerhash)

    Calculates a 32-bit integer using the internal state of the moniker\.&nbsp;


## [PyIMoniker](#pyimoniker)\.BindToObject

[PyIUnknown](#pyiunknown) =BindToObject\(bindCtx, moniker, iidResult\)
Uses the moniker to bind to the object it identifies\.

#### Parameters


  - bindCtx :[PyIBindCtx](#pyibindctx)

    bind context object to be used\.

  - moniker :[PyIMoniker](#pyimoniker)

    If the moniker is part of a composite moniker, otherwise None

  - iidResult :IID

    IID of the result object\.

## [PyIMoniker](#pyimoniker)\.BindToStorage

[PyIUnknown](#pyiunknown) =BindToStorage\(bindCtx, moniker, iidResult\)
Retrieves an interface object to the storage that contains the object identified by the moniker\.

#### Parameters


  - bindCtx :[PyIBindCtx](#pyibindctx)

    bind context object to be used\.

  - moniker :[PyIMoniker](#pyimoniker)

    If the moniker is part of a composite moniker, otherwise None

  - iidResult :IID

    IID of the result object\.

## [PyIMoniker](#pyimoniker)\.ComposeWith

[PyIMoniker](#pyimoniker) =ComposeWith\(mkRight, fOnlyIfNotGeneric\)
Combines the current moniker with another moniker, creating a new composite moniker\.

#### Parameters


  - mkRight :[PyIMoniker](#pyimoniker)

    The IMoniker interface on the moniker to compose onto the end of this moniker\.

  - fOnlyIfNotGeneric : int

    If TRUE, the caller requires a non-generic composition, so the operation should proceed only if pmkRight is a moniker class that this moniker can compose with in some way other than forming a generic composite\. If FALSE, the method can create a generic composite if necessary\.

## [PyIMoniker](#pyimoniker)\.Enum

[PyIEnumMoniker](#pyienummoniker) =Enum\(fForward\)
Supplies an enumerator that can enumerate the components of a composite moniker\.

#### Parameters


  - fForward=True : int

    If TRUE, enumerates the monikers from left to right\. If FALSE, enumerates from right to left\.

## [PyIMoniker](#pyimoniker)\.GetDisplayName



string =GetDisplayName\(bindCtx, moniker\)
Gets the display name , which is a user-readable representation of this moniker\.

#### Parameters


  - bindCtx :[PyIBindCtx](#pyibindctx)

    bind context object to be used\.

  - moniker :[PyIMoniker](#pyimoniker)

    If the moniker is part of a composite moniker, otherwise None

## [PyIMoniker](#pyimoniker)\.Hash



int =Hash\(\)
Calculates a 32-bit integer using the internal state of the moniker\.

## [PyIMoniker](#pyimoniker)\.IsEqual



int =IsEqual\(other\)
Compares this moniker with a specified moniker and indicates whether they are identical\.

#### Parameters


  - other :[PyIMoniker](#pyimoniker)

    The moniker to compare

## [PyIMoniker](#pyimoniker)\.IsSystemMoniker



int =IsSystemMoniker\(\)
Indicates whether this moniker is of one of the system-supplied moniker classes\.