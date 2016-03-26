# CHARFORMAT

## CHARFORMAT Object

Describes a CHARFORMAT tuple

#### Items


  - \[0\] *int* : mask

    The mask to use\.  Bits in this mask indicate which of the following parameter are interpreted\.  Must be a combination the win32con\.CFM\_\* constants\.

  - \[1\] *int* : effects

    The effects to use\.  Must be a combination the win32con\.CFE\_\* constants\.

  - \[2\] *int* : yHeight

    The y height\.

  - \[3\] *int* : yOffset

    Character offset from the baseline\. If this member is positive, the character is a superscript; if it is negative, the character is a subscript\.

  - \[4\] *int* : colorText

    The color to use\.

  - \[5\] *int* : bCharSet

    The charset\.  See the LOGFONT structure for details\.

  - \[6\] *int* : bPitchAndFamily

    The charset\.  See the LOGFONT structure for details\.

  - \[7\] *string* : faceName

    The font name\.

#### Comments
Executing d\=win32ui\.CreateFontDialog\(\); d\.DoModal\(\); print d\.GetCharFormat\(\) 

will print a valid CHARFORMAT tuple\.