# DOCINFO

## DOCINFO Object



A tuple of information representing a DOCINFO struct

#### Properties

  - string/[PyUnicode](#pyunicode) DocName
    Name of document

  - string/[PyUnicode](#pyunicode) Output
    Name of output file when printing to file\. Use None for normal printing\.

  - string/[PyUnicode](#pyunicode) DataType
    Type of data to be sent to printer, eg RAW, EMF, TEXT\. Use None for printer default\.

  - int Type
    Flag specifying mode of operation\.  Can be DI\_APPBANDING, DI\_ROPS\_READ\_DESTINATION, or 0