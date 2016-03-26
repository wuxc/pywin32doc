# PyTime

## PyTime Object

A Python object, representing an instant in time.

#### Comments
A PyTime object is used primarily when exchanging date/time information 

with COM objects or other win32 functions.
Using int(timeObject) will return an integer compatible with 

the standard Python time module.

#### Example
First import the time module
import timeTo return a simple string
time.ctime(int(timeObject))To return a string formatted as the long date in control panel
time.strftime("%#c", time.localtime(int(timeObject)))
#### See Also


  - [pywintypes::Time](pywintypes.md#pywintypestime)

#### Methods


  - [Format](PyTime.md#pytimeformat)

    Formats the time value&nbsp;

  - [__int__](PyTime.md#pytime__int__)

    Used when an integer representation of the time object is required.&nbsp;

  - [__float__](PyTime.md#pytime__float__)

    Used when a floating point representation of the time object is required.&nbsp;

  - [__cmp__](PyTime.md#pytime__cmp__)

    Used when time objects are compared. 

tp_compare&nbsp;

  - [__repr__](PyTime.md#pytime__repr__)

    Used for repr(ob) 

tp_repr&nbsp;

  - [__hash__](PyTime.md#pytime__hash__)

    Used when the hash value of an time object is required 

tp_hash&nbsp;

  - [__str__](PyTime.md#pytime__str__)

    Used for str(ob) 

tp_str&nbsp;

#### Properties

  -  __int year__ 
    

  -  __int month__ 
    

  -  __int weekday__ 
    

  -  __int day__ 
    

  -  __int hour__ 
    

  -  __int minute__ 
    

  -  __int second__ 
    

  -  __int msec__ 
    

## [PyTime](#pytime).Format

[PyUnicode](#pyunicode)= __Format( *format* __ )
Formats the time value.

#### Parameters


  -  *format=%c* : string

    The format.  See the comments section for a description of the supported flags.

#### Comments
The following format characters are supported.

 __Character__  __Description__ %aAbbreviated weekday name%AFull weekday name%bAbbreviated month name%BFull month name%cDate and time representation appropriate for locale%dDay of month as decimal number (01 - 31)%HHour in 24-hour format (00 - 23)%IHour in 12-hour format (01 - 12)%jDay of year as decimal number (001 - 366)%mMonth as decimal number (01 - 12)%MMinute as decimal number (00 - 59)%pCurrent locale's A.M./P.M. indicator for 12-hour clock%SSecond as decimal number (00 - 59)%UWeek of year as decimal number, with Sunday as first day of week (00 - 51)%wWeekday as decimal number (0 - 6; Sunday is 0)%WWeek of year as decimal number, with Monday as first day of week (00 - 51)%xDate representation for current locale%XTime representation for current locale%yYear without century, as decimal number (00 - 99)%YYear with century, as decimal number%z, %ZTime-zone name or abbreviation; no characters if time zone is unknown%%Percent signAs in the printf function, the # flag may prefix any formatting code. In that case, the meaning of the format code is changed as follows.


## [PyTime](#pytime).__cmp__

int = ____cmp__(__ )
Used when time objects are compared.

## [PyTime](#pytime).__float__

 ____float__(__ )
Used when a floating point representation of the time object is required.

## [PyTime](#pytime).__hash__

int = ____hash__(__ )
Used when the hash value of an time object is required

## [PyTime](#pytime).__int__

 ____int__(__ )
Used when an integer representation of the time object is required.

#### Return Value
The integer result can be used with the time module. 

Please see the main description for the[PyTime](#pytime)object.

## [PyTime](#pytime).__nonzero__

 ____nonzero__(__ )
Used for detecting true/false. 

static*/ int PyTime::nonzeroFunc(PyObject *ob)

## [PyTime](#pytime).__repr__

 ____repr__(__ )


## [PyTime](#pytime).__str__

string = ____str__(__ )
Used when a (8-bit) string representation of the time object is required.