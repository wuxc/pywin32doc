# win32timezone

## Module win32timezone

win32timezone: 

Module for handling datetime\.tzinfo time zones using the windows 

registry for time zone information\.  The time zone names are dependent 

on the registry entries defined by the operating system\.

#### Comments
This module may be tested using the doctest module\.
Written by Jason R\. Coombs \(jaraco@jaraco\.com\)\. 

Copyright &\#194&\#169 2003-2012\. 

All Rights Reserved\.
This module is licenced for use in Mark Hammond's pywin32 

library under the same terms as the pywin32 library\.
To use this time zone module with the datetime module, simply pass 

the TimeZoneInfo object to the datetime constructor\.  For example,
&gt&gt&gt import win32timezone, datetime

&gt&gt&gt assert 'Mountain Standard Time' in win32timezone\.TimeZoneInfo\.get\_sorted\_time\_zone\_names\(\)

&gt&gt&gt MST \= win32timezone\.TimeZoneInfo\('Mountain Standard Time'\)

&gt&gt&gt now \= datetime\.datetime\.now\(MST\)
The now object is now a time-zone aware object, and daylight savings- 

aware methods may be called on it\.
&gt&gt&gt now\.utcoffset\(\) in \(datetime\.timedelta\(-1, 61200\), datetime\.timedelta\(-1, 64800\)\)

True
\(note that the result of utcoffset call will be different based on when now was 

generated, unless standard time is always used\)
&gt&gt&gt now \= datetime\.datetime\.now\(TimeZoneInfo\('Mountain Standard Time', True\)\)

&gt&gt&gt now\.utcoffset\(\)

datetime\.timedelta\(-1, 61200\)
&gt&gt&gt aug2 \= datetime\.datetime\(2003, 8, 2, tzinfo \= MST\)

&gt&gt&gt tuple\(aug2\.utctimetuple\(\)\)

\(2003, 8, 2, 6, 0, 0, 5, 214, 0\)

&gt&gt&gt nov2 \= datetime\.datetime\(2003, 11, 25, tzinfo \= MST\)

&gt&gt&gt tuple\(nov2\.utctimetuple\(\)\)

\(2003, 11, 25, 7, 0, 0, 1, 329, 0\)
To convert from one timezone to another, just use the astimezone method\.
&gt&gt&gt aug2\.isoformat\(\)

'2003-08-02T00:00:00-06:00'

&gt&gt&gt aug2est \= aug2\.astimezone\(win32timezone\.TimeZoneInfo\('Eastern Standard Time'\)\)

&gt&gt&gt aug2est\.isoformat\(\)

'2003-08-02T02:00:00-04:00'
calling the displayName member will return the display name as set in the 

registry\.
&gt&gt&gt est \= win32timezone\.TimeZoneInfo\('Eastern Standard Time'\)

&gt&gt&gt str\(est\.displayName\)

'\(UTC-05:00\) Eastern Time \(US & Canada\)'
&gt&gt&gt gmt \= win32timezone\.TimeZoneInfo\('GMT Standard Time', True\)

&gt&gt&gt str\(gmt\.displayName\)

'\(UTC\) Dublin, Edinburgh, Lisbon, London'
To get the complete list of available time zone keys,
&gt&gt&gt zones \= win32timezone\.TimeZoneInfo\.get\_all\_time\_zones\(\)
If you want to get them in an order that's sorted longitudinally
&gt&gt&gt zones \= win32timezone\.TimeZoneInfo\.get\_sorted\_time\_zones\(\)
TimeZoneInfo now supports being pickled and comparison
&gt&gt&gt import pickle

&gt&gt&gt tz \= win32timezone\.TimeZoneInfo\('China Standard Time'\)

&gt&gt&gt tz \=\= pickle\.loads\(pickle\.dumps\(tz\)\)

True
It's possible to construct a TimeZoneInfo from a TimeZoneDescription 

including the currently-defined zone\.
&gt&gt&gt tz \= win32timezone\.TimeZoneInfo\(TimeZoneDefinition\.current\(\)\)

&gt&gt&gt tz \=\= pickle\.loads\(pickle\.dumps\(tz\)\)

True
&gt&gt&gt aest \= win32timezone\.TimeZoneInfo\('AUS Eastern Standard Time'\)

&gt&gt&gt est \= win32timezone\.TimeZoneInfo\('E\. Australia Standard Time'\)

&gt&gt&gt dt \= datetime\.datetime\(2006, 11, 11, 1, 0, 0, tzinfo \= aest\)

&gt&gt&gt estdt \= dt\.astimezone\(est\)

