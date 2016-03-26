# PyIDebugDocumentHelper

## PyIDebugDocumentHelper Object

Description of the interface

#### Methods


  - [Init](PyIDebugDocumentHelper.md#pyidebugdocumenthelperinit)

    Description of Init&nbsp;

  - [Attach](PyIDebugDocumentHelper.md#pyidebugdocumenthelperattach)

    Add the document to the doc tree&nbsp;

  - [Detach](PyIDebugDocumentHelper.md#pyidebugdocumenthelperdetach)

    Description of Detach&nbsp;

  - [AddUnicodeText](PyIDebugDocumentHelper.md#pyidebugdocumenthelperaddunicodetext)

    Description of AddUnicodeText&nbsp;

  - [AddDBCSText](PyIDebugDocumentHelper.md#pyidebugdocumenthelperadddbcstext)

    Description of AddDBCSText&nbsp;

  - [SetDebugDocumentHost](PyIDebugDocumentHelper.md#pyidebugdocumenthelpersetdebugdocumenthost)

    Description of SetDebugDocumentHost&nbsp;

  - [AddDeferredText](PyIDebugDocumentHelper.md#pyidebugdocumenthelperadddeferredtext)

    Description of AddDeferredText&nbsp;

  - [DefineScriptBlock](PyIDebugDocumentHelper.md#pyidebugdocumenthelperdefinescriptblock)

    Description of DefineScriptBlock&nbsp;

  - [SetDefaultTextAttr](PyIDebugDocumentHelper.md#pyidebugdocumenthelpersetdefaulttextattr)

    Description of SetDefaultTextAttr&nbsp;

  - [SetTextAttributes](PyIDebugDocumentHelper.md#pyidebugdocumenthelpersettextattributes)

    Description of SetTextAttributes&nbsp;

  - [SetLongName](PyIDebugDocumentHelper.md#pyidebugdocumenthelpersetlongname)

    Description of SetLongName&nbsp;

  - [SetShortName](PyIDebugDocumentHelper.md#pyidebugdocumenthelpersetshortname)

    Description of SetShortName&nbsp;

  - [SetDocumentAttr](PyIDebugDocumentHelper.md#pyidebugdocumenthelpersetdocumentattr)

    Description of SetDocumentAttr&nbsp;

  - [GetDebugApplicationNode](PyIDebugDocumentHelper.md#pyidebugdocumenthelpergetdebugapplicationnode)

    Description of GetDebugApplicationNode&nbsp;

  - [GetScriptBlockInfo](PyIDebugDocumentHelper.md#pyidebugdocumenthelpergetscriptblockinfo)

    Description of GetScriptBlockInfo&nbsp;

  - [CreateDebugDocumentContext](PyIDebugDocumentHelper.md#pyidebugdocumenthelpercreatedebugdocumentcontext)

    Description of CreateDebugDocumentContext&nbsp;

  - [BringDocumentToTop](PyIDebugDocumentHelper.md#pyidebugdocumenthelperbringdocumenttotop)

    Description of BringDocumentToTop&nbsp;

  - [BringDocumentContextToTop](PyIDebugDocumentHelper.md#pyidebugdocumenthelperbringdocumentcontexttotop)

    Description of BringDocumentContextToTop&nbsp;

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.AddDBCSText

 **AddDBCSText\(** \)
Description of AddDBCSText\.

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.AddDeferredText

 **AddDeferredText\( *cChars*  *, dwTextStartCookie* ** \)
Description of AddDeferredText\.

#### Parameters


  -  *cChars* : int

    Description for cChars

  -  *dwTextStartCookie* : int

    Description for dwTextStartCookie

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.AddUnicodeText

 **AddUnicodeText\( *pszText* ** \)
Description of AddUnicodeText\.

#### Parameters


  -  *pszText* : **unicode** 

    Description for pszText

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.Attach

 **Attach\( *pddhParent* ** \)
Add the document to the doc tree

#### Parameters


  -  *pddhParent* :[PyIDebugDocumentHelper](#pyidebugdocumenthelper)

    Parent item\.  If none, this item is top level\.

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.BringDocumentContextToTop

 **BringDocumentContextToTop\( *pddc* ** \)
Description of BringDocumentContextToTop\.

#### Parameters


  -  *pddc* :[PyIDebugDocumentContext](#pyidebugdocumentcontext)

    Description for pddc

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.BringDocumentToTop

 **BringDocumentToTop\(** \)
Description of BringDocumentToTop\.

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.CreateDebugDocumentContext

 **CreateDebugDocumentContext\( *iCharPos*  *, cChars* ** \)
Description of CreateDebugDocumentContext\.

#### Parameters


  -  *iCharPos* : int

    Description for iCharPos

  -  *cChars* : int

    Description for cChars

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.DefineScriptBlock

 **DefineScriptBlock\( *ulCharOffset*  *, cChars*  *, pas*  *, fScriptlet* ** \)
Description of DefineScriptBlock\.

#### Parameters


  -  *ulCharOffset* : int

    Description for ulCharOffset

  -  *cChars* : int

    Description for cChars

  -  *pas* : **PyIActiveScript** 

    Description for pas

  -  *fScriptlet* : int

    Description for fScriptlet

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.Detach

 **Detach\(** \)
Description of Detach\.

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.GetDebugApplicationNode

 **GetDebugApplicationNode\(** \)
Description of GetDebugApplicationNode\.

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.GetScriptBlockInfo

 **GetScriptBlockInfo\( *dwSourceContext* ** \)
Description of GetScriptBlockInfo\.

#### Parameters


  -  *dwSourceContext* : int

    Description for dwSourceContext

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.Init

 **Init\( *pda*  *, pszShortName*  *, pszLongName*  *, docAttr* ** \)
Description of Init\.

#### Parameters


  -  *pda* :[PyIDebugApplication](#pyidebugapplication)

    Description for pda

  -  *pszShortName* : **unicode** 

    Description for pszShortName

  -  *pszLongName* : **unicode** 

    Description for pszLongName

  -  *docAttr* : int

    Description for docAttr

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.SetDebugDocumentHost

 **SetDebugDocumentHost\( *pddh* ** \)
Description of SetDebugDocumentHost\.

#### Parameters


  -  *pddh* :[PyIDebugDocumentHost](#pyidebugdocumenthost)

    Description for pddh

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.SetDefaultTextAttr

 **SetDefaultTextAttr\( *staTextAttr* ** \)
Description of SetDefaultTextAttr\.

#### Parameters


  -  *staTextAttr* : int

    Description for staTextAttr

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.SetDocumentAttr

 **SetDocumentAttr\( *pszAttributes* ** \)
Description of SetDocumentAttr\.

#### Parameters


  -  *pszAttributes* : int

    Description for pszAttributes

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.SetLongName

 **SetLongName\( *pszLongName* ** \)
Description of SetLongName\.

#### Parameters


  -  *pszLongName* : **unicode** 

    Description for pszLongName

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.SetShortName

 **SetShortName\( *pszShortName* ** \)
Description of SetShortName\.

#### Parameters


  -  *pszShortName* : **unicode** 

    Description for pszShortName

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper)\.SetTextAttributes

 **SetTextAttributes\( *ulCharOffset*  *, obAttr* ** \)
Description of SetTextAttributes\.

#### Parameters


  -  *ulCharOffset* : int

    Description for ulCharOffset

  -  *obAttr* : object

    A sequence of attributes\.