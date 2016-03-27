    
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
            break
            
    if not completedCheck:
        element = text
        
    return (element, number)

# Super class
class ChemBaseObject(object):
    pass
    
# Interfaces
class UnitInterface():
    unit = ""

    def ratio(self):
        if type(self.element) == Element:
            return 1.0
        else:
            print(self.element.GetMass())
            ratios = []
            for el in self.element.elements:
                print("{}: {:,.02%} -> {:,} / {:,}".format(
                        el, #Element 
                        (el.GetMass().amount / self.element.GetMass().amount), #Precentage 
                        self.amount * (el.GetMass().amount / self.element.GetMass().amount), #Mass amount of element
                        self.amount #Total amount
                    )
                )

                ratios.append(el.GetMass().amount / self.element.GetMass().amount)

            

    def __init__(self, Element, Amount):
        self.element = Element
        self.amount = Amount
    
    def __str__(self):
        return "{element}: {amount} {unit}".format(element=self.element.GetName(), amount=self.amount, unit=self.unit)
        
    def __repr__(self):
        return self.__str__()
        
    def __add__(self, other):
        if type(other) == UnitInterface:
            return self.amount + other.amount
        return self.amount + other
       
    def __radd__(self, other):
        if type(other) == UnitInterface:
            return self.amount + other.amount
            
        return self.amount + other
    
    def __call__(self):
        print(self)
        return self

class MassInterface:
    def GetMass(self, amountOf=None):
        raise NotImplementedError( "Should have implemented this" )
       
    def __str__(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def __repr__(self):
        return self.__str__()

    def __call__(self):
        print(self)
        


    def GetName(self):
        raise NotImplementedError( "Should have implemented this" )
        
# Element Inspection Classes         
class Element(MassInterface, ChemBaseObject):
    def __init__(self, ElementName):
        self._rep = Sorter(ElementName)
        self.ElementRep = periodic.element(self._rep[0])
        self.Amount = self._rep[1]
        
    def GetMass(self, amountOf=None):
        if amountOf == None:
            return Grams(self, self.ElementRep.mass * self.Amount)
        else:
            return Grams(self, amountOf)
        
    def __str__(self):
        return "{} x {} = {}".format(Grams(self, self.ElementRep.mass), self.Amount, self.GetMass())
    
    def GetName(self):
        return self.ElementRep.name
        
class Compound(MassInterface, ChemBaseObject):
    def __init__(self, ElementString):
        
        self.elements = []
        for ElementItem in ElementString.split(" "):
            if len(ElementItem) < 1: continue
            self.elements.append(Element(ElementItem))
            
    def GetMass(self, amountOf=None):
        tempLamda = lambda x: Element.GetMass(x)
        GTemp = Grams(self, sum(map(tempLamda, self.elements)))

        if amountOf is not None:
            GTemp.amount = amountOf

        return GTemp
       
    def GetCompoundName(self):
        compoundString = ""
        for element in self.elements:
            compoundString += "".join(map(str, (element.ElementRep.symbol, element.Amount))) + " "
            
        return compoundString
    
    def GetName(self):
        return self.GetCompoundName()
        
    def __str__(self):
        return "{}: {} ==\n\t{}".format(self.GetCompoundName(), self.GetMass().amount,"\n\t".join(map(Element.__str__, self.elements)))
    
    # def __repr__(self):
    #     return self.__str__()

# Unit Convertion Utility Classes
class Grams(UnitInterface, ChemBaseObject):
    def __init__(self, Element, Amount):
        super(Grams, self).__init__(Element, Amount)
        self.unit = "g/mol"
    
    def ToMoles(self, NewAmount=None):
        if NewAmount == None:
            return Moles(self.element, self.amount / self.element.GetMass().amount)
        else:
            return Moles(self.element, NewAmount)
    
class Moles(UnitInterface, ChemBaseObject):
    def __init__(self, Element, Amount):
        super(Moles, self).__init__(Element, Amount)
        self.unit = "mol"
    
    def ToGrams(self, NewAmount = None):
        if NewAmount == None:
            return Grams(self.element, self.element.GetMass().amount * self.amount)
        else:
            return Grams(self.element, self.element.GetMass().amount * NewAmount)
            
    def ToParticles(self, NewAmount = None):
        if NewAmount == None:
            return Particles(self.element, self.amount * mol)
        else:
            return Particles(self.element, NewAmount * mol)
    
class Particles(UnitInterface, ChemBaseObject):
    def __init__(self, Element, Amount):
        super(Particles, self).__init__(Element, Amount)
        self.unit = "particles"
        
    def ToMoles(self, NewAmount=None):
        if NewAmount == None:
            return Moles(self.element, self.amount / mol)
        else:
            return Moles(self.element, NewAmount / mol)
