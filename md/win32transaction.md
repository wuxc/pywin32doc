# win32transaction

## Module win32transaction

Module wrapping Kernal Transaction Manager functions, as used with 

transacted NTFS and transacted registry functions.

#### Comments
These functions are only available on Vista and later.
All functions accept keyword arguments.

#### Methods


  - [CreateTransaction](win32transaction.md#win32transactioncreatetransaction)

    Creates a transaction&nbsp;

  - [RollbackTransaction](win32transaction.md#win32transactionrollbacktransaction)

    Rolls back a transaction&nbsp;

  - [RollbackTransactionAsync](win32transaction.md#win32transactionrollbacktransactionasync)

    Rolls back a transaction asynchronously&nbsp;

  - [CommitTransaction](win32transaction.md#win32transactioncommittransaction)

    Commits a transaction&nbsp;

  - [CommitTransactionAsync](win32transaction.md#win32transactioncommittransactionasync)

    Commits a transaction asynchronously&nbsp;

  - [GetTransactionId](win32transaction.md#win32transactiongettransactionid)

    Returns the transaction's GUID&nbsp;

  - [OpenTransaction](win32transaction.md#win32transactionopentransaction)

    Creates a handle to an existing transaction&nbsp;

## [win32transaction](#win32transaction).CommitTransaction

 __CommitTransaction( *TransactionHandle* __ )
Commits a transaction

#### Parameters


  -  *TransactionHandle* :[PyHANDLE](#pyhandle)

    Handle to a transaction

#### Win32 API References


  - Search for *CommitTransaction* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=committransaction),[google](#http://www.google.com/search?q=committransaction)or[google groups](#http://groups.google.com/groups?q=committransaction).

## [win32transaction](#win32transaction).CommitTransactionAsync

 __CommitTransactionAsync( *TransactionHandle* __ )
Commits a transaction asynchronously

#### Parameters


  -  *TransactionHandle* :[PyHANDLE](#pyhandle)

    Handle to a transaction

#### Win32 API References


  - Search for *CommitTransactionAsync* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=committransactionasync),[google](#http://www.google.com/search?q=committransactionasync)or[google groups](#http://groups.google.com/groups?q=committransactionasync).

## [win32transaction](#win32transaction).CreateTransaction

[PyHANDLE](#pyhandle)= __CreateTransaction( *TransactionAttributes*  *, UOW*  *, CreateOptions*  *, IsolationLevel*  *, IsolationFlags*  *, Timeout*  *, Description* __ )
Creates a transaction

#### Parameters


  -  *TransactionAttributes=None* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Security and inheritance for the transaction, can be None

  -  *UOW=None* :[PyIID](#pyiid)

    Reserved, use only None

  -  *CreateOptions=0* : int

    TRANSACTION_DO_NOT_PROMOTE is only defined flag

  -  *IsolationLevel=0* : int

    Reserved, use only 0

  -  *IsolationFlags=0* : int

    Reserved, use only 0

  -  *Timeout=0* : int

    Abort timeout in milliseconds

  -  *Description=None* :[PyUnicode](#pyunicode)

    Text description of transaction, can be None

#### Win32 API References


  - Search for *CreateTransaction* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createtransaction),[google](#http://www.google.com/search?q=createtransaction)or[google groups](#http://groups.google.com/groups?q=createtransaction).

## [win32transaction](#win32transaction).GetTransactionId

[PyIID](#pyiid)= __GetTransactionId( *TransactionHandle* __ )
Returns the transaction's GUID

#### Parameters


  -  *TransactionHandle* :[PyHANDLE](#pyhandle)

    Handle to a transaction

## [win32transaction](#win32transaction).OpenTransaction

[PyHANDLE](#pyhandle)= __OpenTransaction( *DesiredAccess*  *, TransactionId* __ )
Creates a handle to an existing transaction

#### Parameters


  -  *DesiredAccess* : int

    Combination of TRANSACTION_* access rights

  -  *TransactionId* :[PyIID](#pyiid)

    GUID identifying the transaction

## [win32transaction](#win32transaction).RollbackTransaction

 __RollbackTransaction( *TransactionHandle* __ )
Rolls back a transaction

#### Parameters


  -  *TransactionHandle* :[PyHANDLE](#pyhandle)

    Handle to a transaction

#### Win32 API References


  - Search for *RollbackTransaction* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rollbacktransaction),[google](#http://www.google.com/search?q=rollbacktransaction)or[google groups](#http://groups.google.com/groups?q=rollbacktransaction).

## [win32transaction](#win32transaction).RollbackTransactionAsync

 __RollbackTransactionAsync( *TransactionHandle* __ )
Rolls back a transaction asynchronously

#### Parameters


  -  *TransactionHandle* :[PyHANDLE](#pyhandle)

    Handle to a transaction

#### Win32 API References


  - Search for *RollbackTransactionAsync* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rollbacktransactionasync),[google](#http://www.google.com/search?q=rollbacktransactionasync)or[google groups](#http://groups.google.com/groups?q=rollbacktransactionasync).