# PyTime

## PyTime Object

A Python object, representing an instant in time\.

#### Comments
A PyTime object is used primarily when exchanging date/time information 

with COM objects or other win32 functions\.
Using int\(timeObject\) will return an integer compatible with 

the standard Python time module\.

#### Example
First import the time module
import timeTo return a simple string
time\.ctime\(int\(timeObject\)\)To return a string formatted as the long date in control panel
time\.strftime\("%\#c", time\.localtime\(int\(timeObject\)\)\)
#### See Also


  - [pywintypes::Time](pywintypes.md#pywintypestime)

#### Methods


  - [Format](PyTime.md#pytimeformat)

    Formats the time value&nbsp;

  - [\_\_int\_\_](PyTime.md#pytime__int__)

    Used when an integer representation of the time object is required\.&nbsp;

  - [\_\_float\_\_](PyTime.md#pytime__float__)

    Used when a floating point representation of the time object is required\.&nbsp;

  - [\_\_cmp\_\_](PyTime.md#pytime__cmp__)

    Used when time objects are compared\. 

tp\_compare&nbsp;

  - [\_\_repr\_\_](PyTime.md#pytime__repr__)

    Used for repr\(ob\) 

tp\_repr&nbsp;

  - [\_\_hash\_\_](PyTime.md#pytime__hash__)

    Used when the hash value of an time object is required 

tp\_hash&nbsp;

  - [\_\_str\_\_](PyTime.md#pytime__str__)

    Used for str\(ob\) 

tp\_str&nbsp;

#### Properties

  -  **int year** 
    

  -  **int month** 
    

  -  **int weekday** 
    

  -  **int day** 
    

  -  **int hour** 
    

  -  **int minute** 
    

  -  **int second** 
    

  -  **int msec** 
    

## [PyTime](#pytime)\.Format

[PyUnicode](#pyunicode)\= **Format\( *format* ** \)
Formats the time value\.

#### Parameters


  -  *format\=%c* : string

    The format\.  See the comments section for a description of the supported flags\.

#### Comments
The following format characters are supported\.

 **Character**  **Description** %aAbbreviated weekday name%AFull weekday name%bAbbreviated month name%BFull month name%cDate and time representation appropriate for locale%dDay of month as decimal number \(01 - 31\)%HHour in 24-hour format \(00 - 23\)%IHour in 12-hour format \(01 - 12\)%jDay of year as decimal number \(001 - 366\)%mMonth as decimal number \(01 - 12\)%MMinute as decimal number \(00 - 59\)%pCurrent locale's A\.M\./P\.M\. indicator for 12-hour clock%SSecond as decimal number \(00 - 59\)%UWeek of year as decimal number, with Sunday as first day of week \(00 - 51\)%wWeekday as decimal number \(0 - 6; Sunday is 0\)%WWeek of year as decimal number, with Monday as first day of week \(00 - 51\)%xDate representation for current locale%XTime representation for current locale%yYear without century, as decimal number \(00 - 99\)%YYear with century, as decimal number%z, %ZTime-zone name or abbreviation; no characters if time zone is unknown%%Percent signAs in the printf function, the \# flag may prefix any formatting code\. In that case, the meaning of the format code is changed as follows\.


## [PyTime](#pytime)\.\_\_cmp\_\_

int \= **\_\_cmp\_\_\(** \)
Used when time objects are compared\.

## [PyTime](#pytime)\.\_\_float\_\_

 **\_\_float\_\_\(** \)
Used when a floating point representation of the time object is required\.

## [PyTime](#pytime)\.\_\_hash\_\_

int \= **\_\_hash\_\_\(** \)
Used when the hash value of an time object is required

## [PyTime](#pytime)\.\_\_int\_\_

 **\_\_int\_\_\(** \)
Used when an integer representation of the time object is required\.

#### Return Value
The integer result can be used with the time module\. 

Please see the main description for the[PyTime](#pytime)object\.

## [PyTime](#pytime)\.\_\_nonzero\_\_

 **\_\_nonzero\_\_\(** \)
Used for detecting true/false\. 

static\*/ int PyTime::nonzeroFunc\(PyObject \*ob\)

## [PyTime](#pytime)\.\_\_repr\_\_

 **\_\_repr\_\_\(** \)


## [PyTime](#pytime)\.\_\_str\_\_

string \= **\_\_str\_\_\(** \)
Used when a \(8-bit\) string representation of the time object is required\.