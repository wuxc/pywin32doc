# RASDIALPARAMS


## RASDIALPARAMS Object

A tuple that describes a Win32 RASDIALPARAMS structure

#### Comments

When used as a parameter, RASDIALPARAMS must be a sequence, of up to 

6 items long\.  All items must be strings - None is not allowed\. 

When this is returned from a RAS function, all six fields will exist\. 

RAS will often accept an empty string to mean "default" - ie, passing 

an empty string to phoneNumber uses the stored phone number\.

#### Items

  - \[0\] string : entryName

    name of RAS entry\.

  - \[1\] string : phoneNumber

    phone number to be used\.

  - \[2\] string : callBackNumber

    phone number to be used if callback is enabled\.

  - \[3\] string : userName

    username to log on with\.

  - \[4\] string : password

    password to use

  - \[5\] string : domain

    Network domain to log on to\.

#### Example
An example with win32ras\.Dial