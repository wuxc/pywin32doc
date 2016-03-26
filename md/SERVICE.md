# SERVICE

## SERVICE_FAILURE_ACTIONS Object

A dictionary representing a SERVICE_FAILURE_ACTIONS structure

#### Properties

  -  __int ResetPeriod__ 
    Indicates how many seconds to wait to reset the failure count, can be INFINITE

  -  __str/[PyUnicode](#pyunicode)RebootMsg__ 
    Message displayed when reboot action is taken

  -  __str/[PyUnicode](#pyunicode)Command__ 
    Command line to execute for SC_ACTION_RUN_COMMAND

  -  __tuple Actions__ 
    A tuple of[SC_ACTION](SC.md#scaction)tuples

## SERVICE_STATUS Object

A Win32 service status object is represented by a tuple:

#### Items


  - [0] *int* : serviceType

    The type of service.

  - [1] *int* : serviceState

    The current state of the service.

  - [2] *int* : controlsAccepted

    The controls the service accepts.

  - [3] *int* : win32ExitCode

    The win32 error code for the service.

  - [4] *int* : serviceSpecificErrorCode

    The service specific error code.

  - [5] *int* : checkPoint

    The checkpoint reported by the service.

  - [6] *int* : waitHint

    The wait hint reported by the service.