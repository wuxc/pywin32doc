
## [win32transaction](#README.md#win32transaction).CommitTransaction

 **CommitTransaction( *TransactionHandle* ** )
Commits a transaction

#### Parameters


     *TransactionHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a transaction

#### Win32 API References


    Search for *CommitTransaction* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CommitTransaction),[google](#README.md#http://www.google.com/search?q=CommitTransaction)or[google groups](#README.md#http://groups.google.com/groups?q=CommitTransaction).

## [win32transaction](#README.md#win32transaction).CommitTransactionAsync

 **CommitTransactionAsync( *TransactionHandle* ** )
Commits a transaction asynchronously

#### Parameters


     *TransactionHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a transaction

#### Win32 API References


    Search for *CommitTransactionAsync* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CommitTransactionAsync),[google](#README.md#http://www.google.com/search?q=CommitTransactionAsync)or[google groups](#README.md#http://groups.google.com/groups?q=CommitTransactionAsync).

## [win32transaction](#README.md#win32transaction).CreateTransaction

[PyHANDLE](#README.md#PyHANDLE)= **CreateTransaction( *TransactionAttributes*  *, UOW*  *, CreateOptions*  *, IsolationLevel*  *, IsolationFlags*  *, Timeout*  *, Description* ** )
Creates a transaction

#### Parameters


     *TransactionAttributes=None* :[PySECURITY_ATTRIBUTES](#PySECURITY.md#PySECURITYATTRIBUTES)

    Security and inheritance for the transaction, can be None

     *UOW=None* :[PyIID](#README.md#PyIID)

    Reserved, use only None

     *CreateOptions=0* : int

    TRANSACTION_DO_NOT_PROMOTE is only defined flag

     *IsolationLevel=0* : int

    Reserved, use only 0

     *IsolationFlags=0* : int

    Reserved, use only 0

     *Timeout=0* : int

    Abort timeout in milliseconds

     *Description=None* :[PyUnicode](#README.md#PyUnicode)

    Text description of transaction, can be None

#### Win32 API References


    Search for *CreateTransaction* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CreateTransaction),[google](#README.md#http://www.google.com/search?q=CreateTransaction)or[google groups](#README.md#http://groups.google.com/groups?q=CreateTransaction).

## [win32transaction](#README.md#win32transaction).GetTransactionId

[PyIID](#README.md#PyIID)= **GetTransactionId( *TransactionHandle* ** )
Returns the transaction's GUID

#### Parameters


     *TransactionHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a transaction

## [win32transaction](#README.md#win32transaction).OpenTransaction

[PyHANDLE](#README.md#PyHANDLE)= **OpenTransaction( *DesiredAccess*  *, TransactionId* ** )
Creates a handle to an existing transaction

#### Parameters


     *DesiredAccess* : int

    Combination of TRANSACTION_* access rights

     *TransactionId* :[PyIID](#README.md#PyIID)

    GUID identifying the transaction

## [win32transaction](#README.md#win32transaction).RollbackTransaction

 **RollbackTransaction( *TransactionHandle* ** )
Rolls back a transaction

#### Parameters


     *TransactionHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a transaction

#### Win32 API References


    Search for *RollbackTransaction* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RollbackTransaction),[google](#README.md#http://www.google.com/search?q=RollbackTransaction)or[google groups](#README.md#http://groups.google.com/groups?q=RollbackTransaction).

## [win32transaction](#README.md#win32transaction).RollbackTransactionAsync

 **RollbackTransactionAsync( *TransactionHandle* ** )
Rolls back a transaction asynchronously

#### Parameters


     *TransactionHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a transaction

#### Win32 API References


    Search for *RollbackTransactionAsync* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RollbackTransactionAsync),[google](#README.md#http://www.google.com/search?q=RollbackTransactionAsync)or[google groups](#README.md#http://groups.google.com/groups?q=RollbackTransactionAsync).