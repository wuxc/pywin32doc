# win32transaction


## Module win32transaction

Module wrapping Kernal Transaction Manager functions, as used with 

transacted NTFS and transacted registry functions\.

#### Comments

These functions are only available on Vista and later\.

All functions accept keyword arguments\.

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


## [win32transaction](win32transaction.md#win32transaction)\.CommitTransaction

CommitTransaction\(TransactionHandle\)
Commits a transaction

#### Parameters

  - TransactionHandle : [PyHANDLE](PyHANDLE.md)

    Handle to a transaction

#### Win32 API References

  - Search for CommitTransaction at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CommitTransaction.md), [google](http://www.google.com/search?q=CommitTransaction.md) or [google groups](http://groups.google.com/groups?q=CommitTransaction.md)\.


## [win32transaction](win32transaction.md#win32transaction)\.CommitTransactionAsync

CommitTransactionAsync\(TransactionHandle\)
Commits a transaction asynchronously

#### Parameters

  - TransactionHandle : [PyHANDLE](PyHANDLE.md)

    Handle to a transaction

#### Win32 API References

  - Search for CommitTransactionAsync at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CommitTransactionAsync.md), [google](http://www.google.com/search?q=CommitTransactionAsync.md) or [google groups](http://groups.google.com/groups?q=CommitTransactionAsync.md)\.


## [win32transaction](win32transaction.md#win32transaction)\.CreateTransaction

[PyHANDLE](PyHANDLE.md) = CreateTransaction\(TransactionAttributes, UOW

, CreateOptions

, IsolationLevel

, IsolationFlags

, Timeout

, Description

\)
Creates a transaction

#### Parameters

  - TransactionAttributes=None : [PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Security and inheritance for the transaction, can be None

  - UOW=None : [PyIID](PyIID.md)

    Reserved, use only None

  - CreateOptions=0 : int

    TRANSACTION\_DO\_NOT\_PROMOTE is only defined flag

  - IsolationLevel=0 : int

    Reserved, use only 0

  - IsolationFlags=0 : int

    Reserved, use only 0

  - Timeout=0 : int

    Abort timeout in milliseconds

  - Description=None : [PyUnicode](PyUnicode.md)

    Text description of transaction, can be None

#### Win32 API References

  - Search for CreateTransaction at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CreateTransaction.md), [google](http://www.google.com/search?q=CreateTransaction.md) or [google groups](http://groups.google.com/groups?q=CreateTransaction.md)\.


## [win32transaction](win32transaction.md#win32transaction)\.GetTransactionId

[PyIID](PyIID.md) = GetTransactionId\(TransactionHandle\)
Returns the transaction's GUID

#### Parameters

  - TransactionHandle : [PyHANDLE](PyHANDLE.md)

    Handle to a transaction


## [win32transaction](win32transaction.md#win32transaction)\.OpenTransaction

[PyHANDLE](PyHANDLE.md) = OpenTransaction\(DesiredAccess, TransactionId

\)
Creates a handle to an existing transaction

#### Parameters

  - DesiredAccess : int

    Combination of TRANSACTION\_\* access rights

  - TransactionId : [PyIID](PyIID.md)

    GUID identifying the transaction


## [win32transaction](win32transaction.md#win32transaction)\.RollbackTransaction

RollbackTransaction\(TransactionHandle\)
Rolls back a transaction

#### Parameters

  - TransactionHandle : [PyHANDLE](PyHANDLE.md)

    Handle to a transaction

#### Win32 API References

  - Search for RollbackTransaction at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RollbackTransaction.md), [google](http://www.google.com/search?q=RollbackTransaction.md) or [google groups](http://groups.google.com/groups?q=RollbackTransaction.md)\.


## [win32transaction](win32transaction.md#win32transaction)\.RollbackTransactionAsync

RollbackTransactionAsync\(TransactionHandle\)
Rolls back a transaction asynchronously

#### Parameters

  - TransactionHandle : [PyHANDLE](PyHANDLE.md)

    Handle to a transaction

#### Win32 API References

  - Search for RollbackTransactionAsync at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RollbackTransactionAsync.md), [google](http://www.google.com/search?q=RollbackTransactionAsync.md) or [google groups](http://groups.google.com/groups?q=RollbackTransactionAsync.md)\.