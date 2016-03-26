# Windows

## Windows NT Eventlog


Python's win32 access for the Eventlog

If you need to scan the eventlog of many servers or do specific 

filtering based off of the event log, python's win32evtlog 

win32evtlogutil libraries give you an means to do it efficiently\.


The library of primary importance is win32evtlog\. With it you can 

connect to a server's eventlog with the call\.

#### Example
Here is the basic call:
logtype='System'

hand=win32evtlog\.OpenEventLog\(server,logtype\)

This returns a handle from which you can make calls such as one that 

will give you the total number of events or another examine the 

details for each event\. The logtype variable is set to the type of log 

you want to look at\. The default ones are: Application, Security, and System\.


After you have the handle you can get ask for things such as the number of 

records, or the specific event records:
total=win32evtlog\.GetNumberOfEventLogRecords\(hand\)

flags = win32evtlog\.EVENTLOG\_BACKWARDS\_READ|win32evtlog\.EVENTLOG\_SEQUENTIAL\_READ

events=win32evtlog\.ReadEventLog\(hand,flags,0\)

ReadEventLog returns a number of event objects which may not be all of 

them\.  You need to continously check in a loop until there are no more 

events returned by ReadEventLog\. You may notice that ReadEventLog has 

a flags argument\.  The flags \(which are convinently available with the 

win32evtlog library\) specify how to read the event log\.

Here is a simple loop getting the data from the events that ReadEventLog 

returned:
for ev\_obj in events:

&\#09the\_time=ev\_obj\.TimeGenerated\.Format\(\) \#'12/23/99 15:54:09'

&\#09evt\_id=str\(winerror\.HRESULT\_CODE\(ev\_obj\.EventID\)\)

&\#09computer=str\(ev\_obj\.ComputerName\)

&\#09cat=ev\_obj\.EventCategory

&\#09seconds=date2sec\(the\_time\)

&\#09record=ev\_obj\.RecordNumber

&\#09msg=str\(win32evtlogutil\.SafeFormatMessage\(ev\_obj, logtype\)\)

&\#09source=str\(ev\_obj\.SourceName\)

We use the library win32evtlogutil to get the actual text body for the 

event\.  To get a easily readable date for the event, you need to 

specify the 'Format' method for the TimeGenerated part of the event 

object\.

The win32evtlogutil comes in handy to give us the actual text body of 

the eventlog message\.  If you want to do any sorting based of off 

time, here is a handy function that converts the eventlog's time 

format into seconds using's python's time and regexp library:
def date2sec\(self,evt\_date\):

&\#09'''

&\#09converts '12/23/99 15:54:09' to seconds

&\#09print '333333',evt\_date

&\#09'''

&\#09regexp=re\.compile\('\(\.\*\)\\\\s\(\.\*\)'\)

&\#09reg\_result=regexp\.search\(evt\_date\)

&\#09date=reg\_result\.group\(1\)

&\#09the\_time=reg\_result\.group\(2\)

&\#09\(mon,day,yr\)=map\(lambda x: string\.atoi\(x\),string\.split\(date,'/'\)\)

&\#09\(hr,min,sec\)=map\(lambda x: string\.atoi\(x\),string\.split\(the\_time,':'\)\)

&\#09tup=\[yr,mon,day,hr,min,sec,0,0,0\]

&\#09sec=time\.mktime\(tup\)

&\#09return sec

If you want to get the current localtime in seconds, you can make the call: 

begin\_sec=time\.time\(\)\. To convert that to a date use: 

begin\_time=str\(time\.strftime\('%H:%M:%S  ',time\.localtime\( begin\_sec \)\)\)

Finally here is all the code that puts together an application which looks 

for all events for a server since a certain time\.

Find events:
import win32evtlog

import win32evtlogutil

import win32security

import win32con

import winerror

import time

import re

import string

import sys

import traceback



def date2sec\(evt\_date\):

&\#09'''

&\#09This function converts dates with format

&\#09'12/23/99 15:54:09' to seconds since 1970\.

&\#09'''

&\#09regexp=re\.compile\('\(\.\*\)\\\\s\(\.\*\)'\) \#store result in site

&\#09reg\_result=regexp\.search\(evt\_date\)

&\#09date=reg\_result\.group\(1\)

&\#09the\_time=reg\_result\.group\(2\)

