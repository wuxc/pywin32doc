# PyWKSTA

## PyWKSTA_INFO_* Object

The following WKSTA_INFO levels are supported.


## PyWKSTA_INFO_100 Object

A dictionary holding the infomation in a Win32 WKSTA_INFO_100 structure.

#### Properties

  -  __int platform_id__ 
    Indicates platform level to use to retrieve platform specific information

  -  __string/[PyUnicode](#pyunicode)computername__ 
    Name of the local computer

  -  __string/[PyUnicode](#pyunicode)langroup__ 
    Name of the domain to which computer belongs

  -  __int ver_major__ 
    Major version number of operating system running on the computer

  -  __int ver_minor__ 
    Minor version number of operating system running on the computer

## PyWKSTA_INFO_101 Object

A dictionary holding the infomation in a Win32 WKSTA_INFO_101 structure.

#### Properties

  -  __int platform_id__ 
    Indicates platform level to use to retrieve platform specific information

  -  __string/[PyUnicode](#pyunicode)computername__ 
    Name of the local computer

  -  __string/[PyUnicode](#pyunicode)langroup__ 
    Name of the domain to which computer belongs

  -  __int ver_major__ 
    Major version number of operating system running on the computer

  -  __int ver_minor__ 
    Minor version number of operating system running on the computer

  -  __string/[PyUnicode](#pyunicode)lanroot__ 
    Path to the LANMAN directory

## PyWKSTA_INFO_102 Object

A dictionary holding the infomation in a Win32 WKSTA_INFO_102 structure.

#### Properties

  -  __int platform_id__ 
    Indicate platform level to use to retrieve platform specific information

  -  __string/[PyUnicode](#pyunicode)computername__ 
    Name of the local computer

  -  __string/[PyUnicode](#pyunicode)langroup__ 
    Name of the domain to which computer belongs

  -  __int ver_major__ 
    Major version number of operating system running on the computer

  -  __int ver_minor__ 
    Minor version number of operating system running on the computer

  -  __string/[PyUnicode](#pyunicode)lanroot__ 
    Path to the LANMAN directory

  -  __int logged_on_users__ 
    Number of users who are logged on to the local computer

## PyWKSTA_INFO_302 Object

A dictionary holding the infomation in a Win32 WKSTA_INFO_302 structure.

#### Properties

  -  __int char_wait__ 
    number of seconds the computer will wait for a remote resource to become available

  -  __int collection_time__ 
    number of milliseconds the computer will collect data before sending the data to a character device resource. The workstation waits the specified time or collects the number of characters specified by wki302_maximum_collection_count, whichever comes first.

  -  __int maximum_collection_count__ 
    Specifies the number of bytes of information the computer will collect before sending the data to a character device resource. The workstation collects the specified number of bytes or waits the time specified by wki302_collection_time, whichever comes first.

  -  __int keep_conn__ 
    Specifies the 

number of seconds the server will 

maintain an inactive connection 

to a resource.

  -  __int keep_search__ 
    Defines 

the number of seconds an 

inactive search will continue.

  -  __int max_cmds__ 
    Specifies the number of simultaneous network device driver commands that can be sent to the network.

  -  __int num_work_buf__ 
    Specifies the number of internal buffers the computer has.

  -  __int siz_work_buf__ 
    Specifies the size, in bytes, of each internal buffer.

  -  __int max_wrk_cache__ 
    Specifies the maximum size, in bytes, of an internal cache buffer.

  -  __int max_wrk_cache__ 
    Indicates the number of seconds the server waits before disconnecting an inactive session.

  -  __int siz_error__ 
    Specifies the size, in bytes, of an internal error buffer.

  -  __int num_alerts__ 
    Specifies the maximum number of clients that can receive alert messages. (This member is not supported under MS-DOS.) The Alerter service registers at least three clients when it begins to run.

  -  __int num_services__ 
    Specifies the number of services that can be installed on the computer at any time.

  -  __int errlog_sz__ 
    Specifies the maximum size, in kilobytes, of the client's error log file.

  -  __int print_buf_time__ 
    Specifies the number of seconds the server waits before closing inactive compatibility-mode print jobs.

  -  __int num_char_buf__ 
    Specifies the number of character pipe buffers and device buffers the client can have.

  -  __int siz_char_buf__ 
    Specifies the maximum size, in bytes, of a character pipe buffer and device buffer.

  -  __string/[PyUnicode](#pyunicode)wrk_heuristics__ 
    Pointer to a Unicode string of flags used to control a client's operation.

  -  __int mailslots__ 
    Specifies the maximum number of mailslots allowed.

  -  __int num_dgram_buf__ 
    Specifies the number of buffers to allocate for receiving datagrams.

## PyWKSTA_INFO_402 Object

A dictionary holding the infomation in a Win32 WKSTA_INFO_402 structure.

#### Properties

  -  __int char_wait__ 
    number of seconds the computer will wait for a remote resource to become available

  -  __int collection_time__ 
    number of milliseconds the computer will collect data before sending the data to a character device resource. The workstation waits the specified time or collects the number of characters specified by wki402_maximum_collection_count, whichever comes first.

  -  __string/[PyUnicode](#pyunicode)maximum_collection_count__ 
    Name of the domain to which computer belongs

  -  __int keep_conn__ 
    Major version number of operating system running on the computer

  -  __int keep_search__ 
    Minor version number of operating system running on the computer

  -  __int max_cmds__ 
    ..

  -  __int num_work_buf__ 
    Number of users who are logged on to the local computer

  -  __int siz_work_buf__ 
    Number of users who are logged on to the local computer

  -  __int max_wrk_cache__ 
    ..

  -  __int sess_timeout__ 
    ..

  -  __int siz_error__ 
    ..

  -  __int num_alerts__ 
    ..

  -  __int num_services__ 
    ..

  -  __int errlog_sz__ 
    ..

  -  __int print_buf_time__ 
    ..

  -  __int num_char_buf__ 
    ..

  -  __int siz_char_buf__ 
    Specifies the maximum size, in bytes, of a character pipe buffer and device buffer.

  -  __string/[PyUnicode](#pyunicode)siz_char_buf__ 
    ..

  -  __int mailslots__ 
    ..

  -  __int num_dgram_buf__ 
    ..

  -  __int max_threads__ 
    Number of threads the computer can dedicate to the network

## PyWKSTA_INFO_502 Object

A dictionary holding the infomation in a Win32 WKSTA_INFO_502 structure.

#### Properties

  -  __int char_wait__ 
    number of seconds the computer will wait for a remote resource to become available

  -  __int collection_time__ 
    number of milliseconds the computer will collect data before sending the data to a character device resource. The workstation waits the specified time or collects the number of characters specified by wki502_maximum_collection_count, whichever comes first.

  -  __int maximum_collection_count__ 
    Specifies the number of bytes of information the computer will collect before sending the data to a character device resource. The workstation collects the specified number of bytes or waits the time specified by wki302_collection_time, whichever comes first.

  -  __int keep_conn__ 
    Specifies the 

number of seconds the server will 

maintain an inactive connection 

to a resource.

  -  __int max_cmds__ 
    Specifies the number of simultaneous network device driver commands that can be sent to the network.

  -  __int max_wrk_cache__ 
    Indicates the number of seconds the server waits before disconnecting an inactive session.

  -  __int siz_char_buf__ 
    Specifies the maximum size, in bytes, of a character pipe buffer and device buffer.

  -  __int lock_quota__ 
    TODO

  -  __int lock_increment__ 
    TODO

  -  __int lock_maximum__ 
    TODO

  -  __int pipe_increment__ 
    TODO

  -  __int pipe_maximum__ 
    TODO

  -  __int cache_file_timeout__ 
    TODO

  -  __int dormant_file_limit__ 
    TODO

  -  __int read_ahead_throughput__ 
    TODO

  -  __int num_mailslot_buffers__ 
    TODO

  -  __int num_srv_announce_buffers__ 
    TODO

  -  __int max_illegal_datagram_events__ 
    TODO

  -  __int illegal_datagram_event_reset_frequency__ 
    TODO

  -  __bool log_election_packets__ 
    TODO

  -  __bool use_opportunistic_locking__ 
    TODO

  -  __bool use_unlock_behind__ 
    TODO

  -  __bool use_close_behind__ 
    TODO

  -  __bool buf_named_pipes__ 
    TODO

  -  __bool use_lock_read_unlock__ 
    TODO

  -  __bool utilize_nt_caching__ 
    TODO

  -  __bool use_raw_read__ 
    TODO

  -  __bool use_raw_write__ 
    TODO

  -  __bool use_write_raw_data__ 
    TODO

  -  __bool use_encryption__ 
    TODO

  -  __bool buf_files_deny_write__ 
    TODO

  -  __bool buf_read_only_files__ 
    TODO

  -  __bool force_core_create_mode__ 
    TODO

  -  __bool use_512_byte_max_transfer__ 
    TODO

## PyWKSTA_TRANSPORT_INFO_* Object

The following WKSTA_TRANSPORT_INFO levels are supported.


## PyWKSTA_TRANSPORT_INFO_0 Object

A dictionary holding the infomation in a Win32 WKSTA_TRANSPORT_INFO_0 structure.

#### Properties

  -  __int quality_of_service__ 
    Supplies a value that specifies the search order of the transport protocol with respect to other transport protocols. The highest value is searched first.

  -  __int number_of_vcs__ 
    Specifies the number of clients communicating with the server using this transport protocol.

  -  __string/[PyUnicode](#pyunicode)transport_name__ 
    Specifies the device name of the transport protocol.

  -  __string/[PyUnicode](#pyunicode)transport_address__ 
    Specifies the address of the server on this transport protocol.

  -  __bool wan_ish__ 
    This member is ignored by the NetWkstaTransportAdd function. For the NetWkstaTransportEnum function, this member indicates that this transport protocol is a WAN transport protocol. This member is set TRUE for NetBIOS/TCIP; it is set FALSE for NetBEUI and NetBIOS/IPX.

## PyWKSTA_USER_INFO_* Object

The following WKSTA_USER_INFO levels are supported.


## PyWKSTA_USER_INFO_0 Object

A dictionary holding the infomation in a Win32 WKSTA_USER_INFO_0 structure.

#### Properties

  -  __string/[PyUnicode](#pyunicode)username__ 
    Name of user currently logged on to the workstation

## PyWKSTA_USER_INFO_1 Object

A dictionary holding the infomation in a Win32 WKSTA_USER_INFO_1 structure.

#### Properties

  -  __string/[PyUnicode](#pyunicode)username__ 
    Name of user currently logged on to the workstation

  -  __string/[PyUnicode](#pyunicode)logon_domain__ 
    Returns the domain name of the user account of the user currently logged on to the workstation.

  -  __string/[PyUnicode](#pyunicode)oth_domains__ 
    Returns the list of other operating system domains browsed by the workstation. The domain names are separated by blanks.

  -  __string/[PyUnicode](#pyunicode)logon_server__ 
    Returns the name of the computer that authenticated the server.