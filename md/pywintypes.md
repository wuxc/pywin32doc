# pywintypes


## Module pywintypes

A module which supports common Windows types\.

#### Methods

  - [DosDateTimeToTime](pywintypes.md#pywintypesdosdatetimetotime)

    Converts an MS-DOS Date/Time to a standard Time object&nbsp;

  - [Unicode](pywintypes.md#pywintypesunicode)

    Creates a new [PyUnicode](PyUnicode.md) object&nbsp;

  - [UnicodeFromRaw](pywintypes.md#pywintypesunicodefromraw)

    Creates a new [PyUnicode](PyUnicode.md) object from raw binary data&nbsp;

  - [IsTextUnicode](pywintypes.md#pywintypesistextunicode)

    Determines whether a buffer probably contains a form of Unicode text\.&nbsp;

  - [OVERLAPPED](pywintypes.md#pywintypesoverlapped)

    Creates a new [PyOVERLAPPED](PyOVERLAPPED.md) object&nbsp;

  - [IID](pywintypes.md#pywintypesiid)

    Makes an [PyIID](PyIID.md) object from a string\.&nbsp;

  - [Time](pywintypes.md#pywintypestime)

    Makes a [PyTime](PyTime.md) object from the argument\.&nbsp;

  - [CreateGuid](pywintypes.md#pywintypescreateguid)

    Creates a new, unique GUIID\. 

MS\_WINCE&nbsp;

  - [ACL](pywintypes.md#pywintypesacl)

    Creates a new [PyACL](PyACL.md) object\.&nbsp;

  - [SID](pywintypes.md#pywintypessid)

    Creates a new [PySID](PySID.md) object\.&nbsp;

  - [SECURITY\_ATTRIBUTES](pywintypes.md#pywintypessecurity_attributes)

    Creates a new [PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes) object\.&nbsp;

  - [SECURITY\_DESCRIPTOR](pywintypes.md#pywintypessecurity_descriptor)

    Creates a new [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor) object\. 

NO\_PYWINTYPES\_SECURITY&nbsp;

  - [HANDLE](pywintypes.md#pywintypeshandle)

    Creates a new [PyHANDLE](PyHANDLE.md) object\.&nbsp;

  - [HKEY](pywintypes.md#pywintypeshkey)

    Creates a new [PyHKEY](PyHKEY.md) object\.&nbsp;

  - [WAVEFORMATEX](pywintypes.md#pywintypeswaveformatex)

    Creates a new [PyWAVEFORMATEX](PyWAVEFORMATEX.md) object\.&nbsp;


## [pywintypes](pywintypes.md#pywintypes)\.ACL

[PyACL](PyACL.md) = ACL\(bufSize\)
Creates a new ACL object

#### Parameters

  - bufSize=64 : int

    The size for the ACL\.


## [pywintypes](pywintypes.md#pywintypes)\.CreateGuid

[PyIID](PyIID.md) = CreateGuid\(\)
Creates a new, unique GUIID\.


## [pywintypes](pywintypes.md#pywintypes)\.DosDateTimeToTime

[PyTime](PyTime.md) = DosDateTimeToTime\(\)
Converts an MS-DOS Date/Time to a standard Time object\.


## [pywintypes](pywintypes.md#pywintypes)\.HANDLE

[PyHANDLE](PyHANDLE.md) = HANDLE\(\)
Creates a new HANDLE object


## [pywintypes](pywintypes.md#pywintypes)\.HKEY

[PyHKEY](PyHKEY.md) = HKEY\(\)
Creates a new HKEY object


## [pywintypes](pywintypes.md#pywintypes)\.IID

[PyIID](PyIID.md) = IID\(iidString, is\_bytes

\)
Creates a new IID object

#### Parameters

  - iidString : string/Unicode

    A string representation of an IID, or a ProgID\.

  - is\_bytes=False : bool

    Indicates if the first param is actually the bytes of an IID structure\.


## [pywintypes](pywintypes.md#pywintypes)\.IsTextUnicode

int, int = IsTextUnicode\(str, flags

\)
Determines whether a buffer probably contains a form of Unicode text\.

#### Parameters

  - str : string

    The string containing the binary data\.

  - flags : int

    Determines the specific tests to make

#### Return Value
The function returns \(result, flags\), both integers\. 

result is nonzero if the data in the buffer passes the specified tests\. 

result is zero if the data in the buffer does not pass the specified tests\. 

In either case, flags contains the results of the specific tests the function applied to make its determination\.


## [pywintypes](pywintypes.md#pywintypes)\.OVERLAPPED

[PyOVERLAPPED](PyOVERLAPPED.md) = OVERLAPPED\(\)
Creates a new OVERLAPPED object


## [pywintypes](pywintypes.md#pywintypes)\.SECURITY\_ATTRIBUTES

[PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes) = SECURITY\_ATTRIBUTES\(\)
Creates a new SECURITY\_ATTRIBUTES object


## [pywintypes](pywintypes.md#pywintypes)\.SECURITY\_DESCRIPTOR

[PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor) = SECURITY\_DESCRIPTOR\(\)
Creates a new SECURITY\_DESCRIPTOR object

#### Alternative Parameters

  - data

    A buffer \(eg, a string\) with the raw bytes for the security descriptor\.


## [pywintypes](pywintypes.md#pywintypes)\.SID

[PySID](PySID.md) = SID\(bufSize\)
Creates a new SID object

#### Parameters

  - bufSize=32 : int

    Size for the SID buffer

#### Alternative Parameters

  - buffer

    A raw data buffer, assumed to hold the SID data\.

#### Alternative Parameters

  - idAuthority

    The identifier authority\.

  - subAuthorities

    A list of sub authorities\.


## [pywintypes](pywintypes.md#pywintypes)\.Time

[PyTime](PyTime.md) = Time\(timeRepr\)
Creates a new time object\.

#### Parameters

  - timeRepr : object

    An integer/float/tuple time representation\.

#### Comments

Note that the parameter can be any object that supports 

int\(object\) - for example , another PyTime object\. 

The integer should be as defined by the Python time module\. 

See the description of the [PyTime](PyTime.md) object for more information\.


## [pywintypes](pywintypes.md#pywintypes)\.Unicode

[PyUnicode](PyUnicode.md) = Unicode\(\)
Creates a new Unicode object


## [pywintypes](pywintypes.md#pywintypes)\.UnicodeFromRaw

[PyUnicode](PyUnicode.md) = UnicodeFromRaw\(str\)
Creates a new Unicode object from raw binary data

#### Parameters

  - str : string/buffer

    The string containing the binary data\.


## [pywintypes](pywintypes.md#pywintypes)\.WAVEFORMATEX

[PyWAVEFORMATEX](PyWAVEFORMATEX.md) = WAVEFORMATEX\(\)
Creates a new WAVEFORMATEX object