&\#09\(mon,day,yr\)=map\(lambda x: string\.atoi\(x\),string\.split\(date,'/'\)\)

&\#09\(hr,min,sec\)=map\(lambda x: string\.atoi\(x\),string\.split\(the\_time,':'\)\)

&\#09tup=\[yr,mon,day,hr,min,sec,0,0,0\]



&\#09sec=time\.mktime\(tup\)



&\#09return sec



\#\#\#\#Main program

\#initialize variables

flags = win32evtlog\.EVENTLOG\_BACKWARDS\_READ|\\\\

&\#09&\#09win32evtlog\.EVENTLOG\_SEQUENTIAL\_READ



\#This dict converts the event type into a human readable form

evt\_dict=\{win32con\.EVENTLOG\_AUDIT\_FAILURE:'EVENTLOG\_AUDIT\_FAILURE',\\\\

&\#09&\#09  win32con\.EVENTLOG\_AUDIT\_SUCCESS:'EVENTLOG\_AUDIT\_SUCCESS',\\\\

&\#09&\#09  win32con\.EVENTLOG\_INFORMATION\_TYPE:'EVENTLOG\_INFORMATION\_TYPE',\\\\

&\#09&\#09  win32con\.EVENTLOG\_WARNING\_TYPE:'EVENTLOG\_WARNING\_TYPE',\\\\

&\#09&\#09  win32con\.EVENTLOG\_ERROR\_TYPE:'EVENTLOG\_ERROR\_TYPE'\}

computer='bedrock'

logtype='System'

begin\_sec=time\.time\(\)

begin\_time=time\.strftime\('%H:%M:%S  ',time\.localtime\(begin\_sec\)\)



\#open event log

hand=win32evtlog\.OpenEventLog\(computer,logtype\)

print logtype,' events found in the last 8 hours since:',begin\_time



try:

  events=1

  while events:

    events=win32evtlog\.ReadEventLog\(hand,flags,0\)

      for ev\_obj in events:

&\#09\#check if the event is recent enough

&\#09\#only want data from last 8hrs

&\#09the\_time=ev\_obj\.TimeGenerated\.Format\(\)

&\#09seconds=date2sec\(the\_time\)

&\#09if seconds &lt begin\_sec-28800: break



&\#09\#data is recent enough, so print it out

&\#09computer=str\(ev\_obj\.ComputerName\)

&\#09cat=str\(ev\_obj\.EventCategory\)

&\#09src=str\(ev\_obj\.SourceName\)

&\#09record=str\(ev\_obj\.RecordNumber\)

&\#09evt\_id=str\(winerror\.HRESULT\_CODE\(ev\_obj\.EventID\)\)

&\#09evt\_type=str\(evt\_dict\[ev\_obj\.EventType\]\)

&\#09msg = str\(win32evtlogutil\.SafeFormatMessage\(ev\_obj, logtype\)\)

&\#09print string\.join\(\(the\_time,computer,src,cat,record,evt\_id,evt\_type,msg\[0:15\]\),':'\)



    if seconds &lt begin\_sec-28800: break \#get out of while loop as well

  win32evtlog\.CloseEventLog\(hand\)

except:

    print traceback\.print\_exc\(sys\.exc\_info\(\)\)





&\#09Some useful additions to this would be to make it

multi-threaded and deploy it as a web application, to look at many servers\.

Have a great time with programming with python\!


## Windows NT Eventlog and Threading


Python's threading to manage access access to many Eventlogs

If you need to access the eventlog of many servers, it can take 

quite some time if you go through a list sequentially -- since you 

need to wait for each operation to complete\. There are a few ways you 

can do this in python\.  You can spawn many processes, use python's 

win32 libraries for win32 style-threading, or use python's native 

libraries\.

In NT spawning a process is slow \(though in this case that may not 

matter\) and it can be a little cumbersome to get them to share 

data\. Since python's win32 libraries are thread-safe, you can use 

python's win32 libraries to do win32-style threading or use python's 

native threading library to spawn threads\. Win32 style threading is 

available via python's win32process library\. It gives you excellent 

control and ability to do some sophisticated stuff, however raw win32 

threaded programming can be tricky\. The final option is Python's 

native high-level threading library which is built on top of a lower 

level thread library\. It turns out that it is easy to use and 

cross-platform \(well at least to platforms that support 

threading\)\. It's only disadvantage is that your thread 

control\(synchronization, giving them priorities, suspending them, 

etc\.\)  is limited\. In many cases, however, that is not important, you 

just need the ability to \_easily\_ do a few things at once\.  Thus, 

we'll focus on Python's native threading\.

One final note, the python interpreter has a global lock for 

threads forcing them to run serially\. Which means only one thread can 

intrepret python code at any given time\. After a certain amount of 

python code has been run, then control is switched to another 

thread\. Thus, this means you can't have things like many threads 

running on many processors\. Fortunately, in cases with I/O and 

extension modules \(in which you can manipulate the interpreter lock\), 

this isn't an issue\. In our case \(accessing the eventlog of many 

servers\) the global lock shouldn't be a bottleneck\(i/o will be\)\.

