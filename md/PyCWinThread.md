# PyCWinThread

## PyCWinThread Object

An application class.  Encapsulates an MFC __CWinThread__ class

#### Methods


  - [CreateThread](PyCWinThread.md#pycwinthreadcreatethread)

    Creates the actual thread behind the thread object.&nbsp;

  - [PumpIdle](PyCWinThread.md#pycwinthreadpumpidle)

    Pumps idle messages.&nbsp;

  - [PumpMessages](PyCWinThread.md#pycwinthreadpumpmessages)

    Pumps all messages to the application until a WM_QUIT message is received.&nbsp;

  - [Run](PyCWinThread.md#pycwinthreadrun)

    Starts the main application message pump.&nbsp;

  - [SetMainFrame](PyCWinThread.md#pycwinthreadsetmainframe)

    Sets the C++ applications main frame&nbsp;

  - [SetThreadPriority](PyCWinThread.md#pycwinthreadsetthreadpriority)

    Sets the threads priority&nbsp;

## [PyCWinThread](#pycwinthread).CreateThread

 __CreateThread(__ )
Creates the actual thread behind the thread object.

## [PyCWinThread](#pycwinthread).PumpIdle

 __PumpIdle(__ )
Pumps all idle messages.

## [PyCWinThread](#pycwinthread).PumpMessages

 __PumpMessages(__ )
Pumps all messages to the application until a WM_QUIT message is received.

#### Comments
This allows an application which is performing a long operation to dispatch paint messages during the operation.

## [PyCWinThread](#pycwinthread).Run

int = __Run(__ )
Starts the message pump.  Advanced users only

## [PyCWinThread](#pycwinthread).SetMainFrame

 __SetMainFrame( *mainFrame* __ )
Sets the threads main frame

#### Parameters


  -  *mainFrame* :[PyCWnd](#pycwnd)

    The applications main frame.

#### Comments
You can pass None to this function to reset the main frame. 

Should I free this?  I dont think so!

## [PyCWinThread](#pycwinthread).SetThreadPriority

 __SetThreadPriority( *priority* __ )
Sets the threads priority.  Returns TRUE if successful.

#### Parameters


  -  *priority* :[PyCWnd](#pycwnd)

    The threads priority.