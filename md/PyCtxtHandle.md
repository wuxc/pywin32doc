# PyCtxtHandle

## PyCtxtHandle Object

Security context handle, as used with sspi functions

#### Comments
Create using win32security\.PyCtxtHandleType\(\)\.  The handle must be initialized by passing it to[win32security::InitializeSecurityContext](win32security.md#win32securityinitializesecuritycontext)or[win32security::AcceptSecurityContext](win32security.md#win32securityacceptsecuritycontext)

#### Methods


  - [Detach](PyCtxtHandle.md#pyctxthandledetach)

    Disassociates object from handle and returns integer value of handle&nbsp;

  - [CompleteAuthToken](PyCtxtHandle.md#pyctxthandlecompleteauthtoken)

    Completes the authentication token&nbsp;

  - [QueryContextAttributes](PyCtxtHandle.md#pyctxthandlequerycontextattributes)

    Retrieves info about a security context&nbsp;

  - [DeleteSecurityContext](PyCtxtHandle.md#pyctxthandledeletesecuritycontext)

    Frees the security context and invalidates the handle&nbsp;

  - [QuerySecurityContextToken](PyCtxtHandle.md#pyctxthandlequerysecuritycontexttoken)

    Returns the access token for a security context&nbsp;

  - [MakeSignature](PyCtxtHandle.md#pyctxthandlemakesignature)

    Generates a signature for a message&nbsp;

  - [VerifySignature](PyCtxtHandle.md#pyctxthandleverifysignature)

    Verifies  a signature created using[PyCtxtHandle::MakeSignature](PyCtxtHandle.md#pyctxthandlemakesignature)&nbsp;

  - [EncryptMessage](PyCtxtHandle.md#pyctxthandleencryptmessage)

    Encrypts data with security context's session key&nbsp;

  - [DecryptMessage](PyCtxtHandle.md#pyctxthandledecryptmessage)

    Decrypts data encrypted by[PyCtxtHandle::EncryptMessage](PyCtxtHandle.md#pyctxthandleencryptmessage)&nbsp;

  - [ImpersonateSecurityContext](PyCtxtHandle.md#pyctxthandleimpersonatesecuritycontext)

    Causes a server to act in the security context of an authenticated client&nbsp;

  - [RevertSecurityContext](PyCtxtHandle.md#pyctxthandlerevertsecuritycontext)

    Stops impersonation of a client initiated by[PyCtxtHandle::ImpersonateSecurityContext](PyCtxtHandle.md#pyctxthandleimpersonatesecuritycontext)&nbsp;

## [PyCtxtHandle](#pyctxthandle)\.CompleteAuthToken

 **CompleteAuthToken\( *Token* ** \)
Completes the authentication token

#### Parameters


  -  *Token* :[PySecBufferDesc](#pysecbufferdesc)

    The buffer that contains the token buffer used when the context was initialized

#### Comments
This method should be invoked on a context handle if the InitializeSecurityContext call that created it 

returned SEC\_I\_COMPLETE\_NEEDED or SEC\_I\_COMPLETE\_AND\_CONTINUE

## [PyCtxtHandle](#pyctxthandle)\.DecryptMessage

 **DecryptMessage\( *Message*  *, MessageSeqNo* ** \)
Decrypts data produced by[PyCtxtHandle::EncryptMessage](PyCtxtHandle.md#pyctxthandleencryptmessage)

#### Parameters


  -  *Message* :[PySecBufferDesc](#pysecbufferdesc)

    [PySecBufferDesc](#pysecbufferdesc)containing data buffers to be decrypted

  -  *MessageSeqNo* : int

    A sequential number used by some packages to verify that no extraneous messages have been received

#### Comments
The buffer configuration is dependent on the security package\.  Usually there is one buffer 

of type SECBUFFER\_DATA which is modified in place and a second buffer of type SECBUFFER\_TOKEN or 

SECBUFFER\_PADDING containing signature, padding, or other extra data from encryption process that doesn't fit 

in first buffer

#### Return Value
Returns flags specfic to security package indicating quality of protection

## [PyCtxtHandle](#pyctxthandle)\.DeleteSecurityContext

 **DeleteSecurityContext\(** \)
Frees the security context and invalidates the handle

## [PyCtxtHandle](#pyctxthandle)\.Detach

long \= **Detach\(** \)
Disassociates object from handle and returns integer value of handle

#### Comments
Use when the security context needs to persist beyond the lifetime of the Python object

## [PyCtxtHandle](#pyctxthandle)\.EncryptMessage

 **EncryptMessage\( *fqop*  *, Message*  *, MessageSeqNo* ** \)
Encrypts data with session key of security context

#### Parameters


  -  *fqop* : int

    Flags that indicate quality of protection desired, specific to each security package

  -  *Message* :[PySecBufferDesc](#pysecbufferdesc)

    [PySecBufferDesc](#pysecbufferdesc)that contains data buffer\(s\) to be encrypted

  -  *MessageSeqNo* : int

    A sequential number used by some packages to verify that no extraneous messages have been received

#### Comments
The buffer configuration is dependent on the security package\.  Usually there is one input buffer 

of type SECBUFFER\_DATA to be encrypted in-place and another empty buffer of type SECBUFFER\_PADDING or SECBUFFER\_TOKEN 

to receive signature or padding data

#### Return Value
Returns None on success, and buffer\(s\) will contain encrypted data

## [PyCtxtHandle](#pyctxthandle)\.ImpersonateSecurityContext

 **ImpersonateSecurityContext\(** \)
Impersonates a client security context

## [PyCtxtHandle](#pyctxthandle)\.MakeSignature

 **MakeSignature\( *fqop*  *, Message*  *, MessageSeqNo* ** \)
Creates a crytographic hash of a message using session key of the security context

#### Parameters


  -  *fqop* : int

    Flags that indicate quality of protection desired, specific to each security package

  -  *Message* :[PySecBufferDesc](#pysecbufferdesc)

    Buffer set that includes buffers for input data and output signature

  -  *MessageSeqNo* : int

    A sequential number used by some packages to verify that no extraneous messages have been received

#### Comments
The buffer configuration is dependent on the security package\.  Usually there is one input buffer of 

type SECBUFFER\_DATA and an output buffer of type SECBUFFER\_TOKEN

#### Return Value
Returns None on success, and output buffer in Message will contain the signature

## [PyCtxtHandle](#pyctxthandle)\.QueryContextAttributes

 **QueryContextAttributes\( *Attribute* ** \)
Retrieves info about a security context

#### Parameters


  -  *Attribute* : int

    SECPKG\_ATTR\_\* constant

#### Comments
Not all attributes are available for every security package


## [PyCtxtHandle](#pyctxthandle)\.QuerySecurityContextToken

[PyHandle](#pyhandle)\= **QuerySecurityContextToken\(** \)
Returns the access token for a security context

## [PyCtxtHandle](#pyctxthandle)\.RevertSecurityContext

 **RevertSecurityContext\(** \)
Stops impersonation of client context \(see[PyCtxtHandle::ImpersonateSecurityContext](PyCtxtHandle.md#pyctxthandleimpersonatesecuritycontext)\)

## [PyCtxtHandle](#pyctxthandle)\.VerifySignature

 **VerifySignature\( *Message*  *, MessageSeqNo* ** \)
Verifies a signature created using[PyCtxtHandle::MakeSignature](PyCtxtHandle.md#pyctxthandlemakesignature)

#### Parameters


  -  *Message* :[PySecBufferDesc](#pysecbufferdesc)

    SecBufferDesc that contains data buffer and signature buffer

  -  *MessageSeqNo* : int

    A sequential number used by some packages to verify that no extraneous messages have been received

#### Comments
The buffer configuration is dependent on the security package\.  Usually there is a data buffer of type SECBUFFER\_DATA 

and a signature buffer of type SECBUFFER\_TOKEN

#### Return Value
Returns quality of protection flags used to create signature