# Keyboard

## Keyboard Bindings
Pythonwin has a new, flexible keyboard 

binding mechanism. Bindings (and even code) can be defined in a 

configuration file, stored in the pywin directory.

Many bindings are still builtin to Python using Window's accelerators - 

see the Pythonwin menus for the specific keyboard shortcuts.

The default configuration file is named default.cfg. You can view 

this file with a text editor (eg, Pythonwin) This file has extensive 

comments, including how to create your own configuration based on the 

default. An example configuration which provides keyboard bindings 

similar to IDLE exists in IDLE.cfg, and this makes a good example of a 

custom configuration.

Please see default.cfg for a complete list, but the default bindings 

provided with Pythonwin are:

 __Common Keystrokes__  __Description__ Alt+QReformat the current paragraph/comment block.  Note this does NOT reformat code correctly - use only within comment blocks!Ctrl+WToggle view whitespace.Alt+/Expand the word at the cursor.  Eg, pressing "st&ltAlt+/&gt" 

will complete based on all words in the current file - eg, "string" 

would be likely to result assuming the code has an "import string" 

statement.  Pressing the key again expands to the next match..Auto expand the attribute.  Eg, typing "string." will display a listbox with the contents of the string module.  Select an item with TAB or the mouse.Alt+IToggle focus to/from the interactive window.
 __Builtin Keystrokes__  __Keystrokes built into Scintilla__ Ctrl+Keypad+PlusZoom-in for the current window.  Non True-Type fonts may require multiple presses.Ctrl+Keypad+MinusZoom-out for the current window.  Non True-Type fonts may require multiple presses.Ctrl+BackspaceDelete the word to the left of the cursor.Ctrl+ZUndoCtrl+YRedoCtrl+XCutCtrl+CCopyCtrl+VPasteCtrl+ASelect AllCtrl+Shift+LDelete the current lineCtrl+TTranspose (swap) the current line with the line aboveCtrl+UConvert the selection to lower caseCtrl+Shift+UConvert the selection to upper case
 __Editor Specific Keystrokes__  __Description__ F2Move to the next bookmark.Ctrl+F2Add or remove a bookmark on the current line.Ctrl+GPrompt for and goto a specific line number.Alt+BAdds a simple comment banner at the current location.Alt+3Block comment the selected region.Shift+Alt+3Uncomment the selected region.Alt+4Uncomment the selected region (IDLE default keystroke)Alt+5Tabify the selected region.
Alt+6Untabify the selected region.BackSpaceRemove selected region or one character or indent to the left.Ctrl+TToggle the use of tabs for the current file (after confirmation)Alt+UChange the indent width for the current file.EnterInsert a newline and indent.TabInsert an indent, perform a block indent if a selection exists, or accept an attribute selection.Shift-TabBlock dedent the selection
F6Toggle view when editor splitter is open.
Keypad-PlusIf the current line is a collapsed fold, expand it (see __Folding__ )Alt-Keypad-PlusExpand all folds in the current file (see __Folding__ )Keypad-MinusIf the current line is an expanded fold, collapse it (see __Folding__ )Alt-Keypad-MinusCollapse all folds in the current file. regardless of how deep the fold becomes. (see __Folding__ )Keypad-MultiplyExpand or collapse all top-level folds in the current file.  No second level or deeper folds are changed. 

If the first fold in the file is collapsed, all top-level folds are opened.  Otherwise, all top-level folds are collapsed (see __Folding__ )
 __Debugger Keystrokes__  __Description__ F9Toggle breakpointF5Run (ie, go)Shift+F5Stop debuggingF11Single step into functionsF10Step over functionsShift+F11Step out of the current function