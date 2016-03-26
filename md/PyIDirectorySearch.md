# PyIDirectorySearch


## PyIDirectorySearch Object

A COM interface to ADSI's IDirectorySearch interface\. 

Derived from [PyIUnknown](PyIUnknown.md)

#### Methods

  - [SetSearchPreference](PyIDirectorySearch.md#pyidirectorysearchsetsearchpreference)

    &nbsp;

  - [ExecuteSearch](PyIDirectorySearch.md#pyidirectorysearchexecutesearch)

    Executes a search and passes the results to the caller\. 

Some providers, such as LDAP, will defer the actual execution until the caller invokes the 

[PyIDirectorySearch::GetFirstRow](PyIDirectorySearch.md#pyidirectorysearchgetfirstrow) method or the [PyIDirectorySearch::GetNextRow](PyIDirectorySearch.md#pyidirectorysearchgetnextrow) method\.&nbsp;

  - [GetNextRow](PyIDirectorySearch.md#pyidirectorysearchgetnextrow)

    &nbsp;

  - [GetFirstRow](PyIDirectorySearch.md#pyidirectorysearchgetfirstrow)

    &nbsp;

  - [GetPreviousRow](PyIDirectorySearch.md#pyidirectorysearchgetpreviousrow)

    &nbsp;

  - [CloseSearchHandle](PyIDirectorySearch.md#pyidirectorysearchclosesearchhandle)

    Closes a previously opened search handle\.&nbsp;

  - [AdandonSearch](PyIDirectorySearch.md#pyidirectorysearchadandonsearch)

    &nbsp;

  - [GetColumn](PyIDirectorySearch.md#pyidirectorysearchgetcolumn)

    &nbsp;

  - [GetNextColumnName](PyIDirectorySearch.md#pyidirectorysearchgetnextcolumnname)

    &nbsp;


## [PyIDirectorySearch](PyIDirectorySearch.md#pyidirectorysearch)\.AdandonSearch

AdandonSearch\(handle\)

#### Parameters

  - handle : int

    


## [PyIDirectorySearch](PyIDirectorySearch.md#pyidirectorysearch)\.CloseSearchHandle

CloseSearchHandle\(handle\)
Closes a previously opened search handle\.

#### Parameters

  - handle : int

    


## [PyIDirectorySearch](PyIDirectorySearch.md#pyidirectorysearch)\.ExecuteSearch

int = ExecuteSearch\(filter, attrNames

\)
Executes a search and passes the results to the caller\. 

Some providers, such as LDAP, will defer the actual execution until the caller invokes the 

[PyIDirectorySearch::GetFirstRow](PyIDirectorySearch.md#pyidirectorysearchgetfirstrow) method or the [PyIDirectorySearch::GetNextRow](PyIDirectorySearch.md#pyidirectorysearchgetnextrow) method\.

#### Parameters

  - filter : [PyUnicode](PyUnicode.md)

    

  - attrNames : \[[PyUnicode](PyUnicode.md), \.\.\.\]

    

#### Return Value
The result is an integer search handle\.  [PyIDirectorySearch::CloseSearchHandle](PyIDirectorySearch.md#pyidirectorysearchclosesearchhandle) 

should be called to close the handle\.


## [PyIDirectorySearch](PyIDirectorySearch.md#pyidirectorysearch)\.GetColumn

\(name, type, values\) = GetColumn\(handle, name

\)

#### Parameters

  - handle : int

    Handle to a search

  - name : [PyUnicode](PyUnicode.md)

    The column name to fetch


## [PyIDirectorySearch](PyIDirectorySearch.md#pyidirectorysearch)\.GetFirstRow

int = GetFirstRow\(handle\)

#### Parameters

  - handle : int

    

#### Return Value
The result is the HRESULT from the call - no exceptions are thrown


## [PyIDirectorySearch](PyIDirectorySearch.md#pyidirectorysearch)\.GetNextColumnName

GetNextColumnName\(\)

#### Return Value
Returns None when the underlying ADSI function return S\_ADS\_NOMORE\_COLUMNS\.


## [PyIDirectorySearch](PyIDirectorySearch.md#pyidirectorysearch)\.GetNextRow

int = GetNextRow\(handle\)

#### Parameters

  - handle : int

    

#### Return Value
The result is the HRESULT from the call - no exceptions are thrown


## [PyIDirectorySearch](PyIDirectorySearch.md#pyidirectorysearch)\.GetPreviousRow

int = GetPreviousRow\(handle\)

#### Parameters

  - handle : int

    

#### Return Value
The result is the HRESULT from the call - no exceptions are thrown


## [PyIDirectorySearch](PyIDirectorySearch.md#pyidirectorysearch)\.SetSearchPreference

int, \[int, \.\.\.\] = SetSearchPreference\(prefs\)

#### Parameters

  - prefs : ADS\_SEARCHPREF\_INFO

    

#### Return Value
The result is the hresult of the call, and a list of integer status 

codes for each of the preferences set\.