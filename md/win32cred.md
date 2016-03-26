# win32cred

## Module win32cred

Interface to credentials management functions. 

The functions in this module are only available on Windows XP and later.
Functions operate only on the credential set of the calling user.
User's profile must be loaded for stored credentials to be accessible.
Each credential is uniquely identified by its TargetName and Type.
All functions accept keyword arguments.

#### Methods


  - [CredMarshalCredential](win32cred.md#win32credcredmarshalcredential)

    Marshals a credential into a unicode string&nbsp;

  - [CredUnmarshalCredential](win32cred.md#win32credcredunmarshalcredential)

    Unmarshals credentials formatted using[win32cred::CredMarshalCredential](win32cred.md#win32credcredmarshalcredential)&nbsp;

  - [CredIsMarshaledCredential](win32cred.md#win32credcredismarshaledcredential)

    Checks if a string matches the form of a marshaled credential&nbsp;

  - [CredEnumerate](win32cred.md#win32credcredenumerate)

    Lists stored credentials for current logon session&nbsp;

  - [CredGetTargetInfo](win32cred.md#win32credcredgettargetinfo)

    Determines type and location of credential target&nbsp;

  - [CredWriteDomainCredentials](win32cred.md#win32credcredwritedomaincredentials)

    Creates or updates credential for a domain or server&nbsp;

  - [CredReadDomainCredentials](win32cred.md#win32credcredreaddomaincredentials)

    Retrieves a user's credentials for a domain or server&nbsp;

  - [CredDelete](win32cred.md#win32credcreddelete)

    Deletes a stored credential&nbsp;

  - [CredWrite](win32cred.md#win32credcredwrite)

    Creates or updates a stored credential&nbsp;

  - [CredRead](win32cred.md#win32credcredread)

    Retrieves a stored credential&nbsp;

  - [CredRename](win32cred.md#win32credcredrename)

    Changes the target name of stored credentials&nbsp;

  - [CredUICmdLinePromptForCredentials](win32cred.md#win32credcreduicmdlinepromptforcredentials)

    Prompt for username/passwd from a console app&nbsp;

  - [CredUIPromptForCredentials](win32cred.md#win32credcreduipromptforcredentials)

    Initiates dialog to request user credentials&nbsp;

  - [CredUIConfirmCredentials](win32cred.md#win32credcreduiconfirmcredentials)

    Confirms whether credentials entered by user are valid or not&nbsp;

  - [CredUIReadSSOCredW](win32cred.md#win32credcreduireadssocredw)

    Retrieves single sign on username&nbsp;

  - [CredUIStoreSSOCredW](win32cred.md#win32credcreduistoressocredw)

    Creates a single sign on credential&nbsp;

  - [CredUIParseUserName](win32cred.md#win32credcreduiparseusername)

    Parses a full username into domain and username&nbsp;

## [win32cred](#win32cred).CredDelete

 __CredDelete( *TargetName*  *, Type*  *, Flags* __ )
Deletes a stored credential

#### Parameters


  -  *TargetName* :[PyUnicode](#pyunicode)

    Target of credential to be deleted

  -  *Type* : int

    One of the CRED_TYPE_* values

  -  *Flags=0* : int

    Reserved, use only 0

## [win32cred](#win32cred).CredEnumerate

(dict,...) = __CredEnumerate( *Filter*  *, Flags* __ )
Lists credentials for current logon session

#### Parameters


  -  *Filter=None* :[PyUnicode](#pyunicode)

    Matches credentials' target names by prefix, can be None

  -  *Flags=0* : int

    Reserved, use 0 if passed in

#### Return Value
Returns a sequence of[PyCREDENTIAL](#pycredential)dictionaries

## [win32cred](#win32cred).CredGetTargetInfo

dict = __CredGetTargetInfo( *TargetName*  *, Flags* __ )
Determines type and location of credential target

#### Parameters


  -  *TargetName* :[PyUnicode](#pyunicode)

    Name of server that is target of stored credentials

  -  *Flags=0* : int

    CRED_ALLOW_NAME_RESOLUTION, or 0

#### Comments
The target information will not be available until an attempt is made to authenticate against it

#### Return Value
Returns a[PyCREDENTIAL_TARGET_INFORMATION](PyCREDENTIAL.md#pycredentialtarget_information)dict

## [win32cred](#win32cred).CredIsMarshaledCredential

boolean = __CredIsMarshaledCredential( *MarshaledCredential* __ )
Checks if a string matches the form of a marshaled credential

#### Parameters


  -  *MarshaledCredential* :[PyUnicode](#pyunicode)

    Marshaled credential as returned by[win32cred::CredMarshalCredential](win32cred.md#win32credcredmarshalcredential)

## [win32cred](#win32cred).CredMarshalCredential

[PyUnicode](#pyunicode)= __CredMarshalCredential( *CredType*  *, Credential* __ )
Marshals a credential into a unicode string

#### Parameters


  -  *CredType* : int

    CertCredential or UsernameTargetCredential

  -  *Credential* : str/[PyUnicode](#pyunicode)

    The credential to be marshalled.  Type is dependent on CredType.

 __CredType__  __Type of Credential__ CertCredentialString containing the SHA1 hash of user's certificateUsernameTargetCredentialUnicode string containing a username for which credentials exist in current logon session
#### Comments
Credentials with Flags that contain CRED_FLAGS_USERNAME_TARGET can be marshalled to be passed as the username 

to functions that normally require a username/password combination, such as[win32security::LogonUser](win32security.md#win32securitylogonuser)and[win32net::NetUseAdd](win32net.md#win32netnetuseadd)

## [win32cred](#win32cred).CredRead

dict = __CredRead( *TargetName*  *, Type*  *, Flags* __ )
Retrieves a stored credential

#### Parameters


  -  *TargetName* :[PyUnicode](#pyunicode)

    The target of the credentials to retrieve

  -  *Type* : int

    One of the CRED_TYPE_* constants

  -  *Flags=0* : int

    Reserved, use 0

#### Return Value
Returns a[PyCREDENTIAL](#pycredential)dict

## [win32cred](#win32cred).CredReadDomainCredentials

(dict,...) = __CredReadDomainCredentials( *TargetInfo*  *, Flags* __ )
Retrieves credentials for a domain or server

#### Parameters


  -  *TargetInfo* : dict

    [PyCREDENTIAL_TARGET_INFORMATION](PyCREDENTIAL.md#pycredentialtarget_information)identifying a domain or server. At least one of the Names is required.

  -  *Flags=0* : int

    CRED_CACHE_TARGET_INFORMATION is only valid flag

#### Return Value
Returns a sequence of[PyCREDENTIAL](#pycredential)dicts

## [win32cred](#win32cred).CredRename

dict = __CredRename( *OldTargetName*  *, NewTargetName*  *, Type*  *, Flags* __ )
Changes the target name of stored credentials

#### Parameters


  -  *OldTargetName* :[PyUnicode](#pyunicode)

    The target of credential to be renamed

  -  *NewTargetName* :[PyUnicode](#pyunicode)

    New target for the specified credential

  -  *Type* : int

    Type of the credential to be renamed (CRED_TYPE_*)

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
CRED_FLAGS_USERNAME_TARGET credentials can't be renamed since their TargetName and Username must be equal

## [win32cred](#win32cred).CredUICmdLinePromptForCredentials

([PyUnicode](#pyunicode),[PyUnicode](#pyunicode), boolean) = __CredUICmdLinePromptForCredentials( *TargetName*  *, AuthError*  *, UserName*  *, Password*  *, Save*  *, Flags* __ )
Prompt for username/passwd from a console app

#### Parameters


  -  *TargetName* :[PyUnicode](#pyunicode)

    Server or domain against which to authenticate

  -  *AuthError=0* : int

    Error code indicating why credentials are required, can be 0

  -  *UserName=None* :[PyUnicode](#pyunicode)

    Default username, can be None.  At most CREDUI_MAX_USERNAME_LENGTH chars

  -  *Password=None* :[PyUnicode](#pyunicode)

    Password, can be None.  At most CREDUI_MAX_PASSWORD_LENGTH chars

  -  *Save=True* : boolean

    Specifies default value for Save prompt

  -  *Flags=CREDUI_FLAGS_EXCLUDE_CERTIFICATES* : int

    Combination of CREDUI_FLAGS_* values

#### Comments
The command-line version of this function does not accept certificates, so Flags 

must contain CREDUI_FLAGS_EXCLUDE_CERTIFICATES or CREDUI_FLAGS_REQUIRE_SMARTCARD

#### Return Value
Returns the username and password entered, and a boolean indicating if credential was saved

## [win32cred](#win32cred).CredUIConfirmCredentials

 __CredUIConfirmCredentials( *TargetName*  *, Confirm* __ )
Confirms whether credentials entered by user are valid or not

#### Parameters


  -  *TargetName* :[PyUnicode](#pyunicode)

    Target of credentials that are pending confirmation

  -  *Confirm* : boolean

    Indicates if authentication succeeded

#### Comments
This function should be called to confirm credentials entered via[win32cred::CredUICmdLinePromptForCredentials](win32cred.md#win32credcreduicmdlinepromptforcredentials)or[win32cred::CredUIPromptForCredentials](win32cred.md#win32credcreduipromptforcredentials)if CREDUI_FLAGS_EXPECT_CONFIRMATION was passed in Flags to either function.
Sequence of operations:
Prompt for credentials
Authenticate against target using credentials
Call this function to indicate if authentication succeeded or not

## [win32cred](#win32cred).CredUIParseUserName

([PyUnicode](#pyunicode),[PyUnicode](#pyunicode)) = __CredUIParseUserName( *UserName* __ )
Parses a full username into domain and username

#### Parameters


  -  *UserName* :[PyUnicode](#pyunicode)

    Username as returned by[win32cred::CredUIPromptForCredentials](win32cred.md#win32credcreduipromptforcredentials)

#### Return Value
Returns the username and domain

## [win32cred](#win32cred).CredUIPromptForCredentials

([PyUnicode](#pyunicode),[PyUnicode](#pyunicode), boolean) = __CredUIPromptForCredentials( *TargetName*  *, AuthError*  *, UserName*  *, Password*  *, Save*  *, Flags*  *, UiInfo* __ )
Initiates dialog to request user credentials

#### Parameters


  -  *TargetName* :[PyUnicode](#pyunicode)

    Server or domain against which to authenticate

  -  *AuthError=0* : int

    Error code indicating why credentials are required, can be 0

  -  *UserName=None* :[PyUnicode](#pyunicode)

    Default username, can be None.  At most CREDUI_MAX_USERNAME_LENGTH chars

  -  *Password=None* :[PyUnicode](#pyunicode)

    Password, can be None.  At most CREDUI_MAX_PASSWORD_LENGTH chars

  -  *Save=True* : boolean

    Specifies whether Save checkbox defaults to checked or unchecked

  -  *Flags=0* : int

    Combination of CREDUI_FLAGS_* values

  -  *UiInfo=None* : dict

    [PyCREDUI_INFO](PyCREDUI.md#pycreduiinfo)dict for customizing the dialog, can be None

#### Return Value
Returns the username, password, and a boolean indicating if credential was persisted

## [win32cred](#win32cred).CredUIReadSSOCredW

[PyUnicode](#pyunicode)= __CredUIReadSSOCredW( *Realm* __ )
Retrieves single sign on username

#### Parameters


  -  *Realm=None* :[PyUnicode](#pyunicode)

    Realm for which to read username, can be None

## [win32cred](#win32cred).CredUIStoreSSOCredW

 __CredUIStoreSSOCredW( *Realm*  *, Username*  *, Password*  *, Persist* __ )
Creates a single sign on credential

#### Parameters


  -  *Realm* :[PyUnicode](#pyunicode)

    Realm for which to read username, can be None for default realm

  -  *Username* :[PyUnicode](#pyunicode)

    Username for realm

  -  *Password* :[PyUnicode](#pyunicode)

    User's password

  -  *Persist* : boolean

    Specifies whether to save credential

## [win32cred](#win32cred).CredUnmarshalCredential

int,[PyUnicode](#pyunicode)= __CredUnmarshalCredential( *MarshaledCredential* __ )
Unmarshals credentials formatted using[win32cred::CredMarshalCredential](win32cred.md#win32credcredmarshalcredential)

#### Parameters


  -  *MarshaledCredential* :[PyUnicode](#pyunicode)

    Unicode string containing marshaled credential

 __CredType__  __Type of output credentials__ CertCredentialCharacter string containing SHA1 hash of a certificateUsernameTargetCredentialUnicode string containing username
#### Return Value
Returns the credential type and credentials.

## [win32cred](#win32cred).CredWrite

 __CredWrite( *Credential*  *, Flags* __ )
Creates or updates a stored credential

#### Parameters


  -  *Credential* : dict

    [PyCREDENTIAL](#pycredential)dict containing the credentials to be stored

  -  *Flags=0* : int

    CRED_PRESERVE_CREDENTIAL_BLOB is only defined flag

#### Comments
When updating a credential, to preserve a previously stored password use None or '' 

for CredentialBlob member of Credential and pass CRED_PRESERVE_CREDENTIAL_BLOB in Flags

## [win32cred](#win32cred).CredWriteDomainCredentials

 __CredWriteDomainCredentials( *TargetInfo*  *, Credential*  *, Flags* __ )
Creates or updates credential for a domain or server

#### Parameters


  -  *TargetInfo* : dict

    [PyCREDENTIAL_TARGET_INFORMATION](PyCREDENTIAL.md#pycredentialtarget_information)identifying the target domain. At least one of the Names is required

  -  *Credential* : dict

    [PyCREDENTIAL](#pycredential)dict containing the credentials to be stored

  -  *Flags=0* : int

    CRED_PRESERVE_CREDENTIAL_BLOB is only defined flag

#### Comments
When updating a credential, to preserve a previously stored password use None or '' 

for CredentialBlob member of Credential and pass CRED_PRESERVE_CREDENTIAL_BLOB in Flags