There are a couple of ways to use the threading library\. We'll 

look at the case in which you override the run method of the 

threading\.Thread class\. The run method will contain the actual 

code you want to run many times\.

The basic procedure to follow is this\. 

For every server in the list: 

1\)create a thread class 

2\)call start method in thread class\(which invokes your run method\) 

3\)call join method to force main thread to wait for threads to complete 

4\)compile data together from all thread classes created\.


Since you don't use the return values of the 

thread, you need to store data with the thread object that you 

create\. Furthermore, you'll notice we use the join method to force the 

calling thread to wait for the other threads to finish\.

#### Example
Here is the skeleton of that:
\#We are overiding run\(\) method of the threading\.Thread class\.

class thread\_it \( threading\.Thread \) :

  def \_\_init\_\_ \( self, server\) :

    threading\.Thread\.\_\_init\_\_\(self\)

    self\.data=\[\] \#store data here to get later

    self\.server=server

\# the start\(\) method invokes run

  def run \( self \): \#overridden from threading library

    try:

      pass \#get event information here and store in data

    except:

      \#append any errors to self\.data, to get later

      self\.data\.append\('Error for '\+self\.server\+':'\+str\(traceback\.print\_exc\(sys\.exc\_info\(\)\)\)\)



\#\#\#\#\#\#main here

try:

    l\_servers=\('fred','barney','wilma','betty'\)

    for server in l\_servers: \#make a thread for each server

&\#09    thread = thread\_it \(server\)

&\#09    threads\.append \( thread \) \#append to the a threads list



    for thread in threads: \#now go thru list and start threads running

&\#09    thread\.start\(\)



    for thread in threads: \#make main thread wait for all in list to complete

&\#09thread\.join\(\)



    for thread in threads: \#print thread results

      for event in thread\.data:

&\#09print event





except:

    print traceback\.print\_exc\(sys\.exc\_info\(\)\)

Looking at the skeleton, all one really needs to do is put the 

eventlog code in the run function and have it store results in the 

data variable\. The main part is almost boilerplate code\.  So you can 

see multi-threading at work, I've added a 'now' column to the eventlog 

printout which tells you the current time, and easily shows that the 

data was gathered simultaneously on the servers\.

Filling out the skeleton we get code like this:
import win32evtlog

import win32evtlogutil

import win32security

import win32con

import winerror

import time

import re

import string

import sys

import threading

import traceback



\#We are overiding run\(\) method of the threading\.Thread class\.

class thread\_it \( threading\.Thread \) :

&\#09def \_\_init\_\_ \( self, server\) :

&\#09&\#09threading\.Thread\.\_\_init\_\_\(self\)

&\#09&\#09self\.data=\[\] \#store data here to get later

&\#09&\#09self\.server=server

\# the start\(\) method invokes run

&\#09def run \( self\): \#overridden from threading library

&\#09&\#09flags = win32evtlog\.EVENTLOG\_BACKWARDS\_READ|\\\\

&\#09&\#09win32evtlog\.EVENTLOG\_SEQUENTIAL\_READ

&\#09&\#09\#This dict converts the event type into a human readable form

&\#09&\#09evt\_dict=\{win32con\.EVENTLOG\_AUDIT\_FAILURE:'EVENTLOG\_AUDIT\_FAILURE',\\\\

&\#09&\#09win32con\.EVENTLOG\_AUDIT\_SUCCESS:'EVENTLOG\_AUDIT\_SUCCESS',\\\\

