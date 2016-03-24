
# coding: utf-8

import sys, six
sys.version
import periodic
from periodic import element
import math

mol = 6.022 * 10**23
if six.PY2:
    pass
else:

    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

def Sorter(text):
    element = ""
    number = 1
    completedCheck = False
    for idx in range(len(text)):
        if (text[idx].isdigit()):
            

            completedCheck = True
            element = text[:idx]
            number = int(text[idx:])
            #return (element, number)
            break
            
    if not completedCheck:
        element = text
        
    return (element, number)

class ChemBaseObject(object):
    pass
    
class UnitBaseObject(ChemBaseObject):
    unit = ""
    def __init__(self, Element, Amount):
        self.element = Element
        self.amount = Amount
    
    def __str__(self):
        return "{element}: {amount} {unit}".format(element=self.element.GetName(), amount=self.amount, unit=self.unit)
        
    def __repr__(self):
        return self.__str__()
        
    def __add__(self, other):
        if type(other) == UnitBaseObject:
            return self.amount + other.amount
        return self.amount + other
       
    def __radd__(self, other):
        if type(other) == UnitBaseObject:
            return self.amount + other.amount
            
        return self.amount + other
    
class MassInterface():
    def GetMass(self):
        raise NotImplementedError( "Should have implemented this" )
       
    def __str__(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def __repr__(self):
        return self.__str__()
    def GetName(self):
        raise NotImplementedError( "Should have implemented this" )
        
           
class Element(ChemBaseObject, MassInterface):
    def __init__(self, ElementName):
        self._rep = Sorter(ElementName)
        self.ElementRep = periodic.element(self._rep[0])
        self.Amount = self._rep[1]
        
    def GetMass(self):
        # Check #@TODO: Convert to Grams Representation
        
        return Grams(self, self.ElementRep.mass * self.Amount)
        
    def __str__(self):
        return "{}: {} x {} = {}".format(self.ElementRep.name, self.ElementRep.mass, self.Amount, self.ElementRep.mass * self.Amount)
    
    def GetName(self):
        return self.ElementRep.name
        
class Compound(ChemBaseObject, MassInterface):
    def __init__(self, ElementString):
        
        self.elements = []
        for ElementItem in ElementString.split(" "):
            if len(ElementItem) < 1: continue
            self.elements.append(Element(ElementItem))
            
    def GetMass(self):
        #@TODO: Convert to Grams Representation
        return Grams(self, sum(map(Element.GetMass, self.elements)))
       
    def GetCompoundName(self):
        compoundString = ""
        for element in self.elements:
            compoundString += "".join(map(str, (element.ElementRep.symbol, element.Amount))) + " "
            
        return compoundString
    
    def GetName(self):
        return self.GetCompoundName()
        
    def __str__(self):
        return "{}: {} ==\n\t{}".format(self.GetCompoundName(), self.GetMass().amount,"\n\t".join(map(Element.__str__, self.elements)))
    
class Grams(UnitBaseObject):
    def __init__(self, Element, Amount):
        super(Grams, self).__init__(Element, Amount)
        self.unit = "g/mol"
    
    def ToMoles(self):
        return Moles(self.element, self.amount / self.element.GetMass().amount)
    
class Moles(UnitBaseObject):
    def __init__(self, Element, Amount):
        super(Moles, self).__init__(Element, Amount)
        self.unit = "mol"
    
    def ToGrams(self):
        return Grams(self.element, self.element.GetMass().amount * self.amount)
            
    def ToParticles(self):
        return Particles(self.element, self.amount * mol)
    
class Particles(UnitBaseObject):
    def __init__(self, Element, Amount):
        super(Particles, self).__init__(Element, Amount)
        self.unit = "particles"
        
    def ToMoles(self):
        return Moles(self.element, self.amount / mol)
