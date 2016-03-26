# PyCRichEditView

## PyCRichEditView Object



A class which implementes a CRichEditView\.  Derived fromPyCRichEditView and[PyCRichEditCtrl](#pycricheditctrl)\.

#### Methods


  - [GetRichEditCtrl](PyCRichEditView.md#pycricheditviewgetricheditctrl)

    Returns the underlying rich edit control object\.&nbsp;

  - [SetWordWrap](PyCRichEditView.md#pycricheditviewsetwordwrap)

    Sets the wordwrap state for the control\.&nbsp;

  - [WrapChanged](PyCRichEditView.md#pycricheditviewwrapchanged)

    Calls the underlying WrapChanged method\.&nbsp;

  - [SaveTextFile](PyCRichEditView.md#pycricheditviewsavetextfile)

    Saves the control to a text file&nbsp;

## [PyCRichEditView](#pycricheditview)\.GetRichEditCtrl

[PyCRichEditCtrl](#pycricheditctrl) =GetRichEditCtrl\(\)
Returns the underlying rich edit control object\.

## [PyCRichEditView](#pycricheditview)\.SaveTextFile



None =SaveTextFile\(FileName\)
Saves the contents of the control as a test file

#### Parameters


  - FileName : str

    Name of file to save

#### Comments


Theere is no equivilent MFC method\.  This is implemented in this module for performance reasons\.

## [PyCRichEditView](#pycricheditview)\.SetWordWrap



None =SetWordWrap\(wordWrap\)
Sets the wordwrap state for the control\.

#### Parameters


  - wordWrap : int

    The new word-wrap state\.

#### MFC References


  - CRichEditCtrl::m\_nWordWrap

## [PyCRichEditView](#pycricheditview)\.WrapChanged



None =WrapChanged\(\)
Calls the underlying WrapChanged method\.

#### MFC References


  - CRichEditCtrl::WrapChanged