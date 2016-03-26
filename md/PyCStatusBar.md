# PyCStatusBar


## PyCStatusBar Object

A class which encapsulates an MFC CStatusBar

\.  Derived from a [PyCControlBar](PyCControlBar.md) object\.

#### Methods

  - [GetPaneInfo](PyCStatusBar.md#pycstatusbargetpaneinfo)

    Returns indicator ID, style, and width for a given pane index\.&nbsp;

  - [GetStatusBarCtrl](PyCStatusBar.md#pycstatusbargetstatusbarctrl)

    Returns the status bar control object associated with the status bar\.&nbsp;

  - [SetIndicators](PyCStatusBar.md#pycstatusbarsetindicators)

    Sets each indicator's ID\.&nbsp;

  - [SetPaneInfo](PyCStatusBar.md#pycstatusbarsetpaneinfo)

    Sets indicator ID, style, and width for a given pane index\.&nbsp;


## [PyCStatusBar](PyCStatusBar.md#pycstatusbar)\.GetPaneInfo

\(id, style, width\) = GetPaneInfo\(index\)
Returns the id, style, and width of the indicator pane at the location specified by index\.

#### Parameters

  - index : int

    Index of the pane whose information is to be retrieved\.

#### MFC References

  - CStatusBar::GetPaneInfo


## [PyCStatusBar](PyCStatusBar.md#pycstatusbar)\.GetStatusBarCtrl

[PyCStatusBarCtrl](PyCStatusBarCtrl.md) = GetStatusBarCtrl\(\)
Gets the statusbar control object for the statusbar\.

#### MFC References

  - CStatusBar::GetStatusBarCtrl 

Note that below we take the address of rTBC because it's a reference and not a pointer 

and ui\_assoc\_object::make expects a pointer\. 

We need to create a new class and not do a map lookup because in MFC CToolBarCtrl is 

simply a casted CToolBarCtrl \(afxext\.inl\) so the lookup will return the PyCToolBar object 

which will fail the type tests\.


## [PyCStatusBar](PyCStatusBar.md#pycstatusbar)\.SetIndicators

SetIndicators\(indicators\)
Sets each indicator's ID\.

#### Parameters

  - indicators : tuple

    A tuple containing the ID's of the indicators\.


## [PyCStatusBar](PyCStatusBar.md#pycstatusbar)\.SetPaneInfo

SetPaneInfo\(index, id, style, width\)
Sets the specified indicator pane to a new ID, style, and width\.

#### Parameters

  - index : int

    Index of the indicator pane whose style is to be set\.

  - id : int

    New ID for the indicator pane\.

  - style : int

    New style for the indicator pane\.
The following indicator styles are supported:
afxres\.SBPS\_NOBORDERS - No 3-D border around the pane\.
afxres\.SBPS\_POPOUT - Reverse border so that text "pops out\."
afxres\.SBPS\_DISABLED - Do not draw text\.
afxres\.SBPS\_STRETCH - Stretch pane to fill unused space\. Only one pane per status bar can have this style\.
afxres\.SBPS\_NORMAL - No stretch, borders, or pop-out\.

  - width : int

    New width for the indicator pane\.

#### MFC References

  - CStatusBar::SetPaneInfo