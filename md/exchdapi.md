# exchdapi

## Module exchdapi

An COM interface to Exchange's DAPI

#### Methods


  - [HrInstallService](exchdapi.md#exchdapihrinstallservice)

    &nbsp;

  - [HrInstallMailboxAgent](exchdapi.md#exchdapihrinstallmailboxagent)

    &nbsp;

  - [HrCreateMailboxAgentProfile](exchdapi.md#exchdapihrcreatemailboxagentprofile)

    &nbsp;

  - [HrCreateGatewayProfile](exchdapi.md#exchdapihrcreategatewayprofile)

    &nbsp;

  - [HrMailboxAgentExists](exchdapi.md#exchdapihrmailboxagentexists)

    &nbsp;

  - [HrAdminProgramExists](exchdapi.md#exchdapihradminprogramexists)

    &nbsp;

  - [HrRemoveMailboxAgent](exchdapi.md#exchdapihrremovemailboxagent)

    Removes a Mailbox Agent&nbsp;

  - [HrRemoveProfile](exchdapi.md#exchdapihrremoveprofile)

    Removes a profile&nbsp;

  - [HrEnumOrganizations](exchdapi.md#exchdapihrenumorganizations)

    Lists the names of the organizations on the server\.&nbsp;

  - [HrEnumSites](exchdapi.md#exchdapihrenumsites)

    Lists the names of the sites in an organization\.&nbsp;

  - [HrEnumContainers](exchdapi.md#exchdapihrenumcontainers)

    Lists the names of the containers on the server&nbsp;

  - [HrEnumSiteAdmins](exchdapi.md#exchdapihrenumsiteadmins)

    Lists the administrators for a site\.&nbsp;

  - [HrGetServiceAccountName](exchdapi.md#exchdapihrgetserviceaccountname)

    Obtains the account name for a service\.&nbsp;

## [exchdapi](#exchdapi)\.HrAdminProgramExists

 **HrAdminProgramExists\(** \)


## [exchdapi](#exchdapi)\.HrCreateGatewayProfile

 **HrCreateGatewayProfile\( *serviceName*  *, profile* ** \)


#### Parameters


  -  *serviceName* : string

    The name of the service\.

  -  *profile* : string

    The profile\.

## [exchdapi](#exchdapi)\.HrCreateMailboxAgentProfile

 **HrCreateMailboxAgentProfile\( *serviceName*  *, profile* ** \)


#### Parameters


  -  *serviceName* : string

    The name of the service\.

  -  *profile* : string

    The profile\.

## [exchdapi](#exchdapi)\.HrEnumContainers

\[string, \.\.\.\] \= **HrEnumContainers\( *server*  *, siteDN*  *, fSubtree* ** \)
Lists the names of the containers on the server

#### Parameters


  -  *server* : string

    The name of the server

  -  *siteDN* : string

    Distinguished name \(DN\) of the site\.

  -  *fSubtree* : int

    

## [exchdapi](#exchdapi)\.HrEnumOrganizations

\[string, \.\.\.\] \= **HrEnumOrganizations\( *rootDN*  *, server* ** \)
Lists the names of the organizations on the server\.

#### Parameters


  -  *rootDN* : string

    Contains the distinguished name \(DN\) of the directory information tree \(DIT\) root\.

  -  *server* : string

    The name of the server

## [exchdapi](#exchdapi)\.HrEnumSiteAdmins

\[string, \.\.\.\] \= **HrEnumSiteAdmins\( *server*  *, siteDN* ** \)
Lists the administrators for a site\.

#### Parameters


  -  *server* : string

    The name of the server

  -  *siteDN* : string

    Distinguished name \(DN\) of the site\.

## [exchdapi](#exchdapi)\.HrEnumSites

\[string, \.\.\.\] \= **HrEnumSites\( *server*  *, organizationDN* ** \)
Lists the names of the sites in an organization\.

#### Parameters


  -  *server* : string

    The name of the server

  -  *organizationDN* : string

    Contains the distinguished name \(DN\) of the organization\.

## [exchdapi](#exchdapi)\.HrGetServiceAccountName

string \= **HrGetServiceAccountName\( *serviceName*  *, serviceName* ** \)
Obtains the account name for a service\.

#### Parameters


  -  *serviceName* : string

    The name of the service

  -  *serviceName* : string

    The name of the service

## [exchdapi](#exchdapi)\.HrInstallMailboxAgent

 **HrInstallMailboxAgent\(** \)


## [exchdapi](#exchdapi)\.HrInstallService

 **HrInstallService\(** \)


## [exchdapi](#exchdapi)\.HrMailboxAgentExists

 **HrMailboxAgentExists\( *server*  *, siteDN*  *, rdn* ** \)


#### Parameters


  -  *server* : string

    The name of the server

  -  *siteDN* : string

    Contains the distinguished name \(DN\) of the site\.

  -  *rdn* : string

    RDN of the site where the mailbox agent might exist\.

## [exchdapi](#exchdapi)\.HrRemoveMailboxAgent

 **HrRemoveMailboxAgent\( *server*  *, siteDN*  *, rdn* ** \)
Removes a Mailbox Agent

#### Parameters


  -  *server* : string

    The name of the server

  -  *siteDN* : string

    Contains the distinguished name \(DN\) of the site\.

  -  *rdn* : string

    RDN of the site where the mailbox agent exists\.

## [exchdapi](#exchdapi)\.HrRemoveProfile

 **HrRemoveProfile\( *profile* ** \)
Removes a profile

#### Parameters


  -  *profile* : string

    The profile to delete\.