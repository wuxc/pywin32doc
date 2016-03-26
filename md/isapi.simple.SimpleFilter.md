# isapi.simple.SimpleFilter

## isapi.simple.SimpleFilter Object

Base class for a a simple ISAPI filter

#### Methods


  - [HttpFilterProc](isapi.simple.SimpleFilter.md#isapi.simple.simplefilterhttpfilterproc)

    Called by the ISAPI framework for each filter request.&nbsp;

  - [GetFilterVersion](isapi.simple.SimpleFilter.md#isapi.simple.simplefiltergetfilterversion)

    Called by the ISAPI framework to get the extension version&nbsp;

  - [TerminateFilter](isapi.simple.SimpleFilter.md#isapi.simple.simplefilterterminatefilter)

    Called by the ISAPI framework as the filter terminates.&nbsp;

## [isapi.simple.SimpleFilter](#isapi.simple.simplefilter).GetFilterVersion

 __GetFilterVersion(__ )
Called by the ISAPI framework to get the extension version

#### Comments
The default implementation uses the classes docstring to 

set the extension description, and uses the classes 

filter_flags attribute to set the ISAPI filter flags - you 

must specify filter_flags in your class.

## [isapi.simple.SimpleFilter](#isapi.simple.simplefilter).GetFilterVersion

 __GetFilterVersion( *self*  *, fv* __ )
Called by the ISAPI framework to get the extension version

#### Parameters


  -  *self* :

    self

  -  *fv* :

    fv

#### Comments
The default implementation uses the classes docstring to 

set the extension description, and uses the classes 

filter_flags attribute to set the ISAPI filter flags - you 

must specify filter_flags in your class.

## [isapi.simple.SimpleFilter](#isapi.simple.simplefilter).HttpFilterProc

 __HttpFilterProc(__ )
Called by the ISAPI framework for each filter request.

#### Comments
sub-classes must provide an implementation for this method.

## [isapi.simple.SimpleFilter](#isapi.simple.simplefilter).HttpFilterProc

 __HttpFilterProc( *self*  *, fc* __ )
Called by the ISAPI framework for each filter request.

#### Parameters


  -  *self* :

    self

  -  *fc* :

    fc

#### Comments
sub-classes must provide an implementation for this method.

## [isapi.simple.SimpleFilter](#isapi.simple.simplefilter).TerminateFilter

 __TerminateFilter(__ )
Called by the ISAPI framework as the filter terminates.

## [isapi.simple.SimpleFilter](#isapi.simple.simplefilter).TerminateFilter

 __TerminateFilter( *self*  *, status* __ )
Called by the ISAPI framework as the filter terminates.

#### Parameters


  -  *self* :

    self

  -  *status* :

    status