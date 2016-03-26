# cursor


## cursor Object

An object representing an ODBC cursor\.

#### Methods

  - [close](cursor.md#cursorclose)

    Closes the cursor&nbsp;

  - [execute](cursor.md#cursorexecute)

    Execute some SQL&nbsp;

  - [fetchone](cursor.md#cursorfetchone)

    Fetch one row of data&nbsp;

  - [fetchmany](cursor.md#cursorfetchmany)

    Fetch many rows of data&nbsp;

  - [fetchall](cursor.md#cursorfetchall)

    Fetch all the rows of data&nbsp;

  - [setinputsizes](cursor.md#cursorsetinputsizes)

    &nbsp;

  - [setoutputsize](cursor.md#cursorsetoutputsize)

    &nbsp;


## [cursor](cursor.md#cursor)\.close

close\(\)
Closes the cursor

#### Comments

This method does nothing\!\!  I presume it should\!?\!?\!


## [cursor](cursor.md#cursor)\.execute

int = execute\(sql, \[var, \.\.\.\]

\)
Execute some SQL

#### Parameters

  - sql : string

    The SQL to execute

  - \[var, \.\.\.\]=\[\] : sequence

    Input variables\.


## [cursor](cursor.md#cursor)\.fetchall

\[data, \.\.\.\] = fetchall\(\)
Fetch all rows of data


## [cursor](cursor.md#cursor)\.fetchmany

\[data, \.\.\.\] = fetchmany\(\)
Fetch many rows of data


## [cursor](cursor.md#cursor)\.fetchone

data = fetchone\(\)
Fetch one row of data


## [cursor](cursor.md#cursor)\.setinputsizes

setinputsizes\(\)



## [cursor](cursor.md#cursor)\.setoutputsize

setoutputsize\(\)
