# PySERVER

## PySERVER\_INFO\_\* Object

The following SERVER\_INFO levels are supported\.


## PySERVER\_INFO\_100 Object

A dictionary holding the information in a Win32 SERVER\_INFO\_100 structure\.

#### Properties

  -  **int platform\_id** 
    

  -  **string/[PyUnicode](#pyunicode)name** 
    

## PySERVER\_INFO\_101 Object

A dictionary holding the information in a Win32 SERVER\_INFO\_101 structure\.

#### Properties

  -  **int platform\_id** 
    

  -  **string/[PyUnicode](#pyunicode)name** 
    

  -  **int version\_major** 
    

  -  **int version\_minor** 
    

  -  **int type** 
    one of the SV\_TYPE\_\* constants

  -  **string/[PyUnicode](#pyunicode)comment** 
    

## PySERVER\_INFO\_102 Object

A dictionary holding the information in a Win32 SERVER\_INFO\_102 structure\.

#### Properties

  -  **int platform\_id** 
    

  -  **string/[PyUnicode](#pyunicode)name** 
    

  -  **int version\_major** 
    

  -  **int version\_minor** 
    

  -  **int type** 
    one of the SV\_TYPE\_\* constants

  -  **string/[PyUnicode](#pyunicode)comment** 
    

  -  **int users** 
    

  -  **int disc** 
    

  -  **bool hidden** 
    

  -  **int announce** 
    

  -  **int anndelta** 
    

  -  **string/[PyUnicode](#pyunicode)userpath** 
    

## PySERVER\_INFO\_402 Object

A dictionary holding the information in a Win32 SERVER\_INFO\_402 structure\.

#### Properties

  -  **int ulist\_mtime** 
    

  -  **int glist\_mtime** 
    

  -  **int alist\_mtime** 
    

  -  **int security** 
    

  -  **int numadmin** 
    

  -  **int lanmask** 
    

  -  **string/[PyUnicode](#pyunicode)guestacct** 
    

  -  **int chdevs** 
    

  -  **int chdevq** 
    

  -  **int chdevjobs** 
    

  -  **int connections** 
    

  -  **int shares** 
    

  -  **int openfiles** 
    

  -  **int sessopens** 
    

  -  **int sessvcs** 
    

  -  **int sessreqs** 
    

  -  **int opensearch** 
    

  -  **int activelocks** 
    

  -  **int numreqbuf** 
    

  -  **int sizreqbuf** 
    

  -  **int numbigbuf** 
    

  -  **int numfiletasks** 
    

  -  **int alertsched** 
    

  -  **int erroralert** 
    

  -  **int logonalert** 
    

  -  **int accessalert** 
    

  -  **int diskalert** 
    

  -  **int netioalert** 
    

  -  **int maxauditsz** 
    

  -  **string/[PyUnicode](#pyunicode)srvheuristics** 
    

## PySERVER\_INFO\_403 Object

A dictionary holding the information in a Win32 SERVER\_INFO\_403 structure\.

#### Properties

  -  **int ulist\_mtime** 
    

  -  **int glist\_mtime** 
    

  -  **int alist\_mtime** 
    

  -  **int security** 
    

  -  **int numadmin** 
    

  -  **int lanmask** 
    

  -  **string/[PyUnicode](#pyunicode)guestacct** 
    

  -  **int chdevs** 
    

  -  **int chdevq** 
    

  -  **int chdevjobs** 
    

  -  **int connections** 
    

  -  **int shares** 
    

  -  **int openfiles** 
    

  -  **int sessopens** 
    

  -  **int sessvcs** 
    

  -  **int sessreqs** 
    

  -  **int opensearch** 
    

  -  **int activelocks** 
    

  -  **int numreqbuf** 
    

  -  **int sizreqbuf** 
    

  -  **int numbigbuf** 
    

  -  **int numfiletasks** 
    

  -  **int alertsched** 
    

  -  **int erroralert** 
    

  -  **int logonalert** 
    

  -  **int accessalert** 
    

  -  **int diskalert** 
    

  -  **int netioalert** 
    

  -  **int maxauditsz** 
    

  -  **string/[PyUnicode](#pyunicode)srvheuristics** 
    

  -  **int auditedevents** 
    

  -  **int autoprofile** 
    

  -  **string/[PyUnicode](#pyunicode)autopath** 
    

## PySERVER\_INFO\_502 Object

A dictionary holding the information in a Win32 SERVER\_INFO\_502 structure\.

#### Properties

  -  **int sessopens** 
    

  -  **int sessvcs** 
    

  -  **int opensearch** 
    

  -  **int sizreqbuf** 
    

  -  **int initworkitems** 
    

  -  **int maxworkitems** 
    

  -  **int rawworkitems** 
    

  -  **int irpstacksize** 
    

  -  **int maxrawbuflen** 
    

  -  **int sessusers** 
    

  -  **int sessconns** 
    

  -  **int maxpagedmemoryusage** 
    

  -  **int maxnonpagedmemoryusage** 
    

  -  **bool enableforcedlogoff** 
    

  -  **bool timesource** 
    

  -  **bool acceptdownlevelapis** 
    

  -  **bool lmannounce** 
    

## PySERVER\_INFO\_503 Object

A dictionary holding the information in a Win32 SERVER\_INFO\_503 structure\.

#### Properties

  -  **int sessopens** 
    

  -  **int sessvcs** 
    

  -  **int opensearch** 
    

  -  **int sizreqbuf** 
    

  -  **int initworkitems** 
    

  -  **int maxworkitems** 
    

  -  **int rawworkitems** 
    

  -  **int irpstacksize** 
    

  -  **int maxrawbuflen** 
    

  -  **int sessusers** 
    

  -  **int sessconns** 
    

  -  **int maxpagedmemoryusage** 
    

  -  **int maxnonpagedmemoryusage** 
    

  -  **bool enableforcedlogoff** 
    

  -  **bool timesource** 
    

  -  **bool acceptdownlevelapis** 
    

  -  **bool lmannounce** 
    

  -  **string/[PyUnicode](#pyunicode)domain** 
    

  -  **int maxkeepsearch** 
    

  -  **int scavtimeout** 
    

  -  **int minrcvqueue** 
    

  -  **int minfreeworkitems** 
    

  -  **int xactmemsize** 
    

  -  **int threadpriority** 
    

  -  **int maxmpxct** 
    

  -  **int oplockbreakwait** 
    

  -  **int oplockbreakresponsewait** 
    

  -  **bool enableoplocks** 
    

  -  **bool enablefcbopens** 
    

  -  **bool enableraw** 
    

  -  **bool enablesharednetdrives** 
    

  -  **int minfreeconnections** 
    

  -  **int maxfreeconnections** 
    