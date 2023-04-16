import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
#     def test_short_vardecl(self):
#         input="""x: integer = 3.9;"""
#         expect="Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FloatLit(3.9))"
#         self.assertTrue(TestChecker.test(input,expect,400))
    
#     def test_integer_float(self):
#         input="""x: float = 7;
#         y: integer = x;"""
#         expect="Type mismatch in Variable Declaration: VarDecl(y, IntegerType, Id(x))"
#         self.assertTrue(TestChecker.test(input,expect,401))

#     def test_type_missmatch_in_vardecl(self):
#         input="""x: integer = 3.9;"""
#         expect="Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FloatLit(3.9))"
#         self.assertTrue(TestChecker.test(input,expect,402))

#     def test_type_missmatch_in_vardecl_2(self):
#         input="""x: boolean = 3;"""
#         expect="""Type mismatch in Variable Declaration: VarDecl(x, BooleanType, IntegerLit(3))"""
#         self.assertTrue(TestChecker.test(input,expect,403))
        
#     def test_type_missmatch_in_vardecl_3(self):
#         input="""x: string = 3;"""
#         expect="""Type mismatch in Variable Declaration: VarDecl(x, StringType, IntegerLit(3))"""
#         self.assertTrue(TestChecker.test(input,expect,404))

#     def test_auto_type(self):
#         input="""x: auto = 3;
# y: float = x;
# z: boolean = y;"""
#         expect="""Type mismatch in Variable Declaration: VarDecl(z, BooleanType, Id(y))"""
#         self.assertTrue(TestChecker.test(input,expect,405))

#     def test_auto_type_2(self):
#         input="""b : auto = " h e l l o " ;
# a: float = b;"""
#         expect="""Type mismatch in Variable Declaration: VarDecl(a, FloatType, Id(b))"""
#         self.assertTrue(TestChecker.test(input,expect,406))

    def test_auto_type_3(self):
        input="""c : auto = 10 < 100;
        a: boolean = c;
        b: float = a;
        """
        expect="""Type mismatch in Variable Declaration: VarDecl(c, BooleanType, Id(a))"""
        self.assertTrue(TestChecker.test(input,expect,407))