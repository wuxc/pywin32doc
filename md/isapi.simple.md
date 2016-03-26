# isapi.simple


## Module isapi\.simple

Simple base-classes for extensions and filters\.

#### Comments

None of the filter and extension functions are considered 'optional' by the 

framework\.  These base-classes provide simple implementations for the 

Initialize and Terminate functions, allowing you to omit them,

It is not necessary to use these base-classes - but if you don't, you 

must ensure each of the required methods are implemented\.

#### Classes

  - [SimpleExtension](isapi.simple.SimpleExtension.md)

    Base class for a simple ISAPI extension&nbsp;

  - [SimpleFilter](isapi.simple.SimpleFilter.md)

    Base class for a a simple ISAPI filter&nbsp;