# pywintypes

## Module pywintypes



A module which supports common Windows types\.

#### Methods


  - [DosDateTimeToTime](pywintypes.md#pywintypesdosdatetimetotime)

    Converts an MS-DOS Date/Time to a standard Time object&nbsp;

  - [Unicode](pywintypes.md#pywintypesunicode)

    Creates a new[PyUnicode](#pyunicode) object&nbsp;

  - [UnicodeFromRaw](pywintypes.md#pywintypesunicodefromraw)

    Creates a new[PyUnicode](#pyunicode) object from raw binary data&nbsp;

  - [IsTextUnicode](pywintypes.md#pywintypesistextunicode)

    Determines whether a buffer probably contains a form of Unicode text\.&nbsp;

  - [OVERLAPPED](pywintypes.md#pywintypesoverlapped)

    Creates a new[PyOVERLAPPED](#pyoverlapped) object&nbsp;

  - [IID](pywintypes.md#pywintypesiid)

    Makes an[PyIID](#pyiid) object from a string\.&nbsp;

  - [Time](pywintypes.md#pywintypestime)

    Makes a[PyTime](#pytime) object from the argument\.&nbsp;

  - [CreateGuid](pywintypes.md#pywintypescreateguid)

    Creates a new, unique GUIID\. 

MS\_WINCE&nbsp;

  - [ACL](pywintypes.md#pywintypesacl)

    Creates a new[PyACL](#pyacl) object\.&nbsp;

  - [SID](pywintypes.md#pywintypessid)

    Creates a new[PySID](#pysid) object\.&nbsp;

  - [SECURITY\_ATTRIBUTES](pywintypes.md#pywintypessecurity_attributes)

    Creates a new[PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes) object\.&nbsp;

  - [SECURITY\_DESCRIPTOR](pywintypes.md#pywintypessecurity_descriptor)

    Creates a new[PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor) object\. 

NO\_PYWINTYPES\_SECURITY&nbsp;

  - [HANDLE](pywintypes.md#pywintypeshandle)

    Creates a new[PyHANDLE](#pyhandle) object\.&nbsp;

  - [HKEY](pywintypes.md#pywintypeshkey)

    Creates a new[PyHKEY](#pyhkey) object\.&nbsp;

  - [WAVEFORMATEX](pywintypes.md#pywintypeswaveformatex)

    Creates a new[PyWAVEFORMATEX](#pywaveformatex) object\.&nbsp;

## [pywintypes](#pywintypes)\.ACL

[PyACL](#pyacl) =ACL\(bufSize\)
Creates a new ACL object

#### Parameters


  - bufSize=64 : int

    The size for the ACL\.

## [pywintypes](#pywintypes)\.CreateGuid

[PyIID](#pyiid) =CreateGuid\(\)
Creates a new, unique GUIID\.

## [pywintypes](#pywintypes)\.DosDateTimeToTime

[PyTime](#pytime) =DosDateTimeToTime\(\)
Converts an MS-DOS Date/Time to a standard Time object\.

## [pywintypes](#pywintypes)\.HANDLE

[PyHANDLE](#pyhandle) =HANDLE\(\)
Creates a new HANDLE object

## [pywintypes](#pywintypes)\.HKEY

[PyHKEY](#pyhkey) =HKEY\(\)
Creates a new HKEY object

## [pywintypes](#pywintypes)\.IID

[PyIID](#pyiid) =IID\(iidString, is\_bytes\)
Creates a new IID object

#### Parameters


  - iidString : string/Unicode

    A string representation of an IID, or a ProgID\.

  - is\_bytes=False : bool

    Indicates if the first param is actually the bytes of an IID structure\.

## [pywintypes](#pywintypes)\.IsTextUnicode



int, int =IsTextUnicode\(str, flags\)
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

## [pywintypes](#pywintypes)\.OVERLAPPED

[PyOVERLAPPED](#pyoverlapped) =OVERLAPPED\(\)
Creates a new OVERLAPPED object

## [pywintypes](#pywintypes)\.SECURITY\_ATTRIBUTES

[PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes) =SECURITY\_ATTRIBUTES\(\)
Creates a new SECURITY\_ATTRIBUTES object

## [pywintypes](#pywintypes)\.SECURITY\_DESCRIPTOR

[PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor) =SECURITY\_DESCRIPTOR\(\)
Creates a new SECURITY\_DESCRIPTOR object

#### Alternative Parameters


  - data

    A buffer \(eg, a string\) with the raw bytes for the security descriptor\.

## [pywintypes](#pywintypes)\.SID

[PySID](#pysid) =SID\(bufSize\)
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

## [pywintypes](#pywintypes)\.Time

[PyTime](#pytime) =Time\(timeRepr\)
Creates a new time object\.

#### Parameters


  - timeRepr : object

    An integer/float/tuple time representation\.

#### Comments


Note that the parameter can be any object that supports 

int\(object\) - for example , another PyTime object\.
The integer should be as defined by the Python time module\. 

See the description of the[PyTime](#pytime) object for more information\.

## [pywintypes](#pywintypes)\.Unicode

[PyUnicode](#pyunicode) =Unicode\(\)
Creates a new Unicode object

## [pywintypes](#pywintypes)\.UnicodeFromRaw

[PyUnicode](#pyunicode) =UnicodeFromRaw\(str\)
Creates a new Unicode object from raw binary data

#### Parameters


  - str : string/buffer

    The string containing the binary data\.

## [pywintypes](#pywintypes)\.WAVEFORMATEX

[PyWAVEFORMATEX](#pywaveformatex) =WAVEFORMATEX\(\)
Creates a new WAVEFORMATEX object