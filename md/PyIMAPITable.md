# PyIMAPITable


## PyIMAPITable Object

An COM interface to MAPI 

Derived from [PyIUnknown](PyIUnknown.md)

#### Methods

  - [Advise](PyIMAPITable.md#pyimapitableadvise)

    Registers to receive notification of specified events affecting the table\.&nbsp;

  - [SeekRow](PyIMAPITable.md#pyimapitableseekrow)

    Moves the cursor to a specific position in the table\.&nbsp;

  - [SeekRowApprox](PyIMAPITable.md#pyimapitableseekrowapprox)

    Moves the cursor to an approximate fractional position in the table\.&nbsp;

  - [GetRowCount](PyIMAPITable.md#pyimapitablegetrowcount)

    Returns the total number of rows in the table\.&nbsp;

  - [QueryRows](PyIMAPITable.md#pyimapitablequeryrows)

    Returns one or more rows from a table, beginning at the current cursor position\.&nbsp;

  - [SetColumns](PyIMAPITable.md#pyimapitablesetcolumns)

    Defines the particular properties and order of properties to appear as columns in the table\.&nbsp;

  - [GetStatus](PyIMAPITable.md#pyimapitablegetstatus)

    Returns the table's status and type\.&nbsp;

  - [QueryPosition](PyIMAPITable.md#pyimapitablequeryposition)

    Retrieves the current table row position of the cursor, based on a fractional value\.&nbsp;

  - [QueryColumns](PyIMAPITable.md#pyimapitablequerycolumns)

    Returns a list of columns for the table\.&nbsp;

  - [Abort](PyIMAPITable.md#pyimapitableabort)

    Stops any asynchronous operations currently in progress for the table\.&nbsp;

  - [FreeBookmark](PyIMAPITable.md#pyimapitablefreebookmark)

    Releases the memory associated with a bookmark\.&nbsp;

  - [CreateBookmark](PyIMAPITable.md#pyimapitablecreatebookmark)

    Marks the table's current position\.&nbsp;

  - [Restrict](PyIMAPITable.md#pyimapitablerestrict)

    Applies a filter to a table, reducing the row set to only those rows matching the specified criteria\.&nbsp;

  - [FindRow](PyIMAPITable.md#pyimapitablefindrow)

    Finds the next row in a table that matches specific search criteria\.&nbsp;

  - [SortTable](PyIMAPITable.md#pyimapitablesorttable)

    Orders the rows of the table based on sort criteria\.&nbsp;

  - [Unadvise](PyIMAPITable.md#pyimapitableunadvise)

    Cancels the sending of notifications previously set up with a call to the IMAPITable::Advise method\.&nbsp;


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.Abort

Abort\(\)
Stops any asynchronous operations currently in progress for the table\.


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.Advise

int = Advise\(eventMask, adviseSink

\)
Registers to receive notification of specified events affecting the table\.

#### Parameters

  - eventMask : int

    

  - adviseSink : PyIMAPIAdviseSink

    


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.CreateBookmark

int = CreateBookmark\(\)
Marks the table's current position\.


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.FindRow

FindRow\(restriction, bookmarkOrigin, flags\)
Finds the next row in a table that matches specific search criteria\.

#### Parameters

  - restriction : [PySRestriction](PySRestriction.md)

    

  - bookmarkOrigin : int

    

  - flags : int

    


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.FreeBookmark

FreeBookmark\(bookmark\)
Releases the memory associated with a bookmark\.

#### Parameters

  - bookmark : int

    


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.GetRowCount

int = GetRowCount\(flags\)
Returns the total number of rows in the table\.

#### Parameters

  - flags : int

    Reserved - must be zero


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.GetStatus

GetStatus\(\)
Returns the table's status and type\.

#### Return Value
Result is a tuple of \(tableStatus, tableType\)


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.QueryColumns

SPropTagArray

 = QueryColumns\(flags\)
Returns a list of columns for the table\.

#### Parameters

  - flags : int

    


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.QueryPosition

QueryPosition\(\)
Retrieves the current table row position of the cursor, based on a fractional value\.

#### Return Value
Result is a tuple of \(row, numerator, denominator\)


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.QueryRows

SRowSet

 = QueryRows\(rowCount, flags

\)
Returns one or more rows from a table, beginning at the current cursor position\.

#### Parameters

  - rowCount : int

    Number of rows to retrieve

  - flags : int

    Flags\.


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.Restrict

Restrict\(restriction, flags\)
Applies a filter to a table, reducing the row set to only those rows matching the specified criteria\.

#### Parameters

  - restriction : [PySRestriction](PySRestriction.md)

    

  - flags : int

    


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.SeekRow

int = SeekRow\(bookmark, rowCount

\)
Moves the cursor to a specific position in the table\.

#### Parameters

  - bookmark : int

    The bookmark\.

  - rowCount : int

    

#### Return Value
The result is the number of rows processed\.


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.SeekRowApprox

SeekRowApprox\(numerator, denominator\)
Moves the cursor to an approximate fractional position in the table\.

#### Parameters

  - numerator : int

    The numerator of the fraction representing the table position

  - denominator : int

    The denominator of the fraction representing the table position\. This must not be zero\.


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.SetColumns

SetColumns\(propTags, flags\)
Defines the particular properties and order of properties to appear as columns in the table\.

#### Parameters

  - propTags : SPropTagArray

    Sequence of property tags identifying properties to be included as columns in the table\.

  - flags : int

    


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.SortTable

SortTable\(sortOrderSet, flags\)
Orders the rows of the table based on sort criteria\.

#### Parameters

  - sortOrderSet : [PySSortOrderSet](PySSortOrderSet.md)

    

  - flags : int

    


## [PyIMAPITable](PyIMAPITable.md#pyimapitable)\.Unadvise

Unadvise\(handle\)
Cancels the sending of notifications previously set up with a call to the IMAPITable::Advise method\.

#### Parameters

  - handle : int

    Handle returned from [PyIMAPITable::Advise](PyIMAPITable.md#pyimapitableadvise)