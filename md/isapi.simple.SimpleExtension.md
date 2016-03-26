# isapi.simple.SimpleExtension


## isapi\.simple\.SimpleExtension Object

Base class for a simple ISAPI extension

#### Methods

  - [TerminateExtension](isapi.simple.SimpleExtension.md#isapi.simple.simpleextensionterminateextension)

    Called by the ISAPI framework as the extension terminates\.&nbsp;

  - [HttpExtensionProc](isapi.simple.SimpleExtension.md#isapi.simple.simpleextensionhttpextensionproc)

    Called by the ISAPI framework for each extension request\.&nbsp;

  - [GetExtensionVersion](isapi.simple.SimpleExtension.md#isapi.simple.simpleextensiongetextensionversion)

    Called by the ISAPI framework to get the extension version&nbsp;


## [isapi\.simple\.SimpleExtension](isapi.simple.SimpleExtension.md#isapi.simple.simpleextension)\.GetExtensionVersion

GetExtensionVersion\(\)
Called by the ISAPI framework to get the extension version

#### Comments

The default implementation uses the classes docstring to 

set the extension description\.


## [isapi\.simple\.SimpleExtension](isapi.simple.SimpleExtension.md#isapi.simple.simpleextension)\.GetExtensionVersion

GetExtensionVersion\(self, vi\)
Called by the ISAPI framework to get the extension version

#### Parameters

  - self : 

    self

  - vi : 

    vi

#### Comments

The default implementation uses the classes docstring to 

set the extension description\.


## [isapi\.simple\.SimpleExtension](isapi.simple.SimpleExtension.md#isapi.simple.simpleextension)\.HttpExtensionProc

HttpExtensionProc\(\)
Called by the ISAPI framework for each extension request\.

#### Comments

sub-classes must provide an implementation for this method\.


## [isapi\.simple\.SimpleExtension](isapi.simple.SimpleExtension.md#isapi.simple.simpleextension)\.HttpExtensionProc

HttpExtensionProc\(self, control\_block\)
Called by the ISAPI framework for each extension request\.

#### Parameters

  - self : 

    self

  - control\_block : 

    control\_block

#### Comments

sub-classes must provide an implementation for this method\.


## [isapi\.simple\.SimpleExtension](isapi.simple.SimpleExtension.md#isapi.simple.simpleextension)\.TerminateExtension

TerminateExtension\(\)
Called by the ISAPI framework as the extension terminates\.


## [isapi\.simple\.SimpleExtension](isapi.simple.SimpleExtension.md#isapi.simple.simpleextension)\.TerminateExtension

TerminateExtension\(self, status\)
Called by the ISAPI framework as the extension terminates\.

#### Parameters

  - self : 

    self

  - status : 

    status