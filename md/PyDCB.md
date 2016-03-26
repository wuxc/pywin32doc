# PyDCB


## PyDCB Object

A Python object, representing an DCB structure

#### Comments

Typically you query a device for its DCB using 

[win32file::GetCommState](win32file.md#win32filegetcommstate), change any setting necessary, then 

call [win32file::SetCommState](win32file.md#win32filesetcommstate) with the new structure\. 

TRUE\*/\)

#### Properties

  - integer BaudRate

    current baud rate

  - integer wReserved

    not currently used

  - integer XonLim

    transmit XON threshold

  - integer XoffLim

    transmit XOFF threshold

  - integer ByteSize

    number of bits/byte, 4-8

  - integer Parity

    0-4=no,odd,even,mark,space

  - integer StopBits

    0,1,2 = 1, 1\.5, 2

  - character XonChar

    Tx and Rx XON character

  - character XoffChar

    Tx and Rx XOFF character

  - character ErrorChar

    error replacement character

  - character EofChar

    end of input character

  - character EvtChar

    received event character

  - integer wReserved1

    reserved; do not use

  - integer fBinary

    binary mode, no EOF check

  - integer fParity

    enable parity checking

  - integer fOutxCtsFlow

    CTS output flow control

  - integer fOutxDsrFlow

    DSR output flow control

  - integer fDtrControl

    DTR flow control type

  - integer fDsrSensitivity

    DSR sensitivity

  - integer fTXContinueOnXoff

    XOFF continues Tx

  - integer fOutX

    XON/XOFF out flow control

  - integer fInX

    XON/XOFF in flow control

  - integer fErrorChar

    enable error replacement

  - integer fNull

    enable null stripping

  - integer fRtsControl

    RTS flow control

  - integer fAbortOnError

    abort on error

  - integer fDummy2

    reserved