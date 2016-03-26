# PyCRichEditDoc

## PyCRichEditDoc Object

A class which implements a CRichEditView object\.  Derived from[PyCDocument](#pycdocument)\.

#### Methods


  - [OnCloseDocument](PyCRichEditDoc.md#pycricheditdoconclosedocument)

    Call the MFC OnCloseDocument handler\.&nbsp;

## [PyCRichEditDoc](#pycricheditdoc)\.OnCloseDocument

 **OnCloseDocument\(** \)
Call the MFC OnCloseDocument handler\. 

This routine is provided so a document object which overrides this method 

can call the original MFC version if required\.

#### See Also


  - [PyCDocument\.OnCloseDocument](PyCDocument.md#pycdocumentonclosedocument_virtual)virtual method

#### MFC References


  - CRichEditDoc::OnCloseDocument