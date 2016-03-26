# PyCOMSTAT

## PyCOMSTAT Object

A Python object, representing an COMSTAT structure

#### Properties

  -  **integer cbInQue** 
    Specifies the number of bytes received by the serial provider but not yet read by a[win32file::ReadFile](win32file.md#win32filereadfile)operation

  -  **integer cbOutQue** 
    Specifies the number of bytes of user data remaining to be transmitted for all write operations\. This value will be zero for a nonoverlapped write\.

  -  **integer fCtsHold** 
    Specifies whether transmission is waiting for the CTS \(clear-to-send\) signal to be sent\. If this member is TRUE, transmission is waiting\.

  -  **integer fDsrHold** 
    Specifies whether transmission is waiting for the DSR \(data-set-ready\) signal to be sent\. If this member is TRUE, transmission is waiting\.

  -  **integer fRlsdHold** 
    Specifies whether transmission is waiting for the RLSD \(receive-line-signal-detect\) signal to be sent\. If this member is TRUE, transmission is waiting\.

  -  **integer fXoffHold** 
    Specifies whether transmission is waiting because the XOFF character was received\. If this member is TRUE, transmission is waiting\.

  -  **integer fXoffSent** 
    Specifies whether transmission is waiting because the XOFF character was transmitted\. If this member is TRUE, transmission is waiting\. Transmission halts when the XOFF character is transmitted to a system that takes the next character as XON, regardless of the actual character\.

  -  **integer fEof** 
    Specifies whether the end-of-file \(EOF\) character has been received\. If this member is TRUE, the EOF character has been received\.

  -  **integer fTxim** 
    If this member is TRUE, there is a character queued for transmission that has come to the communications device by way of the TransmitCommChar function\. The communications device transmits such a character ahead of other characters in the device's output buffer\.

  -  **integer fReserved** 
    Reserved; do not use\.