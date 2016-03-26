# PyIMAPIStatus


## PyIMAPIStatus Object

Provides status information about the MAPI 

subsystem, the integrated address book and the MAPI 

spooler\. 

Derived from [PyIMAPIProp](PyIMAPIProp.md)

#### Methods

  - [ChangePassword](PyIMAPIStatus.md#pyimapistatuschangepassword)

    &nbsp;

  - [SettingsDialog](PyIMAPIStatus.md#pyimapistatussettingsdialog)

    &nbsp;

  - [ValidateState](PyIMAPIStatus.md#pyimapistatusvalidatestate)

    &nbsp;

  - [FlushQueues](PyIMAPIStatus.md#pyimapistatusflushqueues)

    &nbsp;

  - [FlushQueues](PyIMAPIStatus.md#pyimapistatusflushqueues)

    &nbsp;


## [PyIMAPIStatus](PyIMAPIStatus.md#pyimapistatus)\.ChangePassword

ChangePassword\(oldPassword, newPassword, ulFlags\)

#### Parameters

  - oldPassword : unicode

    

  - newPassword : unicode

    

  - ulFlags : int

    


## [PyIMAPIStatus](PyIMAPIStatus.md#pyimapistatus)\.FlushQueues

FlushQueues\(ulUIParam, transport, ulFlags\)

#### Parameters

  - ulUIParam : int

    

  - transport : string

    Blob of data

  - ulFlags : int

    


## [PyIMAPIStatus](PyIMAPIStatus.md#pyimapistatus)\.FlushQueues

FlushQueues\(uiparam, entryID, flags\)

#### Parameters

  - uiparam : int

    

  - entryID : string

    A blob

  - flags : int

    


## [PyIMAPIStatus](PyIMAPIStatus.md#pyimapistatus)\.SettingsDialog

SettingsDialog\(ulUIParam, ulFlags\)

#### Parameters

  - ulUIParam : int

    

  - ulFlags : int

    


## [PyIMAPIStatus](PyIMAPIStatus.md#pyimapistatus)\.ValidateState

ValidateState\(ulUIParam, ulFlags\)

#### Parameters

  - ulUIParam : int

    

  - ulFlags : int

    