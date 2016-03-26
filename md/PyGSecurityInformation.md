# PyGSecurityInformation

## PyGSecurityInformation Object

Gateway wrapper for the implement-only ISecurityInformation interface

#### Methods


  - [GetObjectInformation](PyGSecurityInformation.md#pygsecurityinformationgetobjectinformation)

    Returns information identifying the object&nbsp;

  - [GetSecurity](PyGSecurityInformation.md#pygsecurityinformationgetsecurity)

    Requests the object's current security descriptor&nbsp;

  - [SetSecurity](PyGSecurityInformation.md#pygsecurityinformationsetsecurity)

    Applies the modified security information to the object&nbsp;

  - [GetAccessRights](PyGSecurityInformation.md#pygsecurityinformationgetaccessrights)

    Requests the permission flags that will be available for user to set&nbsp;

  - [MapGeneric](PyGSecurityInformation.md#pygsecurityinformationmapgeneric)

    Translates generic permission flags into specific flags&nbsp;

  - [GetInheritTypes](PyGSecurityInformation.md#pygsecurityinformationgetinherittypes)

    Retrieves inheritance flags that will be shown in dialog for containers&nbsp;

  - [PropertySheetPageCallback](PyGSecurityInformation.md#pygsecurityinformationpropertysheetpagecallback)

    Invoked each time a property sheet page is created or destroyed&nbsp;

## [PyGSecurityInformation](#pygsecurityinformation).GetAccessRights

(([SI_ACCESS](SI.md#siaccess),...)  int) = __GetAccessRights( *ObjectType*  *, Flags* __ )
Retrieves permission that can be set

#### Parameters


  -  *ObjectType* :[PyIID](#pyiid)

    GUID representing type of object, may be None

  -  *Flags* : int

    Indicates which page is requesting the access rights (SI_ADVANCED, SI_EDIT_AUDITS, SI_EDIT_PROPERTIES)

#### Return Value
This method should return a 2-tuple containing a sequence of[SI_ACCESS](SI.md#siaccess)tuples, 

and a zero-based index indicating which of them is the default

## [PyGSecurityInformation](#pygsecurityinformation).GetInheritTypes

([SI_INHERIT_TYPE](SI.md#siinherit_type),...) = __GetInheritTypes(__ )
Requests types of inheritance that your implementation supports

#### Return Value
Returns a sequence of[SI_INHERIT_TYPE](SI.md#siinherit_type)tuples

## [PyGSecurityInformation](#pygsecurityinformation).GetObjectInformation

[SI_OBJECT_INFO](SI.md#siobject_info)= __GetObjectInformation(__ )
Returns information identifying the object 

whose security is to be editted, and which pages are to appear in the property sheet

#### Comments
Due to peculiarities of the underlying system calls, this method will only be called once, 

and subsequent calls will return the information obtained on the first call.  As a consequence, a new 

instance of the interface will need to be created for each object whose security is to be displayed.

#### Return Value
Your implementation of this method should return a[SI_OBJECT_INFO](SI.md#siobject_info)tuple

## [PyGSecurityInformation](#pygsecurityinformation).GetSecurity

[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)= __GetSecurity( *RequestedInformation*  *, Default* __ )
Retrieves the object's current security settings

#### Parameters


  -  *RequestedInformation* : int

    Combination of SECURITY_INFORMATION flags indicating which components of the object's security descriptor you should return

  -  *Default* : bool

    If true, return a default security descriptor rather than current security.  (invoked when 'Reset' button is clicked)

## [PyGSecurityInformation](#pygsecurityinformation).MapGeneric

int = __MapGeneric( *ObjectType*  *, AceFlags*  *, Mask* __ )
Translates generic access rights to specific equivalents

#### Parameters


  -  *ObjectType* :[PyIID](#pyiid)

    Type of object that permissions apply to, None or GUID_NULL indicates object itself

  -  *AceFlags* : int

    Flags from the ACE that contains the permissions

  -  *Mask* : int

    Bitmask containing access rights

#### Comments
See[win32security::MapGenericMask](win32security.md#win32securitymapgenericmask)

#### Return Value
This method should return the input bitmask will all generic rights mapped to specific rights

## [PyGSecurityInformation](#pygsecurityinformation).PropertySheetPageCallback

 __PropertySheetPageCallback( *hwnd*  *, Msg*  *, Page* __ )
Called by each page as it is created and destroyed

#### Parameters


  -  *hwnd* : int

    Handle to the window for the page

  -  *Msg* : int

    Flag indicating type of event, one of PSPCB_CREATE,PSPCB_RELEASE,PSPCB_SI_INITDIALOG

  -  *Page* : int

    SI_PAGE_TYPE value indicating which page is making the call (ntsecuritycon.SI_PAGE_*)

#### Return Value
Any returned value will be ignored

## [PyGSecurityInformation](#pygsecurityinformation).SetSecurity

 __SetSecurity( *SecurityInformation*  *, SecurityDescriptor* __ )
Applies the modified security to the object

#### Parameters


  -  *SecurityInformation* : int

    SECURITY_INFORMATION flags specifying which types of security information are to be applied

  -  *SecurityDescriptor* :[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)

    The security information to be applied to the object

#### Return Value
Any returned value is ignored