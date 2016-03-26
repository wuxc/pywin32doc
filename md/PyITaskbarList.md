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

## [PyITaskbarList](#pyitaskbarlist)\.ActivateTab

ActivateTab\(hwnd\)
Marks a window as the active tab on the taskbar

#### Parameters


  - hwnd :[PyHANDLE](#pyhandle)

    Handle to window, should have WS\_CAPTION style

## [PyITaskbarList](#pyitaskbarlist)\.AddTab

AddTab\(hwnd\)
Places a window on the taskbar

#### Parameters


  - hwnd :[PyHANDLE](#pyhandle)

    Handle to window, should have WS\_CAPTION style

## [PyITaskbarList](#pyitaskbarlist)\.DeleteTab

DeleteTab\(hwnd\)
Removes a window from the taskbar

#### Parameters


  - hwnd :[PyHANDLE](#pyhandle)

    Handle to window, should have WS\_CAPTION style

## [PyITaskbarList](#pyitaskbarlist)\.HrInit

HrInit\(\)
Intializes the interface before use

## [PyITaskbarList](#pyitaskbarlist)\.SetActiveAlt

SetActiveAlt\(hwnd\)
Sets the window as the active tab, without displaying it as pressed on the taskbar

#### Parameters


  - hwnd :[PyHANDLE](#pyhandle)

    Handle to window, should have WS\_CAPTION style