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

## [PyIOleInPlaceFrame](#pyioleinplaceframe)\.EnableModeless

EnableModeless\(fEnable\)
Description of EnableModeless\.

#### Parameters


  - fEnable : int

    Description for fEnable

## [PyIOleInPlaceFrame](#pyioleinplaceframe)\.InsertMenus

InsertMenus\(hmenuShared, menuWidths\)
Description of InsertMenus\.

#### Parameters


  - hmenuShared : int/long

    Description for hmenuShared

  - menuWidths :[PyOLEMENUGROUPWIDTHS](#pyolemenugroupwidths)

    

## [PyIOleInPlaceFrame](#pyioleinplaceframe)\.RemoveMenus

RemoveMenus\(hmenuShared\)
Description of RemoveMenus\.

#### Parameters


  - hmenuShared : int/long

    Description for hmenuShared

## [PyIOleInPlaceFrame](#pyioleinplaceframe)\.SetMenu

SetMenu\(hmenuShared, holemenu, hwndActiveObject\)
Description of SetMenu\.

#### Parameters


  - hmenuShared : int/long

    Description for hmenuShared

  - holemenu : int/long

    Description for holemenu

  - hwndActiveObject : int/long

    Description for hwndActiveObject

## [PyIOleInPlaceFrame](#pyioleinplaceframe)\.SetStatusText

SetStatusText\(pszStatusText\)
Description of SetStatusText\.

#### Parameters


  - pszStatusText :unicode

    Description for pszStatusText

## [PyIOleInPlaceFrame](#pyioleinplaceframe)\.TranslateAccelerator

TranslateAccelerator\(lpmsg, wID\)
Description of TranslateAccelerator\.

#### Parameters


  - lpmsg :[PyMSG](#pymsg)

    Description for lpmsg

  - wID : int

    Description for wID