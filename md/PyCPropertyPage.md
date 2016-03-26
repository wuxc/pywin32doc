# PyCPropertyPage

## PyCPropertyPage Object

A class which encapsulates an MFC CPropertyPage object\.  Derived from a[PyCDialog](#pycdialog)object\.

#### Methods


  - [CancelToClose](PyCPropertyPage.md#pycpropertypagecanceltoclose)

    Changes the Cancel button to Close\.&nbsp;

  - [OnCancel](PyCPropertyPage.md#pycpropertypageoncancel)

    Calls the default MFC OnCancel handler\.&nbsp;

  - [OnOK](PyCPropertyPage.md#pycpropertypageonok)

    Calls the default MFC OnOK handler\.&nbsp;

  - [OnApply](PyCPropertyPage.md#pycpropertypageonapply)

    Calls the default MFC OnApply handler\.&nbsp;

  - [OnReset](PyCPropertyPage.md#pycpropertypageonreset)

    Calls the default MFC OnReset handler\.&nbsp;

  - [OnQueryCancel](PyCPropertyPage.md#pycpropertypageonquerycancel)

    Calls the default MFC OnQueryCancel handler\.&nbsp;

  - [OnWizardBack](PyCPropertyPage.md#pycpropertypageonwizardback)

    Calls the default MFC OnWizardBack handler\.&nbsp;

  - [OnWizardNext](PyCPropertyPage.md#pycpropertypageonwizardnext)

    Calls the default MFC OnWizardNext handler\.&nbsp;

  - [OnWizardFinish](PyCPropertyPage.md#pycpropertypageonwizardfinish)

    Calls the default MFC OnWizardFinish handler\.&nbsp;

  - [OnSetActive](PyCPropertyPage.md#pycpropertypageonsetactive)

    Calls the default MFC OnSetActive handler\.&nbsp;

  - [OnKillActive](PyCPropertyPage.md#pycpropertypageonkillactive)

    Calls the default MFC OnKillActive handler\.&nbsp;

  - [SetModified](PyCPropertyPage.md#pycpropertypagesetmodified)

    Sets the modified flag \(for the Apply button\)\.&nbsp;

  - [SetPSPBit](PyCPropertyPage.md#pycpropertypagesetpspbit)

    Sets \(or clears\) a bit in m\_psp\.dwFlags\.&nbsp;

## [PyCPropertyPage](#pycpropertypage)\.CancelToClose

 **CancelToClose\(** \)
Changes the Cancel button to Close\.

## [PyCPropertyPage](#pycpropertypage)\.OnApply

 **OnApply\(** \)
Calls the default MFC OnApply handler\.

#### See Also


  - [PyCPropertyPage\.OnApply](PyCPropertyPage.md#pycpropertypageonapply_virtual)virtual method

## [PyCPropertyPage\.OnApply](#pycpropertypage)Virtual

 **OnApply\(** \)
Called by the framework when the user chooses the OK or the Apply Now button\.

#### Comments
Note - If you provide a handler, you must call the underlying MFC method \([PyCPropertyPage::OnApply](PyCPropertyPage.md#pycpropertypageonapply)\) yourself

#### See Also


  - [PyCPropertyPage::OnApply](PyCPropertyPage.md#pycpropertypageonapply)

#### Return Value
Return Nonzero if the changes are accepted; otherwise 0\.

## [PyCPropertyPage](#pycpropertypage)\.OnCancel

 **OnCancel\(** \)
Calls the default MFC OnCancel handler\.

#### See Also


  - [PyCDialog\.OnCancel](PyCDialog.md#pycdialogoncancel_virtual)virtual method

## [PyCPropertyPage](#pycpropertypage)\.OnKillActive

int \= **OnKillActive\(** \)
Calls the default MFC OnKillActive handler\.

#### See Also


  - [PyCPropertyPage\.OnKillActive](PyCPropertyPage.md#pycpropertypageonkillactive_virtual)virtual method

  - [PyCPropertyPage\.OnKillActive](PyCPropertyPage.md#pycpropertypageonkillactive_virtual)virtual method

#### Return Value
The result is true if the page should be deselected\. 

Typically this result should be passed to the original OnSetActive handler\.

## [PyCPropertyPage\.OnKillActive](#pycpropertypage)Virtual

 **OnKillActive\(** \)
Called when the page loses focus\.

#### Comments
Note - If you provide a handler, you must call the underlying MFC method \([PyCPropertyPage::OnKillActive](PyCPropertyPage.md#pycpropertypageonkillactive)\) yourself

#### See Also


  - [PyCPropertyPage::OnKillActive](PyCPropertyPage.md#pycpropertypageonkillactive)

#### Return Value
The method should return TRUE if the page can be de-activated\.

## [PyCPropertyPage](#pycpropertypage)\.OnOK

 **OnOK\(** \)
Calls the default MFC OnOK handler\.

#### See Also


  - [PyCDialog\.OnOK](PyCDialog.md#pycdialogonok_virtual)virtual method

## [PyCPropertyPage](#pycpropertypage)\.OnQueryCancel

 **OnQueryCancel\(** \)
Calls the default MFC OnQueryCancel handler\.

#### See Also


  - [PyCPropertyPage\.OnQueryCancel](PyCPropertyPage.md#pycpropertypageonquerycancel_virtual)virtual method

## [PyCPropertyPage\.OnQueryCancel](#pycpropertypage)Virtual

 **OnQueryCancel\(** \)
Called by the framework when the user clicks the Cancel button and before the cancel action has taken place\.

#### Comments
Note - If you provide a handler, you must call the underlying MFC method \([PyCPropertyPage::OnQueryCancel](PyCPropertyPage.md#pycpropertypageonquerycancel)\) yourself

#### See Also


  - [PyCPropertyPage::OnQueryCancel](PyCPropertyPage.md#pycpropertypageonquerycancel)

#### Return Value
Return FALSE to prevent the cancel operation or TRUE to allow it\.

## [PyCPropertyPage](#pycpropertypage)\.OnReset

 **OnReset\(** \)
Calls the default MFC OnReset handler\.

#### See Also


  - [PyCPropertyPage\.OnReset](PyCPropertyPage.md#pycpropertypageonreset_virtual)virtual method

## [PyCPropertyPage\.OnReset](#pycpropertypage)Virtual

 **OnReset\(** \)
Called by the framework when the user chooses the Cancel button\.

#### Comments
Note - If you provide a handler, you must call the underlying MFC method \([PyCPropertyPage::OnReset](PyCPropertyPage.md#pycpropertypageonreset)\) yourself

#### See Also


  - [PyCPropertyPage::OnReset](PyCPropertyPage.md#pycpropertypageonreset)

## [PyCPropertyPage](#pycpropertypage)\.OnSetActive

int \= **OnSetActive\(** \)
Calls the default MFC OnSetActive handler\.

#### See Also


  - [PyCPropertyPage\.OnSetActive](PyCPropertyPage.md#pycpropertypageonsetactive_virtual)virtual method

  - [PyCPropertyPage\.OnSetActive](PyCPropertyPage.md#pycpropertypageonsetactive_virtual)virtual method

#### Return Value
The result is true if the page should be made active\. 

Typically this result should be passed to the original OnSetActive handler\.

## [PyCPropertyPage\.OnSetActive](#pycpropertypage)Virtual

 **OnSetActive\(** \)
Called when the page becomes active\.

#### Comments
Note - If you provide a handler, you must call the underlying MFC method \([PyCPropertyPage::OnSetActive](PyCPropertyPage.md#pycpropertypageonsetactive)\) yourself

#### See Also


  - [PyCPropertyPage::OnSetActive](PyCPropertyPage.md#pycpropertypageonsetactive)

#### Return Value
The method should return TRUE if the page can be activated\.

## [PyCPropertyPage](#pycpropertypage)\.OnWizardBack

 **OnWizardBack\(** \)
Calls the default MFC OnWizardBack handler\.

#### See Also


  - [PyCPropertyPage\.OnWizardBack](PyCPropertyPage.md#pycpropertypageonwizardback_virtual)virtual method

## [PyCPropertyPage\.OnWizardBack](#pycpropertypage)Virtual

 **OnWizardBack\(** \)
Called by the framework when the user clicks on the Back button in a wizard\.

#### Comments
Note - If you provide a handler, you must call the underlying MFC method \([PyCPropertyPage::OnWizardBack](PyCPropertyPage.md#pycpropertypageonwizardback)\) yourself

#### See Also


  - [PyCPropertyPage::OnWizardBack](PyCPropertyPage.md#pycpropertypageonwizardback)

#### Return Value
Return 0 to automatically advance to the next page;  -1 to prevent the page from changing\. To jump to a page other than the next one, return the identifier of the dialog to be displayed\.

## [PyCPropertyPage](#pycpropertypage)\.OnWizardFinish

 **OnWizardFinish\(** \)
Calls the default MFC OnWizardFinish handler\.

#### See Also


  - [PyCPropertyPage\.OnWizardFinish](PyCPropertyPage.md#pycpropertypageonwizardfinish_virtual)virtual method

## [PyCPropertyPage\.OnWizardFinish](#pycpropertypage)Virtual

 **OnWizardFinish\(** \)
Called by the framework when the user clicks on the Finish button in a wizard\.

#### Comments
Note - If you provide a handler, you must call the underlying MFC method \([PyCPropertyPage::OnWizardFinish](PyCPropertyPage.md#pycpropertypageonwizardfinish)\) yourself

#### See Also


  - [PyCPropertyPage::OnWizardFinish](PyCPropertyPage.md#pycpropertypageonwizardfinish)

#### Return Value
Return nonzero if the property sheet is destroyed when the wizard finishes; otherwise zero\.

## [PyCPropertyPage](#pycpropertypage)\.OnWizardNext

 **OnWizardNext\(** \)
Calls the default MFC OnWizardNext handler\.

#### See Also


  - [PyCPropertyPage\.OnWizardNext](PyCPropertyPage.md#pycpropertypageonwizardnext_virtual)virtual method

## [PyCPropertyPage\.OnWizardNext](#pycpropertypage)Virtual

 **OnWizardNext\(** \)
Called by the framework when the user clicks on the Next button in a wizard\.

#### Comments
Note - If you provide a handler, you must call the underlying MFC method \([PyCPropertyPage::OnWizardNext](PyCPropertyPage.md#pycpropertypageonwizardnext)\) yourself

#### See Also


  - [PyCPropertyPage::OnWizardNext](PyCPropertyPage.md#pycpropertypageonwizardnext)

#### Return Value
Return 0 to automatically advance to the next page;  -1 to prevent the page from changing\. To jump to a page other than the next one, return the identifier of the dialog to be displayed\.

## [PyCPropertyPage](#pycpropertypage)\.SetModified

 **SetModified\( *bChanged* ** \)
Sets the modified flag\.

#### Parameters


  -  *bChanged\=1* : int

    A flag to indicate the new modified state\.

## [PyCPropertyPage](#pycpropertypage)\.SetPSPBit

 **SetPSPBit\( *bitMask*  *, bitValue* ** \)
Sets or clears a bit in m\_psp\.dwFlags

#### Parameters


  -  *bitMask* : int

    The PSP\_\* bit mask constant

  -  *bitValue* : int

    1 to set, 0 to clear