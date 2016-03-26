# Pymmapfile

## Pymmapfile Object

Object that provides access to memory-mapped file operations.

#### Methods


  - [close](Pymmapfile.md#pymmapfileclose)

    Closes the file mapping handle and releases mapped view&nbsp;

  - [find](Pymmapfile.md#pymmapfilefind)

    Finds a string in the buffer.&nbsp;

  - [flush](Pymmapfile.md#pymmapfileflush)

    Flushes memory buffer to disk&nbsp;

  - [move](Pymmapfile.md#pymmapfilemove)

    Moves data from one place in buffer to another&nbsp;

  - [read](Pymmapfile.md#pymmapfileread)

    Returns specified number of bytes from buffer, and advances current position&nbsp;

  - [read_byte](Pymmapfile.md#pymmapfileread_byte)

    Reads a single character from current pos&nbsp;

  - [read_line](Pymmapfile.md#pymmapfileread_line)

    Reads data from current pos up to next EOL.&nbsp;

  - [resize](Pymmapfile.md#pymmapfileresize)

    Resizes the file mapping and view&nbsp;

  - [seek](Pymmapfile.md#pymmapfileseek)

    Changes current position&nbsp;

  - [size](Pymmapfile.md#pymmapfilesize)

    Returns size of file mapping&nbsp;

  - [tell](Pymmapfile.md#pymmapfiletell)

    Returns current position in buffer&nbsp;

  - [write](Pymmapfile.md#pymmapfilewrite)

    Places data at current pos in buffer.&nbsp;

  - [write_byte](Pymmapfile.md#pymmapfilewrite_byte)

    Writes a single character of data&nbsp;

## [Pymmapfile](#pymmapfile).close

 __close(__ )
Closes the file mapping handle and releases mapped view

## [Pymmapfile](#pymmapfile).find

int = __find( *needle*  *, start* __ )
Finds a string in the buffer.

#### Parameters


  -  *needle* : str

    String to be located

  -  *start* : int

    Pos at which to start search, current pos assumed if not specified

#### Return Value
Returns pos of string, or -1 if not found

## [Pymmapfile](#pymmapfile).flush

 __flush( *offset*  *, size* __ )
Flushes memory buffer to disk

#### Parameters


  -  *offset=0* : int

    Position in buffer at which to flush

  -  *size=0* : int

    Number of bytes to flush, 0 to flush remainder of buffer past the offset

## [Pymmapfile](#pymmapfile).move

 __move( *dest*  *, src*  *, count* __ )
Moves data from one place in buffer to another

#### Parameters


  -  *dest* : int

    Destination position in buffer

  -  *src* : int

    Source position in buffer

  -  *count* : int

    Number of bytes to move

## [Pymmapfile](#pymmapfile).read

str = __read( *num_bytes* __ )
Returns specified number of bytes from buffer, and advances current position

#### Parameters


  -  *num_bytes* : int

    Number of bytes to read

## [Pymmapfile](#pymmapfile).read_byte

str = __read_byte(__ )
Reads a single character from current pos

## [Pymmapfile](#pymmapfile).read_line

str = __read_line(__ )
Reads data from current pos up to next EOL.

## [Pymmapfile](#pymmapfile).resize

 __resize( *MaximumSize*  *, FileOffset*  *, NumberOfBytesToMap* __ )
Resizes the file mapping and view.

#### Parameters


  -  *MaximumSize* : long

    New size for file mapping. Use a multiple of system page size (see[win32api::GetSystemInfo](win32api.md#win32apigetsysteminfo))

  -  *FileOffset=0* : long

    Offset into file mapping.  Must be multiple of allocation granularity.

  -  *NumberOfBytesToMap=0* : long

    New view size.  Specify a multiple of system page size.

#### Comments
If MaximumSize is 0, only the mapped view will be affected.
Accepts keyword args.

## [Pymmapfile](#pymmapfile).seek

 __seek( *dist*  *, how* __ )
Changes current position

#### Parameters


  -  *dist* : int

    Distance to seek

  -  *how=0* : int

    Pos from which to seek


## [Pymmapfile](#pymmapfile).size

long = __size(__ )
Returns size of current view

## [Pymmapfile](#pymmapfile).tell

int = __tell(__ )
Returns current position in buffer

## [Pymmapfile](#pymmapfile).write

 __write( *data* __ )
Places data at current pos in buffer.

#### Parameters


  -  *data* : str

    Data to be written

## [Pymmapfile](#pymmapfile).write_byte

 __write_byte( *char* __ )
Writes a single character of data

#### Parameters


  -  *char* : str

    Single byte to be placed in buffer