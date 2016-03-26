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

## [internet](#internet).CoInternetCreateSecurityManager

[PyIInternetSecurityManager](#pyiinternetsecuritymanager)= __CoInternetCreateSecurityManager( *reserved* __ )


#### Parameters


  -  *reserved* : int

    

## [internet](#internet).CoInternetIsFeatureEnabled

bool = __CoInternetIsFeatureEnabled( *flags* __ )


#### Parameters


  -  *flags* : int

    

#### Return Value
Returns true for S_OK, False for other non-error hresults, or 

raises a com_error.

## [internet](#internet).CoInternetSetFeatureEnabled

int = __CoInternetSetFeatureEnabled( *flags*  *, enable* __ )


#### Parameters


  -  *flags* : int

    

  -  *enable* : bool

    

## FEATURE_ADDON_MANAGEMENT
 __const internet.FEATURE_ADDON_MANAGEMENT;__ 


## FEATURE_BEHAVIORS
 __const internet.FEATURE_BEHAVIORS;__ 


## FEATURE_DISABLE_MK_PROTOCOL
 __const internet.FEATURE_DISABLE_MK_PROTOCOL;__ 


## FEATURE_ENTRY_COUNT
 __const internet.FEATURE_ENTRY_COUNT;__ 


## FEATURE_GET_URL_DOM_FILEPATH_UNENCODED
 __const internet.FEATURE_GET_URL_DOM_FILEPATH_UNENCODED;__ 


## FEATURE_HTTP_USERNAME_PASSWORD_DISABLE
 __const internet.FEATURE_HTTP_USERNAME_PASSWORD_DISABLE;__ 


## FEATURE_LOCALMACHINE_LOCKDOWN
 __const internet.FEATURE_LOCALMACHINE_LOCKDOWN;__ 


## FEATURE_MIME_HANDLING
 __const internet.FEATURE_MIME_HANDLING;__ 


## FEATURE_MIME_SNIFFING
 __const internet.FEATURE_MIME_SNIFFING;__ 


## FEATURE_OBJECT_CACHING
 __const internet.FEATURE_OBJECT_CACHING;__ 


## FEATURE_PROTOCOL_LOCKDOWN
 __const internet.FEATURE_PROTOCOL_LOCKDOWN;__ 


## FEATURE_RESTRICT_ACTIVEXINSTALL
 __const internet.FEATURE_RESTRICT_ACTIVEXINSTALL;__ 


## FEATURE_RESTRICT_FILEDOWNLOAD
 __const internet.FEATURE_RESTRICT_FILEDOWNLOAD;__ 


## FEATURE_SAFE_BINDTOOBJECT
 __const internet.FEATURE_SAFE_BINDTOOBJECT;__ 


## FEATURE_SECURITYBAND
 __const internet.FEATURE_SECURITYBAND;__ 


## FEATURE_UNC_SAVEDFILECHECK
 __const internet.FEATURE_UNC_SAVEDFILECHECK;__ 


## FEATURE_VALIDATE_NAVIGATE_URL
 __const internet.FEATURE_VALIDATE_NAVIGATE_URL;__ 


## FEATURE_WEBOC_POPUPMANAGEMENT
 __const internet.FEATURE_WEBOC_POPUPMANAGEMENT;__ 


## FEATURE_WINDOW_RESTRICTIONS
 __const internet.FEATURE_WINDOW_RESTRICTIONS;__ 


## FEATURE_ZONE_ELEVATION
 __const internet.FEATURE_ZONE_ELEVATION;__ 


## GET_FEATURE_FROM_PROCESS
 __const internet.GET_FEATURE_FROM_PROCESS;__ 


## GET_FEATURE_FROM_REGISTRY
 __const internet.GET_FEATURE_FROM_REGISTRY;__ 


## GET_FEATURE_FROM_THREAD
 __const internet.GET_FEATURE_FROM_THREAD;__ 


## GET_FEATURE_FROM_THREAD_INTERNET
 __const internet.GET_FEATURE_FROM_THREAD_INTERNET;__ 


## GET_FEATURE_FROM_THREAD_INTRANET
 __const internet.GET_FEATURE_FROM_THREAD_INTRANET;__ 


## GET_FEATURE_FROM_THREAD_LOCALMACHINE
 __const internet.GET_FEATURE_FROM_THREAD_LOCALMACHINE;__ 


## GET_FEATURE_FROM_THREAD_RESTRICTED
 __const internet.GET_FEATURE_FROM_THREAD_RESTRICTED;__ 


## GET_FEATURE_FROM_THREAD_TRUSTED
 __const internet.GET_FEATURE_FROM_THREAD_TRUSTED;__ 


## SET_FEATURE_IN_REGISTRY
 __const internet.SET_FEATURE_IN_REGISTRY;__ 


## SET_FEATURE_ON_PROCESS
 __const internet.SET_FEATURE_ON_PROCESS;__ 


## SET_FEATURE_ON_THREAD
 __const internet.SET_FEATURE_ON_THREAD;__ 


## SET_FEATURE_ON_THREAD_INTERNET
 __const internet.SET_FEATURE_ON_THREAD_INTERNET;__ 


## SET_FEATURE_ON_THREAD_INTRANET
 __const internet.SET_FEATURE_ON_THREAD_INTRANET;__ 


## SET_FEATURE_ON_THREAD_LOCALMACHINE
 __const internet.SET_FEATURE_ON_THREAD_LOCALMACHINE;__ 


## SET_FEATURE_ON_THREAD_RESTRICTED
 __const internet.SET_FEATURE_ON_THREAD_RESTRICTED;__ 


## SET_FEATURE_ON_THREAD_TRUSTED
 __const internet.SET_FEATURE_ON_THREAD_TRUSTED;__ 
