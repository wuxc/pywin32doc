# SERVICE

## SERVICE\_FAILURE\_ACTIONS Object

A dictionary representing a SERVICE\_FAILURE\_ACTIONS structure

#### Properties

  -  **int ResetPeriod** 
    Indicates how many seconds to wait to reset the failure count, can be INFINITE

  -  **str/[PyUnicode](#pyunicode)RebootMsg** 
    Message displayed when reboot action is taken

  -  **str/[PyUnicode](#pyunicode)Command** 
    Command line to execute for SC\_ACTION\_RUN\_COMMAND

  -  **tuple Actions** 
    A tuple of[SC\_ACTION](SC.md#scaction)tuples

## SERVICE\_STATUS Object

A Win32 service status object is represented by a tuple:

#### Items


  - \[0\] *int* : serviceType

    The type of service\.

  - \[1\] *int* : serviceState

    The current state of the service\.

  - \[2\] *int* : controlsAccepted

    The controls the service accepts\.

  - \[3\] *int* : win32ExitCode

    The win32 error code for the service\.

  - \[4\] *int* : serviceSpecificErrorCode

    The service specific error code\.

  - \[5\] *int* : checkPoint

    The checkpoint reported by the service\.

  - \[6\] *int* : waitHint

    The wait hint reported by the service\.