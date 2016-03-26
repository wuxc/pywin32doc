# STATSTG

## STATSTG Object

A tuple representing a STATSTG structure

#### Items


  - \[0\] *string* : name

    The name of the storage object

  - \[1\] *int* : type

    Indicates the type of storage object\. This is one of the values from the storagecon\.STGTY\_\* values\.

  - \[2\] *[ULARGE\_INTEGER](ULARGE.md#ulargeinteger)* : size

    Specifies the size in bytes of the stream or byte array\.

  - \[3\] *[PyTime](#pytime)* : modificationTime

    Indicates the last modification time for this storage, stream, or byte array\.

  - \[4\] *[PyTime](#pytime)* : creationTime

    Indicates the creation time for this storage, stream, or byte array\.

  - \[5\] *[PyTime](#pytime)* : accessTime

    Indicates the last access time for this storage, stream or byte array\.

  - \[6\] *int* : mode

    Indicates the access mode specified when the object was opened\. This member is only valid in calls to Stat methods\.

  - \[7\] *int* : locksSupported

    Indicates the types of region locking supported by the stream or byte array\. See the storagecon\.LOCKTYPES\_\* constants for the values available\. This member is not used for storage objects\.

  - \[8\] *[PyIID](#pyiid)* : clsid

    Indicates the class identifier for the storage object; set to CLSID\_NULL for new storage objects\. This member is not used for streams or byte arrays\.

  - \[9\] *int* : stateBits

    Indicates the current state bits of the storage object, that is, the value most recently set by the[PyIStorage::SetStateBits](PyIStorage.md#pyistoragesetstatebits)method\. This member is not valid for streams or byte arrays\.

  - \[10\] *int* : storageFormat

    Indicates the format of the storage object\. This is one of the values from the STGFMT\_\* constants\.  In some Win32 API documentation, this member is known as 'reserved'