import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input="""x: integer = 3.9;"""
        expect="Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FloatLit(3.9))"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_integer_float(self):
        input="""x: float = 7;
        y: integer = x;"""
        expect="Type mismatch in Variable Declaration: VarDecl(y, IntegerType, Id(x))"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_type_missmatch_in_vardecl(self):
        input="""x: integer = 3.9;"""
        expect="Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FloatLit(3.9))"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_type_missmatch_in_vardecl_2(self):
        input="""x: boolean = 3;"""
        expect="""Type mismatch in Variable Declaration: VarDecl(x, BooleanType, IntegerLit(3))"""
        self.assertTrue(TestChecker.test(input,expect,403))
        
    def test_type_missmatch_in_vardecl_3(self):
        input="""x: string = 3;"""
        expect="""Type mismatch in Variable Declaration: VarDecl(x, StringType, IntegerLit(3))"""
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_auto_type(self):
        input="""x: auto = 3;
y: float = x;
z: boolean = y;"""
        expect="""Type mismatch in Variable Declaration: VarDecl(z, BooleanType, Id(y))"""
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_auto_type_2(self):
        input="""b : auto = " h e l l o " ;
a: float = b;"""
        expect="""Type mismatch in Variable Declaration: VarDecl(a, FloatType, Id(b))"""
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_auto_type_3(self):
        input="""c : auto = 10 < 100;
        a: boolean = c;
        b: float = a;
        """
        expect="""Type mismatch in Variable Declaration: VarDecl(b, FloatType, Id(a))"""
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_bin_expr(self):
        input="""a: integer = 3;
        b: integer = 4;
        c: integer = a + b;
        d: float = a - b;
        f: boolean = a * b;
        """
        expect="""Type mismatch in Variable Declaration: VarDecl(f, BooleanType, BinExpr(*, Id(a), Id(b)))"""
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_bin_expr2(self):
        input= """
        a: integer = 3;
        b: integer = 4 + a;
        c: integer = a + true;
        """
        expect="""Type mismatch in expression: BinExpr(+, Id(a), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_bin_expr3(self):
        input= """
        a: integer = 3;
        b: float = 4 + a;
        c: integer = b + 10;
        """
        expect="""Type mismatch in Variable Declaration: VarDecl(c, IntegerType, BinExpr(+, Id(b), IntegerLit(10)))"""
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_bin_expr4(self):
        input= """
        a: integer = 3;
        c: integer = 10;
        d: auto = 10 % 3;
        f: boolean = d;
        """
        expect="""Type mismatch in Variable Declaration: VarDecl(f, BooleanType, Id(d))"""
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_bin_expr5(self):
        input = """
        a: integer = 7;
        b: boolean = true;
        c: boolean = false;
        d: float = ((b || c) && c) && a;
        """
        expect = """Type mismatch in expression: BinExpr(&&, BinExpr(&&, BinExpr(||, Id(b), Id(c)), Id(c)), Id(a))"""
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_bin_expr6(self):
        input = """
        a: string = "halo";
        b: string = a :: "balo";
        c: boolean = a && b;
        """
        expect = """Type mismatch in expression: BinExpr(&&, Id(a), Id(b))"""
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_bin_expr7(self):
        input = """
d : auto;
e : auto = 1 + d;
        """
        expect = """Invalid Variable: d"""
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_bin_expr8(self):
        input = """
