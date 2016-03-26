# PyIDispatch


## PyIDispatch Object

A OLE automation client object\.

#### Methods

  - [Invoke](PyIDispatch.md#pyidispatchinvoke)

    Invokes a DISPID, using the passed arguments\.&nbsp;

  - [InvokeTypes](PyIDispatch.md#pyidispatchinvoketypes)

    Invokes a DISPID, using the passed arguments and type descriptions\.&nbsp;

  - [GetIDsOfNames](PyIDispatch.md#pyidispatchgetidsofnames)

    Get the DISPID for the passed names\.&nbsp;

  - [GetTypeInfo](PyIDispatch.md#pyidispatchgettypeinfo)

    Get type information for the object\.&nbsp;

  - [GetTypeInfoCount](PyIDispatch.md#pyidispatchgettypeinfocount)

    Retrieves the number of [PyITypeInfo](PyITypeInfo.md)s the object provides\.&nbsp;




## [PyIDispatch](PyIDispatch.md#pyidispatch)\.GetIDsOfNames

\(int, \.\.\.\)/int = GetIDsOfNames\(name\)
Get the DISPID for the passed names\.

#### Parameters

  - name : string

    A name to query for

#### Alternative Parameters

  - \[name, \.\.\.\]

    A sequence of string names to query

#### Comments

Currently the LCID can not be specified, and  LOCALE\_SYSTEM\_DEFAULT is used\.

#### Return Value
If the first parameter is a sequence, the result will be a tuple of integers 

for each name in the sequence\.  If the first parameter is a single string, the result 

is a single integer with the ID of requested item\.


## [PyIDispatch](PyIDispatch.md#pyidispatch)\.GetTypeInfo

[PyITypeInfo](PyITypeInfo.md) = GetTypeInfo\(locale, index

\)
Get type information for the object\.

#### Parameters

  - locale=LOCALE\_USER\_DEFAULT : int

    The locale to use\.

  - index=0 : int

    The index of the typelibrary to fetch\. 

Note that these params are reversed from the win32 call\.


## [PyIDispatch](PyIDispatch.md#pyidispatch)\.GetTypeInfoCount

int = GetTypeInfoCount\(\)
Retrieves the number of [PyITypeInfo](PyITypeInfo.md)s the object provides\.


## [PyIDispatch](PyIDispatch.md#pyidispatch)\.Invoke

object = Invoke\(dispid, lcid

, flags

, bResultWanted

, params, \.\.\.

\)
Invokes a DISPID, using the passed arguments\.

#### Parameters

  - dispid : int

    The dispid to use\.  Typically this value will come from [PyIDispatch::GetIDsOfNames](PyIDispatch.md#pyidispatchgetidsofnames) or from a type library\.

  - lcid : int

    The locale id to use\.

  - flags : int

    The flags for the call\.  The following flags can be used\.

   

       Flag

   

   

       Description

   

DISPATCH\_METHODThe member is invoked as a method\. If a property has the same name, both this and the DISPATCH\_PROPERTYGET flag may be set\.

DISPATCH\_PROPERTYGETThe member is retrieved as a property or data member\.

DISPATCH\_PROPERTYPUTThe member is changed as a property or data member\.

DISPATCH\_PROPERTYPUTREFThe member is changed by a reference assignment, rather than a value assignment\. This flag is valid only when the property accepts a reference to an object\.

  - bResultWanted : int

    Indicates if the result of the call should be requested\.

  - params, \.\.\. : object, \.\.\.

    The parameters to pass\.

#### Return Value
If the bResultWanted parameter is False, then the result will be None\. 

Otherwise, the result is determined by the COM object itself \(and may still be None\)


## [PyIDispatch](PyIDispatch.md#pyidispatch)\.InvokeTypes

object = InvokeTypes\(dispid, lcid

, wFlags

, resultTypeDesc

, typeDescs

, args

\)
Invokes a DISPID, using the passed arguments and type descriptions\.

#### Parameters

  - dispid : int

    The dispid to use\.  Please see [PyIDispatch::Invoke](PyIDispatch.md#pyidispatchinvoke)\.

  - lcid : int

    The locale ID\.  Please see [PyIDispatch::Invoke](PyIDispatch.md#pyidispatchinvoke)\.

  - wFlags : int

    Flags for the call\.  Please see [PyIDispatch::Invoke](PyIDispatch.md#pyidispatchinvoke)\.

  - resultTypeDesc : tuple

    A tuple describing the type of the 

result\.  See the comments for more information\.

  - typeDescs : \(tuple, \.\.\.\)

    A sequence of tuples describing 

the types of the parameters for the function\.  See the comments 

for more information\.

  - args : object, \.\.\.

    The args to the function\.

#### Comments

The Microsoft documentation for IDispatch should be used for all 

params except 'resultTypeDesc' and 'typeDescs'\. 'resultTypeDesc' describes 

the return value of the function, and is a tuple of \(type\_id, flags\)\. 

'typeDescs' describes the type of each parameters, and is a list of the 

same \(type\_id, flags\) tuple\.

   

       item

   

   

       Description

   

type\_idA valid "variant type" constant \(eg, VT\_I4 | VT\_ARRAY, VT\_DATE, etc - see VARIANT at MSDN\)\.

flagsOne of the PARAMFLAG constants \(eg, PARAMFLAG\_FIN, PARAMFLAG\_FOUT etc - see PARAMFLAG at MSDN\)\.

#### Example
An example from the makepy generated file for Word

class Cells\(DispatchBaseClass\):

\.\.\.

    def SetWidth\(self, ColumnWidth=\.\.\., RulerStyle=\.\.\.\):

&\#09return self\.\_oleobj\_\.InvokeTypes\(202, LCID, 1, \(24, 0\), \(\(4, 1\), \(3, 1\)\),\.\.\.\)

The interesting bits are

resultTypeDesc: \(24, 0\) - \(VT\_VOID, &ltno flags&gt\)

typeDescs: \(\(4, 1\), \(3, 1\)\) - \(\(VT\_R4, PARAMFLAG\_FIN\), \(VT\_I4, PARAMFLAG\_FIN\)\)

So, in this example, the function returns no value and takes 2 "in" 

params - ColumnWidth is a float, and RulerStule is an int\.