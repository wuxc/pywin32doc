# PyIID

## PyIID Object



A Python object, representing an IID/CLSID\.
All pythoncom functions that return a CLSID/IID will return one of these 

objects\.  However, in almost all cases, functions that expect a CLSID/IID 

as a param will accept either a string object, or a native PyIID object\.

#### Methods


  - [\_\_repr\_\_](PyIID.md#pyiid__repr__)

    Used whenever a repr\(\) is called for the object 

tp\_repr&nbsp;

  - [\_\_hash\_\_](PyIID.md#pyiid__hash__)

    Used when the hash value of an IID object is required 

tp\_hash&nbsp;

  - [\_\_str\_\_](PyIID.md#pyiid__str__)

    Used whenever a string representation of the IID is required\. 

tp\_str&nbsp;

#### Comments


Note that IID objects support the buffer interface\.  Thus buffer\(iid\) can be used to obtain the raw bytes\. 

tp\_as\_buffer

## [PyIID](#pyiid)\.\_\_hash\_\_



int =\_\_hash\_\_\(\)
Used when the hash value of an IID object is required

## [PyIID](#pyiid)\.\_\_repr\_\_



string =\_\_repr\_\_\(\)


## [PyIID](#pyiid)\.\_\_str\_\_



string =\_\_str\_\_\(\)
Used whenever a string representation of the IID is required\.