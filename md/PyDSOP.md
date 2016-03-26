# PyDSOP


## PyDSOP\_FILTER\_FLAGS Object

An object representing an ActiveDirectory DSOP\_FILTER\_FLAGS structure 

These objects can only be accessed via a [PyDSOP\_SCOPE\_INIT\_INFO](PyDSOP.md#pydsopscope_init_info) object\.

#### Properties

  - [PyDSOP\_UPLEVEL\_FILTER\_FLAGS](PyDSOP.md#pydsopuplevel_filter_flags) uplevel

    

  - int downlevel

    


## PyDSOP\_SCOPE\_INIT\_INFO Object

An object representing an ActiveDirectory 

DSOP\_SCOPE\_INIT\_INFO structure\. 

These objects can only be accessed by indexing a [PyDSOP\_SCOPE\_INIT\_INFOs](PyDSOP.md#pydsopscope_init_infos) object\.

#### Properties

  - int type

    

  - int scope

    

  - int hr

    

  - [PyUnicode](PyUnicode.md) dcName

    

  - [PyDSOP\_FILTER\_FLAGS](PyDSOP.md#pydsopfilter_flags) filterFlags

    


## PyDSOP\_SCOPE\_INIT\_INFOs Object

An object representing an array of [PyDSOP\_SCOPE\_INIT\_INFO](PyDSOP.md#pydsopscope_init_info) objects

#### Comments

You must pass the number of items in the array to the constructor\. 

Once set, this can not be changed\.  You can index the index \(eg, ob\[2\]\)\.  The 

object has no other \(interesting\) methods or attributes\. 

These objects are created via [adsi::DSOP\_SCOPE\_INIT\_INFOs](adsi.md#adsidsop_scope_init_infos)\(size\)


## PyDSOP\_UPLEVEL\_FILTER\_FLAGS Object

An object representing an ActiveDirectory 

DSOP\_UPLEVEL\_FILTER\_FLAGS structure\. 

These objects can only be accessed via a [PyDSOP\_FILTER\_FLAGS](PyDSOP.md#pydsopfilter_flags) object\.

#### Properties

  - int bothModes

    

  - int mixedModeOnly

    

  - int nativeModeOnly

    