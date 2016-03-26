# PyCCmdUI

## PyCCmdUI Object

A class for manipulating user-interface elements.  Encapsulates an MFC __CCmdUI__ class

#### Methods


  - [Enable](PyCCmdUI.md#pyccmduienable)

    Enables or disables the user-interface item for this command.&nbsp;

  - [SetCheck](PyCCmdUI.md#pyccmduisetcheck)

    Sets the check state of the user-interface item for this command.&nbsp;

  - [SetRadio](PyCCmdUI.md#pyccmduisetradio)

    Like the SetCheck member function, but operates on radio groups.&nbsp;

  - [SetText](PyCCmdUI.md#pyccmduisettext)

    Sets the text for the user-interface item for this command.&nbsp;

  - [ContinueRouting](PyCCmdUI.md#pyccmduicontinuerouting)

    Tells the command-routing mechanism to continue routing the current message down the chain of handlers.&nbsp;

#### Properties

  -  __int m_nIndex__ 
    

  -  __int m_nID__ 
    

  -  __[PyCMenu](#pycmenu)m_pMenu__ 
    

  -  __[PyCMenu](#pycmenu)m_pSubMenu__ 
    

## [PyCCmdUI](#pyccmdui).ContinueRouting

 __ContinueRouting(__ )
Tells the command-routing mechanism to continue routing the current message down the chain of handlers.

## [PyCCmdUI](#pyccmdui).Enable

 __Enable( *bEnable* __ )
Enables or disables the user-interface item for this command.

#### Parameters


  -  *bEnable=1* : int

    TRUE if the item should be enabled, false otherwise.

## [PyCCmdUI](#pyccmdui).SetCheck

 __SetCheck( *state* __ )
Sets the check state of the user-interface item for this command.

#### Parameters


  -  *state=1* : int

    0 for unchecked, 1 for checked, or 2 for indeterminate.

## [PyCCmdUI](#pyccmdui).SetRadio

 __SetRadio( *bOn* __ )
Like the SetCheck member function, but operates on radio groups.

#### Parameters


  -  *bOn=1* : int

    TRUE if the item should be enabled, false otherwise.

## [PyCCmdUI](#pyccmdui).SetText

 __SetText( *text* __ )
Sets the text for the user-interface item for this command.

#### Parameters


  -  *text* : string

    The text for the interface element.