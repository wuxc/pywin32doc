# PyCOMSTAT

## PyCOMSTAT Object

A Python object, representing an COMSTAT structure

#### Properties

  -  __integer cbInQue__ 
    Specifies the number of bytes received by the serial provider but not yet read by a[win32file::ReadFile](win32file.md#win32filereadfile)operation

  -  __integer cbOutQue__ 
    Specifies the number of bytes of user data remaining to be transmitted for all write operations. This value will be zero for a nonoverlapped write.

  -  __integer fCtsHold__ 
    Specifies whether transmission is waiting for the CTS (clear-to-send) signal to be sent. If this member is TRUE, transmission is waiting.

  -  __integer fDsrHold__ 
    Specifies whether transmission is waiting for the DSR (data-set-ready) signal to be sent. If this member is TRUE, transmission is waiting.

  -  __integer fRlsdHold__ 
    Specifies whether transmission is waiting for the RLSD (receive-line-signal-detect) signal to be sent. If this member is TRUE, transmission is waiting.

  -  __integer fXoffHold__ 
    Specifies whether transmission is waiting because the XOFF character was received. If this member is TRUE, transmission is waiting.

  -  __integer fXoffSent__ 
    Specifies whether transmission is waiting because the XOFF character was transmitted. If this member is TRUE, transmission is waiting. Transmission halts when the XOFF character is transmitted to a system that takes the next character as XON, regardless of the actual character.

  -  __integer fEof__ 
    Specifies whether the end-of-file (EOF) character has been received. If this member is TRUE, the EOF character has been received.

  -  __integer fTxim__ 
    If this member is TRUE, there is a character queued for transmission that has come to the communications device by way of the TransmitCommChar function. The communications device transmits such a character ahead of other characters in the device's output buffer.

  -  __integer fReserved__ 
    Reserved; do not use.