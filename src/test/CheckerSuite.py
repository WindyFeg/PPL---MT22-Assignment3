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

#     def test_auto_type_3(self):
#         input="""c : auto = 10 < 100;
#         a: boolean = c;
#         b: float = a;
#         """
#         expect="""Type mismatch in Variable Declaration: VarDecl(b, FloatType, Id(a))"""
#         self.assertTrue(TestChecker.test(input,expect,407))

#     def test_bin_expr(self):
#         input="""a: integer = 3;
#         b: integer = 4;
#         c: integer = a + b;
#         d: float = a - b;
#         f: boolean = a * b;
#         """
#         expect="""Type mismatch in Variable Declaration: VarDecl(f, BooleanType, BinExpr(*, Id(a), Id(b)))"""
#         self.assertTrue(TestChecker.test(input,expect,408))

#     def test_bin_expr2(self):
#         input= """
#         a: integer = 3;
#         b: integer = 4 + a;
#         c: integer = a + true;
#         """
#         expect="""Type mismatch in expression: BinExpr(+, Id(a), BooleanLit(True))"""
#         self.assertTrue(TestChecker.test(input,expect,409))

#     def test_bin_expr3(self):
#         input= """
#         a: integer = 3;
#         b: float = 4 + a;
#         c: integer = b + 10;
#         """
#         expect="""Type mismatch in Variable Declaration: VarDecl(c, IntegerType, BinExpr(+, Id(b), IntegerLit(10)))"""
#         self.assertTrue(TestChecker.test(input,expect,410))

#     def test_bin_expr4(self):
#         input= """
#         a: integer = 3;
#         c: integer = 10;
#         d: auto = 10 % 3;
#         f: boolean = d;
#         """
#         expect="""Type mismatch in Variable Declaration: VarDecl(f, BooleanType, Id(d))"""
#         self.assertTrue(TestChecker.test(input,expect,411))

#     def test_bin_expr5(self):
#         input = """
#         a: integer = 7;
#         b: boolean = true;
#         c: boolean = false;
#         d: float = ((b || c) && c) && a;
#         """
#         expect = """Type mismatch in expression: BinExpr(&&, BinExpr(&&, BinExpr(||, Id(b), Id(c)), Id(c)), Id(a))"""
#         self.assertTrue(TestChecker.test(input,expect,412))

    # def test_bin_expr6(self):
    #     input = """
    #     a: string = "halo";
    #     b: string = a :: "balo";
    #     c: boolean = a && b;
    #     """
    #     expect = """Type mismatch in expression: BinExpr(&&, Id(a), Id(b))"""
    #     self.assertTrue(TestChecker.test(input,expect,413))

#     def test_bin_expr7(self):
#         input = """
# d : auto;
# e : auto = 1 + d;
#         """
#         expect = """Invalid Variable: VarDecl(d, AutoType)"""
#         self.assertTrue(TestChecker.test(input,expect,414))

#     def test_bin_expr8(self):
#         input = """
# a : auto = 1;
# b : auto = 2.0;
# c : auto = a <= b;
# d : auto = a == b;
#         """
#         expect = """Type mismatch in expression: BinExpr(==, Id(a), Id(b))"""
#         self.assertTrue(TestChecker.test(input,expect,415))

#     def test_long_vardecl(self):
#         input = """x, y, z: integer = 1,2,3;
#                    a: float = x + 1;
#                    b: integer = a + 1;"""
#         expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(+, Id(a), IntegerLit(1)))"
#         self.assertTrue(TestChecker.test(input, expect, 416))

    # def test_array_decl(self):
    #     input = """a: array [1,2] of integer;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 417))

    # def test_array_decl2(self):
    #     input = """
    #     a: array [1,2] of boolean = {true, true};
    #     """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 418))

    # def test_array_decl3(self):
    #     input = """
    #     a: array [1,2] of boolean = {true, 1};
    #     """
    #     expect = "Type mismatch in expression: ArrayLit([BooleanLit(True), IntegerLit(1)])"
    #     self.assertTrue(TestChecker.test(input, expect, 419))

    # def test_array_decl3(self):
    #     input = """
    #     a: array [1,2] of string = {"true", "1"};
    #     b: array [1,2] of boolean = {true, 1};
    #     """
    #     expect = "Type mismatch in expression: ArrayLit([BooleanLit(True), IntegerLit(1)])"
    #     self.assertTrue(TestChecker.test(input, expect, 420))

    # def test_array_decl4(self):
    #     input = """
    #     a: array [1,2] of string = {"true", "1"};
    #     a: array [1,2] of boolean = {true, 1};
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 421))

    # def test_array_decl5(self):
    #     input = """
    #     a: array [1,2] of string = {"true", "1"};
    #     b: array [1,2,3,4] of string = {a[1]};
    #     """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 422))
    
    # def test_array_decl6(self):
    #     input = """
    #     a: array [1,2] of string = {"true", "1"};
    #     b: array [1,2,3,4] of boolean = {a[1]};
    #     """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(b, ArrayType([1, 2, 3, 4], BooleanType), ArrayLit([ArrayCell(a, [IntegerLit(1)])]))"
    #     self.assertTrue(TestChecker.test(input, expect, 423))

    def test_auto_array(self):
        input = """
        a: array [1,2] of auto = {"true", "1"};
        b: array [1,2,3,4] of auto = {a[1]};
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_auto_array1(self):
        input = """
        a: array [1,2] of auto = {"true", "1"};
        b: array [1,2,3,4] of auto = {1};
        d: boolean = false;
        c: array [1,2,3,4] of auto = {a[1], d, b[1]};
        """
        expect = "Type mismatch in expression: ArrayLit([ArrayCell(a, [IntegerLit(1)]), Id(d), ArrayCell(b, [IntegerLit(1)])])"
        self.assertTrue(TestChecker.test(input, expect, 425))