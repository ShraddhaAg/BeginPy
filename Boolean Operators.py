and : Logical and # return operator instead of True or False
#if the expression is true, it will return the last operand, if the expression is false, it will return the first falsey operand.
or : Logical or # return operator instead of True or False
# it will return the first truthy value in the expression, since when it finds one, the whole expression is true. In case of every operand being falsey, or will return the last operand, meaning that it iterated over every one of them not being able to find a truthy one.
not : Logical not
!=
==
<=
>=
<
>
True
False

# 2 < x < 4 is allowed
# or use x in range (2,4) [These brackets are inclusive that is same as [] in maths]

if/elif/else : if executes the codes indented within it if the expression within it returns a non zero value or True
                #eg 1 in [1,0] == True evaluates like :
                #(1 in [1, 0]) and ([1, 0] == True)
for: #used for looping through different the range given
    #for i in range(0,5):
    #    print "Adding %d to the line." % i
