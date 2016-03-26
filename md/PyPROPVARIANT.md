# PyPROPVARIANT

## PyPROPVARIANT Object

Encapsulates a PROPVARIANT structure\. 

Constructed using PROPVARIANTType\(Value, Type\=VT\_ILLEGAL\)\. 

Value can be any object that can be be converted to the requested variant type\. 

Type should be a combination of VARENUM values \(pythoncom\.VT\_\*\)\. 

VT\_ILLEGAL indicates that an appropriate variant type should be inferred from the Value\. 

If the requested Type includes VT\_VECTOR, Value should be a sequence of compatible objects\. 

Currently VT\_ARRAY and VT\_BYREF are not supported, although some types can be coerced 

into a safearray using[PyPROPVARIANT::ChangeType](PyPROPVARIANT.md#pypropvariantchangetype)\.

#### Properties

  -  **int vt** 
    The variant type, a combination of VARENUM values including flags\.  \(read only\)

#### Methods


  - [GetValue](PyPROPVARIANT.md#pypropvariantgetvalue)

    Returns an object representing the variant value&nbsp;

  - [ToString](PyPROPVARIANT.md#pypropvarianttostring)

    Returns the value as a string&nbsp;

  - [ChangeType](PyPROPVARIANT.md#pypropvariantchangetype)

    Coerce to a different variant type&nbsp;

## [PyPROPVARIANT](#pypropvariant)\.ChangeType

[PyPROPVARIANT](#pypropvariant)\= **ChangeType\( *Type*  *, Flags* ** \)
Coerce to a different variant type

#### Parameters


  -  *Type* : int

    New variant type, combination of pythoncom\.VT\_\* values

  -  *Flags\=0* : int

    Reserved \(PROPVAR\_CHANGE\_FLAGS\)

#### Win32 API References


  - Search for *PropVariantChangeType* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=propvariantchangetype),[google](#http://www.google.com/search?q=propvariantchangetype)or[google groups](#http://groups.google.com/groups?q=propvariantchangetype)\.

## [PyPROPVARIANT](#pypropvariant)\.GetValue

object \= **GetValue\(** \)
Returns an object representing the variant value

## [PyPROPVARIANT](#pypropvariant)\.ToString

str \= **ToString\(** \)
Returns the value as a string

#### Win32 API References


  - Search for *PropVariantToString* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=propvarianttostring),[google](#http://www.google.com/search?q=propvarianttostring)or[google groups](#http://groups.google.com/groups?q=propvarianttostring)\.