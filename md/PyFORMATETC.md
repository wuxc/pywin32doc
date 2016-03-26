# PyFORMATETC

## PyFORMATETC Object



Tuple representing a FORMATETC struct describing an OLE data format

#### Items


  - \[0\]int : Format

    CLIPFORMAT value \(CF\_\*\) identifying the type of data

  - \[1\]None : td

    DVTARGETDEVICE \(currently not supported, use only None\)

  - \[2\]int : Aspect

    One of pythoncom\.DVASPECT\_\* values specifying level of detail

  - \[3\]int : index

    Usually -1, used only when data spans multiple pages

  - \[4\]int : tymed

    One of pythoncom\.TYMED\_\* values indicating how the data is stored