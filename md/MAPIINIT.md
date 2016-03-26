# MAPIINIT


## MAPIINIT\_0 Object

A MAPIINIT\_0 is represented as a tuple of:

#### Items

  - \[0\] int : version

    This must be MAPI\_INIT\_VERSION\.

  - \[1\] int : flags

    MAPI initlization flags\.

   

       Value

   

   

       Meaning

   

MAPI\_MULTITHREAD\_NOTIFICATIONSMAPI should generate notifications using a thread dedicated to notification handling rather than the first thread used to call [mapi::MAPIInitialize](mapi.md#mapimapiinitialize)\.

MAPI\_NT\_SERVICEThe caller is running as a NT service\. Callers that are not running in a Windows NT service should not set this flag; callers that are running as a service must set this flag\.

#### Comments

Multithreaded clients should set MAPI\_MULTITHREAD\_NOTIFICATIONS flag so that they can receive notifications on threads other than the first thread to call [mapi::MAPIInitialize](mapi.md#mapimapiinitialize)\.