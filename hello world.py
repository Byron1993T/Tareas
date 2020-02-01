Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5+1
6
>>> 58-48
10
>>> str1="cisco"
>>> str2=Networking"
SyntaxError: EOL while scanning string literal
>>> str2="Networking"
>>> str3="Academy"
>>> space=""
>>> print(str1+space+str2+space+str3)
ciscoNetworkingAcademy
>>> print (str1,str2,str3)
cisco Networking Academy
>>> x=3
>>> print ("this value of x is " + x)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print ("this value of x is " + x)
TypeError: can only concatenate str (not "int") to str
>>> print ("this value of x is " + str (x))
this value of x is 3
>>> type (x)
<class 'int'>
>>> p1=22/7
>>> print (pi)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print (pi)
NameError: name 'pi' is not defined
>>> pi = 22/7
>>> print (pi)
3.142857142857143
>>> hostnames=["R1","R2","R3","R4")
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> hostnames=["R1","R2","R3","R4"]
>>> len (hostnames)
4
>>> hostnames
['R1', 'R2', 'R3', 'R4']
>>> hostnames=["R1","R2","R3","S1","S2"]
>>> type(hostnames)
<class 'list'>
>>> len(hostnames)
5
>>> hostnames
['R1', 'R2', 'R3', 'S1', 'S2']
>>> hostnames [0]
'R1'
>>> hostnames [1]
'R2'
>>> hostnames [0]="RTR1"
>>> hostnames
['RTR1', 'R2', 'R3', 'S1', 'S2']
>>> del hostnames [3]
>>> hostnames
['RTR1', 'R2', 'R3', 'S2']
>>> firstname = input ("what is your first name")
what is your first name
>>> print ("hello" +firstname +"!")
hello!
>>> 