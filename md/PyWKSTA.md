# PyWKSTA

## PyWKSTA\_INFO\_\* Object



The following WKSTA\_INFO levels are supported\.


## PyWKSTA\_INFO\_100 Object



A dictionary holding the infomation in a Win32 WKSTA\_INFO\_100 structure\.

#### Properties

  - int platform\_id
    Indicates platform level to use to retrieve platform specific information

  - string/[PyUnicode](#pyunicode) computername
    Name of the local computer

  - string/[PyUnicode](#pyunicode) langroup
    Name of the domain to which computer belongs

  - int ver\_major
    Major version number of operating system running on the computer

  - int ver\_minor
    Minor version number of operating system running on the computer

## PyWKSTA\_INFO\_101 Object



A dictionary holding the infomation in a Win32 WKSTA\_INFO\_101 structure\.

#### Properties

  - int platform\_id
    Indicates platform level to use to retrieve platform specific information

  - string/[PyUnicode](#pyunicode) computername
    Name of the local computer

  - string/[PyUnicode](#pyunicode) langroup
    Name of the domain to which computer belongs

  - int ver\_major
    Major version number of operating system running on the computer

  - int ver\_minor
    Minor version number of operating system running on the computer

  - string/[PyUnicode](#pyunicode) lanroot
    Path to the LANMAN directory

## PyWKSTA\_INFO\_102 Object



A dictionary holding the infomation in a Win32 WKSTA\_INFO\_102 structure\.

#### Properties

  - int platform\_id
    Indicate platform level to use to retrieve platform specific information

  - string/[PyUnicode](#pyunicode) computername
    Name of the local computer

  - string/[PyUnicode](#pyunicode) langroup
    Name of the domain to which computer belongs

  - int ver\_major
    Major version number of operating system running on the computer

  - int ver\_minor
    Minor version number of operating system running on the computer

  - string/[PyUnicode](#pyunicode) lanroot
    Path to the LANMAN directory

  - int logged\_on\_users
    Number of users who are logged on to the local computer

## PyWKSTA\_INFO\_302 Object



A dictionary holding the infomation in a Win32 WKSTA\_INFO\_302 structure\.

#### Properties

  - int char\_wait
    number of seconds the computer will wait for a remote resource to become available

  - int collection\_time
    number of milliseconds the computer will collect data before sending the data to a character device resource\. The workstation waits the specified time or collects the number of characters specified by wki302\_maximum\_collection\_count, whichever comes first\.

  - int maximum\_collection\_count
    Specifies the number of bytes of information the computer will collect before sending the data to a character device resource\. The workstation collects the specified number of bytes or waits the time specified by wki302\_collection\_time, whichever comes first\.

  - int keep\_conn
    Specifies the 

number of seconds the server will 

maintain an inactive connection 

to a resource\.

  - int keep\_search
    Defines 

the number of seconds an 

inactive search will continue\.

  - int max\_cmds
    Specifies the number of simultaneous network device driver commands that can be sent to the network\.

  - int num\_work\_buf
    Specifies the number of internal buffers the computer has\.

  - int siz\_work\_buf
    Specifies the size, in bytes, of each internal buffer\.

  - int max\_wrk\_cache
    Specifies the maximum size, in bytes, of an internal cache buffer\.

  - int max\_wrk\_cache
    Indicates the number of seconds the server waits before disconnecting an inactive session\.

  - int siz\_error
    Specifies the size, in bytes, of an internal error buffer\.

  - int num\_alerts
    Specifies the maximum number of clients that can receive alert messages\. \(This member is not supported under MS-DOS\.\) The Alerter service registers at least three clients when it begins to run\.

  - int num\_services
    Specifies the number of services that can be installed on the computer at any time\.

  - int errlog\_sz
    Specifies the maximum size, in kilobytes, of the client's error log file\.

  - int print\_buf\_time
    Specifies the number of seconds the server waits before closing inactive compatibility-mode print jobs\.

  - int num\_char\_buf
    Specifies the number of character pipe buffers and device buffers the client can have\.

  - int siz\_char\_buf
    Specifies the maximum size, in bytes, of a character pipe buffer and device buffer\.

  - string/[PyUnicode](#pyunicode) wrk\_heuristics
    Pointer to a Unicode string of flags used to control a client's operation\.

  - int mailslots
    Specifies the maximum number of mailslots allowed\.

  - int num\_dgram\_buf
    Specifies the number of buffers to allocate for receiving datagrams\.

## PyWKSTA\_INFO\_402 Object



A dictionary holding the infomation in a Win32 WKSTA\_INFO\_402 structure\.

#### Properties

  - int char\_wait
    number of seconds the computer will wait for a remote resource to become available

  - int collection\_time
    number of milliseconds the computer will collect data before sending the data to a character device resource\. The workstation waits the specified time or collects the number of characters specified by wki402\_maximum\_collection\_count, whichever comes first\.

  - string/[PyUnicode](#pyunicode) maximum\_collection\_count
    Name of the domain to which computer belongs

  - int keep\_conn
    Major version number of operating system running on the computer

  - int keep\_search
    Minor version number of operating system running on the computer

  - int max\_cmds
    \.\.

  - int num\_work\_buf
    Number of users who are logged on to the local computer

  - int siz\_work\_buf
    Number of users who are logged on to the local computer

  - int max\_wrk\_cache
    \.\.

  - int sess\_timeout
    \.\.

  - int siz\_error
    \.\.

  - int num\_alerts
    \.\.

  - int num\_services
    \.\.

  - int errlog\_sz
    \.\.

  - int print\_buf\_time
    \.\.

  - int num\_char\_buf
    \.\.

  - int siz\_char\_buf
    Specifies the maximum size, in bytes, of a character pipe buffer and device buffer\.

  - string/[PyUnicode](#pyunicode) siz\_char\_buf
    \.\.

  - int mailslots
    \.\.

  - int num\_dgram\_buf
    \.\.

  - int max\_threads
    Number of threads the computer can dedicate to the network

## PyWKSTA\_INFO\_502 Object



A dictionary holding the infomation in a Win32 WKSTA\_INFO\_502 structure\.

#### Properties

  - int char\_wait
    number of seconds the computer will wait for a remote resource to become available

  - int collection\_time
    number of milliseconds the computer will collect data before sending the data to a character device resource\. The workstation waits the specified time or collects the number of characters specified by wki502\_maximum\_collection\_count, whichever comes first\.

  - int maximum\_collection\_count
    Specifies the number of bytes of information the computer will collect before sending the data to a character device resource\. The workstation collects the specified number of bytes or waits the time specified by wki302\_collection\_time, whichever comes first\.

  - int keep\_conn
    Specifies the 

number of seconds the server will 

maintain an inactive connection 

to a resource\.

  - int max\_cmds
    Specifies the number of simultaneous network device driver commands that can be sent to the network\.

  - int max\_wrk\_cache
    Indicates the number of seconds the server waits before disconnecting an inactive session\.

  - int siz\_char\_buf
    Specifies the maximum size, in bytes, of a character pipe buffer and device buffer\.

  - int lock\_quota
    TODO

  - int lock\_increment
    TODO

  - int lock\_maximum
    TODO

  - int pipe\_increment
    TODO

  - int pipe\_maximum
    TODO

  - int cache\_file\_timeout
    TODO

  - int dormant\_file\_limit
    TODO

  - int read\_ahead\_throughput
    TODO

  - int num\_mailslot\_buffers
    TODO

  - int num\_srv\_announce\_buffers
    TODO

  - int max\_illegal\_datagram\_events
    TODO

  - int illegal\_datagram\_event\_reset\_frequency
    TODO

  - bool log\_election\_packets
    TODO

  - bool use\_opportunistic\_locking
    TODO

  - bool use\_unlock\_behind
    TODO

  - bool use\_close\_behind
    TODO

  - bool buf\_named\_pipes
    TODO

  - bool use\_lock\_read\_unlock
    TODO

  - bool utilize\_nt\_caching
    TODO

  - bool use\_raw\_read
    TODO

  - bool use\_raw\_write
    TODO

  - bool use\_write\_raw\_data
    TODO

  - bool use\_encryption
    TODO

  - bool buf\_files\_deny\_write
    TODO

  - bool buf\_read\_only\_files
    TODO

  - bool force\_core\_create\_mode
    TODO

  - bool use\_512\_byte\_max\_transfer
    TODO

## PyWKSTA\_TRANSPORT\_INFO\_\* Object



The following WKSTA\_TRANSPORT\_INFO levels are supported\.


## PyWKSTA\_TRANSPORT\_INFO\_0 Object



A dictionary holding the infomation in a Win32 WKSTA\_TRANSPORT\_INFO\_0 structure\.

#### Properties

  - int quality\_of\_service
    Supplies a value that specifies the search order of the transport protocol with respect to other transport protocols\. The highest value is searched first\.

  - int number\_of\_vcs
    Specifies the number of clients communicating with the server using this transport protocol\.

  - string/[PyUnicode](#pyunicode) transport\_name
    Specifies the device name of the transport protocol\.

  - string/[PyUnicode](#pyunicode) transport\_address
    Specifies the address of the server on this transport protocol\.

  - bool wan\_ish
    This member is ignored by the NetWkstaTransportAdd function\. For the NetWkstaTransportEnum function, this member indicates that this transport protocol is a WAN transport protocol\. This member is set TRUE for NetBIOS/TCIP; it is set FALSE for NetBEUI and NetBIOS/IPX\.

## PyWKSTA\_USER\_INFO\_\* Object



The following WKSTA\_USER\_INFO levels are supported\.


## PyWKSTA\_USER\_INFO\_0 Object



A dictionary holding the infomation in a Win32 WKSTA\_USER\_INFO\_0 structure\.

#### Properties

  - string/[PyUnicode](#pyunicode) username
    Name of user currently logged on to the workstation

## PyWKSTA\_USER\_INFO\_1 Object



A dictionary holding the infomation in a Win32 WKSTA\_USER\_INFO\_1 structure\.

#### Properties

  - string/[PyUnicode](#pyunicode) username
    Name of user currently logged on to the workstation

  - string/[PyUnicode](#pyunicode) logon\_domain
    Returns the domain name of the user account of the user currently logged on to the workstation\.

  - string/[PyUnicode](#pyunicode) oth\_domains
    Returns the list of other operating system domains browsed by the workstation\. The domain names are separated by blanks\.

  - string/[PyUnicode](#pyunicode) logon\_server
    Returns the name of the computer that authenticated the server\.