# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:55:23 2020

@author: CEC
"""

class Employee:
   'Common base class for all employees'
   empCount = 0

   def_init_(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

print ("Employee._doc_:", Employee._doc)
print ("Employee._name_:", Employee._name)
print ("Employee._module_:", Employee.module)
print ("Employee._bases_:", Employee.bases)
print ("Employee._dict_:", Employee.dict)