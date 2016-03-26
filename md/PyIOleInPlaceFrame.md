# PyIOleInPlaceFrame

## PyIOleInPlaceFrame Object

Description of the interface

#### Methods


  - [InsertMenus](PyIOleInPlaceFrame.md#pyioleinplaceframeinsertmenus)

    Description of InsertMenus&nbsp;

  - [SetMenu](PyIOleInPlaceFrame.md#pyioleinplaceframesetmenu)

    Description of SetMenu&nbsp;

  - [RemoveMenus](PyIOleInPlaceFrame.md#pyioleinplaceframeremovemenus)

    Description of RemoveMenus&nbsp;

  - [SetStatusText](PyIOleInPlaceFrame.md#pyioleinplaceframesetstatustext)

    Description of SetStatusText&nbsp;

  - [EnableModeless](PyIOleInPlaceFrame.md#pyioleinplaceframeenablemodeless)

    Description of EnableModeless&nbsp;

  - [TranslateAccelerator](PyIOleInPlaceFrame.md#pyioleinplaceframetranslateaccelerator)

    Description of TranslateAccelerator&nbsp;

## [PyIOleInPlaceFrame](#pyioleinplaceframe).EnableModeless

 __EnableModeless( *fEnable* __ )
Description of EnableModeless.

#### Parameters


  -  *fEnable* : int

    Description for fEnable

## [PyIOleInPlaceFrame](#pyioleinplaceframe).InsertMenus

 __InsertMenus( *hmenuShared*  *, menuWidths* __ )
Description of InsertMenus.

#### Parameters


  -  *hmenuShared* : int/long

    Description for hmenuShared

  -  *menuWidths* :[PyOLEMENUGROUPWIDTHS](#pyolemenugroupwidths)

    

## [PyIOleInPlaceFrame](#pyioleinplaceframe).RemoveMenus

 __RemoveMenus( *hmenuShared* __ )
Description of RemoveMenus.

#### Parameters


  -  *hmenuShared* : int/long

    Description for hmenuShared

## [PyIOleInPlaceFrame](#pyioleinplaceframe).SetMenu

 __SetMenu( *hmenuShared*  *, holemenu*  *, hwndActiveObject* __ )
Description of SetMenu.

#### Parameters


  -  *hmenuShared* : int/long

    Description for hmenuShared

  -  *holemenu* : int/long

    Description for holemenu

  -  *hwndActiveObject* : int/long

    Description for hwndActiveObject

## [PyIOleInPlaceFrame](#pyioleinplaceframe).SetStatusText

 __SetStatusText( *pszStatusText* __ )
Description of SetStatusText.

#### Parameters


  -  *pszStatusText* : __unicode__ 

    Description for pszStatusText

## [PyIOleInPlaceFrame](#pyioleinplaceframe).TranslateAccelerator

 __TranslateAccelerator( *lpmsg*  *, wID* __ )
Description of TranslateAccelerator.

#### Parameters


  -  *lpmsg* :[PyMSG](#pymsg)

    Description for lpmsg

  -  *wID* : int

    Description for wID