# PyDCB

## PyDCB Object

A Python object, representing an DCB structure

#### Comments
Typically you query a device for its DCB using[win32file::GetCommState](win32file.md#win32filegetcommstate), change any setting necessary, then 

call[win32file::SetCommState](win32file.md#win32filesetcommstate)with the new structure. 

TRUE*/)

#### Properties

  -  __integer BaudRate__ 
    current baud rate

  -  __integer wReserved__ 
    not currently used

  -  __integer XonLim__ 
    transmit XON threshold

  -  __integer XoffLim__ 
    transmit XOFF threshold

  -  __integer ByteSize__ 
    number of bits/byte, 4-8

  -  __integer Parity__ 
    0-4=no,odd,even,mark,space

  -  __integer StopBits__ 
    0,1,2 = 1, 1.5, 2

  -  __character XonChar__ 
    Tx and Rx XON character

  -  __character XoffChar__ 
    Tx and Rx XOFF character

  -  __character ErrorChar__ 
    error replacement character

  -  __character EofChar__ 
    end of input character

  -  __character EvtChar__ 
    received event character

  -  __integer wReserved1__ 
    reserved; do not use

  -  __integer fBinary__ 
    binary mode, no EOF check

  -  __integer fParity__ 
    enable parity checking

  -  __integer fOutxCtsFlow__ 
    CTS output flow control

  -  __integer fOutxDsrFlow__ 
    DSR output flow control

  -  __integer fDtrControl__ 
    DTR flow control type

  -  __integer fDsrSensitivity__ 
    DSR sensitivity

  -  __integer fTXContinueOnXoff__ 
    XOFF continues Tx

  -  __integer fOutX__ 
    XON/XOFF out flow control

  -  __integer fInX__ 
    XON/XOFF in flow control

  -  __integer fErrorChar__ 
    enable error replacement

  -  __integer fNull__ 
    enable null stripping

  -  __integer fRtsControl__ 
    RTS flow control

  -  __integer fAbortOnError__ 
    abort on error

  -  __integer fDummy2__ 
    reserved