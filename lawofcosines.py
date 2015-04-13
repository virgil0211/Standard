import math

a = raw_input("What's the length of a? ")
b = raw_input("What's the length of b? ")
c = raw_input("What's the length of c? ")

a = float(a)
b = float(b)
c = float(c)
#print " %s %s %s ." % (a,b,c)
asq = a**2 
bsq = b**2
csq = c**2
#print " %s %s %s ." % (asq,bsq,csq)

cosA1 = bsq+csq-asq 
cosA2 = 2.0*b*c
cosB1 = asq+csq-bsq
cosB2 = 2.0*a*c
cosC1 = asq+bsq-csq
cosC2 = 2.0*b*a

#print " %s %s %s %s %s %s ." % (cosA1,cosA2,cosB1,cosB2,cosC1,cosC2)

cosineA = cosA1/cosA2
cosineB = cosB1/cosB2
cosineC = cosC1/cosC2
#print " %s %s %s ." % (cosineA,cosineB,cosineC)
radangleA = math.acos(cosineA)
radangleB = math.acos(cosineB)
radangleC = math.acos(cosineC)
#print " %s %s %s ." % (radangleA,radangleB,radangleC)
degreeangleA = math.degrees(radangleA)
degreeangleB = math.degrees(radangleB)
degreeangleC = math.degrees(radangleC)

print "The length of a is %s and angle A is %s ." % (a,degreeangleA)
print "The length of b is %s and angle B is %s ." % (b,degreeangleB)
print "The length of c is %s and angle C is %s ." % (a,degreeangleC)