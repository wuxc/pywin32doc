# PyCWinThread

## PyCWinThread Object



An application class\.  Encapsulates an MFCCWinThread



 class

#### Methods


  - [CreateThread](PyCWinThread.md#pycwinthreadcreatethread)

    Creates the actual thread behind the thread object\.&nbsp;

  - [PumpIdle](PyCWinThread.md#pycwinthreadpumpidle)

    Pumps idle messages\.&nbsp;

  - [PumpMessages](PyCWinThread.md#pycwinthreadpumpmessages)

    Pumps all messages to the application until a WM\_QUIT message is received\.&nbsp;

  - [Run](PyCWinThread.md#pycwinthreadrun)

    Starts the main application message pump\.&nbsp;

  - [SetMainFrame](PyCWinThread.md#pycwinthreadsetmainframe)

    Sets the C\+\+ applications main frame&nbsp;

  - [SetThreadPriority](PyCWinThread.md#pycwinthreadsetthreadpriority)

    Sets the threads priority&nbsp;

## [PyCWinThread](#pycwinthread)\.CreateThread

CreateThread\(\)
Creates the actual thread behind the thread object\.

## [PyCWinThread](#pycwinthread)\.PumpIdle

PumpIdle\(\)
Pumps all idle messages\.

## [PyCWinThread](#pycwinthread)\.PumpMessages

PumpMessages\(\)
Pumps all messages to the application until a WM\_QUIT message is received\.

#### Comments


This allows an application which is performing a long operation to dispatch paint messages during the operation\.

## [PyCWinThread](#pycwinthread)\.Run



int =Run\(\)
Starts the message pump\.  Advanced users only

## [PyCWinThread](#pycwinthread)\.SetMainFrame

SetMainFrame\(mainFrame\)
Sets the threads main frame

#### Parameters


  - mainFrame :[PyCWnd](#pycwnd)

    The applications main frame\.

#### Comments


You can pass None to this function to reset the main frame\. 

Should I free this?  I dont think so\!

## [PyCWinThread](#pycwinthread)\.SetThreadPriority

SetThreadPriority\(priority\)
Sets the threads priority\.  Returns TRUE if successful\.

#### Parameters


  - priority :[PyCWnd](#pycwnd)

    The threads priority\.