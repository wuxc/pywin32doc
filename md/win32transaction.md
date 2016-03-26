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

## [win32transaction](#win32transaction)\.CommitTransaction

CommitTransaction\(TransactionHandle\)
Commits a transaction

#### Parameters


  - TransactionHandle :[PyHANDLE](#pyhandle)

    Handle to a transaction

#### Win32 API References


  - Search forCommitTransaction at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=committransaction),[google](#http://www.google.com/search?q=committransaction) or[google groups](#http://groups.google.com/groups?q=committransaction)\.

## [win32transaction](#win32transaction)\.CommitTransactionAsync

CommitTransactionAsync\(TransactionHandle\)
Commits a transaction asynchronously

#### Parameters


  - TransactionHandle :[PyHANDLE](#pyhandle)

    Handle to a transaction

#### Win32 API References


  - Search forCommitTransactionAsync at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=committransactionasync),[google](#http://www.google.com/search?q=committransactionasync) or[google groups](#http://groups.google.com/groups?q=committransactionasync)\.

## [win32transaction](#win32transaction)\.CreateTransaction

[PyHANDLE](#pyhandle) =CreateTransaction\(TransactionAttributes, UOW, CreateOptions, IsolationLevel, IsolationFlags, Timeout, Description\)
Creates a transaction

#### Parameters


  - TransactionAttributes=None :[PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Security and inheritance for the transaction, can be None

  - UOW=None :[PyIID](#pyiid)

    Reserved, use only None

  - CreateOptions=0 : int

    TRANSACTION\_DO\_NOT\_PROMOTE is only defined flag

  - IsolationLevel=0 : int

    Reserved, use only 0

  - IsolationFlags=0 : int

    Reserved, use only 0

  - Timeout=0 : int

    Abort timeout in milliseconds

  - Description=None :[PyUnicode](#pyunicode)

    Text description of transaction, can be None

#### Win32 API References


  - Search forCreateTransaction at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createtransaction),[google](#http://www.google.com/search?q=createtransaction) or[google groups](#http://groups.google.com/groups?q=createtransaction)\.

## [win32transaction](#win32transaction)\.GetTransactionId

[PyIID](#pyiid) =GetTransactionId\(TransactionHandle\)
Returns the transaction's GUID

#### Parameters


  - TransactionHandle :[PyHANDLE](#pyhandle)

    Handle to a transaction

## [win32transaction](#win32transaction)\.OpenTransaction

[PyHANDLE](#pyhandle) =OpenTransaction\(DesiredAccess, TransactionId\)
Creates a handle to an existing transaction

#### Parameters


  - DesiredAccess : int

    Combination of TRANSACTION\_\* access rights

  - TransactionId :[PyIID](#pyiid)

    GUID identifying the transaction

## [win32transaction](#win32transaction)\.RollbackTransaction

RollbackTransaction\(TransactionHandle\)
Rolls back a transaction

#### Parameters


  - TransactionHandle :[PyHANDLE](#pyhandle)

    Handle to a transaction

#### Win32 API References


  - Search forRollbackTransaction at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rollbacktransaction),[google](#http://www.google.com/search?q=rollbacktransaction) or[google groups](#http://groups.google.com/groups?q=rollbacktransaction)\.

## [win32transaction](#win32transaction)\.RollbackTransactionAsync

RollbackTransactionAsync\(TransactionHandle\)
Rolls back a transaction asynchronously

#### Parameters


  - TransactionHandle :[PyHANDLE](#pyhandle)

    Handle to a transaction

#### Win32 API References


  - Search forRollbackTransactionAsync at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rollbacktransactionasync),[google](#http://www.google.com/search?q=rollbacktransactionasync) or[google groups](#http://groups.google.com/groups?q=rollbacktransactionasync)\.