&\#09&\#09win32con\.EVENTLOG\_INFORMATION\_TYPE:'EVENTLOG\_INFORMATION\_TYPE',\\\\

&\#09&\#09win32con\.EVENTLOG\_WARNING\_TYPE:'EVENTLOG\_WARNING\_TYPE',\\\\

&\#09&\#09win32con\.EVENTLOG\_ERROR\_TYPE:'EVENTLOG\_ERROR\_TYPE'\}

&\#09&\#09logtype='System'

&\#09&\#09begin\_sec=time\.time\(\)

&\#09&\#09begin\_time=time\.strftime\('%H:%M:%S  ',time\.localtime\(begin\_sec\)\)

&\#09&\#09try:

&\#09&\#09&\#09hand=win32evtlog\.OpenEventLog\(self\.server,logtype\) \#open event log here

&\#09&\#09&\#09self\.data\.append\('events found in the last 8 hours since:'\+begin\_time\+'for '\+self\.server\)

&\#09&\#09&\#09events=1

&\#09&\#09&\#09while events:

&\#09&\#09&\#09&\#09events=win32evtlog\.ReadEventLog\(hand,flags,0\)



&\#09&\#09&\#09&\#09for ev\_obj in events:

&\#09&\#09&\#09&\#09&\#09now\_sec=time\.time\(\)

&\#09&\#09&\#09&\#09&\#09now\_time=time\.strftime\('now=%H:%M:%S  ',time\.localtime\(now\_sec\)\)



&\#09&\#09&\#09&\#09&\#09\#check if the event is recent enough

&\#09&\#09&\#09&\#09&\#09\#only want data from last 8hrs

&\#09&\#09&\#09&\#09&\#09the\_time=ev\_obj\.TimeGenerated\.Format\(\)

&\#09&\#09&\#09&\#09&\#09seconds=self\.date2sec\(the\_time\)

&\#09&\#09&\#09&\#09&\#09if seconds &lt begin\_sec-28800: break

&\#09&\#09&\#09&\#09&\#09\#data is recent enough, so print it out

&\#09&\#09&\#09&\#09&\#09computer=str\(ev\_obj\.ComputerName\)

&\#09&\#09&\#09&\#09&\#09cat=str\(ev\_obj\.EventCategory\)

&\#09&\#09&\#09&\#09&\#09src=str\(ev\_obj\.SourceName\)

&\#09&\#09&\#09&\#09&\#09record=str\(ev\_obj\.RecordNumber\)

&\#09&\#09&\#09&\#09&\#09evt\_id=str\(winerror\.HRESULT\_CODE\(ev\_obj\.EventID\)\)

&\#09&\#09&\#09&\#09&\#09evt\_type=str\(evt\_dict\[ev\_obj\.EventType\]\)

&\#09&\#09&\#09&\#09&\#09msg = str\(win32evtlogutil\.SafeFormatMessage\(ev\_obj, logtype\)\)

&\#09&\#09&\#09&\#09&\#09results=string\.join\(\(now\_time,the\_time,computer,src,cat,record,evt\_id,evt\_type,msg\[0:15\]\),':'\)

&\#09&\#09&\#09&\#09&\#09self\.data\.append\(results\)

&\#09&\#09&\#09&\#09if seconds &lt begin\_sec-28800: break

&\#09&\#09&\#09win32evtlog\.CloseEventLog\(hand\)

&\#09&\#09except:

&\#09&\#09&\#09self\.data\.append\('Error for '\+self\.server\+':'\+str\(traceback\.print\_exc\(sys\.exc\_info\(\)\)\)\)



&\#09def date2sec\(self,evt\_date\):

&\#09&\#09'''

&\#09&\#09This function converts dates with format

&\#09&\#09'12/23/99 15:54:09' to seconds since 1970\.

&\#09&\#09'''

&\#09&\#09regexp=re\.compile\('\(\.\*\)\\\\s\(\.\*\)'\) \#store result in site

&\#09&\#09reg\_result=regexp\.search\(evt\_date\)

&\#09&\#09date=reg\_result\.group\(1\)

&\#09&\#09the\_time=reg\_result\.group\(2\)



&\#09&\#09\(mon,day,yr\)=map\(lambda x: string\.atoi\(x\),string\.split\(date,'/'\)\)

