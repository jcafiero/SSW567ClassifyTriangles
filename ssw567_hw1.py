import unittest

def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right' 
    """
    classification = ''
    longside = max([a,b,c])
    if a == b and a == c:
        classification = 'Equilateral'
    elif (a == b and a != c) or (b == c and a != b) or (a == c and a != b):
        classification = 'Isoceles'
    else:
        classification = 'Scalene'
    if a * a + b * b == c * c:
        classification += ' and Right'
    if (a + b <= c or a + c <= b or b + c <= a):
        classification = 'NotATriangle'
    return classification
    

def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,5),'Scalene and Right','3,4,5 is a Scalene Right triangle')
        
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(12,12,12),'Equilateral','12,12,12 should be equilateral')

    def testEquilateral(self):
        self.assertEqual(classifyTriangle(12,12,12),'Equilateral','12,12,12 should be equilateral')
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(3,4,5),'Equilateral','3,4,5 should be Scalene and Right')

    def testIsoceles(self):
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','10,10,10 should be Equilateral')
        self.assertEqual(classifyTriangle(4,3,4),'Isoceles','4,3,4 should be isoceles')
        self.assertEqual(classifyTriangle(6,6,7),'Isoceles','6,6,7 should be isoceles')

    def testScalene(self):
        self.assertEqual(classifyTriangle(11,9,18),'Scalene','11,9,18 should be scalene')
        self.assertEqual(classifyTriangle(2,6,7),'Scalene','2,6,7 should be scalene')
        self.assertNotEqual(classifyTriangle(10,10,20),'Scalene','10,10,20 should be not a triangle')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,2,20),'NotATriangle','1,2,20 should be not a triangle')
        self.assertEqual(classifyTriangle(3,3,7),'NotATriangle','3,3,7 should be not a triangle')
        self.assertNotEqual(classifyTriangle(100,100,100),'NotATriangle','100,100,100 should be Equilateral')

    def testRight(self):
        #The following test is buggy - a triangle cannot just be right
        self.assertNotEqual(classifyTriangle(3,4,5),'Right','3,4,5 should be Scalene and Right')
        self.assertEqual(classifyTriangle(5,12,13),'Scalene and Right','5,12,13 should be Scalene and Right')
        #The following test is good - a triangle cannot be equilateral and right, no matter its lengths
        self.assertNotEqual(classifyTriangle(5,5,5),'Equilateral and Right','5,5,5 should be Equilateral')
        

if __name__ == '__main__':
    # examples of running the codeself.assertNotEqual(classifyTriangle(2,3,4),'Right','Should be Scalene')self.assertNotEqual(classifyTriangle(2,3,4),'Right','Should be Scalene')
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(3,4,4)
    runClassifyTriangle(2,6,7)
    runClassifyTriangle(3,4,5)
    
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
