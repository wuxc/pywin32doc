# PyDLGITEMTEMPLATE

## PyDLGITEMTEMPLATE Object

A tuple describing a control in a dialog box.

#### Win32 API References


  - Search for *DLGITEMTEMPLATE* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=dlgitemtemplate),[google](#http://www.google.com/search?q=dlgitemtemplate)or[google groups](#http://groups.google.com/groups?q=dlgitemtemplate).

#### Items


  - [0] *string/int* : windowClass

    The window class.  If not a string, it must be in integer defining one of the built-in Windows controls. 

If a string, it must be a pre-registered windows class name, a built-in class, or the CLSID of an OLE controls. 

Built-in classes include:

 __Control Type__  __String Class Name__ Check BoxButtonCombo BoxComboBoxCommand ButtonButtonHeaderSysHeader32LabelStaticList BoxListBox
SysListView32Option ButtonButtonTabSysTabControl32Text BoxEdit
RICHEDITTool BarToolbarWindow32Tool Tipstooltips_class32
tooltips_classTree ViewSysTreeView32 

The built-in windows controls are:
 __Integer Value__  __Window Type__ 0x0080Button0x0081Edit0x0082Static0x0083List box0x0084Scroll bar0x0085Combo box
  - [1] *[PyUnicode](#pyunicode)* : caption

    Caption for the control, or None

  - [2] *int* : ID

    The child ID of this control.  All children should have unique 

IDs.  This ID can be used by __PyCDialog::GetDlgItem__ to retrieve the actual control 

object at runtime.

  - [3] *(int,int,int,int)* : (x,y,cx,cy)

    The bounding rectange for the control, relative to the upper left of the dialog, in dialog units.

  - [4] *int* : style

    The window style of the control (WS_* constants). Depending on the type of control, 

other constants may also be valid (eg, BS_* for Button, ES_* for Edit controls, etc).

  - [5] *int* : extStyle

    The extended style of the control.

  - [6] *buffer* : extraData

    A byte string or buffer used as extra data for the control.  The value depends on the control.