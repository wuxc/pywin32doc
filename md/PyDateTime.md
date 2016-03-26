# PyDateTime

## PyDateTime Object



A Python object, representing an instant in time\.

#### Comments


pywin32 builds for Python 3\.0 use datetime objects instead of the 

old PyTime object\.


PyDateTime is a sub-class of the regular datetime\.datetime object\. 

It is subclassed so it can provide a somewhat backwards compatible[PyDateTime::Format](PyDateTime.md#pydatetimeformat) method, but is otherwise identical\.

#### Methods


  - [Format](PyDateTime.md#pydatetimeformat)

    Formats the time value - an alias for strftime with a default param\.&nbsp;

## [PyDateTime](#pydatetime)\.Format



str =Format\(\)


#### Comments


This method is an alias for the datetime strftime method, using 

%c as the default value for the format string\.