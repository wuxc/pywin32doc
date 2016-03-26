# PyIDebugStackFrame

## PyIDebugStackFrame Object



Description of the interface

#### Methods


  - [GetCodeContext](PyIDebugStackFrame.md#pyidebugstackframegetcodecontext)

    Returns the current code context associated with the stack frame\.&nbsp;

  - [GetDescriptionString](PyIDebugStackFrame.md#pyidebugstackframegetdescriptionstring)

    Returns a short or long textual description of the stack frame\.&nbsp;

  - [GetLanguageString](PyIDebugStackFrame.md#pyidebugstackframegetlanguagestring)

    Returns a short or long textual description of the language\.&nbsp;

  - [GetThread](PyIDebugStackFrame.md#pyidebugstackframegetthread)

    Returns the thread associated with this stack frame\.&nbsp;

  - [GetThread](PyIDebugStackFrame.md#pyidebugstackframegetthread)

    Returns the debug property object associated with this stack frame\.&nbsp;

## [PyIDebugStackFrame](#pyidebugstackframe)\.GetCodeContext

GetCodeContext\(\)
Returns the current code context associated with the stack frame\.

## [PyIDebugStackFrame](#pyidebugstackframe)\.GetDebugProperty

[PyIDebugProperty](#pyidebugproperty) =GetDebugProperty\(\)
Returns the debug property\.

## [PyIDebugStackFrame](#pyidebugstackframe)\.GetDescriptionString

unicode

 =GetDescriptionString\(fLong\)
Returns a short or long textual description of the stack frame\.

#### Parameters


  - fLong : int

    If false, provide only the name of the function associated with the stack frame\. When true it may also provide the parameter\(s\) to the function or whatever else is relevant\.

## [PyIDebugStackFrame](#pyidebugstackframe)\.GetLanguageString

unicode

 =GetLanguageString\(fLong\)
Returns a short or long textual description of the language\.

#### Parameters


  - fLong : int

    If False, just the language name should be provided, eg, "Python"\. If True a full product description may be provided \(eg, "Python 1\.4 ActiveX Debugging Host"\)

## [PyIDebugStackFrame](#pyidebugstackframe)\.GetThread

[PyIDebugApplicationThread](#pyidebugapplicationthread) =GetThread\(\)
Returns the thread associated with this stack frame\.