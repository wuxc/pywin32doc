# isapi.simple.SimpleExtension

## isapi.simple.SimpleExtension Object

Base class for a simple ISAPI extension

#### Methods


  - [TerminateExtension](isapi.simple.SimpleExtension.md#isapi.simple.simpleextensionterminateextension)

    Called by the ISAPI framework as the extension terminates.&nbsp;

  - [HttpExtensionProc](isapi.simple.SimpleExtension.md#isapi.simple.simpleextensionhttpextensionproc)

    Called by the ISAPI framework for each extension request.&nbsp;

  - [GetExtensionVersion](isapi.simple.SimpleExtension.md#isapi.simple.simpleextensiongetextensionversion)

    Called by the ISAPI framework to get the extension version&nbsp;

## [isapi.simple.SimpleExtension](#isapi.simple.simpleextension).GetExtensionVersion

 __GetExtensionVersion(__ )
Called by the ISAPI framework to get the extension version

#### Comments
The default implementation uses the classes docstring to 

set the extension description.

## [isapi.simple.SimpleExtension](#isapi.simple.simpleextension).GetExtensionVersion

 __GetExtensionVersion( *self*  *, vi* __ )
Called by the ISAPI framework to get the extension version

#### Parameters


  -  *self* :

    self

  -  *vi* :

    vi

#### Comments
The default implementation uses the classes docstring to 

set the extension description.

## [isapi.simple.SimpleExtension](#isapi.simple.simpleextension).HttpExtensionProc

 __HttpExtensionProc(__ )
Called by the ISAPI framework for each extension request.

#### Comments
sub-classes must provide an implementation for this method.

## [isapi.simple.SimpleExtension](#isapi.simple.simpleextension).HttpExtensionProc

 __HttpExtensionProc( *self*  *, control_block* __ )
Called by the ISAPI framework for each extension request.

#### Parameters


  -  *self* :

    self

  -  *control_block* :

    control_block

#### Comments
sub-classes must provide an implementation for this method.

## [isapi.simple.SimpleExtension](#isapi.simple.simpleextension).TerminateExtension

 __TerminateExtension(__ )
Called by the ISAPI framework as the extension terminates.

## [isapi.simple.SimpleExtension](#isapi.simple.simpleextension).TerminateExtension

 __TerminateExtension( *self*  *, status* __ )
Called by the ISAPI framework as the extension terminates.

#### Parameters


  -  *self* :

    self

  -  *status* :

    status