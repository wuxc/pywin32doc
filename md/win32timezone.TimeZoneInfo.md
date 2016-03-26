
## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).GetDSTEndTime

 **GetDSTEndTime(** )
Given a year, determines the time when daylight savings ends.

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).GetDSTEndTime

 **GetDSTEndTime( *self*  *, year* ** )
Given a year, determines the time when daylight savings ends.

#### Parameters


     *self* :

    self

     *year* :

    year

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).GetDSTStartTime

 **GetDSTStartTime(** )
Given a year, determines the time when daylight savings time starts

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).GetDSTStartTime

 **GetDSTStartTime( *self*  *, year* ** )
Given a year, determines the time when daylight savings time starts

#### Parameters


     *self* :

    self

     *year* :

    year

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).dst

 **dst(** )
Calculates the daylight savings offset according to the datetime.tzinfo spec

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).dst

 **dst( *self*  *, dt* ** )
Calculates the daylight savings offset according to the datetime.tzinfo spec

#### Parameters


     *self* :

    self

     *dt* :

    dt

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).getWinInfo

 **getWinInfo(** )
Return the most relevant "info" for this time zone 

in the target year.

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).getWinInfo

 **getWinInfo( *self*  *, targetYear* ** )
Return the most relevant "info" for this time zone 

in the target year.

#### Parameters


     *self* :

    self

     *targetYear* :

    targetYear

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).get_sorted_time_zone_names

 **get_sorted_time_zone_names(** )
Return a list of time zone names that can be used to initialize TimeZoneInfo instances

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).get_sorted_time_zone_names

 **get_sorted_time_zone_names(** )
Return a list of time zone names that can be used to initialize TimeZoneInfo instances

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).get_sorted_time_zones

 **get_sorted_time_zones(** )
Return the time zones sorted by some key. 

key must be a function that takes a TimeZoneInfo object and returns 

a value suitable for sorting on. 

The key defaults to the bias (descending), as is done in Windows 

(see http://blogs.msdn.com/michkap/archive/2006/12/22/1350684.aspx)

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).get_sorted_time_zones

 **get_sorted_time_zones( *key* ** )
Return the time zones sorted by some key. 

key must be a function that takes a TimeZoneInfo object and returns 

a value suitable for sorting on. 

The key defaults to the bias (descending), as is done in Windows 

(see http://blogs.msdn.com/michkap/archive/2006/12/22/1350684.aspx)

#### Parameters


     *key=None* :

    key

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).local

 **local(** )
Returns the local time zone as defined by the operating system in the 

registry.

#### Comments
Now one can compare the results of the two offset aware values
&gt&gt&gt (now_UTC - now_local) &lt datetime.timedelta(seconds = 5)

True
This is a @classmethod.
&gt&gt&gt localTZ = TimeZoneInfo.local()

&gt&gt&gt now_local = datetime.datetime.now(localTZ)

&gt&gt&gt now_UTC = datetime.datetime.utcnow()

&gt&gt&gt (now_UTC - now_local) &lt datetime.timedelta(seconds = 5)

Traceback (most recent call last):

...

TypeError: can't subtract offset-naive and offset-aware datetimes
&gt&gt&gt now_UTC = now_UTC.replace(tzinfo = TimeZoneInfo('GMT Standard Time', True))

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).local

 **local( *class_* ** )
Returns the local time zone as defined by the operating system in the 

registry.

#### Parameters


     *class_* :

    class_

#### Comments
Now one can compare the results of the two offset aware values
&gt&gt&gt (now_UTC - now_local) &lt datetime.timedelta(seconds = 5)

True
&gt&gt&gt localTZ = TimeZoneInfo.local()

&gt&gt&gt now_local = datetime.datetime.now(localTZ)

&gt&gt&gt now_UTC = datetime.datetime.utcnow()

&gt&gt&gt (now_UTC - now_local) &lt datetime.timedelta(seconds = 5)

Traceback (most recent call last):

...

TypeError: can't subtract offset-naive and offset-aware datetimes
&gt&gt&gt now_UTC = now_UTC.replace(tzinfo = TimeZoneInfo('GMT Standard Time', True))

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).utc

 **utc(** )
Returns a time-zone representing UTC.

#### Comments
Same as TimeZoneInfo('GMT Standard Time', True) but caches the result 

for performance.
&gt&gt&gt isinstance(TimeZoneInfo.utc(), TimeZoneInfo)

True
This is a @classmethod.

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).utc

 **utc( *class_* ** )
Returns a time-zone representing UTC.

#### Parameters


     *class_* :

    class_

#### Comments
Same as TimeZoneInfo('GMT Standard Time', True) but caches the result 

for performance.
&gt&gt&gt isinstance(TimeZoneInfo.utc(), TimeZoneInfo)

True

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).utcoffset

 **utcoffset(** )
Calculates the utcoffset according to the datetime.tzinfo spec

## [win32timezone.TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo).utcoffset

 **utcoffset( *self*  *, dt* ** )
Calculates the utcoffset according to the datetime.tzinfo spec

#### Parameters


     *self* :

    self

     *dt* :

    dt