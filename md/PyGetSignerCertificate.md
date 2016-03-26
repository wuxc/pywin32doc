# PyGetSignerCertificate

## PyGetSignerCertificate Object

Callback used with CRYPT_VERIFY_MESSAGE_PARA to locate a certficate by issuer and serial nbr. 

This function will receive 4 args: 

1. Arbitrary context object given as GetArg in __CRYPT_VERIFY_MESSAGE_PARA__ 2. CertEncodingType (int) -  specifies the type of encoding used 

3. SignerId - Dict containing issuer and serial nbr that uniquely identifies a certificate 

4.[PyCERTSTORE](#pycertstore)containing certificates extracted from the message 

Function must return a[PyCERT_CONTEXT](PyCERT.md#pycertcontext).  If no certificate could be found, it should raise 

pywintypes.error(winerror.CRYPT_E_NO_MATCH) 

If this function is not specified, the default action is to locate a certificate encoded in the message.