# PARAFORMAT

## PARAFORMAT Object



Describes a PARAFORMAT tuple

#### Items


  - \[0\]int : mask

    The mask to use\.  Bits in this mask indicate which of the following parameters are interpreted\.  Must be a combination the win32con\.PFM\_\* constants\.

  - \[1\]int : numbering

    The numbering style to use\.

  - \[2\]int : yHeight

    Reserved

  - \[3\]int : dxStartIndent

    Indentation of the first line\.

  - \[4\]int : dxRightIndent

    Indentation from the right\.

  - \[5\]int : dxOffset

    The indent of second and subsequent lines\.

  - \[6\]int : wAlignment

    The alignment of the paragraph\.

  - \[7\]\[int ,\.\.\.\] : tabStops

    The tabstops to use\.