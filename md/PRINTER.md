# PRINTER

## PRINTER_DEFAULTS Object

A dictionary representing a PRINTER_DEFAULTS structure

#### Properties

  -  __string pDatatype__ 
    Data type to be used for print jobs, see[win32print::EnumPrintProcessorDatatypes](win32print.md#win32printenumprintprocessordatatypes), optional, can be None

  -  __[PyDEVMODE](#pydevmode)pDevMode__ 
    A PyDEVMODE that specifies default printer parameters, optional, can be None

  -  __int DesiredAccess__ 
    An ACCESS_MASK specifying what level of access is needed, eg PRINTER_ACCESS_ADMINISTER, PRINTER_ACCESS_USE