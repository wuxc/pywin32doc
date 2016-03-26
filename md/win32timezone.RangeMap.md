# win32timezone.RangeMap


## win32timezone\.RangeMap Object

A dictionary-like object that uses the keys as bounds for a range\. 

Inclusion of the value for that range is determined by the 

key\_match\_comparator, which defaults to less-than-or-equal\. 

A value is returned for a key if it is the first key that matches in 

the sorted list of keys\.

#### Comments

One may supply keyword parameters to be passed to the sort function used 

to sort keys \(i\.e\. cmp \[python 2 only\], keys, reverse\) as sort\_params\.

Let's create a map that maps 1-3 -&gt 'a', 4-6 -&gt 'b'

&gt&gt&gt r = RangeMap\(\{3: 'a', 6: 'b'\}\)  \# boy, that was easy

&gt&gt&gt r\[1\], r\[2\], r\[3\], r\[4\], r\[5\], r\[6\]

\('a', 'a', 'a', 'b', 'b', 'b'\)

Even float values should work so long as the comparison operator 

supports it\.

&gt&gt&gt r\[4\.5\]

'b'

But you'll notice that the way rangemap is defined, it must be open-ended on one side\.

&gt&gt&gt r\[0\]

'a'

&gt&gt&gt r\[-1\]

'a'

One can close the open-end of the RangeMap by using undefined\_value

&gt&gt&gt r = RangeMap\(\{0: RangeMap\.undefined\_value, 3: 'a', 6: 'b'\}\)

&gt&gt&gt r\[0\]

Traceback \(most recent call last\):

\.\.\.

KeyError: 0

One can get the first or last elements in the range by using RangeMap\.Item

&gt&gt&gt last\_item = RangeMap\.Item\(-1\)

&gt&gt&gt r\[last\_item\]

'b'

\.last\_item is a shortcut for Item\(-1\)

&gt&gt&gt r\[RangeMap\.last\_item\]

'b'

Sometimes it's useful to find the bounds for a RangeMap

&gt&gt&gt r\.bounds\(\)

\(0, 6\)

RangeMap supports \.get\(key, default\)

&gt&gt&gt r\.get\(0, 'not found'\)

'not found'

&gt&gt&gt r\.get\(7, 'not found'\)

'not found'

#### Methods

  - [get](win32timezone.RangeMap.md#win32timezone.rangemapget)

    Return the value for key if key is in the dictionary, else default\.&nbsp;


## [win32timezone\.RangeMap](win32timezone.RangeMap.md#win32timezone.rangemap)\.get

get\(\)
Return the value for key if key is in the dictionary, else default\. 

If default is not given, it defaults to None, so that this method 

never raises a KeyError\.


## [win32timezone\.RangeMap](win32timezone.RangeMap.md#win32timezone.rangemap)\.get

get\(self, key, default\)
Return the value for key if key is in the dictionary, else default\. 

If default is not given, it defaults to None, so that this method 

never raises a KeyError\.

#### Parameters

  - self : 

    self

  - key : 

    key

  - default=None : 

    default