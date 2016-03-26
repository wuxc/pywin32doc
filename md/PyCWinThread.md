# PyCWinThread


## PyCWinThread Object

An application class\.  Encapsulates an MFC CWinThread

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


## [PyCWinThread](PyCWinThread.md#pycwinthread)\.CreateThread

CreateThread\(\)
Creates the actual thread behind the thread object\.


## [PyCWinThread](PyCWinThread.md#pycwinthread)\.PumpIdle

PumpIdle\(\)
Pumps all idle messages\.


## [PyCWinThread](PyCWinThread.md#pycwinthread)\.PumpMessages

PumpMessages\(\)
Pumps all messages to the application until a WM\_QUIT message is received\.

#### Comments

This allows an application which is performing a long operation to dispatch paint messages during the operation\.


## [PyCWinThread](PyCWinThread.md#pycwinthread)\.Run

int = Run\(\)
Starts the message pump\.  Advanced users only


## [PyCWinThread](PyCWinThread.md#pycwinthread)\.SetMainFrame

SetMainFrame\(mainFrame\)
Sets the threads main frame

#### Parameters

  - mainFrame : [PyCWnd](PyCWnd.md)

    The applications main frame\.

#### Comments

You can pass None to this function to reset the main frame\. 

Should I free this?  I dont think so\!


## [PyCWinThread](PyCWinThread.md#pycwinthread)\.SetThreadPriority

SetThreadPriority\(priority\)
Sets the threads priority\.  Returns TRUE if successful\.

#### Parameters

  - priority : [PyCWnd](PyCWnd.md)

    The threads priority\.