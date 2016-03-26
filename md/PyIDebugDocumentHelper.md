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

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).AddDBCSText

 __AddDBCSText(__ )
Description of AddDBCSText.

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).AddDeferredText

 __AddDeferredText( *cChars*  *, dwTextStartCookie* __ )
Description of AddDeferredText.

#### Parameters


  -  *cChars* : int

    Description for cChars

  -  *dwTextStartCookie* : int

    Description for dwTextStartCookie

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).AddUnicodeText

 __AddUnicodeText( *pszText* __ )
Description of AddUnicodeText.

#### Parameters


  -  *pszText* : __unicode__ 

    Description for pszText

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).Attach

 __Attach( *pddhParent* __ )
Add the document to the doc tree

#### Parameters


  -  *pddhParent* :[PyIDebugDocumentHelper](#pyidebugdocumenthelper)

    Parent item.  If none, this item is top level.

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).BringDocumentContextToTop

 __BringDocumentContextToTop( *pddc* __ )
Description of BringDocumentContextToTop.

#### Parameters


  -  *pddc* :[PyIDebugDocumentContext](#pyidebugdocumentcontext)

    Description for pddc

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).BringDocumentToTop

 __BringDocumentToTop(__ )
Description of BringDocumentToTop.

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).CreateDebugDocumentContext

 __CreateDebugDocumentContext( *iCharPos*  *, cChars* __ )
Description of CreateDebugDocumentContext.

#### Parameters


  -  *iCharPos* : int

    Description for iCharPos

  -  *cChars* : int

    Description for cChars

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).DefineScriptBlock

 __DefineScriptBlock( *ulCharOffset*  *, cChars*  *, pas*  *, fScriptlet* __ )
Description of DefineScriptBlock.

#### Parameters


  -  *ulCharOffset* : int

    Description for ulCharOffset

  -  *cChars* : int

    Description for cChars

  -  *pas* : __PyIActiveScript__ 

    Description for pas

  -  *fScriptlet* : int

    Description for fScriptlet

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).Detach

 __Detach(__ )
Description of Detach.

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).GetDebugApplicationNode

 __GetDebugApplicationNode(__ )
Description of GetDebugApplicationNode.

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).GetScriptBlockInfo

 __GetScriptBlockInfo( *dwSourceContext* __ )
Description of GetScriptBlockInfo.

#### Parameters


  -  *dwSourceContext* : int

    Description for dwSourceContext

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).Init

 __Init( *pda*  *, pszShortName*  *, pszLongName*  *, docAttr* __ )
Description of Init.

#### Parameters


  -  *pda* :[PyIDebugApplication](#pyidebugapplication)

    Description for pda

  -  *pszShortName* : __unicode__ 

    Description for pszShortName

  -  *pszLongName* : __unicode__ 

    Description for pszLongName

  -  *docAttr* : int

    Description for docAttr

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).SetDebugDocumentHost

 __SetDebugDocumentHost( *pddh* __ )
Description of SetDebugDocumentHost.

#### Parameters


  -  *pddh* :[PyIDebugDocumentHost](#pyidebugdocumenthost)

    Description for pddh

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).SetDefaultTextAttr

 __SetDefaultTextAttr( *staTextAttr* __ )
Description of SetDefaultTextAttr.

#### Parameters


  -  *staTextAttr* : int

    Description for staTextAttr

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).SetDocumentAttr

 __SetDocumentAttr( *pszAttributes* __ )
Description of SetDocumentAttr.

#### Parameters


  -  *pszAttributes* : int

    Description for pszAttributes

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).SetLongName

 __SetLongName( *pszLongName* __ )
Description of SetLongName.

#### Parameters


  -  *pszLongName* : __unicode__ 

    Description for pszLongName

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).SetShortName

 __SetShortName( *pszShortName* __ )
Description of SetShortName.

#### Parameters


  -  *pszShortName* : __unicode__ 

    Description for pszShortName

## [PyIDebugDocumentHelper](#pyidebugdocumenthelper).SetTextAttributes

 __SetTextAttributes( *ulCharOffset*  *, obAttr* __ )
Description of SetTextAttributes.

#### Parameters


  -  *ulCharOffset* : int

    Description for ulCharOffset

  -  *obAttr* : object

    A sequence of attributes.