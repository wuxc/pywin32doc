# sspi


## Module sspi

Helper classes for SSPI authentication via the win32security module\.

#### Comments

SSPI authentication involves a token-exchange "dance", the exact details 

of which depends on the authentication provider used\.  There are also 

a number of complex flags and constants that need to be used - in most 

cases, there are reasonable defaults\.

These classes attempt to hide these details from you until you really need 

to know\.  They are not designed to handle all cases, just the common ones\. 

If you need finer control than offered here, just use the win32security 

functions directly\.

#### Classes

  - [ClientAuth](sspi.ClientAuth.md)

    Manages the client side of an SSPI authentication handshake&nbsp;

  - [ServerAuth](sspi.ServerAuth.md)

    Manages the server side of an SSPI authentication handshake&nbsp;