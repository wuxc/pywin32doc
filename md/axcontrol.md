# axcontrol

## Module axcontrol

A module, encapsulating the ActiveX Control interfaces

#### Methods


  - [OleCreate](axcontrol.md#axcontrololecreate)

    Creates a new embedded object identified by a CLSID.&nbsp;

  - [OleLoadPicture](axcontrol.md#axcontrololeloadpicture)

    Creates a new picture object and initializes it from the contents of a stream.&nbsp;

  - [OleLoadPicturePath](axcontrol.md#axcontrololeloadpicturepath)

    Creates a new picture object and initializes it from the contents of a stream.&nbsp;

  - [OleSetContainedObject](axcontrol.md#axcontrololesetcontainedobject)

    Notifies an object embedded in an OLE container to ensure correct reference.&nbsp;

  - [OleTranslateAccelerator](axcontrol.md#axcontrololetranslateaccelerator)

    Called by the object application, allows an object's container to translate accelerators according to the container's accelerator table.&nbsp;

## EMBDHLP_CREATENOW
 __const axcontrol.EMBDHLP_CREATENOW;__ 


## EMBDHLP_DELAYCREATE
 __const axcontrol.EMBDHLP_DELAYCREATE;__ 


## EMBDHLP_INPROC_HANDLER
 __const axcontrol.EMBDHLP_INPROC_HANDLER;__ 


## EMBDHLP_INPROC_SERVER
 __const axcontrol.EMBDHLP_INPROC_SERVER;__ 


## OLECLOSE_NOSAVE
 __const axcontrol.OLECLOSE_NOSAVE;__ 
The object should not be saved, even if it is dirty. This flag is typically used when an object is being deleted.

## OLECLOSE_PROMPTSAVE
 __const axcontrol.OLECLOSE_PROMPTSAVE;__ 
If the object is dirty, the[PyIOleObject::Close](PyIOleObject.md#pyioleobjectclose)implementation should display a dialog box to let the end user determine whether to save the object. However, if the object is in the running state but its user interface is invisible, the end user should not be prompted, and the close should be handled as if OLECLOSE_SAVEIFDIRTY had been specified.

## OLECLOSE_SAVEIFDIRTY
 __const axcontrol.OLECLOSE_SAVEIFDIRTY;__ 
The object should be saved if it is dirty.

## OLECMDF_ENABLED
 __const axcontrol.OLECMDF_ENABLED;__ 


## OLECMDF_LATCHED
 __const axcontrol.OLECMDF_LATCHED;__ 


## OLECMDF_NINCHED
 __const axcontrol.OLECMDF_NINCHED;__ 


## OLECMDF_SUPPORTED
 __const axcontrol.OLECMDF_SUPPORTED;__ 


## OLECMDTEXTF_NAME
 __const axcontrol.OLECMDTEXTF_NAME;__ 


## OLECMDTEXTF_NONE
 __const axcontrol.OLECMDTEXTF_NONE;__ 


## OLECMDTEXTF_STATUS
 __const axcontrol.OLECMDTEXTF_STATUS;__ 


## OLECREATE_LEAVERUNNING
 __const axcontrol.OLECREATE_LEAVERUNNING;__ 


## OLEIVERB_DISCARDUNDOSTATE
 __const axcontrol.OLEIVERB_DISCARDUNDOSTATE;__ 


## OLEIVERB_HIDE
 __const axcontrol.OLEIVERB_HIDE;__ 


## OLEIVERB_INPLACEACTIVATE
 __const axcontrol.OLEIVERB_INPLACEACTIVATE;__ 


## OLEIVERB_OPEN
 __const axcontrol.OLEIVERB_OPEN;__ 


## OLEIVERB_PRIMARY
 __const axcontrol.OLEIVERB_PRIMARY;__ 


## OLEIVERB_SHOW
 __const axcontrol.OLEIVERB_SHOW;__ 


## OLEIVERB_UIACTIVATE
 __const axcontrol.OLEIVERB_UIACTIVATE;__ 


## [axcontrol](#axcontrol).OleCreate

[PyIOleObject](#pyioleobject)= __OleCreate( *clsid*  *, clsid*  *, obCLSID*  *, obIID*  *, renderopt*  *, obFormatEtc*  *, obOleClientSite*  *, obStorage* __ )
Creates a new embedded object identified by a CLSID.

#### Parameters


  -  *clsid* : IID

    A CLSID in string or native format

  -  *clsid* : IID

    A IID in string or native format

  -  *obCLSID* :[PyIID](#pyiid)

    The[PyIID](#pyiid)CLSID for the OLE object to create.

  -  *obIID* :[PyIID](#pyiid)

    The[PyIID](#pyiid)for the interface to return.

  -  *renderopt* : __DWORD__ 

    The __DWORD__ renderopt for redering the Display.

  -  *obFormatEtc* : __FORMATETC__ 

    The __FORMATETC__ structure.

  -  *obOleClientSite* :[PyIOleClientSite](#pyioleclientsite)

    The[PyIOleClientSite](#pyioleclientsite)interface to the container.

  -  *obStorage* :[PyIStorage](#pyistorage)

    The[PyIStorage](#pyistorage)interface.

## [axcontrol](#axcontrol).OleLoadPicture

[PyIUnknown](#pyiunknown)= __OleLoadPicture( *stream*  *, size*  *, runMode*  *,*  *,* __ )
Creates a new picture object and initializes it from the contents of a stream.

#### Parameters


  -  *stream* :[PyIStream](#pyistream)

    The stream that contains picture's data.

  -  *size* : int

    Number of bytes read from the stream

  -  *runMode* : int

    The opposite of the initial value of the KeepOriginalFormat property. If TRUE, KeepOriginalFormat is set to FALSE and vice-versa.

  -  *=iid* :[PyIID](#pyiid)

    The identifier of the interface describing the type of interface pointer to return

  -  *=iidRet* :[PyIID](#pyiid)

    The IID to use for the return object - use only if pythoncom does not support the native interface requested.

## [axcontrol](#axcontrol).OleLoadPicturePath

[PyIUnknown](#pyiunknown)= __OleLoadPicturePath( *url_or_path*  *, unk*  *, reserved*  *, clr*  *,*  *,* __ )
Creates a new picture object and initializes it from the contents of a stream.

#### Parameters


  -  *url_or_path* : string/unicode

    The path or url to the file you want to open.

  -  *unk* : __PyIUknown__ 

    The IUnknown for COM aggregation.

  -  *reserved* : int

    reserved

  -  *clr* : int

    The color you want to reserve to be transparent.

  -  *=iid* :[PyIID](#pyiid)

    The identifier of the interface describing the type of interface pointer to return

  -  *=iidRet* :[PyIID](#pyiid)

    The IID to use for the return object - use only if pythoncom does not support the native interface requested.

## [axcontrol](#axcontrol).OleSetContainedObject

 __OleSetContainedObject( *unk*  *, fContained* __ )
Notifies an object embedded in an OLE container to ensure correct reference.

#### Parameters


  -  *unk* :[PyIUnknown](#pyiunknown)

    The object

  -  *fContained* : int

    

## [axcontrol](#axcontrol).OleTranslateAccelerator

 __OleTranslateAccelerator( *frame*  *, frame_info*  *, msg* __ )
Called by the object application, allows an object's container to translate accelerators according to the container's accelerator table.

#### Parameters


  -  *frame* :[PyIOleInPlaceFrame](#pyioleinplaceframe)

    frame to send keystrokes to.

  -  *frame_info* : __PyOLEINPLACEFRAMEINFO__ 

    

  -  *msg* :[PyMSG](#pymsg)

    