# PyIShellFolder2

## PyIShellFolder2 Object

Represents an explorer folder, giving access to details of items in the folder. 

Inherits all methods of[PyIShellFolder](#pyishellfolder).

#### Methods


  - [GetDefaultSearchGUID](PyIShellFolder2.md#pyishellfolder2getdefaultsearchguid)

    Retrieves the default search for the folder&nbsp;

  - [EnumSearches](PyIShellFolder2.md#pyishellfolder2enumsearches)

    Returns an interface that lists searches defined for the folder&nbsp;

  - [GetDefaultColumn](PyIShellFolder2.md#pyishellfolder2getdefaultcolumn)

    Returns the columns used for sorting and display&nbsp;

  - [GetDefaultColumnState](PyIShellFolder2.md#pyishellfolder2getdefaultcolumnstate)

    Returns flags indicating the default behaviour of the column&nbsp;

  - [GetDetailsEx](PyIShellFolder2.md#pyishellfolder2getdetailsex)

    Returns the details of an item by Column ID&nbsp;

  - [GetDetailsOf](PyIShellFolder2.md#pyishellfolder2getdetailsof)

    Returns the value or title of a column in the folder's Details view.&nbsp;

  - [MapColumnToSCID](PyIShellFolder2.md#pyishellfolder2mapcolumntoscid)

    Returns the unique identifier (FMTID, pid) of a column&nbsp;

  - [__iter__](PyIShellFolder2.md#pyishellfolder2__iter__)

    Enumerates all objects in this folder.&nbsp;

## [PyIShellFolder2](#pyishellfolder2).EnumSearches

 __PyIEnumExtraSearch__ = __EnumSearches(__ )
Returns an interface that lists searches defined for the folder

#### Comments
IEnumExtraSearch is not yet wrapped by Pywin32

## [PyIShellFolder2](#pyishellfolder2).GetDefaultColumn

(int, int) = __GetDefaultColumn(__ )
Returns the columns used for sorting and display

## [PyIShellFolder2](#pyishellfolder2).GetDefaultColumnState

int = __GetDefaultColumnState( *iColumn* __ )
Returns flags indicating the default behaviour of the column

#### Parameters


  -  *iColumn* : int

    Zero-based index of the column

#### Return Value
Returns a combination of shellcon.SHCOLSTATE_* flags

## [PyIShellFolder2](#pyishellfolder2).GetDefaultSearchGUID

[PyIID](#pyiid)= __GetDefaultSearchGUID( *pguid* __ )
Retrieves the default search for the folder

#### Parameters


  -  *pguid* :[PyIID](#pyiid)

    Description for pguid

## [PyIShellFolder2](#pyishellfolder2).GetDetailsEx

object = __GetDetailsEx( *pidl*  *, pscid* __ )
Returns the details of an item by Column ID

#### Parameters


  -  *pidl* :[PyIDL](#pyidl)

    Relative id list of an item in the folder

  -  *pscid* : __SHCOLUMNID__ 

    The Column id/property key of a column in the folder's Details view

#### Return Value
The type of returned object is determined by the variant type of the requested column

## [PyIShellFolder2](#pyishellfolder2).GetDetailsOf

(int, int, str) = __GetDetailsOf( *pidl*  *, iColumn* __ )
Returns the value or title of a column in the folder's Details view.

#### Parameters


  -  *pidl* :[PyIDL](#pyidl)

    The relative idl of an item in the folder.  Use None to retrieve column title.

  -  *iColumn* : int

    Zero based index of column

#### Return Value
Returns a tuple representing a SHELLDETAILS struct, containing the formst (LVCFMT_*), column width in characters, 

and string representation of the requested value

## [PyIShellFolder2](#pyishellfolder2).MapColumnToSCID

 __SHCOLUMNID__ = __MapColumnToSCID( *Column* __ )
Returns the unique identifier (FMTID, pid) of a column

#### Parameters


  -  *Column* : int

    The zero-based index of the column as presented by the folder's Details view

#### Return Value
On XP and earlier, this is the Column Id as provided by[PyIColumnProvider](#pyicolumnprovider). 

For Vista and later, this is the Property Key used with the property system interfaces.