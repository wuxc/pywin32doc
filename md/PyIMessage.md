# PyIMessage

## PyIMessage Object

An COM interface to MAPI
Derived from[PyIMAPIProp](#pyimapiprop)

#### Methods


  - [SetReadFlag](PyIMessage.md#pyimessagesetreadflag)

    Sets the read flags for a message&nbsp;

  - [GetAttachmentTable](PyIMessage.md#pyimessagegetattachmenttable)

    Returns the message's attachment table\.&nbsp;

  - [OpenAttach](PyIMessage.md#pyimessageopenattach)

    Opens an attachment&nbsp;

  - [CreateAttach](PyIMessage.md#pyimessagecreateattach)

    Creates an attachment&nbsp;

  - [DeleteAttach](PyIMessage.md#pyimessagedeleteattach)

    Deletes an attachment&nbsp;

  - [ModifyRecipients](PyIMessage.md#pyimessagemodifyrecipients)

    adds, deletes, or modifies message recipients\.&nbsp;

  - [GetRecipientTable](PyIMessage.md#pyimessagegetrecipienttable)

    Returns the message's recipient table\.&nbsp;

  - [SubmitMessage](PyIMessage.md#pyimessagesubmitmessage)

    Saves all of the message's properties and marks the message as ready to be sent\.&nbsp;

## [PyIMessage](#pyimessage)\.CreateAttach

int, **PyIAttach** \= **CreateAttach\( *interface*  *, flags* ** \)
Creates an attachment

#### Parameters


  -  *interface* :[PyIID](#pyiid)

    The interface to use, or None

  -  *flags* : int

    Bitmask of flags that controls how the attachment is created\.

#### Return Value
The result is a tuple of \(attachmentNum, attachmentObject\)

## [PyIMessage](#pyimessage)\.DeleteAttach

 **DeleteAttach\( *attachmentNum*  *, ulUIParam*  *, interface*  *, flags* ** \)
Deletes an attachment

#### Parameters


  -  *attachmentNum* : int

    

  -  *ulUIParam* : int

    

  -  *interface* : **PyIMAPIProgress** 

    The interface to use, or None

  -  *flags* : int

    Bitmask of flags that controls the display of a user interface\.

## [PyIMessage](#pyimessage)\.GetAttachmentTable

[PyIMAPITable](#pyimapitable)\= **GetAttachmentTable\( *flags* ** \)
Returns the message's attachment table\.

#### Parameters


  -  *flags* : int

    Bitmask of flags that relate to the creation of the table\.

## [PyIMessage](#pyimessage)\.GetRecipientTable

[PyIMAPITable](#pyimapitable)\= **GetRecipientTable\( *flags* ** \)
Returns the message's recipient table\.

#### Parameters


  -  *flags* : int

    Bitmask of flags that relate to the creation of the table\.

## [PyIMessage](#pyimessage)\.ModifyRecipients

 **ModifyRecipients\( *flags*  *, mods* ** \)
adds, deletes, or modifies message recipients\.

#### Parameters


  -  *flags* : int

    Bitmask of flags that controls the recipient changes\. If zero is passed for the ulFlags parameter, ModifyRecipients replaces all existing recipients with the recipient list in the mods parameter\.

  -  *mods* : object

    The list of recipients\.

## [PyIMessage](#pyimessage)\.OpenAttach

 **PyIAttach** \= **OpenAttach\( *attachmentNum*  *, interface*  *, flags* ** \)
Opens an attachment

#### Parameters


  -  *attachmentNum* : int

    

  -  *interface* :[PyIID](#pyiid)

    The interface to use, or None

  -  *flags* : int

    Bitmask of flags that controls how the attachment is opened\.

## [PyIMessage](#pyimessage)\.SetReadFlag

 **SetReadFlag\( *flag* ** \)
Sets the read flags for a message

#### Parameters


  -  *flag* : int

    Bitmask of flags that controls the setting of a message's read flag - that is, the message's MSGFLAG\_READ flag in its PR\_MESSAGE\_FLAGS property and the processing of read reports\.

## [PyIMessage](#pyimessage)\.SubmitMessage

 **SubmitMessage\( *flags* ** \)
Saves all of the message's properties and marks the message as ready to be sent\.

#### Parameters


  -  *flags* : int

    Flags which specify how the message is submitted\.