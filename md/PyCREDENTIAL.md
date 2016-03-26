# PyCREDENTIAL

## PyCREDENTIAL Object

A dictionary containing information for a CREDENTIAL struct

#### Win32 API References


  - Search for *CREDENTIAL struct* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=credential struct),[google](#http://www.google.com/search?q=credential struct)or[google groups](#http://groups.google.com/groups?q=credential struct).

#### Properties

  -  __int Flags__ 
    Combination of CRED_FLAGS_PROMPT_NOW, CRED_FLAGS_USERNAME_TARGET

  -  __int Type__ 
    Type of credential, one of CRED_TYPE_* values

  -  __[PyUnicode](#pyunicode)TargetName__ 
    Target of credential, can end with * for wildcard matching

  -  __[PyUnicode](#pyunicode)Comment__ 
    Descriptive text

  -  __[PyTime](#pytime)LastWritten__ 
    Modification time, ignored on input

  -  __[PyUnicode](#pyunicode)CredentialBlob__ 
    Contains password for username credential, or PIN for certificate credential.  This member is write-only.

  -  __int Persist__ 
    Specifies scope of persistence, one of CRED_PERSIST_* values

  -  __tuple Attributes__ 
    Tuple of[PyCREDENTIAL_ATTRIBUTE](PyCREDENTIAL.md#pycredentialattribute)dicts containing application-specific data, can be None

  -  __[PyUnicode](#pyunicode)TargetAlias__ 
    Alias for TargetName, only valid with CRED_TYPE_GENERIC

  -  __[PyUnicode](#pyunicode)UserName__ 
    User to be authenticated by target. Can be of the form username@domain or domain\\username. 

For CRED_TYPE_DOMAIN_CERTIFICATE, use[win32cred::CredMarshalCredential](win32cred.md#win32credcredmarshalcredential)to marshal the SHA1 hash of user's certficate

## PyCREDENTIAL_ATTRIBUTE Object

A dictionary containing information for a CREDENTIAL_ATTRIBUTE struct

#### Win32 API References


  - Search for *CREDENTIAL_ATTRIBUTE* at[msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CREDENTIAL.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=credentialattribute),[google](http://www.google.com/search?q=CREDENTIAL.md#http://www.google.com/search?q=credentialattribute)or[google groups](http://groups.google.com/groups?q=CREDENTIAL.md#http://groups.google.com/groups?q=credentialattribute).

#### Properties

  -  __[PyUnicode](#pyunicode)Keyword__ 
    Attribute name, at most CRED_MAX_STRING_LENGTH chars

  -  __int Flags__ 
    Reserved, use only 0

  -  __str Value__ 
    Attribute value, at most CRED_MAX_VALUE_SIZE bytes.  Unicode objects are treated as raw bytes.

## PyCREDENTIAL_TARGET_INFORMATION Object

A dictionary representing a CREDENTIAL_TARGET_INFORMATION struct

#### Win32 API References


  - Search for *CREDENTIAL_TARGET_INFORMATION* at[msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CREDENTIAL.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=credentialtarget_information),[google](http://www.google.com/search?q=CREDENTIAL.md#http://www.google.com/search?q=credentialtarget_information)or[google groups](http://groups.google.com/groups?q=CREDENTIAL.md#http://groups.google.com/groups?q=credentialtarget_information).

#### Properties

  -  __[PyUnicode](#pyunicode)TargetName__ 
    Target of credentials

  -  __[PyUnicode](#pyunicode)NetbiosServerName__ 
    

  -  __[PyUnicode](#pyunicode)DnsServerName__ 
    

  -  __[PyUnicode](#pyunicode)NetbiosDomainName__ 
    

  -  __[PyUnicode](#pyunicode)DnsDomainName__ 
    

  -  __[PyUnicode](#pyunicode)DnsTreeName__ 
    

  -  __[PyUnicode](#pyunicode)PackageName__ 
    Name of security package which mapped TargetName

  -  __int Flags__ 
    CRED_TI_* flags

  -  __(int,...) CredTypes__ 
    Tuple of CRED_TYPE_* values indicating which types of credentials are acceptable to target