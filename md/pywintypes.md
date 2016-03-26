# pywintypes

## Module pywintypes

A module which supports common Windows types.

#### Methods


  - [DosDateTimeToTime](pywintypes.md#pywintypesdosdatetimetotime)

    Converts an MS-DOS Date/Time to a standard Time object&nbsp;

  - [Unicode](pywintypes.md#pywintypesunicode)

    Creates a new[PyUnicode](#pyunicode)object&nbsp;

  - [UnicodeFromRaw](pywintypes.md#pywintypesunicodefromraw)

    Creates a new[PyUnicode](#pyunicode)object from raw binary data&nbsp;

  - [IsTextUnicode](pywintypes.md#pywintypesistextunicode)

    Determines whether a buffer probably contains a form of Unicode text.&nbsp;

  - [OVERLAPPED](pywintypes.md#pywintypesoverlapped)

    Creates a new[PyOVERLAPPED](#pyoverlapped)object&nbsp;

  - [IID](pywintypes.md#pywintypesiid)

    Makes an[PyIID](#pyiid)object from a string.&nbsp;

  - [Time](pywintypes.md#pywintypestime)

    Makes a[PyTime](#pytime)object from the argument.&nbsp;

  - [CreateGuid](pywintypes.md#pywintypescreateguid)

    Creates a new, unique GUIID. 

MS_WINCE&nbsp;

  - [ACL](pywintypes.md#pywintypesacl)

    Creates a new[PyACL](#pyacl)object.&nbsp;

  - [SID](pywintypes.md#pywintypessid)

    Creates a new[PySID](#pysid)object.&nbsp;

  - [SECURITY_ATTRIBUTES](pywintypes.md#pywintypessecurity_attributes)

    Creates a new[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)object.&nbsp;

  - [SECURITY_DESCRIPTOR](pywintypes.md#pywintypessecurity_descriptor)

    Creates a new[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)object. 

NO_PYWINTYPES_SECURITY&nbsp;

  - [HANDLE](pywintypes.md#pywintypeshandle)

    Creates a new[PyHANDLE](#pyhandle)object.&nbsp;

  - [HKEY](pywintypes.md#pywintypeshkey)

    Creates a new[PyHKEY](#pyhkey)object.&nbsp;

  - [WAVEFORMATEX](pywintypes.md#pywintypeswaveformatex)

    Creates a new[PyWAVEFORMATEX](#pywaveformatex)object.&nbsp;

## [pywintypes](#pywintypes).ACL

[PyACL](#pyacl)= __ACL( *bufSize* __ )
Creates a new ACL object

#### Parameters


  -  *bufSize=64* : int

    The size for the ACL.

## [pywintypes](#pywintypes).CreateGuid

[PyIID](#pyiid)= __CreateGuid(__ )
Creates a new, unique GUIID.

## [pywintypes](#pywintypes).DosDateTimeToTime

[PyTime](#pytime)= __DosDateTimeToTime(__ )
Converts an MS-DOS Date/Time to a standard Time object.

## [pywintypes](#pywintypes).HANDLE

[PyHANDLE](#pyhandle)= __HANDLE(__ )
Creates a new HANDLE object

## [pywintypes](#pywintypes).HKEY

[PyHKEY](#pyhkey)= __HKEY(__ )
Creates a new HKEY object

## [pywintypes](#pywintypes).IID

[PyIID](#pyiid)= __IID( *iidString*  *, is_bytes* __ )
Creates a new IID object

#### Parameters


  -  *iidString* : string/Unicode

    A string representation of an IID, or a ProgID.

  -  *is_bytes=False* : bool

    Indicates if the first param is actually the bytes of an IID structure.

## [pywintypes](#pywintypes).IsTextUnicode

int, int = __IsTextUnicode( *str*  *, flags* __ )
Determines whether a buffer probably contains a form of Unicode text.

#### Parameters


  -  *str* : string

    The string containing the binary data.

  -  *flags* : int

    Determines the specific tests to make

#### Return Value
The function returns (result, flags), both integers.
result is nonzero if the data in the buffer passes the specified tests.
result is zero if the data in the buffer does not pass the specified tests.
In either case, flags contains the results of the specific tests the function applied to make its determination.

## [pywintypes](#pywintypes).OVERLAPPED

[PyOVERLAPPED](#pyoverlapped)= __OVERLAPPED(__ )
Creates a new OVERLAPPED object

## [pywintypes](#pywintypes).SECURITY_ATTRIBUTES

[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)= __SECURITY_ATTRIBUTES(__ )
Creates a new SECURITY_ATTRIBUTES object

## [pywintypes](#pywintypes).SECURITY_DESCRIPTOR

[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)= __SECURITY_DESCRIPTOR(__ )
Creates a new SECURITY_DESCRIPTOR object

#### Alternative Parameters


  -  *data* 

    A buffer (eg, a string) with the raw bytes for the security descriptor.

## [pywintypes](#pywintypes).SID

[PySID](#pysid)= __SID( *bufSize* __ )
Creates a new SID object

#### Parameters


  -  *bufSize=32* : int

    Size for the SID buffer

#### Alternative Parameters


  -  *buffer* 

    A raw data buffer, assumed to hold the SID data.

#### Alternative Parameters


  -  *idAuthority* 

    The identifier authority.

  -  *subAuthorities* 

    A list of sub authorities.

## [pywintypes](#pywintypes).Time

[PyTime](#pytime)= __Time( *timeRepr* __ )
Creates a new time object.

#### Parameters


  -  *timeRepr* : object

    An integer/float/tuple time representation.

#### Comments
Note that the parameter can be any object that supports 

int(object) - for example , another PyTime object.
The integer should be as defined by the Python time module. 

See the description of the[PyTime](#pytime)object for more information.

## [pywintypes](#pywintypes).Unicode

[PyUnicode](#pyunicode)= __Unicode(__ )
Creates a new Unicode object

## [pywintypes](#pywintypes).UnicodeFromRaw

[PyUnicode](#pyunicode)= __UnicodeFromRaw( *str* __ )
Creates a new Unicode object from raw binary data

#### Parameters


  -  *str* : string/buffer

    The string containing the binary data.

## [pywintypes](#pywintypes).WAVEFORMATEX

[PyWAVEFORMATEX](#pywaveformatex)= __WAVEFORMATEX(__ )
Creates a new WAVEFORMATEX object