&\#09&\#09\(hr,min,sec\)=map\(lambda x: string\.atoi\(x\),string\.split\(the\_time,':'\)\)

&\#09&\#09tup=\[yr,mon,day,hr,min,sec,0,0,0\]



&\#09&\#09sec=time\.mktime\(tup\)

&\#09&\#09return sec

\#\#\#\#\#\#main here

try:

&\#09threads=\[\]

&\#09data=\[\]

&\#09l\_servers=\['barney','betty','fred','wilma'\]

&\#09for server in l\_servers: \#make a thread for each server

&\#09&\#09&\#09thread = thread\_it \(server\)

&\#09&\#09&\#09threads\.append \( thread \) \#append to the a threads list



&\#09for thread in threads: \#now go thru list and start threads running

&\#09&\#09&\#09thread\.start\(\)



&\#09for thread in threads: \#make main thread wait for all in list to complete

&\#09&\#09thread\.join\(\)



&\#09for thread in threads: \#compile all of the threads' data together\.

&\#09&\#09print '\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#'

&\#09&\#09for event in thread\.data:

&\#09&\#09&\#09print event



except:

&\#09print traceback\.print\_exc\(sys\.exc\_info\(\)\)

A very nice addition to this would be to convert it to a web 

application\. HTMLgen is a useful tool in this context\.

Have a great time with programming with python\!


## Windows NT Files -- Locking


Python's win32 access for file locking -- flock style

The need for file locking tends arise every so often\. Some people 

may be used to flock style locking, which has 4 basic cases: 

shared,exclusive,blocking and non-blocking\. Shared locking is 

typically used when multiple people want to read a file\. Exclusive is 

for writing\.  Blocking means that the process will wait until it is 

able to lock the file\.  Non-blocking will return immediately and tell 

you the lock failed\.  In win32 the standard CreateFile api gives you 

the ability to do exclusive or shared locking\. However, what it does 

not give you is the ability to switch between blocking/non-blocking 

\(it fails immediately -- does not block\) To do that, you need to use 

LockfileEx -- which can even lock a specific part of a file\.

The basic procedure for doing this is to first call Createfile to 

give you a filehandle\. Then call LockfileEx with the filehandle\. 

Do whatever to the file\. Call UnlockfileEx\. Then close the filehandle\. 

