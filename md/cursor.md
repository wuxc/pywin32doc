# cursor

## cursor Object

An object representing an ODBC cursor.

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

## [cursor](#cursor).close

 __close(__ )
Closes the cursor

#### Comments
This method does nothing!!  I presume it should!?!?!

## [cursor](#cursor).execute

int = __execute( *sql*  *, [var, ...]* __ )
Execute some SQL

#### Parameters


  -  *sql* : string

    The SQL to execute

  -  *[var, ...]=[]* : sequence

    Input variables.

## [cursor](#cursor).fetchall

[data, ...] = __fetchall(__ )
Fetch all rows of data

## [cursor](#cursor).fetchmany

[data, ...] = __fetchmany(__ )
Fetch many rows of data

## [cursor](#cursor).fetchone

data = __fetchone(__ )
Fetch one row of data

## [cursor](#cursor).setinputsizes

 __setinputsizes(__ )


## [cursor](#cursor).setoutputsize

 __setoutputsize(__ )
