# PySecBufferDesc


## PySecBufferDesc Object

Sequence-like object that contains a group of buffers to be used with SSPI functions\.

#### Comments

This object is created using win32security\.PySecBufferDescType\(Version\), where Version is an int that 

defaults to SECBUFFER\_VERSION if not passed in\.

#### Methods

  - [append](PySecBufferDesc.md#pysecbufferdescappend)

    Adds a [PySecBuffer](PySecBuffer.md) to the list of buffers&nbsp;


## [PySecBufferDesc](PySecBufferDesc.md#pysecbufferdesc)\.append

append\(buffer\)
Adds a [PySecBuffer](PySecBuffer.md) to the buffer configuration

#### Parameters

  - buffer : 

    [PySecBuffer](PySecBuffer.md) object to be attached to the group of buffers