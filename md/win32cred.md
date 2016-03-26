
## Module win32cred

Interface to credentials management functions. 

The functions in this module are only available on Windows XP and later.
Functions operate only on the credential set of the calling user.
User's profile must be loaded for stored credentials to be accessible.
Each credential is uniquely identified by its TargetName and Type.
All functions accept keyword arguments.

#### Methods


  - [CredMarshalCredential](win32cred.md#win32credCredMarshalCredential)

    Marshals a credential into a unicode string&nbsp;

  - [CredUnmarshalCredential](win32cred.md#win32credCredUnmarshalCredential)

    Unmarshals credentials formatted using[win32cred::CredMarshalCredential](win32cred.md#win32credCredMarshalCredential)&nbsp;

  - [CredIsMarshaledCredential](win32cred.md#win32credCredIsMarshaledCredential)

    Checks if a string matches the form of a marshaled credential&nbsp;

  - [CredEnumerate](win32cred.md#win32credCredEnumerate)

    Lists stored credentials for current logon session&nbsp;

  - [CredGetTargetInfo](win32cred.md#win32credCredGetTargetInfo)

    Determines type and location of credential target&nbsp;

  - [CredWriteDomainCredentials](win32cred.md#win32credCredWriteDomainCredentials)

    Creates or updates credential for a domain or server&nbsp;

  - [CredReadDomainCredentials](win32cred.md#win32credCredReadDomainCredentials)

    Retrieves a user's credentials for a domain or server&nbsp;

  - [CredDelete](win32cred.md#win32credCredDelete)

    Deletes a stored credential&nbsp;

  - [CredWrite](win32cred.md#win32credCredWrite)

    Creates or updates a stored credential&nbsp;

  - [CredRead](win32cred.md#win32credCredRead)

    Retrieves a stored credential&nbsp;

  - [CredRename](win32cred.md#win32credCredRename)

    Changes the target name of stored credentials&nbsp;

  - [CredUICmdLinePromptForCredentials](win32cred.md#win32credCredUICmdLinePromptForCredentials)

    Prompt for username/passwd from a console app&nbsp;

  - [CredUIPromptForCredentials](win32cred.md#win32credCredUIPromptForCredentials)

    Initiates dialog to request user credentials&nbsp;

  - [CredUIConfirmCredentials](win32cred.md#win32credCredUIConfirmCredentials)

    Confirms whether credentials entered by user are valid or not&nbsp;

  - [CredUIReadSSOCredW](win32cred.md#win32credCredUIReadSSOCredW)

    Retrieves single sign on username&nbsp;

  - [CredUIStoreSSOCredW](win32cred.md#win32credCredUIStoreSSOCredW)

    Creates a single sign on credential&nbsp;

  - [CredUIParseUserName](win32cred.md#win32credCredUIParseUserName)

    Parses a full username into domain and username&nbsp;

## [win32cred](README.md#win32cred).CredDelete

 **CredDelete( *TargetName*  *, Type*  *, Flags* ** )
Deletes a stored credential

#### Parameters


  -  *TargetName* :[PyUnicode](README.md#PyUnicode)

    Target of credential to be deleted

  -  *Type* : int

    One of the CRED_TYPE_* values

  -  *Flags=0* : int

    Reserved, use only 0

## [win32cred](README.md#win32cred).CredEnumerate

(dict,...) = **CredEnumerate( *Filter*  *, Flags* ** )
Lists credentials for current logon session

#### Parameters


  -  *Filter=None* :[PyUnicode](README.md#PyUnicode)

    Matches credentials' target names by prefix, can be None

  -  *Flags=0* : int

    Reserved, use 0 if passed in

#### Return Value
Returns a sequence of[PyCREDENTIAL](README.md#PyCREDENTIAL)dictionaries

## [win32cred](README.md#win32cred).CredGetTargetInfo

dict = **CredGetTargetInfo( *TargetName*  *, Flags* ** )
Determines type and location of credential target

#### Parameters


  -  *TargetName* :[PyUnicode](README.md#PyUnicode)

    Name of server that is target of stored credentials

  -  *Flags=0* : int

    CRED_ALLOW_NAME_RESOLUTION, or 0

#### Comments
The target information will not be available until an attempt is made to authenticate against it

#### Return Value
Returns a[PyCREDENTIAL_TARGET_INFORMATION](PyCREDENTIAL.md#PyCREDENTIALTARGET_INFORMATION)dict

## [win32cred](README.md#win32cred).CredIsMarshaledCredential

boolean = **CredIsMarshaledCredential( *MarshaledCredential* ** )
Checks if a string matches the form of a marshaled credential

#### Parameters


  -  *MarshaledCredential* :[PyUnicode](README.md#PyUnicode)

    Marshaled credential as returned by[win32cred::CredMarshalCredential](win32cred.md#win32credCredMarshalCredential)

## [win32cred](README.md#win32cred).CredMarshalCredential

[PyUnicode](README.md#PyUnicode)= **CredMarshalCredential( *CredType*  *, Credential* ** )
Marshals a credential into a unicode string

#### Parameters


  -  *CredType* : int

    CertCredential or UsernameTargetCredential

  -  *Credential* : str/[PyUnicode](README.md#PyUnicode)

    The credential to be marshalled.  Type is dependent on CredType.

 **CredType**  **Type of Credential** CertCredentialString containing the SHA1 hash of user's certificateUsernameTargetCredentialUnicode string containing a username for which credentials exist in current logon session
#### Comments
Credentials with Flags that contain CRED_FLAGS_USERNAME_TARGET can be marshalled to be passed as the username 

to functions that normally require a username/password combination, such as[win32security::LogonUser](win32security.md#win32securityLogonUser)and[win32net::NetUseAdd](win32net.md#win32netNetUseAdd)

## [win32cred](README.md#win32cred).CredRead

dict = **CredRead( *TargetName*  *, Type*  *, Flags* ** )
Retrieves a stored credential

#### Parameters


  -  *TargetName* :[PyUnicode](README.md#PyUnicode)

    The target of the credentials to retrieve

  -  *Type* : int

    One of the CRED_TYPE_* constants

  -  *Flags=0* : int

    Reserved, use 0

#### Return Value
Returns a[PyCREDENTIAL](README.md#PyCREDENTIAL)dict

## [win32cred](README.md#win32cred).CredReadDomainCredentials

(dict,...) = **CredReadDomainCredentials( *TargetInfo*  *, Flags* ** )
Retrieves credentials for a domain or server

#### Parameters


  -  *TargetInfo* : dict

    [PyCREDENTIAL_TARGET_INFORMATION](PyCREDENTIAL.md#PyCREDENTIALTARGET_INFORMATION)identifying a domain or server. At least one of the Names is required.

  -  *Flags=0* : int

    CRED_CACHE_TARGET_INFORMATION is only valid flag

#### Return Value
Returns a sequence of[PyCREDENTIAL](README.md#PyCREDENTIAL)dicts

## [win32cred](README.md#win32cred).CredRename

dict = **CredRename( *OldTargetName*  *, NewTargetName*  *, Type*  *, Flags* ** )
Changes the target name of stored credentials

#### Parameters


  -  *OldTargetName* :[PyUnicode](README.md#PyUnicode)

    The target of credential to be renamed

  -  *NewTargetName* :[PyUnicode](README.md#PyUnicode)

    New target for the specified credential

  -  *Type* : int

    Type of the credential to be renamed (CRED_TYPE_*)

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
CRED_FLAGS_USERNAME_TARGET credentials can't be renamed since their TargetName and Username must be equal

## [win32cred](README.md#win32cred).CredUICmdLinePromptForCredentials

([PyUnicode](README.md#PyUnicode),[PyUnicode](README.md#PyUnicode), boolean) = **CredUICmdLinePromptForCredentials( *TargetName*  *, AuthError*  *, UserName*  *, Password*  *, Save*  *, Flags* ** )
Prompt for username/passwd from a console app

#### Parameters


  -  *TargetName* :[PyUnicode](README.md#PyUnicode)

    Server or domain against which to authenticate

  -  *AuthError=0* : int

    Error code indicating why credentials are required, can be 0

  -  *UserName=None* :[PyUnicode](README.md#PyUnicode)

    Default username, can be None.  At most CREDUI_MAX_USERNAME_LENGTH chars

  -  *Password=None* :[PyUnicode](README.md#PyUnicode)

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

## [win32cred](README.md#win32cred).CredUIConfirmCredentials

 **CredUIConfirmCredentials( *TargetName*  *, Confirm* ** )
Confirms whether credentials entered by user are valid or not

#### Parameters


  -  *TargetName* :[PyUnicode](README.md#PyUnicode)

    Target of credentials that are pending confirmation

  -  *Confirm* : boolean

    Indicates if authentication succeeded

#### Comments
This function should be called to confirm credentials entered via[win32cred::CredUICmdLinePromptForCredentials](win32cred.md#win32credCredUICmdLinePromptForCredentials)or[win32cred::CredUIPromptForCredentials](win32cred.md#win32credCredUIPromptForCredentials)if CREDUI_FLAGS_EXPECT_CONFIRMATION was passed in Flags to either function.
Sequence of operations:
Prompt for credentials
Authenticate against target using credentials
Call this function to indicate if authentication succeeded or not

## [win32cred](README.md#win32cred).CredUIParseUserName

([PyUnicode](README.md#PyUnicode),[PyUnicode](README.md#PyUnicode)) = **CredUIParseUserName( *UserName* ** )
Parses a full username into domain and username

#### Parameters


  -  *UserName* :[PyUnicode](README.md#PyUnicode)

    Username as returned by[win32cred::CredUIPromptForCredentials](win32cred.md#win32credCredUIPromptForCredentials)

#### Return Value
Returns the username and domain

## [win32cred](README.md#win32cred).CredUIPromptForCredentials

([PyUnicode](README.md#PyUnicode),[PyUnicode](README.md#PyUnicode), boolean) = **CredUIPromptForCredentials( *TargetName*  *, AuthError*  *, UserName*  *, Password*  *, Save*  *, Flags*  *, UiInfo* ** )
Initiates dialog to request user credentials

#### Parameters


  -  *TargetName* :[PyUnicode](README.md#PyUnicode)

    Server or domain against which to authenticate

  -  *AuthError=0* : int

    Error code indicating why credentials are required, can be 0

  -  *UserName=None* :[PyUnicode](README.md#PyUnicode)

    Default username, can be None.  At most CREDUI_MAX_USERNAME_LENGTH chars

  -  *Password=None* :[PyUnicode](README.md#PyUnicode)

    Password, can be None.  At most CREDUI_MAX_PASSWORD_LENGTH chars

  -  *Save=True* : boolean

    Specifies whether Save checkbox defaults to checked or unchecked

  -  *Flags=0* : int

    Combination of CREDUI_FLAGS_* values

  -  *UiInfo=None* : dict

    [PyCREDUI_INFO](PyCREDUI.md#PyCREDUIINFO)dict for customizing the dialog, can be None

#### Return Value
Returns the username, password, and a boolean indicating if credential was persisted

## [win32cred](README.md#win32cred).CredUIReadSSOCredW

[PyUnicode](README.md#PyUnicode)= **CredUIReadSSOCredW( *Realm* ** )
Retrieves single sign on username

#### Parameters


  -  *Realm=None* :[PyUnicode](README.md#PyUnicode)

    Realm for which to read username, can be None

## [win32cred](README.md#win32cred).CredUIStoreSSOCredW

 **CredUIStoreSSOCredW( *Realm*  *, Username*  *, Password*  *, Persist* ** )
Creates a single sign on credential

#### Parameters


  -  *Realm* :[PyUnicode](README.md#PyUnicode)

    Realm for which to read username, can be None for default realm

  -  *Username* :[PyUnicode](README.md#PyUnicode)

    Username for realm

  -  *Password* :[PyUnicode](README.md#PyUnicode)

    User's password

  -  *Persist* : boolean

    Specifies whether to save credential

## [win32cred](README.md#win32cred).CredUnmarshalCredential

int,[PyUnicode](README.md#PyUnicode)= **CredUnmarshalCredential( *MarshaledCredential* ** )
Unmarshals credentials formatted using[win32cred::CredMarshalCredential](win32cred.md#win32credCredMarshalCredential)

#### Parameters


  -  *MarshaledCredential* :[PyUnicode](README.md#PyUnicode)

    Unicode string containing marshaled credential

 **CredType**  **Type of output credentials** CertCredentialCharacter string containing SHA1 hash of a certificateUsernameTargetCredentialUnicode string containing username
#### Return Value
Returns the credential type and credentials.

## [win32cred](README.md#win32cred).CredWrite

 **CredWrite( *Credential*  *, Flags* ** )
Creates or updates a stored credential

#### Parameters


  -  *Credential* : dict

    [PyCREDENTIAL](README.md#PyCREDENTIAL)dict containing the credentials to be stored

  -  *Flags=0* : int

    CRED_PRESERVE_CREDENTIAL_BLOB is only defined flag

#### Comments
When updating a credential, to preserve a previously stored password use None or '' 

for CredentialBlob member of Credential and pass CRED_PRESERVE_CREDENTIAL_BLOB in Flags

## [win32cred](README.md#win32cred).CredWriteDomainCredentials

 **CredWriteDomainCredentials( *TargetInfo*  *, Credential*  *, Flags* ** )
Creates or updates credential for a domain or server

#### Parameters


  -  *TargetInfo* : dict

    [PyCREDENTIAL_TARGET_INFORMATION](PyCREDENTIAL.md#PyCREDENTIALTARGET_INFORMATION)identifying the target domain. At least one of the Names is required

  -  *Credential* : dict

    [PyCREDENTIAL](README.md#PyCREDENTIAL)dict containing the credentials to be stored

  -  *Flags=0* : int

    CRED_PRESERVE_CREDENTIAL_BLOB is only defined flag

#### Comments
When updating a credential, to preserve a previously stored password use None or '' 

for CredentialBlob member of Credential and pass CRED_PRESERVE_CREDENTIAL_BLOB in Flags