\(Some of you may want to close the filehandle to kill the locks, it 

doesn't work that way with win32, at least according to the msdn\)


Below is a class called Flock, which gives you exclusive/shared 

locking with non-blocking/blocking abilities\. If you can think of any 

optimizations or changes, be sure to let me know\.


CreateFile provides many options\. It can be used for 

files,directories,mailslots,sockets, etc\. In this case, we're only 

interested in standard files\.


The C\+\+ call looks like this:


HANDLE CreateFile\( 

LPCTSTR lpFileName, 

DWORD dwDesiredAccess, 

DWORD dwShareMode, 

LPSECURITY\_ATTRIBUTES lpSecurityAttributes, 

DWORD dwCreationDisposition, 

DWORD dwFlagsAndAttributes, 

HANDLE hTemplateFile 

\);


The python call is virtually the same with:


PyHANDLE = CreateFile\( 

fileName, 

desiredAccess , 

shareMode , 

attributes , 

creationDisposition , 

flagsAndAttributes , 

hTemplateFile 

\)


The module win32con in python is invaluable for setting most of these 

attributes\.  Besides win32con, you need win32security to create a 

security attribute\.

#### Example
Here is a basic example of the raw program:
import win32file

import win32con

import win32security

import win32api

import pywintypes



highbits=0xffff0000 \#high-order 32 bits of byte range to lock

file="c:\\\\\\\\wilma\.txt"

secur\_att = win32security\.SECURITY\_ATTRIBUTES\(\)

secur\_att\.Initialize\(\)



hfile=win32file\.CreateFile\( file,\\\\

&\#09&\#09&\#09    win32con\.GENERIC\_READ|win32con\.GENERIC\_WRITE,\\\\

&\#09&\#09&\#09    win32con\.FILE\_SHARE\_READ|win32con\.FILE\_SHARE\_WRITE,\\\\

&\#09&\#09&\#09    secur\_att,\\\\  \#default

&\#09&\#09&\#09    win32con\.OPEN\_ALWAYS,\\\\

&\#09&\#09&\#09    win32con\.FILE\_ATTRIBUTE\_NORMAL , 0 \)



ov=pywintypes\.OVERLAPPED\(\) \#used to indicate starting region to lock

win32file\.LockFileEx\(hfile,win32con\.LOCKFILE\_EXCLUSIVE\_LOCK,0,highbits,ov\)

win32api\.Sleep\(4000\) \#do something here

win32file\.UnlockFileEx\(hfile,0,highbits,ov\)

hfile\.Close\(\)



&ltnl&gtBelow, I have fleshed it out with a more useable Flock class\.  The

code below works like this: You create an instance of the class,

providing a filename\. It will create/access the file in a default way

and provide an hfile filehandle\.  If you don't want the

default\(shared/blocking\), you can then specify in a dictionary what

type of locking you want\.  Call the lock method on the file\. Do

whatever you want with the hfile filehandle, then call the unlock

method which will remove the locks and close the filehandle\.



Looking at the code below, for desiredAccess and shareMode, I have

both read and write on for most flexibility\. The OPEN\_ALWAYS means

that it will either use the current file or create a new one if none

is to be found\. I use default security for the security attributes

option\. The lock method basically determines what lock flags should be

used, depending on the type of locking you want and then calls

LockFileEx\. An interesting option to LockFileEx is self\.highbits\.  You

can use that to specify portions of a file to lock instead of the

entire thing\. When you're done with whatever you need to do, using the

hfile, filehandle, if necessary, then call the unlock method, to

remove the lock and close the filehandle\.





&ltnl&gtNow for some code|





class Flock:

&\#09def \_\_init\_\_\(self,file\):

&\#09&\#09self\.file=file

&\#09&\#09self\.type=\{'LOCK\_EX':0,'LOCK\_NB':0\}

&\#09&\#09secur\_att = win32security\.SECURITY\_ATTRIBUTES\(\)

&\#09&\#09secur\_att\.Initialize\(\)

&\#09&\#09self\.highbits=0xffff0000 \#high-order 32 bits of byte range to lock

&\#09&\#09\#make a handel with read/write and open or create if doesn't exist

&\#09&\#09self\.hfile=win32file\.CreateFile\( self\.file,\\\\

&\#09&\#09&\#09&\#09&\#09win32con\.GENERIC\_READ|win32con\.GENERIC\_WRITE,\\\\

&\#09&\#09&\#09&\#09&\#09win32con\.FILE\_SHARE\_READ|win32con\.FILE\_SHARE\_WRITE,\\\\

&\#09&\#09&\#09&\#09&\#09secur\_att,\\\\

&\#09&\#09&\#09&\#09&\#09win32con\.OPEN\_ALWAYS,\\\\

&\#09&\#09&\#09&\#09&\#09win32con\.FILE\_ATTRIBUTE\_NORMAL , 0 \)

&\#09def lock\(self\):

&\#09&\#09if self\.type\['LOCK\_EX'\]:  \#exclusive locking

&\#09&\#09&\#09if self\.type\['LOCK\_NB'\]: \#don't wait, non-blocking

&\#09&\#09&\#09&\#09lock\_flags=win32con\.LOCKFILE\_EXCLUSIVE\_LOCK|win32con\.LOCKFILE\_FAIL\_IMMEDIATELY

&\#09&\#09&\#09else: \#wait for lock to free

&\#09&\#09&\#09&\#09lock\_flags=win32con\.LOCKFILE\_EXCLUSIVE\_LOCK

&\#09&\#09else: \#shared locking

&\#09&\#09&\#09if self\.type\['LOCK\_NB'\]: \#don't wait, non-blocking

&\#09&\#09&\#09&\#09lock\_flags=win32con\.LOCKFILE\_FAIL\_IMMEDIATELY

&\#09&\#09&\#09else:\#shared lock wait for lock to free

&\#09&\#09&\#09&\#09lock\_flags=0

&\#09&\#09self\.ov=pywintypes\.OVERLAPPED\(\) \#used to indicate starting region to lock

&\#09&\#09win32file\.LockFileEx\(self\.hfile,lock\_flags,0,self\.highbits,self\.ov\)

&\#09def unlock\(self\):

&\#09&\#09win32file\.UnlockFileEx\(self\.hfile,0,self\.highbits,self\.ov\) \#remove locks

&\#09&\#09self\.hfile\.Close\(\)



l=Flock\("c:\\\\\\\\a3\.txt"\)

l\.type\['LOCK\_EX'\]=0

l\.type\['LOCK\_NB'\]=0



print 'calling lock'

l\.lock\(\)

print 'now locked '



win32api\.Sleep\(1000\)

l\.unlock\(\)

print 'now unlocked'

Have a great time with programming with python\!


## Windows NT Security -- Impersonation


Python's win32 access to help to simplify providing privileged access\.

There may be times when you want to give specific access to 

someone with NT\. One mechanism to do this is with the win32 calls: 

LogonUser and ImpersonateLoggedOnUser\. LogonUser gives you a handel 

which ImpersonateLoggedOnUser can then use to "become" the user\. To do 

this the thread calling, LogonUser, needs SE\_TCB\_NAME, 

SE\_CHANGE\_NOTIFY\_NAME, and SE\_ASSIGNPRIMARYTOKEN\_NAME privileges\.  If 

you plan to do this with something like IIS and cgi, be careful, the anonymous 

account IIS uses is already impersonated from the system account\. You 

will need to use the RevertToSelf, api call to first terminate the 

impersonation\.  And, the system account, a local account, ultimately 

limits you, regardless of who you log in as \(COM/MTS can provide an 

alternative security solution\)\.

#### Example
The c\+\+ api call for Logonasuser looks like:
BOOL LogonUser\(

  LPTSTR lpszUsername,

  LPTSTR lpszDomain,

  LPTSTR lpszPassword,

  DWORD dwLogonType,

  DWORD dwLogonProvider,

  PHANDLE phToken

\);

The python documentation says this:
PyHANDLE = LogonUser\( userName, domain , password , logonType , logonProvider \)

The api call is very similar in both cases except in python the 

handel is returned seperately to the caller\. The interesting options 

in this case are logonType and logonProvider\.  To give values for 

these, you need to use the constants present in win32con \(you can use 

the browser in pythonwin-&gttools to list the constants in 

win32con\)\. Unless you have unusual server requirements, for logonType, 

win32con\.LOGON32\_LOGON\_INTERACTIVE should be fine\. With regards to 

logonProvider, generally use win32con\.LOGON32\_PROVIDER\_DEFAULT -- it's 

for specifiying the type of logon NT 3\.5, 4\.0, win2000\. Generally, 

default is fine\.


ImpersonateLoggedOnUser is extremely simple and you'll see it's usage in the 

examples\.

Now for some code
\#A raw example looks like this:

handel=win32security\.LogonUser\('barney','bedrock','bambam'\\\\

&\#09,win32con\.LOGON32\_LOGON\_INTERACTIVE,win32con\.LOGON32\_PROVIDER\_DEFAULT\)

win32security\.ImpersonateLoggedOnUser\(handel\)



\#do stuff here

print win32api\.GetUserName\(\) \#show you're someone else



win32security\.RevertToSelf\(\) \#terminates impersonation

handel\.Close\(\)



\#The impersonate code can be encapsulated in a class, which then makes it even more

\#trivial to use



import win32security

import win32con

import win32api



class Impersonate:

    def \_\_init\_\_\(self,login,password\):

&\#09self\.domain='bedrock'

&\#09self\.login=login

&\#09self\.password=password

    def logon\(self\):

&\#09self\.handel=win32security\.LogonUser\(self\.login,self\.domain,self\.password,\\\\

&\#09win32con\.LOGON32\_LOGON\_INTERACTIVE,win32con\.LOGON32\_PROVIDER\_DEFAULT\)

&\#09win32security\.ImpersonateLoggedOnUser\(self\.handel\)

    def logoff\(self\):

&\#09win32security\.RevertToSelf\(\) \#terminates impersonation

&\#09self\.handel\.Close\(\) \#guarantees cleanup





a=Impersonate\('barney','bambam'\)



try:

    a\.logon\(\) \#become the user

    \#do whatever here

    print win32api\.GetUserName\(\) \#show you're someone else

    a\.logoff\(\) \#return to normal

except:

    print sys\.exc\_type , sys\.exc\_value

Have a great time with programming with python\!
