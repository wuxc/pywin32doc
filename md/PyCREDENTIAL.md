# PyCREDENTIAL

## PyCREDENTIAL Object

A dictionary containing information for a CREDENTIAL struct

#### Win32 API References


  - Search for *CREDENTIAL struct* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=credential struct),[google](#http://www.google.com/search?q=credential struct)or[google groups](#http://groups.google.com/groups?q=credential struct)\.

#### Properties

  -  **int Flags** 
    Combination of CRED\_FLAGS\_PROMPT\_NOW, CRED\_FLAGS\_USERNAME\_TARGET

  -  **int Type** 
    Type of credential, one of CRED\_TYPE\_\* values

  -  **[PyUnicode](#pyunicode)TargetName** 
    Target of credential, can end with \* for wildcard matching

  -  **[PyUnicode](#pyunicode)Comment** 
    Descriptive text

  -  **[PyTime](#pytime)LastWritten** 
    Modification time, ignored on input

  -  **[PyUnicode](#pyunicode)CredentialBlob** 
    Contains password for username credential, or PIN for certificate credential\.  This member is write-only\.

  -  **int Persist** 
    Specifies scope of persistence, one of CRED\_PERSIST\_\* values

  -  **tuple Attributes** 
    Tuple of[PyCREDENTIAL\_ATTRIBUTE](PyCREDENTIAL.md#pycredentialattribute)dicts containing application-specific data, can be None

  -  **[PyUnicode](#pyunicode)TargetAlias** 
    Alias for TargetName, only valid with CRED\_TYPE\_GENERIC

  -  **[PyUnicode](#pyunicode)UserName** 
    User to be authenticated by target\. Can be of the form username@domain or domain\\\\username\. 

For CRED\_TYPE\_DOMAIN\_CERTIFICATE, use[win32cred::CredMarshalCredential](win32cred.md#win32credcredmarshalcredential)to marshal the SHA1 hash of user's certficate

## PyCREDENTIAL\_ATTRIBUTE Object

A dictionary containing information for a CREDENTIAL\_ATTRIBUTE struct

#### Win32 API References


  - Search for *CREDENTIAL\_ATTRIBUTE* at[msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CREDENTIAL.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=credentialattribute),[google](http://www.google.com/search?q=CREDENTIAL.md#http://www.google.com/search?q=credentialattribute)or[google groups](http://groups.google.com/groups?q=CREDENTIAL.md#http://groups.google.com/groups?q=credentialattribute)\.

#### Properties

  -  **[PyUnicode](#pyunicode)Keyword** 
    Attribute name, at most CRED\_MAX\_STRING\_LENGTH chars

  -  **int Flags** 
    Reserved, use only 0

  -  **str Value** 
    Attribute value, at most CRED\_MAX\_VALUE\_SIZE bytes\.  Unicode objects are treated as raw bytes\.

## PyCREDENTIAL\_TARGET\_INFORMATION Object

A dictionary representing a CREDENTIAL\_TARGET\_INFORMATION struct

#### Win32 API References


  - Search for *CREDENTIAL\_TARGET\_INFORMATION* at[msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CREDENTIAL.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=credentialtarget_information),[google](http://www.google.com/search?q=CREDENTIAL.md#http://www.google.com/search?q=credentialtarget_information)or[google groups](http://groups.google.com/groups?q=CREDENTIAL.md#http://groups.google.com/groups?q=credentialtarget_information)\.

#### Properties

  -  **[PyUnicode](#pyunicode)TargetName** 
    Target of credentials

  -  **[PyUnicode](#pyunicode)NetbiosServerName** 
    

  -  **[PyUnicode](#pyunicode)DnsServerName** 
    

  -  **[PyUnicode](#pyunicode)NetbiosDomainName** 
    

  -  **[PyUnicode](#pyunicode)DnsDomainName** 
    

  -  **[PyUnicode](#pyunicode)DnsTreeName** 
    

  -  **[PyUnicode](#pyunicode)PackageName** 
    Name of security package which mapped TargetName

  -  **int Flags** 
    CRED\_TI\_\* flags

  -  **\(int,\.\.\.\) CredTypes** 
    Tuple of CRED\_TYPE\_\* values indicating which types of credentials are acceptable to target