a : auto = 1;
b : auto = 2.0;
c : auto = a <= b;
d : auto = a == b;
        """
        expect = """Type mismatch in expression: BinExpr(==, Id(a), Id(b))"""
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_long_vardecl(self):
        input = """x, y, z: integer = 1,2,3;
                   a: float = x + 1;
                   b: integer = a + 1;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(+, Id(a), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_array_decl(self):
        input = """a: array [1,2] of integer;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_array_decl2(self):
        input = """
        a: array [2] of boolean = {true, true};
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_array_decl3(self):
        input = """
        a: array [1,2] of boolean = {true, 1};
        """
        expect = "Illegal array literal: ArrayLit([BooleanLit(True), IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_array_decl3(self):
        input = """
        a: array [1,2] of string;
        b: array [2] of boolean = {true, 1};
        """
        expect = "Illegal array literal: ArrayLit([BooleanLit(True), IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_array_decl4(self):
        input = """
        a: array [1,2] of string;
        a: array [1,2] of boolean = {true, 1};
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_array_decl5(self):
        input = """
        a: array [1,2] of string;
        b: array [1,2,3,4] of string = { a[1] };
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, ArrayType([1, 2, 3, 4], StringType), ArrayLit([ArrayCell(a, [IntegerLit(1)])]))"
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test_array_decl6(self):
        input = """
        a: array [1,2] of string = {"true", "1"};
        b: array [1,2,3,4] of boolean = {a[1]};
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([1, 2], StringType), ArrayLit([StringLit(true), StringLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_auto_array(self):
        input = """
        a: array [1,2] of auto = {"true", "1"};
        b: array [1] of auto = {a[1]};
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([1, 2], AutoType), ArrayLit([StringLit(true), StringLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_auto_array1(self):
        input = """
        a: array [1,2] of auto = {"true", "1"};
        b: array [1,2,3,4] of auto = {1};
        d: boolean = false;
        c: array [1,2,3,4] of auto = {a[1], d, b[1]};
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([1, 2], AutoType), ArrayLit([StringLit(true), StringLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_auto_array2(self):
        input = """
        a: string;
        b: auto = a;
        b = "aloha";
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_assign_stmt(self):
        input = """
        /*$?? b still dose not have any value*/ 
        a: integer;
        b: float;
        a = b + 1;
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), BinExpr(+, Id(b), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_assign_stmt1(self):
        input = """
        /*$?? b still dose not have any value*/ 
        a: integer;
        b: float;
        c: boolean;
        a = 2012;
        b = a + 239.8;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_long_vardecl6(self):
        input = """b: integer = a[1];"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_long_vardecl7(self):
        input = """a: array [2] of integer;
                    b: integer = a[1.0];"""
        expect = "Type mismatch in expression: ArrayCell(a, [FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test_long_vardecl8(self):
        input = """a: array [2] of boolean;
                    b: integer = a[1];"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayCell(a, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_long_vardecl9(self):
        input = """a: array [2,2] of integer = { { {1,"a"} , {3,4} }, { {5,6}, {7,8} } };"""
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), StringLit(a)])"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_long_vardecl10(self):
        input = """
a: array [2,2] of integer = { {1,2}, {1,2,3} };
                  b: string = a[1];"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))"
        self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test_long_vardecl11(self):
        input = """
