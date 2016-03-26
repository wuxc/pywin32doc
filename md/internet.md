# internet


## Module internet

A module, encapsulating the ActiveX Internet interfaces

#### Methods

  - [CoInternetCreateSecurityManager](internet.md#internetcointernetcreatesecuritymanager)

    &nbsp;

  - [CoInternetIsFeatureEnabled](internet.md#internetcointernetisfeatureenabled)

    &nbsp;

  - [CoInternetSetFeatureEnabled](internet.md#internetcointernetsetfeatureenabled)

    &nbsp;


## [internet](internet.md#internet)\.CoInternetCreateSecurityManager

[PyIInternetSecurityManager](PyIInternetSecurityManager.md) = CoInternetCreateSecurityManager\(reserved\)

#### Parameters

  - reserved : int

    


## [internet](internet.md#internet)\.CoInternetIsFeatureEnabled

bool = CoInternetIsFeatureEnabled\(flags\)

#### Parameters

  - flags : int

    

#### Return Value
Returns true for S\_OK, False for other non-error hresults, or 

raises a com\_error\.


## [internet](internet.md#internet)\.CoInternetSetFeatureEnabled

int = CoInternetSetFeatureEnabled\(flags, enable

\)

#### Parameters

  - flags : int

    

  - enable : bool

    


## FEATURE\_ADDON\_MANAGEMENT

const internet\.FEATURE\_ADDON\_MANAGEMENT;




## FEATURE\_BEHAVIORS

const internet\.FEATURE\_BEHAVIORS;




## FEATURE\_DISABLE\_MK\_PROTOCOL

const internet\.FEATURE\_DISABLE\_MK\_PROTOCOL;




## FEATURE\_ENTRY\_COUNT

const internet\.FEATURE\_ENTRY\_COUNT;




## FEATURE\_GET\_URL\_DOM\_FILEPATH\_UNENCODED

const internet\.FEATURE\_GET\_URL\_DOM\_FILEPATH\_UNENCODED;




## FEATURE\_HTTP\_USERNAME\_PASSWORD\_DISABLE

const internet\.FEATURE\_HTTP\_USERNAME\_PASSWORD\_DISABLE;




## FEATURE\_LOCALMACHINE\_LOCKDOWN

const internet\.FEATURE\_LOCALMACHINE\_LOCKDOWN;




## FEATURE\_MIME\_HANDLING

const internet\.FEATURE\_MIME\_HANDLING;




## FEATURE\_MIME\_SNIFFING

const internet\.FEATURE\_MIME\_SNIFFING;




## FEATURE\_OBJECT\_CACHING

const internet\.FEATURE\_OBJECT\_CACHING;




## FEATURE\_PROTOCOL\_LOCKDOWN

const internet\.FEATURE\_PROTOCOL\_LOCKDOWN;




## FEATURE\_RESTRICT\_ACTIVEXINSTALL

const internet\.FEATURE\_RESTRICT\_ACTIVEXINSTALL;




## FEATURE\_RESTRICT\_FILEDOWNLOAD

const internet\.FEATURE\_RESTRICT\_FILEDOWNLOAD;




## FEATURE\_SAFE\_BINDTOOBJECT

const internet\.FEATURE\_SAFE\_BINDTOOBJECT;




## FEATURE\_SECURITYBAND

const internet\.FEATURE\_SECURITYBAND;




## FEATURE\_UNC\_SAVEDFILECHECK

const internet\.FEATURE\_UNC\_SAVEDFILECHECK;




## FEATURE\_VALIDATE\_NAVIGATE\_URL

const internet\.FEATURE\_VALIDATE\_NAVIGATE\_URL;




## FEATURE\_WEBOC\_POPUPMANAGEMENT

const internet\.FEATURE\_WEBOC\_POPUPMANAGEMENT;




## FEATURE\_WINDOW\_RESTRICTIONS

const internet\.FEATURE\_WINDOW\_RESTRICTIONS;




## FEATURE\_ZONE\_ELEVATION

const internet\.FEATURE\_ZONE\_ELEVATION;




## GET\_FEATURE\_FROM\_PROCESS

const internet\.GET\_FEATURE\_FROM\_PROCESS;




## GET\_FEATURE\_FROM\_REGISTRY

const internet\.GET\_FEATURE\_FROM\_REGISTRY;




## GET\_FEATURE\_FROM\_THREAD

const internet\.GET\_FEATURE\_FROM\_THREAD;




## GET\_FEATURE\_FROM\_THREAD\_INTERNET

const internet\.GET\_FEATURE\_FROM\_THREAD\_INTERNET;




## GET\_FEATURE\_FROM\_THREAD\_INTRANET

const internet\.GET\_FEATURE\_FROM\_THREAD\_INTRANET;




## GET\_FEATURE\_FROM\_THREAD\_LOCALMACHINE

const internet\.GET\_FEATURE\_FROM\_THREAD\_LOCALMACHINE;




## GET\_FEATURE\_FROM\_THREAD\_RESTRICTED

const internet\.GET\_FEATURE\_FROM\_THREAD\_RESTRICTED;




## GET\_FEATURE\_FROM\_THREAD\_TRUSTED

const internet\.GET\_FEATURE\_FROM\_THREAD\_TRUSTED;




## SET\_FEATURE\_IN\_REGISTRY

const internet\.SET\_FEATURE\_IN\_REGISTRY;




## SET\_FEATURE\_ON\_PROCESS

const internet\.SET\_FEATURE\_ON\_PROCESS;




## SET\_FEATURE\_ON\_THREAD

const internet\.SET\_FEATURE\_ON\_THREAD;




## SET\_FEATURE\_ON\_THREAD\_INTERNET

const internet\.SET\_FEATURE\_ON\_THREAD\_INTERNET;




## SET\_FEATURE\_ON\_THREAD\_INTRANET

const internet\.SET\_FEATURE\_ON\_THREAD\_INTRANET;




## SET\_FEATURE\_ON\_THREAD\_LOCALMACHINE

const internet\.SET\_FEATURE\_ON\_THREAD\_LOCALMACHINE;




## SET\_FEATURE\_ON\_THREAD\_RESTRICTED

const internet\.SET\_FEATURE\_ON\_THREAD\_RESTRICTED;




## SET\_FEATURE\_ON\_THREAD\_TRUSTED

const internet\.SET\_FEATURE\_ON\_THREAD\_TRUSTED;

