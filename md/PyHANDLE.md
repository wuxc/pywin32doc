# PyHANDLE

## PyHANDLE Object

A Python object, representing a win32 HANDLE.

#### Comments
This object wraps a win32 HANDLE object, automatically closing it when the object 

is destroyed.  To guarantee cleanup, you can call either[PyHANDLE::Close](PyHANDLE.md#pyhandleclose), or[win32api::CloseHandle](win32api.md#win32apiclosehandle).
Most functions which accept a handle object also accept an integer - however, 

use of the handle object is encouraged.

#### Properties

  -  __long handle__ 
    Integer value of the handle

#### Methods


  - [Close](PyHANDLE.md#pyhandleclose)

    Closes the handle&nbsp;

  - [close](PyHANDLE.md#pyhandleclose)

    Synonym for[PyHANDLE::Close](PyHANDLE.md#pyhandleclose)&nbsp;

  - [Detach](PyHANDLE.md#pyhandledetach)

    Detaches the Win32 handle from the handle object.&nbsp;

  - [__nonzero__](PyHANDLE.md#pyhandle__nonzero__)

    Used for detecting true/false. 

is nb_bool in Python 3.0&nbsp;

  - [__int__](PyHANDLE.md#pyhandle__int__)

    Used when an integer representation of the handle object is required.&nbsp;

  - [__print__](PyHANDLE.md#pyhandle__print__)

    Used when the object is printed. 

tp_print&nbsp;

  - [__hash__](PyHANDLE.md#pyhandle__hash__)

    Used when the hash value of an object is required 

tp_hash&nbsp;

  - [__str__](PyHANDLE.md#pyhandle__str__)

    Used when a string representation is required 

tp_str&nbsp;

## [PyHANDLE](#pyhandle).Close

 __Close(__ )
Closes the underlying Win32 handle.

#### Comments
If the handle is already closed, no error is raised.

## [PyHANDLE](#pyhandle).Detach

int = __Detach(__ )
Detaches the Win32 handle from the handle object.

#### Comments
After calling this function, the handle is effectively invalidated, 

but the handle is not closed.  You would call this function when you 

need the underlying win32 handle to exist beyond the lifetime of the 

handle object.

#### Return Value
The result is the value of the handle before it is detached.  If the 

handle is already detached, this will return zero.

## [PyHANDLE](#pyhandle).__hash__

int = ____hash__(__ )
Used when the hash value of a HANDLE object is required

## [PyHANDLE](#pyhandle).__int__

 ____int__(__ )
Used when the handle as an integer is required.

#### Comments
To get the underling win32 handle from a PyHANDLE object, use int(handleObject)

## [PyHANDLE](#pyhandle).__long__

 ____long__(__ )
Used when the handle as an integer is required.

#### Comments
To get the underling win32 handle from a PyHANDLE object, use long(handleObject)

## [PyHANDLE](#pyhandle).__nonzero__

 ____nonzero__(__ )
Used for detecting true/false.

#### Return Value
The result is 1 if the attached handle is non zero, else 0. 

static*/ int PyHANDLE::nonzeroFunc(PyObject *ob)

## [PyHANDLE](#pyhandle).__print__

 ____print__(__ )
Used when the HANDLE object is printed.

## [PyHANDLE](#pyhandle).__str__

 ____str__(__ )
Used when a string representation of the handle object is required.