a: array [2,2] of auto = { {1,2}, {1, true} };
                    b: integer = a[1];"""
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_function(self):
        input = """
        foo: integer = 2;
        foo : function integer (c: integer, b: integer) {
        
        }
        """
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_auto_array3(self):
        input = """
        a: string;
        b: auto = a;
        arr: array [1,2] of auto = { b };
        b = "1" :: arr[4];
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([1, 2], AutoType), ArrayLit([Id(b)]))"
        self.assertTrue(TestChecker.test(input, expect, 436))
    

    def test_auto_array4(self):
        input = """
        a: string;
        b: auto = a;
        arr: array [1,2] of auto = { b };
        b = "1" :: arr[4];
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([1, 2], AutoType), ArrayLit([Id(b)]))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_function2(self):
        input = """
        foo: integer = foo2(1,2);
        foo : function integer (c: integer, d: integer) {
        }
        """
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_function3(self):
        input = """
        foo: integer = foo2(1,2);
        foo2 : function integer (c: integer, c: integer) {
        }
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_function4(self):
        input = """
        foo: integer = foo2(1,2);
        foo2 : function integer (c: integer, d: float) {
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_function5(self):
        input = """
        foo: integer = foo2(1,2);
        foo2 : function integer (c: integer, d: float) {
            return;
        }
        """
        expect = "Type mismatch in statement: ReturnStmt()"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_function6(self):
        input = """
        foo: integer = foo2(1.0,2);
        foo2 : function integer (c: integer, d: float) {
        }
        """
        # expect = "Type mismatch in expression: FuncCall(foo2, [FloatLit(1.0), IntegerLit(2)])"
        expect = "Type mismatch in expression: FloatLit(1.0)"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_function7(self):
        input = """
        foo: integer = foo2(1.0,2);
        foo2 : function integer (c: auto, d: auto) {
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_function8(self):
        input = """
        foo2 : function integer (c: auto, d: auto) inherit foo {
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_function9(self):
        input = """
        foo: integer = foo2(1,2);
        foo2 : function auto (c: integer, d: integer) {
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_function10(self):
        input = """
        a: integer;
        b: integer;
        b: integer;
        a: integer;
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_function11(self):
        input = """
        foo : function integer (c: integer, d: integer) {
            a: integer;
            b: integer;
            b: integer;
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_function12(self):
        input = """
        foo : function integer (inherit c : integer, d: integer) {
            a: integer;
            b: float = 34.0;
            a = 2 + 34;
            b = a + 2.4;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_function13(self):
        input = """
        foo2: function auto (c: integer, d: integer, a: integer) inherit foo{
            
        }
        foo : function integer (inherit a : float, b: integer) {
        }
        """
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_function14(self):
        input = """
        foo2: function auto (c: integer, d: integer) inherit foo{
            preventDefault();
            a: integer;
        }
        foo : function integer (inherit a : float, b: integer) {
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_function15(self):
        input = """
        a: integer;
        foo2: function auto (c: integer, d: integer) inherit foo{
            a: integer;
        }
        foo : function integer ( a : float, b: integer) {
        }
        """
        expect = "Invalid statement in function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_function16(self):
        input = """
        a: integer;
        b: integer = 5;
        foo2: function auto (c: integer, d: integer) inherit foo{
            a: integer = b;
        }
        foo : function integer ( a : float, b: integer) {
        }
        """
        expect = "Invalid statement in function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_function17(self):
        input = """
        a: integer;
        b: integer = 5;
        foo2: function auto (c: integer, d: integer) inherit foo{
            super(1.0, 2);
            b: float = 5.0;
            a: integer = b;
            c: integer = foo(2.3,4);
        }
        foo : function integer ( a : float, b: integer) {
            a: integer = b;
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_confuse(self):
        input = """
        a: integer = foo();
        foo : function integer(){
            a = 100;
            return a;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 454))    

    def test_return(self):
        input = """
        a: integer = foo();
        foo : function integer(){
            a = 100;
            b: string;
            return b;
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 455))   

    def test_return2(self):
        input = """
        a: integer = foo();
        foo : function auto(){
            a = 100;
            b: string;
            return b;
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 456))   

    def test_return3(self):
        input = """
        a: integer;
        foo : function integer(){
            a = foo2();
        }

        foo2: function auto(){
            return 1.0;
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 457))   

    def test_declare_in_function(self):
        input = """
        a: integer;
        foo : function integer(){
            a: float;
        }

        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 458)) 

    def test_declare_in_function2(self):
        input = """
        a: integer;
        foo : function integer(){
            a: float;
            a: integer;
        }

        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 459)) 
    
    def test_declare_in_function3(self):
        input = """
        x: boolean;
        foo: function void(){ }
        main: function auto(out i: auto){
            a: integer;
            i,j : integer = 0, 10;
            while (j>0){
                    i=i+1;
                    j = j + 2;
                    a = i + j; 
                    break;
                    b = i + j;
            }
        }

        """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_loop(self):
        input = """
        a: integer;
        foo : function integer(){
            a: float;
            i: integer;
            for (i = 0, i < 10, i + 1){
                a = a + 1;
            }
        }

        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_loop2(self):
        input = """
        a: integer;
        foo : function integer(){
            a: float;
            i: integer;
            for (i = 1.0, i < 10, i + 1){
                a = a + 1;
                break;
                a = a + 1;
            }
        }

        """
        expect = "Type mismatch in statement: AssignStmt(Id(i), FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_loop3(self):
        input = """
        a: integer;
        foo : function integer(){
            a: float;
            i: integer;
            for (i = 0, i < 10, a + 1){
                a = a + 1;
                break;
                a = a + 1;
            }
        }

        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), BreakStmt(), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_loop4(self):
        input = """
        a: integer;
        foo : function integer(){
            a: float;
            i: integer;
            for (i = 0, i < 10, i + 1){
                a: integer;
                break;
            }
            a = a + 1;
        }

        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_loop5(self):
        input = """
        a: integer;
        foo : function integer(){
            a: float;
            i: integer;
            break;
            /*for (i = 0, i < 10, i + 1){
                a: integer;
                break;
                a = a + 1;
            }*/
        }

        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 465))    

    def test_loop6(self):
        input = """
        a: integer;
        continue;
        foo : function integer(){
            a: float;
            i: integer;
            continue;
            /*for (i = 0, i < 10, i + 1){
                a: integer;
                break;
                a = a + 1;
            }*/
        }

        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_loop7(self):
        input = """
        a: integer;
        foo : function integer(){
            while(a<10){
                a = a + 1;
                continue;
            }
            
        }

        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_loop8(self):
        input = """
        a: integer;
        foo : function integer(){
            while(a<10){
                a = a + 1;
                break;
            }
            a = a + 1;
            break;
        }

        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test_loop9(self):
        input = """
        a: integer;
        foo : function integer(){
            while(a<10){
                a = a + 1;
                continue;
            }
            a = a + 1;
            continue;
        }

        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_loop10(self):
        input = """
        a: integer;
        foo : function auto(){
            while(a<10){
                a = a + 1;
                break;
                return a;
            }
            a = a + 1;
            
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_loop11(self):
        input = """
        foo : function auto(){
            while(a<10){
                a = a + 1;
                break;
                return a;
            }
            a = a + 1;
         return 1.0;   
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 471))
    
    def test_loop12(self):
        input = """
        a: integer;
        foo : function auto(){
            while(a<10){
                break;
                return a;
            }
         return 1.0;   
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_declare_in_function3(self):
        input = """
        x: boolean;
        foo: function void(){ }
        main: function auto(out z: auto){
            a: integer;
            i,j : integer = 0, 10;
            while (j>0){
                    i=i+1;
                    j = j + 2;
                    a = i + j; 
                    break;
                    b = i + j;
            }
        }

        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_declare_in_function4(self):
        input = """
        a: integer;
                    foo : function auto(){
                    while(a<10){
                        a = a + 1;
                        break;
                        return a;
                    }
                        a = a + 1;
                    return "hello";   
                    }

        """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(hello))"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_void(self):
        input = """
        foo();
        foo : function auto(){
            a = a + 1;
            return;
        }

        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_void2(self):
        input = """
        foo();
        foo : function auto(){
            a: auto = "ase";
            return;
        }

        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_void3(self):
        input = """
        foo();
        foo : function string(){
            a: auto = "ase";
            return a;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_if(self):
        input = """
        foo();
        a: integer;
        foo : function auto(){
            if (a<10){
                a = a + 1;
                return a;
            }
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_if2(self):
        input = """
        a: integer;
        foo : function auto(){
            if (a<10){
                a = a + 1;
                return a;
            }
            
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_if3(self):
        input = """
        a: integer;
        foo : function auto(){
            if (a<10){
                a = a + 1;
                return a;
            }else{
                a = a + 1;
                return true;
            }
            
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_if4(self):
        input = """
        a: integer;
        foo : function auto(){
            if (a<10){
                a = a + 1;
                return a;
            }else{
                a = a + 1;
                if (a>10){
                    return 1;
                }
                else{
                    return true;
                }
            }
            
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test_dowhile(self):
        input = """
        a: integer;
        foo : function auto(){
            do{
                a = a + 1;
                return a;
            }while(a<10);
            
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test_dowhile2(self):
        input = """
        a: integer;
        foo : function auto(){
            do{
                a = a + 1;
                return a;
                for(i = 1, i<10, i+1){
                    if (i>10){
                        return 1;}
                    else{
                        return true;
                    }
                }
            }while(a<10);
            return true;
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_inheritfunc(self):
        input = """
        foo: function auto() inherit foo2{
            preventDefault();
            return a;
        }

        foo2: function auto(inherit a: integer){
        
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_inheritfunc2(self):
        input = """
        foo: function auto() inherit foo2{
            
            return a;
        }

        foo2: function auto(){
                a: integer;
                return a;
        }
        """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_inheritfunc3(self):
        input = """
        foo: function auto() inherit foo2{
            i: integer = 23;
            return a;
        }

        foo2: function auto(){
                a: integer;
                return a;
        }
        """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_inheritfunc4(self):
        input = """
        foo: function auto() inherit foo2{
            foo2();
            i: integer = 23;
            return a;
        }

        foo2: function auto(){
                a: integer;
                return a;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_inheritfunc5(self):
        input = """
        foo: function auto() inherit foo2{
            super();
            foo2();
            i: integer = 23;
            return a;
        }

        foo2: function auto(){
                a: integer;
                return a;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_arrayy(self):
        input = """
        a : array [1, 2] of integer = {{1, 1}};
        main: function void (){
            b : integer = a[1,2] + 2 + 3;
            if (b == 1) return "lol";
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(lol))"
        self.assertTrue(TestChecker.test(input, expect, 489))
