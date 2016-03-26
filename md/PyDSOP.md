# PyDSOP

## PyDSOP_FILTER_FLAGS Object

An object representing an ActiveDirectory DSOP_FILTER_FLAGS structure
These objects can only be accessed via a[PyDSOP_SCOPE_INIT_INFO](PyDSOP.md#pydsopscope_init_info)object.

#### Properties

  -  __[PyDSOP_UPLEVEL_FILTER_FLAGS](PyDSOP.md#pydsopuplevel_filter_flags)uplevel__ 
    

  -  __int downlevel__ 
    

## PyDSOP_SCOPE_INIT_INFO Object

An object representing an ActiveDirectory 

DSOP_SCOPE_INIT_INFO structure.
These objects can only be accessed by indexing a[PyDSOP_SCOPE_INIT_INFOs](PyDSOP.md#pydsopscope_init_infos)object.

#### Properties

  -  __int type__ 
    

  -  __int scope__ 
    

  -  __int hr__ 
    

  -  __[PyUnicode](#pyunicode)dcName__ 
    

  -  __[PyDSOP_FILTER_FLAGS](PyDSOP.md#pydsopfilter_flags)filterFlags__ 
    

## PyDSOP_SCOPE_INIT_INFOs Object

An object representing an array of[PyDSOP_SCOPE_INIT_INFO](PyDSOP.md#pydsopscope_init_info)objects

#### Comments
You must pass the number of items in the array to the constructor. 

Once set, this can not be changed.  You can index the index (eg, ob[2]).  The 

object has no other (interesting) methods or attributes.
These objects are created via[adsi::DSOP_SCOPE_INIT_INFOs](adsi.md#adsidsop_scope_init_infos)(size)

## PyDSOP_UPLEVEL_FILTER_FLAGS Object

An object representing an ActiveDirectory 

DSOP_UPLEVEL_FILTER_FLAGS structure.
These objects can only be accessed via a[PyDSOP_FILTER_FLAGS](PyDSOP.md#pydsopfilter_flags)object.

#### Properties

  -  __int bothModes__ 
    

  -  __int mixedModeOnly__ 
    

  -  __int nativeModeOnly__ 
    