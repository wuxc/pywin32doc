# PyIShellIconOverlayIdentifier


## PyIShellIconOverlayIdentifier Object

Interface that supplies icon overlay information to the shell

#### Methods

  - [IsMemberOf](PyIShellIconOverlayIdentifier.md#pyishelliconoverlayidentifierismemberof)

    Determines if a shell object should have an icon overlay&nbsp;

  - [GetOverlayInfo](PyIShellIconOverlayIdentifier.md#pyishelliconoverlayidentifiergetoverlayinfo)

    Retrieves the path to the overlay icon&nbsp;

  - [GetPriority](PyIShellIconOverlayIdentifier.md#pyishelliconoverlayidentifiergetpriority)

    Retrieves the relative priority of the overlay&nbsp;


## [PyIShellIconOverlayIdentifier](PyIShellIconOverlayIdentifier.md#pyishelliconoverlayidentifier)\.GetOverlayInfo

\([PyUnicode](PyUnicode.md), int, int\) = GetOverlayInfo\(\)
Retrieves the path to the overlay icon

#### Return Value
Returns the path to the icon file, the index of icon within the file, and Flags containing 

combination of shellcon\.ISIOI\_ICON\* flags


## [PyIShellIconOverlayIdentifier](PyIShellIconOverlayIdentifier.md#pyishelliconoverlayidentifier)\.GetPriority

int = GetPriority\(\)
Retrieves the relative priority of the overlay

#### Return Value
Implementation of this function should return a number in the range 0-100 \(0 is highest priority\)


## [PyIShellIconOverlayIdentifier](PyIShellIconOverlayIdentifier.md#pyishelliconoverlayidentifier)\.IsMemberOf

int = IsMemberOf\(path, attrib

\)
Determines if a shell object should have an icon overlay

#### Parameters

  - path : [PyUnicode](PyUnicode.md)

    Fully qualified path of the shell object

  - attrib : int

    Shell attributes, combination of shellcon\.SFGAO\_\* flags

#### Return Value
The gateway implementation of this function should return winerror\.S\_OK to 

display the overlay, S\_FALSE if not, or throw a COM exception with E\_FAIL on error\. 

The client implementation of this function returns the same values - ie, 

Python's True and False should not be used, as S\_OK==0==False\.