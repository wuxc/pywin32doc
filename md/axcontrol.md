# axcontrol

## Module axcontrol

A module, encapsulating the ActiveX Control interfaces

#### Methods


  - [OleCreate](axcontrol.md#axcontrololecreate)

    Creates a new embedded object identified by a CLSID\.&nbsp;

  - [OleLoadPicture](axcontrol.md#axcontrololeloadpicture)

    Creates a new picture object and initializes it from the contents of a stream\.&nbsp;

  - [OleLoadPicturePath](axcontrol.md#axcontrololeloadpicturepath)

    Creates a new picture object and initializes it from the contents of a stream\.&nbsp;

  - [OleSetContainedObject](axcontrol.md#axcontrololesetcontainedobject)

    Notifies an object embedded in an OLE container to ensure correct reference\.&nbsp;

  - [OleTranslateAccelerator](axcontrol.md#axcontrololetranslateaccelerator)

    Called by the object application, allows an object's container to translate accelerators according to the container's accelerator table\.&nbsp;

## EMBDHLP\_CREATENOW
 **const axcontrol\.EMBDHLP\_CREATENOW;** 


## EMBDHLP\_DELAYCREATE
 **const axcontrol\.EMBDHLP\_DELAYCREATE;** 


## EMBDHLP\_INPROC\_HANDLER
 **const axcontrol\.EMBDHLP\_INPROC\_HANDLER;** 


## EMBDHLP\_INPROC\_SERVER
 **const axcontrol\.EMBDHLP\_INPROC\_SERVER;** 


## OLECLOSE\_NOSAVE
 **const axcontrol\.OLECLOSE\_NOSAVE;** 
The object should not be saved, even if it is dirty\. This flag is typically used when an object is being deleted\.

## OLECLOSE\_PROMPTSAVE
 **const axcontrol\.OLECLOSE\_PROMPTSAVE;** 
If the object is dirty, the[PyIOleObject::Close](PyIOleObject.md#pyioleobjectclose)implementation should display a dialog box to let the end user determine whether to save the object\. However, if the object is in the running state but its user interface is invisible, the end user should not be prompted, and the close should be handled as if OLECLOSE\_SAVEIFDIRTY had been specified\.

## OLECLOSE\_SAVEIFDIRTY
 **const axcontrol\.OLECLOSE\_SAVEIFDIRTY;** 
The object should be saved if it is dirty\.

## OLECMDF\_ENABLED
 **const axcontrol\.OLECMDF\_ENABLED;** 


## OLECMDF\_LATCHED
 **const axcontrol\.OLECMDF\_LATCHED;** 


## OLECMDF\_NINCHED
 **const axcontrol\.OLECMDF\_NINCHED;** 


## OLECMDF\_SUPPORTED
 **const axcontrol\.OLECMDF\_SUPPORTED;** 


## OLECMDTEXTF\_NAME
 **const axcontrol\.OLECMDTEXTF\_NAME;** 


## OLECMDTEXTF\_NONE
 **const axcontrol\.OLECMDTEXTF\_NONE;** 


## OLECMDTEXTF\_STATUS
 **const axcontrol\.OLECMDTEXTF\_STATUS;** 


## OLECREATE\_LEAVERUNNING
 **const axcontrol\.OLECREATE\_LEAVERUNNING;** 


## OLEIVERB\_DISCARDUNDOSTATE
 **const axcontrol\.OLEIVERB\_DISCARDUNDOSTATE;** 


## OLEIVERB\_HIDE
 **const axcontrol\.OLEIVERB\_HIDE;** 


## OLEIVERB\_INPLACEACTIVATE
 **const axcontrol\.OLEIVERB\_INPLACEACTIVATE;** 


## OLEIVERB\_OPEN
 **const axcontrol\.OLEIVERB\_OPEN;** 


## OLEIVERB\_PRIMARY
 **const axcontrol\.OLEIVERB\_PRIMARY;** 


## OLEIVERB\_SHOW
 **const axcontrol\.OLEIVERB\_SHOW;** 


## OLEIVERB\_UIACTIVATE
 **const axcontrol\.OLEIVERB\_UIACTIVATE;** 


## [axcontrol](#axcontrol)\.OleCreate

[PyIOleObject](#pyioleobject)\= **OleCreate\( *clsid*  *, clsid*  *, obCLSID*  *, obIID*  *, renderopt*  *, obFormatEtc*  *, obOleClientSite*  *, obStorage* ** \)
Creates a new embedded object identified by a CLSID\.

#### Parameters


  -  *clsid* : IID

    A CLSID in string or native format

  -  *clsid* : IID

    A IID in string or native format

  -  *obCLSID* :[PyIID](#pyiid)

    The[PyIID](#pyiid)CLSID for the OLE object to create\.

  -  *obIID* :[PyIID](#pyiid)

    The[PyIID](#pyiid)for the interface to return\.

  -  *renderopt* : **DWORD** 

    The **DWORD** renderopt for redering the Display\.

  -  *obFormatEtc* : **FORMATETC** 

    The **FORMATETC** structure\.

  -  *obOleClientSite* :[PyIOleClientSite](#pyioleclientsite)

    The[PyIOleClientSite](#pyioleclientsite)interface to the container\.

  -  *obStorage* :[PyIStorage](#pyistorage)

    The[PyIStorage](#pyistorage)interface\.

## [axcontrol](#axcontrol)\.OleLoadPicture

[PyIUnknown](#pyiunknown)\= **OleLoadPicture\( *stream*  *, size*  *, runMode*  *,*  *,* ** \)
Creates a new picture object and initializes it from the contents of a stream\.

#### Parameters


  -  *stream* :[PyIStream](#pyistream)

    The stream that contains picture's data\.

  -  *size* : int

    Number of bytes read from the stream

  -  *runMode* : int

    The opposite of the initial value of the KeepOriginalFormat property\. If TRUE, KeepOriginalFormat is set to FALSE and vice-versa\.

  -  *\=iid* :[PyIID](#pyiid)

    The identifier of the interface describing the type of interface pointer to return

  -  *\=iidRet* :[PyIID](#pyiid)

    The IID to use for the return object - use only if pythoncom does not support the native interface requested\.

## [axcontrol](#axcontrol)\.OleLoadPicturePath

[PyIUnknown](#pyiunknown)\= **OleLoadPicturePath\( *url\_or\_path*  *, unk*  *, reserved*  *, clr*  *,*  *,* ** \)
Creates a new picture object and initializes it from the contents of a stream\.

#### Parameters


  -  *url\_or\_path* : string/unicode

    The path or url to the file you want to open\.

  -  *unk* : **PyIUknown** 

    The IUnknown for COM aggregation\.

  -  *reserved* : int

    reserved

  -  *clr* : int

    The color you want to reserve to be transparent\.

  -  *\=iid* :[PyIID](#pyiid)

    The identifier of the interface describing the type of interface pointer to return

  -  *\=iidRet* :[PyIID](#pyiid)

    The IID to use for the return object - use only if pythoncom does not support the native interface requested\.

## [axcontrol](#axcontrol)\.OleSetContainedObject

 **OleSetContainedObject\( *unk*  *, fContained* ** \)
Notifies an object embedded in an OLE container to ensure correct reference\.

#### Parameters


  -  *unk* :[PyIUnknown](#pyiunknown)

    The object

  -  *fContained* : int

    

## [axcontrol](#axcontrol)\.OleTranslateAccelerator

 **OleTranslateAccelerator\( *frame*  *, frame\_info*  *, msg* ** \)
Called by the object application, allows an object's container to translate accelerators according to the container's accelerator table\.

#### Parameters


  -  *frame* :[PyIOleInPlaceFrame](#pyioleinplaceframe)

    frame to send keystrokes to\.

  -  *frame\_info* : **PyOLEINPLACEFRAMEINFO** 

    

  -  *msg* :[PyMSG](#pymsg)

    