&gt&gt&gt estdt\.strftime\('%Y-%m-%d %H:%M:%S'\)

'2006-11-11 00:00:00'
&gt&gt&gt dt \= datetime\.datetime\(2007, 1, 12, 1, 0, 0, tzinfo \= aest\)

&gt&gt&gt estdt \= dt\.astimezone\(est\)

&gt&gt&gt estdt\.strftime\('%Y-%m-%d %H:%M:%S'\)

'2007-01-12 00:00:00'
&gt&gt&gt dt \= datetime\.datetime\(2007, 6, 13, 1, 0, 0, tzinfo \= aest\)

&gt&gt&gt estdt \= dt\.astimezone\(est\)

&gt&gt&gt estdt\.strftime\('%Y-%m-%d %H:%M:%S'\)

'2007-06-13 01:00:00'
Microsoft now has a patch for handling time zones in 2007 \(see 

http://support\.microsoft\.com/gp/cp\_dst\)
As a result, patched systems will give an incorrect result for 

dates prior to the designated year except for Vista and its 

successors, which have dynamic time zone support\.
&gt&gt&gt nov2\_pre\_change \= datetime\.datetime\(2003, 11, 2, tzinfo \= MST\)

&gt&gt&gt old\_response \= \(2003, 11, 2, 7, 0, 0, 6, 306, 0\)

&gt&gt&gt incorrect\_patch\_response \= \(2003, 11, 2, 6, 0, 0, 6, 306, 0\)

&gt&gt&gt pre\_response \= nov2\_pre\_change\.utctimetuple\(\)

&gt&gt&gt pre\_response in \(old\_response, incorrect\_patch\_response\)

True
Furthermore, unpatched systems pre-Vista will give an incorrect 

result for dates after 2007\.
&gt&gt&gt nov2\_post\_change \= datetime\.datetime\(2007, 11, 2, tzinfo \= MST\)

&gt&gt&gt incorrect\_unpatched\_response \= \(2007, 11, 2, 7, 0, 0, 4, 306, 0\)

&gt&gt&gt new\_response \= \(2007, 11, 2, 6, 0, 0, 4, 306, 0\)

&gt&gt&gt post\_response \= nov2\_post\_change\.utctimetuple\(\)

&gt&gt&gt post\_response in \(new\_response, incorrect\_unpatched\_response\)

True
There is a function you can call to get some capabilities of the time 

zone data\.
&gt&gt&gt caps \= GetTZCapabilities\(\)

&gt&gt&gt isinstance\(caps, dict\)

True

&gt&gt&gt 'MissingTZPatch' in caps

True

&gt&gt&gt 'DynamicTZSupport' in caps

True
&gt&gt&gt both\_dates\_correct \= \(pre\_response \=\= old\_response and post\_response \=\= new\_response\)

&gt&gt&gt old\_dates\_wrong \= \(pre\_response \=\= incorrect\_patch\_response\)

&gt&gt&gt new\_dates\_wrong \= \(post\_response \=\= incorrect\_unpatched\_response\)
&gt&gt&gt caps\['DynamicTZSupport'\] \=\= both\_dates\_correct

True
&gt&gt&gt \(not caps\['DynamicTZSupport'\] and caps\['MissingTZPatch'\]\) \=\= new\_dates\_wrong

True
&gt&gt&gt \(not caps\['DynamicTZSupport'\] and not caps\['MissingTZPatch'\]\) \=\= old\_dates\_wrong

True
This test helps ensure language support for unicode characters
&gt&gt&gt x \= TIME\_ZONE\_INFORMATION\(0, u'fran&\#195&\#167ais'\)
Test conversion from one time zone to another at a DST boundary
&gt&gt&gt tz\_hi \= TimeZoneInfo\('Hawaiian Standard Time'\)

&gt&gt&gt tz\_pac \= TimeZoneInfo\('Pacific Standard Time'\)

&gt&gt&gt time\_before \= datetime\.datetime\(2011, 11, 5, 15, 59, 59, tzinfo\=tz\_hi\)

&gt&gt&gt tz\_hi\.utcoffset\(time\_before\)

datetime\.timedelta\(-1, 50400\)

&gt&gt&gt tz\_hi\.dst\(time\_before\)

datetime\.timedelta\(0\)
Hawaii doesn't need dynamic TZ info
&gt&gt&gt getattr\(tz\_hi, 'dynamicInfo', None\)
Here's a time that gave some trouble as reported in \#3523104 

because one minute later, the equivalent UTC time changes from DST 

in the U\.S\.
&gt&gt&gt dt\_hi \= datetime\.datetime\(2011, 11, 5, 15, 59, 59, 0, tzinfo\=tz\_hi\)

&gt&gt&gt dt\_hi\.timetuple\(\)

time\.struct\_time\(tm\_year\=2011, tm\_mon\=11, tm\_mday\=5, tm\_hour\=15, tm\_min\=59, tm\_sec\=59, tm\_wday\=5, tm\_yday\=309, tm\_isdst\=0\)

&gt&gt&gt dt\_hi\.utctimetuple\(\)

time\.struct\_time\(tm\_year\=2011, tm\_mon\=11, tm\_mday\=6, tm\_hour\=1, tm\_min\=59, tm\_sec\=59, tm\_wday\=6, tm\_yday\=310, tm\_isdst\=0\)
Convert the time to pacific time\.
&gt&gt&gt dt\_pac \= dt\_hi\.astimezone\(tz\_pac\)

&gt&gt&gt dt\_pac\.timetuple\(\)

time\.struct\_time\(tm\_year\=2011, tm\_mon\=11, tm\_mday\=5, tm\_hour\=18, tm\_min\=59, tm\_sec\=59, tm\_wday\=5, tm\_yday\=309, tm\_isdst\=1\)
Notice that the UTC time is almost 2am\.
&gt&gt&gt dt\_pac\.utctimetuple\(\)

time\.struct\_time\(tm\_year\=2011, tm\_mon\=11, tm\_mday\=6, tm\_hour\=1, tm\_min\=59, tm\_sec\=59, tm\_wday\=6, tm\_yday\=310, tm\_isdst\=0\)
Now do the same tests one minute later in Hawaii\.
&gt&gt&gt time\_after \= datetime\.datetime\(2011, 11, 5, 16, 0, 0, 0, tzinfo\=tz\_hi\)

&gt&gt&gt tz\_hi\.utcoffset\(time\_after\)

datetime\.timedelta\(-1, 50400\)

&gt&gt&gt tz\_hi\.dst\(time\_before\)

datetime\.timedelta\(0\)
&gt&gt&gt dt\_hi \= datetime\.datetime\(2011, 11, 5, 16, 0, 0, 0, tzinfo\=tz\_hi\)

&gt&gt&gt print dt\_hi\.timetuple\(\)

time\.struct\_time\(tm\_year\=2011, tm\_mon\=11, tm\_mday\=5, tm\_hour\=16, tm\_min\=0, tm\_sec\=0, tm\_wday\=5, tm\_yday\=309, tm\_isdst\=0\)

&gt&gt&gt print dt\_hi\.utctimetuple\(\)

time\.struct\_time\(tm\_year\=2011, tm\_mon\=11, tm\_mday\=6, tm\_hour\=2, tm\_min\=0, tm\_sec\=0, tm\_wday\=6, tm\_yday\=310, tm\_isdst\=0\)
According to the docs, this is what astimezone does\.
&gt&gt&gt utc \= \(dt\_hi - dt\_hi\.utcoffset\(\)\)\.replace\(tzinfo\=tz\_pac\)

&gt&gt&gt utc

datetime\.datetime\(2011, 11, 6, 2, 0, tzinfo\=TimeZoneInfo\('Pacific Standard Time'\)\)

&gt&gt&gt tz\_pac\.fromutc\(utc\) \=\= dt\_hi\.astimezone\(tz\_pac\)

True

&gt&gt&gt tz\_pac\.fromutc\(utc\)

datetime\.datetime\(2011, 11, 5, 19, 0, tzinfo\=TimeZoneInfo\('Pacific Standard Time'\)\)
Make sure the converted time is correct\.
&gt&gt&gt dt\_pac \= dt\_hi\.astimezone\(tz\_pac\)

&gt&gt&gt dt\_pac\.timetuple\(\)

time\.struct\_time\(tm\_year\=2011, tm\_mon\=11, tm\_mday\=5, tm\_hour\=19, tm\_min\=0, tm\_sec\=0, tm\_wday\=5, tm\_yday\=309, tm\_isdst\=1\)

&gt&gt&gt dt\_pac\.utctimetuple\(\)

time\.struct\_time\(tm\_year\=2011, tm\_mon\=11, tm\_mday\=6, tm\_hour\=2, tm\_min\=0, tm\_sec\=0, tm\_wday\=6, tm\_yday\=310, tm\_isdst\=0\)
Check some internal methods
&gt&gt&gt tz\_pac\.\_getStandardBias\(datetime\.datetime\(2011, 1, 1\)\)

datetime\.timedelta\(0, 28800\)

&gt&gt&gt tz\_pac\.\_getDaylightBias\(datetime\.datetime\(2011, 1, 1\)\)

datetime\.timedelta\(0, 25200\)
Test the offsets
&gt&gt&gt offset \= tz\_pac\.utcoffset\(datetime\.datetime\(2011, 11, 6, 2, 0\)\)

&gt&gt&gt offset \=\= datetime\.timedelta\(hours\=-8\)

True

&gt&gt&gt dst\_offset \= tz\_pac\.dst\(datetime\.datetime\(2011, 11, 6, 2, 0\) \+ offset\)

&gt&gt&gt dst\_offset \=\= datetime\.timedelta\(hours\=1\)

True

&gt&gt&gt \(offset \+ dst\_offset\) \=\= datetime\.timedelta\(hours\=-7\)

True
Test offsets that occur right at the DST changeover
&gt&gt&gt datetime\.datetime\.utcfromtimestamp\(1320570000\)\.replace\(

\.\.\.     tzinfo\=TimeZoneInfo\.utc\(\)\)\.astimezone\(tz\_pac\)

datetime\.datetime\(2011, 11, 6, 1, 0, tzinfo\=TimeZoneInfo\('Pacific Standard Time'\)\)

#### Methods


  - [GetTZCapabilities](win32timezone.md#win32timezonegettzcapabilities)

    Run a few known tests to determine the capabilities of the time zone database&nbsp;

  - [GetSortedTimeZoneNames](win32timezone.md#win32timezonegetsortedtimezonenames)

    Return a list of time zone names that can be used to initialize TimeZoneInfo instances&nbsp;

  - [now](win32timezone.md#win32timezonenow)

    Return the local time now with timezone awareness as enabled&nbsp;

  - [resolveMUITimeZone](win32timezone.md#win32timezoneresolvemuitimezone)

    Resolve a multilingual user interface resource for the time zone name&nbsp;

  - [deprecated](win32timezone.md#win32timezonedeprecated)

    This is a decorator which can be used to mark functions&nbsp;

  - [utcnow](win32timezone.md#win32timezoneutcnow)

    Return the UTC time now with timezone awareness as enabled&nbsp;

#### Classes


  - [TimeZoneInfo](#win32timezone.timezoneinfo)

    Main class for handling Windows time zones\.&nbsp;

  - [TimeZoneDefinition](#win32timezone.timezonedefinition)

    A time zone definition class based on the win32&nbsp;

  - [RangeMap](#win32timezone.rangemap)

    A dictionary-like object that uses the keys as bounds for a range\.&nbsp;

## [win32timezone](#win32timezone)\.GetSortedTimeZoneNames

 **GetSortedTimeZoneNames\(** \)
Return a list of time zone names that can be used to initialize TimeZoneInfo instances

## [win32timezone](#win32timezone)\.GetTZCapabilities

 **GetTZCapabilities\(** \)
Run a few known tests to determine the capabilities of the time zone database 

on this machine\. 

Note Dynamic Time Zone support is not available on any platform at this time; this 

is a limitation of this library, not the platform\.

## [win32timezone](#win32timezone)\.deprecated

 **deprecated\( *func*  *, name* ** \)
This is a decorator which can be used to mark functions 

as deprecated\. It will result in a warning being emmitted 

when the function is used\.

#### Parameters


  -  *func* :

    func

  -  *name\='Unknown'* :

    name

## [win32timezone](#win32timezone)\.now

 **now\(** \)
Return the local time now with timezone awareness as enabled 

by this module
&gt&gt&gt now\_local \= now\(\)

## [win32timezone](#win32timezone)\.resolveMUITimeZone

 **resolveMUITimeZone\( *spec* ** \)
Resolve a multilingual user interface resource for the time zone name

#### Parameters


  -  *spec* :

    spec

#### Comments
spec should be of the format @path,-stringID\[;comment\] 

see http://msdn2\.microsoft\.com/en-us/library/ms725481\.aspx for details
&gt&gt&gt \#some pre-amble for the doc-tests to be py2k and py3k aware\)

&gt&gt&gt try: unicode and None

\.\.\. except NameError: unicode\=str

\.\.\.

&gt&gt&gt import sys

&gt&gt&gt result \= resolveMUITimeZone\('@tzres\.dll,-110'\)

&gt&gt&gt expectedResultType \= \[type\(None\),unicode\]\[sys\.getwindowsversion\(\) &gt\= \(6,\)\]

&gt&gt&gt type\(result\) is expectedResultType

True

## [win32timezone](#win32timezone)\.utcnow

 **utcnow\(** \)
Return the UTC time now with timezone awareness as enabled 

by this module
&gt&gt&gt now \= utcnow\(\)