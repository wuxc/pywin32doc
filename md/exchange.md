# exchange

## Module exchange

A COM interface to Exchange's API

#### Methods


  - [HrGetExchangeStatus](exchange.md#exchangehrgetexchangestatus)

    Obtains the current state of the server on a computer\.&nbsp;

  - [HrGetMailboxDN](exchange.md#exchangehrgetmailboxdn)

    Retrieves the distinguished name \(DN\) for a mailbox&nbsp;

  - [HrGetServerDN](exchange.md#exchangehrgetserverdn)

    Retrieves the distinguished name \(DN\) for a server&nbsp;

  - [HrMAPIFindDefaultMsgStore](exchange.md#exchangehrmapifinddefaultmsgstore)

    Retrieves the entry identifier of the default information store\.&nbsp;

  - [HrMAPIFindIPMSubtree](exchange.md#exchangehrmapifindipmsubtree)

    Retrieves the entry ID of the IPM \(interpersonal message\) subtree folder&nbsp;

  - [HrMAPIFindInbox](exchange.md#exchangehrmapifindinbox)

    Retrieves the Entry ID of the IPM inbox folder&nbsp;

  - [HrMAPIFindSubfolderEx](exchange.md#exchangehrmapifindsubfolderex)

    Retrieves a subfolder in an information store using the hierarchical path name of the folder\.&nbsp;

  - [HrMAPIFindFolder](exchange.md#exchangehrmapifindfolder)

    Retrieves the entry ID for a folder in an information store using the hierarchical path name of the folder\.&nbsp;

  - [HrMAPIFindFolderEx](exchange.md#exchangehrmapifindfolderex)

    Retrieves the entry ID of a folder in an information store using the hierarchical path name of the folder\.&nbsp;

  - [HrMAPIFindStore](exchange.md#exchangehrmapifindstore)

    Retrieves a pointer to the entry identifier of an information store from the display name of the store\.&nbsp;

  - [HrCreateProfileName](exchange.md#exchangehrcreateprofilename)

    Creates a profile with the specified name&nbsp;

  - [HrCreateDirEntryIdEx](exchange.md#exchangehrcreatedirentryidex)

    Creates a directory identifier for a MAPI object, given the address of the object in the directory&nbsp;

  - [HrFindExchangeGlobalAddressList](exchange.md#exchangehrfindexchangeglobaladdresslist)

    Retrieves the entry identifier of the global address list \(GAL\) container in the address book\.&nbsp;

  - [HrMailboxLogon](exchange.md#exchangehrmailboxlogon)

    Logs on a server and mailbox\.&nbsp;

  - [HrMailboxLogoff](exchange.md#exchangehrmailboxlogoff)

    Logs off a server and mailbox\.&nbsp;

  - [HrMAPIOpenFolderEx](exchange.md#exchangehrmapiopenfolderex)

    Opens a folder in the information store from the hierarchical path name of the folder\.&nbsp;

  - [HrMAPISetPropBoolean](exchange.md#exchangehrmapisetpropboolean)

    Sets a boolean property\.&nbsp;

  - [HrMAPISetPropLong](exchange.md#exchangehrmapisetproplong)

    Sets a long property\.&nbsp;

  - [HrOpenExchangePublicStore](exchange.md#exchangehropenexchangepublicstore)

    Retrieves an interface to the public information store provider\.&nbsp;

  - [HrOpenExchangePrivateStore](exchange.md#exchangehropenexchangeprivatestore)

    Locates the primary user information store provider\.&nbsp;

  - [HrOpenExchangePublicFolders](exchange.md#exchangehropenexchangepublicfolders)

    Opens the root of the public folder hierarchy in the public information store\.&nbsp;

  - [HrOpenSessionObject](exchange.md#exchangehropensessionobject)

    Retrieves a MAPI[PyIMAPIProp](#pyimapiprop)object for the current session object\.&nbsp;

  - [HrOpenSiteContainer](exchange.md#exchangehropensitecontainer)

    Retrieves a MAPI[PyIMAPIProp](#pyimapiprop)object for a site object\.&nbsp;

  - [HrOpenSiteContainerAddressing](exchange.md#exchangehropensitecontaineraddressing)

    Retrieves a MAPI[PyIMAPIProp](#pyimapiprop)object for a site-addressing object\.&nbsp;

## [exchange](#exchange)\.HrCreateDirEntryIdEx

string \= **HrCreateDirEntryIdEx\( *addrBook*  *, distinguishedName* ** \)
Creates a directory identifier for a MAPI object, given the address of the object in the directory

#### Parameters


  -  *addrBook* :[PyIAddrBook](#pyiaddrbook)

    The address book interface

  -  *distinguishedName* : string

    The dn of the object to obtain the entry ID for\.

## [exchange](#exchange)\.HrCreateProfileName

string \= **HrCreateProfileName\( *profPrefix* ** \)
Creates a profile with the specified name

#### Parameters


  -  *profPrefix* : string/[PyUnicode](#pyunicode)

    A prefix for the new profile\.

## [exchange](#exchange)\.HrFindExchangeGlobalAddressList

string \= **HrFindExchangeGlobalAddressList\( *addrBook* ** \)
Retrieves the entry identifier of the global address list \(GAL\) container in the address book\.

#### Parameters


  -  *addrBook* :[PyIAddrBook](#pyiaddrbook)

    The interface containing the address book

## [exchange](#exchange)\.HrGetExchangeStatus

int, int \= **HrGetExchangeStatus\( *server* ** \)
Obtains the current state of the server on a computer\.

#### Parameters


  -  *server* : string/[PyUnicode](#pyunicode)

    The name of the server to query\.

#### Return Value
The result is a tuple of serviceState, serverState

## [exchange](#exchange)\.HrGetMailboxDN

string \= **HrGetMailboxDN\( *session* ** \)
Retrieves the distinguished name \(DN\) for a mailbox

#### Parameters


  -  *session* : **IMAPISession** 

    The root folder\.

## [exchange](#exchange)\.HrGetServerDN

string \= **HrGetServerDN\( *session* ** \)
Retrieves the distinguished name \(DN\) for a server

#### Parameters


  -  *session* : **IMAPISession** 

    The root folder\.

## [exchange](#exchange)\.HrMAPIFindDefaultMsgStore

string \= **HrMAPIFindDefaultMsgStore\( *session* ** \)
Retrieves the entry identifier of the default information store\.

#### Parameters


  -  *session* :[PyIMAPISession](#pyimapisession)

    

## [exchange](#exchange)\.HrMAPIFindFolder

string \= **HrMAPIFindFolder\( *folder*  *, name* ** \)
Retrieves the entry ID for a folder in an information store using the hierarchical path name of the folder\.

#### Parameters


  -  *folder* :[PyIMAPIFolder](#pyimapifolder)

    The folder to search

  -  *name* : string

    Name of the folder

## [exchange](#exchange)\.HrMAPIFindFolderEx

string \= **HrMAPIFindFolderEx\( *msgStore*  *, sepString*  *, path* ** \)
Retrieves the entry ID of a folder in an information store using the hierarchical path name of the folder\.

#### Parameters


  -  *msgStore* :[PyIMsgStore](#pyimsgstore)

    The folder to search

  -  *sepString* : string

    The character seperating the folder names - eg '\\\\'

  -  *path* : string

    Path to the folder

## [exchange](#exchange)\.HrMAPIFindIPMSubtree

string \= **HrMAPIFindIPMSubtree\( *msgStore* ** \)
Retrieves the entry ID of the IPM \(interpersonal message\) subtree folder

#### Parameters


  -  *msgStore* :[PyIMsgStore](#pyimsgstore)

    

## [exchange](#exchange)\.HrMAPIFindInbox

string \= **HrMAPIFindInbox\( *msgStore* ** \)
Retrieves the Entry ID of the IPM inbox folder

#### Parameters


  -  *msgStore* :[PyIMsgStore](#pyimsgstore)

    

## [exchange](#exchange)\.HrMAPIFindStore

[PyIMsgStore](#pyimsgstore)\= **HrMAPIFindStore\( *session*  *, name* ** \)
Retrieves a pointer to the entry identifier of an information store from the display name of the store\.

#### Parameters


  -  *session* :[PyIMAPISession](#pyimapisession)

    

  -  *name* : string

    

## [exchange](#exchange)\.HrMAPIFindSubfolderEx

[PyIMsgStore](#pyimsgstore)\= **HrMAPIFindSubfolderEx\( *rootFolder*  *, sep*  *, name* ** \)
Retrieves a subfolder in an information store using the hierarchical path name of the folder\.

#### Parameters


  -  *rootFolder* :[PyIMAPIFolder](#pyimapifolder)

    The root folder\.

  -  *sep* : string/[PyUnicode](#pyunicode)

    The folder seperator character\.

  -  *name* : string/[PyUnicode](#pyunicode)

    The folder name

## [exchange](#exchange)\.HrMAPIOpenFolderEx

[PyIMAPIFolder](#pyimapifolder)\= **HrMAPIOpenFolderEx\( *msgStore*  *, sep*  *, name* ** \)
Opens a folder in the information store from the hierarchical path name of the folder\.

#### Parameters


  -  *msgStore* :[PyIMsgStore](#pyimsgstore)

    

  -  *sep* : string/[PyUnicode](#pyunicode)

    The folder seperator character\.

  -  *name* : string/[PyUnicode](#pyunicode)

    The folder name

## [exchange](#exchange)\.HrMAPISetPropBoolean

 **HrMAPISetPropBoolean\( *obj*  *, tag* ** \)
Sets a boolean property\.

#### Parameters


  -  *obj* :[PyIMAPIProp](#pyimapiprop)

    The object to set

  -  *tag* : int

    The property tag

## [exchange](#exchange)\.HrMAPISetPropLong

 **HrMAPISetPropLong\( *obj*  *, tag* ** \)
Sets a long property\.

#### Parameters


  -  *obj* :[PyIMAPIProp](#pyimapiprop)

    The object to set

  -  *tag* : int

    The property tag

## [exchange](#exchange)\.HrMailboxLogoff

 **HrMailboxLogoff\( *inbox* ** \)
Logs off a server and mailbox\.

#### Parameters


  -  *inbox* :[PyIMsgStore](#pyimsgstore)

    The open inbox\.

## [exchange](#exchange)\.HrMailboxLogon

[PyIMsgStore](#pyimsgstore)\= **HrMailboxLogon\( *session*  *, msgStore*  *, msgStoreDN*  *, mailboxDN* ** \)
Logs on a server and mailbox\.

#### Parameters


  -  *session* :[PyIMAPISession](#pyimapisession)

    The session object

  -  *msgStore* :[PyIMsgStore](#pyimsgstore)

    

  -  *msgStoreDN* : string/[PyUnicode](#pyunicode)

    

  -  *mailboxDN* : string/[PyUnicode](#pyunicode)

    

## [exchange](#exchange)\.HrOpenExchangePrivateStore

[PyIMsgStore](#pyimsgstore)\= **HrOpenExchangePrivateStore\( *session* ** \)
Locates the primary user information store provider\.

#### Parameters


  -  *session* :[PyIMAPISession](#pyimapisession)

    The MAPI session object

## [exchange](#exchange)\.HrOpenExchangePublicFolders

[PyIMAPIFolder](#pyimapifolder)\= **HrOpenExchangePublicFolders\( *store* ** \)
Opens the root of the public folder hierarchy in the public information store\.

#### Parameters


  -  *store* :[PyIMsgStore](#pyimsgstore)

    

## [exchange](#exchange)\.HrOpenExchangePublicStore

[PyIMsgStore](#pyimsgstore)\= **HrOpenExchangePublicStore\( *session* ** \)
Retrieves an interface to the public information store provider\.

#### Parameters


  -  *session* :[PyIMAPISession](#pyimapisession)

    The MAPI session object

## [exchange](#exchange)\.HrOpenSessionObject

[PyIMAPIProp](#pyimapiprop)\= **HrOpenSessionObject\( *session* ** \)
Retrieves a MAPI[PyIMAPIProp](#pyimapiprop)object for the current session object\.

#### Parameters


  -  *session* :[PyIMAPISession](#pyimapisession)

    The MAPI session object

## [exchange](#exchange)\.HrOpenSiteContainer

[PyIMAPIProp](#pyimapiprop)\= **HrOpenSiteContainer\( *session* ** \)
Retrieves a MAPI[PyIMAPIProp](#pyimapiprop)object for a site object\.

#### Parameters


  -  *session* :[PyIMAPISession](#pyimapisession)

    The MAPI session object

## [exchange](#exchange)\.HrOpenSiteContainerAddressing

[PyIMAPIProp](#pyimapiprop)\= **HrOpenSiteContainerAddressing\( *session* ** \)
Retrieves a MAPI[PyIMAPIProp](#pyimapiprop)object for a site-addressing object\.

#### Parameters


  -  *session* :[PyIMAPISession](#pyimapisession)

    The MAPI session object

## OPENSTORE\_HOME\_LOGON
 **const exchange\.OPENSTORE\_HOME\_LOGON;** 


## OPENSTORE\_OVERRIDE\_HOME\_MDB
 **const exchange\.OPENSTORE\_OVERRIDE\_HOME\_MDB;** 


## OPENSTORE\_PUBLIC
 **const exchange\.OPENSTORE\_PUBLIC;** 


## OPENSTORE\_TAKE\_OWNERSHIP
 **const exchange\.OPENSTORE\_TAKE\_OWNERSHIP;** 


## OPENSTORE\_USE\_ADMIN\_PRIVILEGE
 **const exchange\.OPENSTORE\_USE\_ADMIN\_PRIVILEGE;** 
