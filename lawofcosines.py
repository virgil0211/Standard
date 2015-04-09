
a = raw_input("What's the length of a? "),
b = raw_input("What's the length of b? "),
c = raw_input("What's the length of c? "),

a = float(a)
b = float(b)
c = float(c)

asq = math.exp(a) 
bsq = math.exp(b)
csq = math.exp(c)
 

cosA1 = bsq+csq-asq 
cosA2 = 2.0*b*c
cosB1 = asq+csq-bsq
cosB2 = 2.0*a*c
cosC1 = asq+bsq-csq
cosC2 = 2.0*b*a

cosineA = cosA1//cosA2
cosineB = cosB1//cosB2
cosineC = cosC1//cosC2

radangleA = math.acos(cosineA)
radangleB = math.acos(cosineB)
radangleC = math.acos(cosineC)

degreeangleA = math.degrees(radangleA)
degreeangleB = math.degrees(radangleB)
degreeangleC = math.degrees(radangleC)

print "The length of a is %s and angle A is %s ." % (a,degreeangleA)
print "The length of b is %s and angle B is %s ." % (b,degreeangleB)
print "The length of c is %s and angle C is %s ." % (a,degreeangleC)