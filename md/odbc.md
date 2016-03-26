# odbc

## Module odbc

A Python wrapper around the ODBC API.

#### Methods


  - [odbc](odbc.md#odbcodbc)

    Creates an[connection](#connection)object.&nbsp;

  - [SQLDataSources](odbc.md#odbcsqldatasources)

    Enumerates ODBC data sources.&nbsp;

## [odbc](#odbc).SQLDataSources

(name, desc)/None = __SQLDataSources( *direction* __ )
Enumerates ODBC data sources

#### Parameters


  -  *direction* : int

    One of SQL_FETCH_* flags indicating how to retrieve data sources

#### Return Value
The result is None when SQL_NO_DATA is returned from ODBC.

## [odbc](#odbc).odbc

[connection](#connection)= __odbc( *connectionString* __ )
Creates an ODBC connection

#### Parameters


  -  *connectionString* : string

    An ODBC connection string. 

For backwards-compatibility, this parameter can be of the form 

DSN[/username[/password]] (e.g. "myDSN/myUserName/myPassword"). 

Alternatively, a full ODBC connection string can be used (e.g., 

"Driver={SQL Server};Server=(local);Database=myDatabase").