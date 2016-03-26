# PyIDirectorySearch

## PyIDirectorySearch Object

A COM interface to ADSI's IDirectorySearch interface.
Derived from[PyIUnknown](#pyiunknown)

#### Methods


  - [SetSearchPreference](PyIDirectorySearch.md#pyidirectorysearchsetsearchpreference)

    &nbsp;

  - [ExecuteSearch](PyIDirectorySearch.md#pyidirectorysearchexecutesearch)

    Executes a search and passes the results to the caller. 

Some providers, such as LDAP, will defer the actual execution until the caller invokes the[PyIDirectorySearch::GetFirstRow](PyIDirectorySearch.md#pyidirectorysearchgetfirstrow)method or the[PyIDirectorySearch::GetNextRow](PyIDirectorySearch.md#pyidirectorysearchgetnextrow)method.&nbsp;

  - [GetNextRow](PyIDirectorySearch.md#pyidirectorysearchgetnextrow)

    &nbsp;

  - [GetFirstRow](PyIDirectorySearch.md#pyidirectorysearchgetfirstrow)

    &nbsp;

  - [GetPreviousRow](PyIDirectorySearch.md#pyidirectorysearchgetpreviousrow)

    &nbsp;

  - [CloseSearchHandle](PyIDirectorySearch.md#pyidirectorysearchclosesearchhandle)

    Closes a previously opened search handle.&nbsp;

  - [AdandonSearch](PyIDirectorySearch.md#pyidirectorysearchadandonsearch)

    &nbsp;

  - [GetColumn](PyIDirectorySearch.md#pyidirectorysearchgetcolumn)

    &nbsp;

  - [GetNextColumnName](PyIDirectorySearch.md#pyidirectorysearchgetnextcolumnname)

    &nbsp;

## [PyIDirectorySearch](#pyidirectorysearch).AdandonSearch

 __AdandonSearch( *handle* __ )


#### Parameters


  -  *handle* : int

    

## [PyIDirectorySearch](#pyidirectorysearch).CloseSearchHandle

 __CloseSearchHandle( *handle* __ )
Closes a previously opened search handle.

#### Parameters


  -  *handle* : int

    

## [PyIDirectorySearch](#pyidirectorysearch).ExecuteSearch

int = __ExecuteSearch( *filter*  *, attrNames* __ )
Executes a search and passes the results to the caller. 

Some providers, such as LDAP, will defer the actual execution until the caller invokes the[PyIDirectorySearch::GetFirstRow](PyIDirectorySearch.md#pyidirectorysearchgetfirstrow)method or the[PyIDirectorySearch::GetNextRow](PyIDirectorySearch.md#pyidirectorysearchgetnextrow)method.

#### Parameters


  -  *filter* :[PyUnicode](#pyunicode)

    

  -  *attrNames* : [[PyUnicode](#pyunicode), ...]

    

#### Return Value
The result is an integer search handle.[PyIDirectorySearch::CloseSearchHandle](PyIDirectorySearch.md#pyidirectorysearchclosesearchhandle)should be called to close the handle.

## [PyIDirectorySearch](#pyidirectorysearch).GetColumn

(name, type, values) = __GetColumn( *handle*  *, name* __ )


#### Parameters


  -  *handle* : int

    Handle to a search

  -  *name* :[PyUnicode](#pyunicode)

    The column name to fetch

## [PyIDirectorySearch](#pyidirectorysearch).GetFirstRow

int = __GetFirstRow( *handle* __ )


#### Parameters


  -  *handle* : int

    

#### Return Value
The result is the HRESULT from the call - no exceptions are thrown

## [PyIDirectorySearch](#pyidirectorysearch).GetNextColumnName

 __GetNextColumnName(__ )


#### Return Value
Returns None when the underlying ADSI function return S_ADS_NOMORE_COLUMNS.

## [PyIDirectorySearch](#pyidirectorysearch).GetNextRow

int = __GetNextRow( *handle* __ )


#### Parameters


  -  *handle* : int

    

#### Return Value
The result is the HRESULT from the call - no exceptions are thrown

## [PyIDirectorySearch](#pyidirectorysearch).GetPreviousRow

int = __GetPreviousRow( *handle* __ )


#### Parameters


  -  *handle* : int

    

#### Return Value
The result is the HRESULT from the call - no exceptions are thrown

## [PyIDirectorySearch](#pyidirectorysearch).SetSearchPreference

int, [int, ...] = __SetSearchPreference( *prefs* __ )


#### Parameters


  -  *prefs* : ADS_SEARCHPREF_INFO

    

#### Return Value
The result is the hresult of the call, and a list of integer status 

codes for each of the preferences set.