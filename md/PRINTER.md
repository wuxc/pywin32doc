# PRINTER

## PRINTER\_DEFAULTS Object

A dictionary representing a PRINTER\_DEFAULTS structure

#### Properties

  -  **string pDatatype** 
    Data type to be used for print jobs, see[win32print::EnumPrintProcessorDatatypes](win32print.md#win32printenumprintprocessordatatypes), optional, can be None

  -  **[PyDEVMODE](#pydevmode)pDevMode** 
    A PyDEVMODE that specifies default printer parameters, optional, can be None

  -  **int DesiredAccess** 
    An ACCESS\_MASK specifying what level of access is needed, eg PRINTER\_ACCESS\_ADMINISTER, PRINTER\_ACCESS\_USE