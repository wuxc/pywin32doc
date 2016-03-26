# PyIPersistStorage

## PyIPersistStorage Object



A Python wrapper of a COM IPersistStorage interface\.

#### Comments


The IPersistStorage interface defines methods that enable a container application to pass a storage object to one of its contained objects and to load and save the storage object\. This interface supports the structured storage model, in which each contained object has its own storage that is nested within the container's storage\.

#### Methods


  - [IsDirty](PyIPersistStorage.md#pyipersiststorageisdirty)

    Checks the object for changes since it was last saved\.&nbsp;

  - [InitNew](PyIPersistStorage.md#pyipersiststorageinitnew)

    Initializes a new object, providing a storage object to be used for the object\.&nbsp;

  - [Load](PyIPersistStorage.md#pyipersiststorageload)

    Loads an object from its existing storage\.&nbsp;

  - [Save](PyIPersistStorage.md#pyipersiststoragesave)

    Saves an object, and any nested objects that it contains, into the specified storage\.&nbsp;

  - [SaveCompleted](PyIPersistStorage.md#pyipersiststoragesavecompleted)

    Notifies the object that it can revert from NoScribble or HandsOff mode\.&nbsp;

  - [HandsOffStorage](PyIPersistStorage.md#pyipersiststoragehandsoffstorage)

    Instructs the object to release all storage objects that have been passed to it by its container and to enter HandsOff mode\.&nbsp;


## [PyIPersistStorage](#pyipersiststorage)\.HandsOffStorage

HandsOffStorage\(\)
Instructs the object to release all storage objects that have been passed to it by its container and to enter HandsOff mode, in which the object cannot do anything and the only operation that works is a close operation\.

## [PyIPersistStorage](#pyipersiststorage)\.InitNew

InitNew\(PyIStorage\)
Initializes a new object, providing a storage object to be used for the object\.

#### Parameters


  - PyIStorage :[PyIStorage](#pyistorage)

    [PyIStorage](#pyistorage) for the new storage object to be initialized\. The container creates a nested storage object in its storage object \(see[PyIStorage::CreateStorage](PyIStorage.md#pyistoragecreatestorage)\)\. Then, the container calls thePyIPersistStorage::WriteClassStg



 function to initialize the new storage object with the object class identifier \(CLSID\)\.

## [PyIPersistStorage](#pyipersiststorage)\.IsDirty



int =IsDirty\(\)
Checks the object for changes since it was last saved\.

## [PyIPersistStorage](#pyipersiststorage)\.Load

Load\(storage\)
Loads an object from its existing storage\.

#### Parameters


  - storage :[PyIStorage](#pyistorage)

    Existing storage for the object\.

## [PyIPersistStorage](#pyipersiststorage)\.Save

Save\(PyIStorage, int\)
Saves an object, and any nested objects that it contains, into the specified storage\. The object is placed in NoScribble mode, and it must not write to the specified storage until it receives a call to its[PyIPersistStorage::SaveCompleted](PyIPersistStorage.md#pyipersiststoragesavecompleted) method\.

#### Parameters


  - PyIStorage :[PyIStorage](#pyistorage)

    Storage for the object

  - int : fSameAsLoad

    Indicates whether the specified storage object is the current one\.
 

This parameter is set to FALSE when performing a Save As or Save A Copy To operation or when performing a full save\. In the latter case, this method saves to a temporary file, deletes the original file, and renames the temporary file\.
 

This parameter is set to TRUE to perform a full save in a low-memory situation or to perform a fast incremental save in which only the dirty components are saved\.

## [PyIPersistStorage](#pyipersiststorage)\.SaveCompleted

SaveCompleted\(PyIStorage\)
Notifies the object that it can revert from NoScribble or HandsOff mode, in which it must not write to its storage object, to Normal mode, in which it can\. The object enters NoScribble mode when it receives an[PyIPersistStorage::Save](PyIPersistStorage.md#pyipersiststoragesave) call\.

#### Parameters


  - PyIStorage :[PyIStorage](#pyistorage)

    The current storage object