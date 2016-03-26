# PyITaskbarList

## PyITaskbarList Object

Description of the interface

#### Methods


  - [HrInit](PyITaskbarList.md#pyitaskbarlisthrinit)

    Intializes the interface before use&nbsp;

  - [AddTab](PyITaskbarList.md#pyitaskbarlistaddtab)

    Places a window on the taskbar&nbsp;

  - [DeleteTab](PyITaskbarList.md#pyitaskbarlistdeletetab)

    Removes a window from the taskbar&nbsp;

  - [ActivateTab](PyITaskbarList.md#pyitaskbarlistactivatetab)

    Marks a window as the active tab on the taskbar&nbsp;

  - [SetActiveAlt](PyITaskbarList.md#pyitaskbarlistsetactivealt)

    Sets the window as the active tab, without displaying it as pressed on the taskbar&nbsp;

## [PyITaskbarList](#pyitaskbarlist).ActivateTab

 __ActivateTab( *hwnd* __ )
Marks a window as the active tab on the taskbar

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    Handle to window, should have WS_CAPTION style

## [PyITaskbarList](#pyitaskbarlist).AddTab

 __AddTab( *hwnd* __ )
Places a window on the taskbar

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    Handle to window, should have WS_CAPTION style

## [PyITaskbarList](#pyitaskbarlist).DeleteTab

 __DeleteTab( *hwnd* __ )
Removes a window from the taskbar

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    Handle to window, should have WS_CAPTION style

## [PyITaskbarList](#pyitaskbarlist).HrInit

 __HrInit(__ )
Intializes the interface before use

## [PyITaskbarList](#pyitaskbarlist).SetActiveAlt

 __SetActiveAlt( *hwnd* __ )
Sets the window as the active tab, without displaying it as pressed on the taskbar

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    Handle to window, should have WS_CAPTION style