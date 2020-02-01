# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 18:32:50 2020

@author: CEC
"""

aclNum = int (input ("What is the IPv4 ACL number? "))
if aclNum >=1 and aclNum <= 99:
    print ("this is a standard IPv4 ACL. " )
elif aclNum >=100 and aclNum <=199:
    print ("this is a extemted IPv4 ACL.")
else:
    print ("this is not a estandard or extended IPv4 ACL.")
    
    
    
