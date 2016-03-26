# PyIObjectCollection

## PyIObjectCollection Object

Modifiable container for a number of IUnknown objects

#### Methods


  - [AddObject](PyIObjectCollection.md#pyiobjectcollectionaddobject)

    Adds a single object to the collection&nbsp;

  - [AddFromArray](PyIObjectCollection.md#pyiobjectcollectionaddfromarray)

    Adds a number of objects contained in an[PyIObjectArray](#pyiobjectarray)collection&nbsp;

  - [RemoveObjectAt](PyIObjectCollection.md#pyiobjectcollectionremoveobjectat)

    Removes a single object from the collection&nbsp;

  - [Clear](PyIObjectCollection.md#pyiobjectcollectionclear)

    Empties the container&nbsp;


## [PyIObjectCollection](#pyiobjectcollection).AddFromArray

 __AddFromArray( *Source* __ )
Adds a number of objects contained in an[PyIObjectArray](#pyiobjectarray)collection

#### Parameters


  -  *Source* :[PyIObjectArray](#pyiobjectarray)

    Objects to be added to the collection

## [PyIObjectCollection](#pyiobjectcollection).AddObject

 __AddObject( *punk* __ )
Adds a single object to the collection

#### Parameters


  -  *punk* :[PyIUnknown](#pyiunknown)

    Object to be added

## [PyIObjectCollection](#pyiobjectcollection).Clear

 __Clear(__ )
Empties the container.

## [PyIObjectCollection](#pyiobjectcollection).RemoveObjectAt

 __RemoveObjectAt( *Index* __ )
Removes a single object from the collection

#### Parameters


  -  *Index* : int

    Zero-based index of item to remove