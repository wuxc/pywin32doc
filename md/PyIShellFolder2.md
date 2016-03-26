# PyIShellFolder2


## PyIShellFolder2 Object

Represents an explorer folder, giving access to details of items in the folder\. 

Inherits all methods of [PyIShellFolder](PyIShellFolder.md)\.

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

    Returns the value or title of a column in the folder's Details view\.&nbsp;

  - [MapColumnToSCID](PyIShellFolder2.md#pyishellfolder2mapcolumntoscid)

    Returns the unique identifier \(FMTID, pid\) of a column&nbsp;

  - [\_\_iter\_\_](PyIShellFolder2.md#pyishellfolder2__iter__)

    Enumerates all objects in this folder\.&nbsp;


## [PyIShellFolder2](PyIShellFolder2.md#pyishellfolder2)\.EnumSearches

PyIEnumExtraSearch

 = EnumSearches\(\)
Returns an interface that lists searches defined for the folder

#### Comments

IEnumExtraSearch is not yet wrapped by Pywin32


## [PyIShellFolder2](PyIShellFolder2.md#pyishellfolder2)\.GetDefaultColumn

\(int, int\) = GetDefaultColumn\(\)
Returns the columns used for sorting and display


## [PyIShellFolder2](PyIShellFolder2.md#pyishellfolder2)\.GetDefaultColumnState

int = GetDefaultColumnState\(iColumn\)
Returns flags indicating the default behaviour of the column

#### Parameters

  - iColumn : int

    Zero-based index of the column

#### Return Value
Returns a combination of shellcon\.SHCOLSTATE\_\* flags


## [PyIShellFolder2](PyIShellFolder2.md#pyishellfolder2)\.GetDefaultSearchGUID

[PyIID](PyIID.md) = GetDefaultSearchGUID\(pguid\)
Retrieves the default search for the folder

#### Parameters

  - pguid : [PyIID](PyIID.md)

    Description for pguid


## [PyIShellFolder2](PyIShellFolder2.md#pyishellfolder2)\.GetDetailsEx

object = GetDetailsEx\(pidl, pscid

\)
Returns the details of an item by Column ID

#### Parameters

  - pidl : [PyIDL](PyIDL.md)

    Relative id list of an item in the folder

  - pscid : SHCOLUMNID

    The Column id/property key of a column in the folder's Details view

#### Return Value
The type of returned object is determined by the variant type of the requested column


## [PyIShellFolder2](PyIShellFolder2.md#pyishellfolder2)\.GetDetailsOf

\(int, int, str\) = GetDetailsOf\(pidl, iColumn

\)
Returns the value or title of a column in the folder's Details view\.

#### Parameters

  - pidl : [PyIDL](PyIDL.md)

    The relative idl of an item in the folder\.  Use None to retrieve column title\.

  - iColumn : int

    Zero based index of column

#### Return Value
Returns a tuple representing a SHELLDETAILS struct, containing the formst \(LVCFMT\_\*\), column width in characters, 

and string representation of the requested value


## [PyIShellFolder2](PyIShellFolder2.md#pyishellfolder2)\.MapColumnToSCID

SHCOLUMNID

 = MapColumnToSCID\(Column\)
Returns the unique identifier \(FMTID, pid\) of a column

#### Parameters

  - Column : int

    The zero-based index of the column as presented by the folder's Details view

#### Return Value
On XP and earlier, this is the Column Id as provided by [PyIColumnProvider](PyIColumnProvider.md)\. 

For Vista and later, this is the Property Key used with the property system interfaces\.