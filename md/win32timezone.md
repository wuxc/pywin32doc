
## [win32timezone](#README.md#win32timezone).GetSortedTimeZoneNames

 **GetSortedTimeZoneNames(** )
Return a list of time zone names that can be used to initialize TimeZoneInfo instances

## [win32timezone](#README.md#win32timezone).GetTZCapabilities

 **GetTZCapabilities(** )
Run a few known tests to determine the capabilities of the time zone database 

on this machine. 

Note Dynamic Time Zone support is not available on any platform at this time; this 

is a limitation of this library, not the platform.

## [win32timezone](#README.md#win32timezone).deprecated

 **deprecated( *func*  *, name* ** )
This is a decorator which can be used to mark functions 

as deprecated. It will result in a warning being emmitted 

when the function is used.

#### Parameters


     *func* :

    func

     *name='Unknown'* :

    name

## [win32timezone](#README.md#win32timezone).now

 **now(** )
Return the local time now with timezone awareness as enabled 

by this module
&gt&gt&gt now_local = now()

## [win32timezone](#README.md#win32timezone).resolveMUITimeZone

 **resolveMUITimeZone( *spec* ** )
Resolve a multilingual user interface resource for the time zone name

#### Parameters


     *spec* :

    spec

#### Comments
spec should be of the format @path,-stringID[;comment] 

see http://msdn2.microsoft.com/en-us/library/ms725481.aspx for details
&gt&gt&gt #some pre-amble for the doc-tests to be py2k and py3k aware)

&gt&gt&gt try: unicode and None

... except NameError: unicode=str

...

&gt&gt&gt import sys

&gt&gt&gt result = resolveMUITimeZone('@tzres.dll,-110')

&gt&gt&gt expectedResultType = [type(None),unicode][sys.getwindowsversion() &gt= (6,)]

&gt&gt&gt type(result) is expectedResultType

True

## [win32timezone](#README.md#win32timezone).utcnow

 **utcnow(** )
Return the UTC time now with timezone awareness as enabled 

by this module
&gt&gt&gt now = utcnow()