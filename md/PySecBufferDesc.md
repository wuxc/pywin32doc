# PySecBufferDesc

## PySecBufferDesc Object



Sequence-like object that contains a group of buffers to be used with SSPI functions\.

#### Comments


This object is created using win32security\.PySecBufferDescType\(Version\), where Version is an int that 

defaults to SECBUFFER\_VERSION if not passed in\.

#### Methods


  - [append](PySecBufferDesc.md#pysecbufferdescappend)

    Adds a[PySecBuffer](#pysecbuffer) to the list of buffers&nbsp;

## [PySecBufferDesc](#pysecbufferdesc)\.append

append\(buffer\)
Adds a[PySecBuffer](#pysecbuffer) to the buffer configuration

#### Parameters


  - buffer :

    [PySecBuffer](#pysecbuffer) object to be attached to the group of buffers