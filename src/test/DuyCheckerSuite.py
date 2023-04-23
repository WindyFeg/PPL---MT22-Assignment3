import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x, y, x: integer;"""
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 400))
    
    def test_long_vardecl1(self):
        input = """x, y, z: integer = 1,2,3;
                   a: float = x + 1;
                   b: integer = a + 1;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(+, Id(a), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_long_vardecl2(self):
        input = """x, y, z: integer = 1,2,3;
                   a: float = x + 1;
                   b: integer = a == 1;"""
        expect = "Type mismatch in expression: BinExpr(==, Id(a), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test_long_vardecl3(self):
        input = """x, y, z: integer = 1,2,3;
                   a: boolean = 2 == 1;
                   b: integer = a != 1;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(!=, Id(a), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test_long_vardecl4(self):
        input = """x, y, z: integer = 1,2,3;
                   a: boolean = 2 == 1;
                   b: auto = a;
                   c: integer = b;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 404))
    
    def test_long_vardecl5(self):
        input = """a: array [2] of integer;
                    b: integer = a;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test_undeclared(self):
        input = """a: integer = b;"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test_long_vardecl6(self):
        input = """b: integer = a[1];"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_long_vardecl7(self):
        input = """a: array [2] of integer;
                    b: integer = a[1.0];"""
        expect = "Type mismatch in expression: ArrayCell(a, [FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 408))
    
    def test_long_vardecl8(self):
        input = """a: array [2] of boolean;
                    b: integer = a[1];"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayCell(a, [IntegerLit(1)]))"
                  
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_long_vardecl81(self):

        input = """
                a: array [2] of integer = {1,2};
                  b: string = a[1];"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, StringType, ArrayCell(a, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 410))
    
    # def test_long_vardecl9(self):

    #     input = """
    #               main: function void(){}"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayCell(a, [IntegerLit(1)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 411))
    
    def test_long_vardecl10(self):

        input = """
                    a: array [2,2] of integer = {{1,2}, {1,2,3} };
                  b: string = a[1];"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])"
        self.assertTrue(TestChecker.test(input, expect, 412))
    def test_program(self):

        input = """ a: array [2] of integer = {1,2};
                    main: function auto(out i: auto){

                    for(i = 7, i + 4, i + 0){}
                    }
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 413))   
    
    def test_redeclare_function(self):

        input = """ a: array [2] of integer = {1,2};
                    a: function auto(out i: auto){
                    break;
                    for(i = 7, i + 4, i + 0){}
                    }
                """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 414))
    
    def test_redeclare_function_2(self):

        input = """ 
                    a: function void(){}
                    a: function auto(out i: auto){
                    break;
                    for(i = 7, i + 4, i + 0){}
                    }
                """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 415))
    
    def test_redeclare_parameter(self):

        input = """ 
                    a: function void(a: integer, b: float, a: auto){}
                    a: function auto(out i: auto){
                    break;
                    for(i = 7, i + 4, i + 0){}
                    }
                """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 416))
    
    

    
    

    def test_redeclare_inside_func(self):

        input = """
                    a: function auto(out i: auto){
                        x, y, z: integer;
                        y: integer;
                        x, y, z: integer = 1,2,3;
                        a: boolean = 2 == 1;
                        b: auto = a;
                        c: integer = b;
                    }
                """
        expect = "Redeclared Variable: y"
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test_redeclare_inside_func2(self):

        input = """
                    a: function auto(out i: auto){
                        x, y, z: integer = 1,2,3;
                        a: boolean = 2 == 1;
                        b: auto = a;
                        c: integer = b;
                    }
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 418))
    
    def test_inside_func(self):

        input = """
                    a: function auto(out i: auto){
                        x, y, z: integer = 1,2,3;
                        a: boolean = 2 == 1;
                        b: auto;
                        c: integer = b;
                    }
                """
        expect = "Invalid Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 419))
    
    def test_inside_func(self):

        input = """
                    a: function auto(out i: auto){
                        x, y, z: integer = 1,2,3;
                        a: boolean = 2 == 1;
                        b: auto;
                        c: integer = b;
                    }
                """
        expect = "Invalid Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 420))
    
    def test_inside_func_1(self):

        input = """
                    x: boolean;
                    a: function auto(out i: auto){
                        y, z: integer = 2,3;
                        a: boolean = 2 == 1;
                        c: integer = x;
                    }
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_inside_func_2(self):

        input = """
                    x: boolean;
                    a: function auto(out i: auto){
                        if (1 + 1) {
                            x = 2;
                        }
                    }
                """
        expect = "Type mismatch in statement: IfStmt(BinExpr(+, IntegerLit(1), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), IntegerLit(2))]))"
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test_inside_func_3(self):

        input = """
                    x: boolean;
                    a: function auto(out i: auto){
                        if (1 == 1) {
                            x:integer = 2.0;
                        }
                    }
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 423))
    
    def test_assign(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out i: auto){
                        foo = 1;
                    }
                """
        expect = "Type mismatch in statement: AssignStmt(Id(foo), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 424))
    
    def test_assign_1(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    a: array [2] of integer;
                    main: function auto(out i: auto){
                        a = 1;
                    }
                """
        expect = "Type mismatch in statement: AssignStmt(Id(a), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test_assign_2(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    a: boolean;
                    main: function auto(out i: auto){
                        a = "hello";
                    }
                """
        expect = "Type mismatch in statement: AssignStmt(Id(a), StringLit(hello))"
        self.assertTrue(TestChecker.test(input, expect, 426))
    
    def test_for(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    a: integer = 1;
                    main: function auto(out i: auto){
                        for (a = 0, a < 2, a + 1) {
                            
                        }
                    }
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 427))
    
    def test_for_1(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out i: auto){
                        for (a = 0, a < 2, a + 1) {
                            
                        }
                    }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_for_2(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out i: auto){
                        a: integer;
                        for (a = 0, b < 2, a + 1) {
                            b: integer = c;
                        }
                    }
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_blockinblock(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out i: auto){
                        a: integer;
                        for (a = 0, a < 2, a + 1) {
                            b: integer = y;
                        }
                    }
                """
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test_break(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out i: auto){
                        a: integer;
                        for (a = 0, a < 2, a + 1) {
                            b: integer = a;
                            break;
                        }

                    }
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 431))
    
    def test_breaK_2(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out i: auto){
                        a: integer;
                        break;
                        for (a = 0, a < 2, a + 1) {
                            b: integer = a;
                            
                        }

                    }
                """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test_continue(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out i: auto){
                        a: integer;
                        continue;
                        for (a = 0, a < 2, a + 1) {
                            b: integer = a;
                            
                        }

                    }
                """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test_continue_2(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out i: auto){
                        a: integer;
                        continue;
                        for (a = 0, a < 2, a + 1) {
                            b: integer = a;
                            
                        }

                    }
                """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_while(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out z: auto){
                        a: integer;
                        for (a = 0, a < 2, a + 1) {
                            b: integer = a;
                        }
                        i,j : integer = 0, 10;
                        while (j>0){
                                i=i+1;
                                j = j + 2;
                                a = i + j; 
                                b = i + j;
                        }
                    }
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test_while_2(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out z: auto){
                        a: integer;
                        i,j : integer = 0, 10;
                        while (j > 0){
                                i=i+1;
                                j = j + 2;
                                a = i + j; 
                                break;
                                b = i + j;
                        }
                    }
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 434))
    
    def test_while_3(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out z: auto){
                        a: integer;
                        i,j : integer = 0, 10;
                        while (j + 0){
                                i=i+1;
                                j = j + 2;
                                a = i + j; 
                                break;
                                b = i + j;
                        }
                    }
                """
        expect = "Type mismatch in statement: WhileStmt(BinExpr(+, Id(j), IntegerLit(0)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(2))), AssignStmt(Id(a), BinExpr(+, Id(i), Id(j))), BreakStmt(), AssignStmt(Id(b), BinExpr(+, Id(i), Id(j)))]))"
        self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test_if_else(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out i: auto){
                        a: integer;
                        i,j : integer = 0, 10;
                        arr: array [3] of string = {"a","b","c"};
                                if(arr[i] == "a") break;
                                else{
                                    if(i%3==0) arr[i] = arr[i] + "d";
                                    else arr[i] = "d";
                                }
                    }
                """
        expect = "Type mismatch in expression: BinExpr(==, ArrayCell(arr, [Id(i)]), StringLit(a))"
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test_if_else(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out z: auto){
                        a: integer;
                        i,j : integer = 0, 10;
                        arr: array [3] of integer = {"a","b","c"};
                                if(arr[i] == 2) break;
                                else{
                                    if(i%3==0) arr[i] = arr[i] + "d";
                                    else arr[i] = "d";
                                }
                    }
                """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test_if_else_2(self):

        input = """
                    x: boolean;
                    main: function auto(out z: auto){
                        a: integer;
                        i,j : integer = 0, 10;
                        arr: array [3] of integer = {"a","b","c"};
                                if(i == 2) arr[i] = 2;
                                else{
                                    if(i%3==0) arr[i] = arr[i] + "d";
                                    else arr[i] = "d";
                                }
                    }
                """
        expect = "Type mismatch in expression: BinExpr(+, ArrayCell(arr, [Id(i)]), StringLit(d))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_dowhile(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out z: auto){
                        a: integer;
                        i,j : integer = 0, 10;
                        do {a = a + 1;} while(a == 2);
                    }
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 439))
    
    def test_dowhile_1(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out z: auto){
                        a: integer;
                        i,j : integer = 0, 10;
                        do {
                            while (j>0){
                                i=i+1;
                                j = j + 2; 
                                arr: array[3] of string = {"a","b","c"};
                                if(arr[i] == 1) break;
                                else{
                                    if(i%3==0) arr[i] = arr[i] + "d";
                                    else arr[i] = "d";
                                }
                            }
                            } while (i > 0);
                    }
                """
        expect = "Type mismatch in expression: BinExpr(==, ArrayCell(arr, [Id(i)]), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 441))
    
    def test_dowhile_2(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out z: auto){
                        a: integer;
                        i,j : integer = 0, 10;
                        do {
                            while (j>0){
                                i=i+1;
                                j = j + 2; 
                                arr: array[3] of integer = {"a","b","c"};
                                if(arr[i] == 1) break;
                                else{
                                    if(i%3==0) arr[i] = arr[i] + 10;
                                    else arr[i] = "d";
                                }
                            }
                            } while (i > 0);
                    }
                """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(arr, [Id(i)]), StringLit(d))"
        self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test_funcall_1(self):

        input = """
                    x: boolean;
                    foo: function void(){}
                    main: function auto(out i: auto){
                        foo = 2;
                    }
                """
        expect = "Type mismatch in statement: AssignStmt(Id(foo), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 443))
    
    def test_funcall_2(self):

        input = """
                    x: boolean;
                    foo: function integer(){}
                    main: function auto(out i: auto){
                        i = foo();
                        break;
                    }
                """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 444))
    
    def test_funcall_3(self):

        input = """
                    x: boolean;
                    foo: function integer(){}
                    main: function auto(out i: float){
                        i = foo();
                        break;
                    }
                """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 446))
    
    def test_funcall_4(self):

        input = """
                    x: boolean;
                    foo: function integer(){}
                    main: function auto(out i: string){
                        i = foo();
                        break;
                    }
                """
        expect = "Type mismatch in statement: AssignStmt(Id(i), FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test_funcall_5(self):

        input = """
                    x: boolean;
                    foo: function integer(a: integer, b: float){}
                    main: function auto(out i: string){
                        i = foo(1,2);
                        break;
                    }
                """
        expect = "Type mismatch in statement: AssignStmt(Id(i), FuncCall(foo, [IntegerLit(1), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 448))
    
    def test_funcall_6(self):

        input = """
                    x: boolean;
                    foo: function integer(a: integer, b: float){}
                    main: function auto(out i: string){
                        i = foo(1,"hello");
                        break;
                    }
                """
        expect = "Type mismatch in statement: FuncCall(foo, [IntegerLit(1), StringLit(hello)])"
        self.assertTrue(TestChecker.test(input, expect, 449))
    
    def test_return(self):

        input = """
                    x: boolean;
                    foo: function integer(a: integer, b: float){}
                    main: function auto(out i: auto){
                        i = foo(1,2);
                        return;
                    }
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test_return_1(self):

        input = """
        x: boolean;
        foo: function integer(a: integer, b: float){
        
        }
        main: function float(out i: auto){
            i = foo(1,2);
            return 2;
            return 2.0;
            return "hello";
        }
                """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(hello))"
        self.assertTrue(TestChecker.test(input, expect, 451))
    
    def test_return_2(self):

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
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test_inherit(self):

        input = """
                    a: integer;
                    foo : function auto(){
                    foo2(1,2,3);
                    while(a + 10){
                        a = a + 1;
                        break;
                        return a;
                    }
                        a = a + 1;
                    return "hello";   
                    }
                """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test_inherit1(self):

        input = """
                    a: integer;
                    foo : function auto() inherit foo2{}
                    foo2: function void(a: integer, b: integer){}
                """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test_inherit2(self):

        input = """
                    a: integer;
                    foo : function auto() inherit foo2{}
                    foo2: function void(){}
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test_inherit3(self):

        input = """
                    a: integer;
                    foo : function auto() inherit foo2{
                        a: integer = 1;
                    }
                    foo2: function void(a: integer, b: integer){}
                """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test_inherit4(self):

        input = """
                    a: integer;
                    foo : function auto() inherit foo2{
                        foo3();
                        a: integer = 1;
                    }
                    foo2: function void(a: integer, b: integer){}
                    foo3: function void(){}
                """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test_inherit5(self):

        input = """
                    a: integer;
                    foo : function auto() inherit foo2{
                        super();
                        a: integer = 1;
                    }
                    foo2: function void(a: integer, b: integer){}
                    foo3: function void(){}
                """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 458))
    
    def test_inherit6(self):

        input = """
                    a: integer;
                    foo : function auto() inherit foo2{
                        super(1,1);
                        a: integer = 1;
                    }
                    foo2: function void(a: integer, b: integer){}
                    foo3: function void(){}
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 459))
    
    def test_inherit7(self):

        input = """
                    a: integer;
                    foo : function auto() inherit foo2{
                        super(1,1);
                        a: integer = 1;
                    }
                    foo2: function void(a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_inherit_8(self):

        input = """
                    a: integer;
                    foo : function auto() inherit foo2{
                        super(1.0,1.0);
                        a: integer = 1;
                    }
                    foo2: function void(a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_inherit_9(self):

        input = """
                    a: integer;
                    foo : function auto(a: integer) inherit foo2{
                        super(1.0,1.0);
                        a: integer = 1;
                    }
                    foo2: function void(inherit a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test_inherit_10(self):

        input = """
                    a: integer;
                    foo : function auto(inherit a: integer) inherit foo2{
                        super(1.0,1.0);
                        a: integer = 1;
                    }
                    foo2: function void(a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 463))
    
    def test_callstmt(self):

        input = """
                    a: integer;
                    foo : function auto(inherit a: integer) inherit foo2{
                        super(a,a);
                        a: integer = 1;
                    }
                    foo2: function void(a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 464))
    
    def test_callstmt_2(self):

        input = """
                    a: integer;
                    foo : function auto(inherit a: integer) inherit foo2{
                        super(a,b);
                        a: integer = 1;
                    }
                    foo2: function void(a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test_callstmt_3(self):

        input = """
                    a: integer;
                    foo : function auto(inherit a: integer) inherit foo2{
                        super(a,b);
                        a: integer = 1;
                    }
                    foo2: function void(a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test_callstmt_4(self):

        input = """
                    a: integer;
                    foo : function auto(inherit a: integer) inherit foo2{
                        preventDefault();
                        a: integer = 1;
                    }
                    foo2: function void(a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test_callstmt_5(self):

        input = """
                    a: integer;
                    foo : function auto(inherit a: integer) inherit foo2{
                        preventDefault(1);
                        a: integer = 1;
                    }
                    foo2: function void(a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "Type mismatch in statement: CallStmt(preventDefault, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test_callstmt_6(self):

        input = """
                    a: integer;
                    foo : function auto( a: integer) inherit foo2{
                        preventDefault(1);
                        a: integer = 1;
                    }
                    foo2: function void(inherit a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test_callstmt_7(self):

        input = """
                    a: integer;
                    foo : function auto( b: integer) inherit foo2{
                        preventDefault();
                        a: integer = 1;
                    }
                    foo2: function void(inherit a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 469))
    
    def test_callstmt_7(self):

        input = """
                    a: integer;
                    foo : function auto( b: integer) inherit foo2{
                        preventDefault();
                        a: integer = 1;
                        readInteger();
                        printInteger();
                    }
                    foo2: function void(inherit a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "Type mismatch in statement: CallStmt(printInteger, )"
        self.assertTrue(TestChecker.test(input, expect, 470))
    
    def test_callstmt_8(self):

        input = """
                    a: integer;
                    foo : function auto( b: integer) inherit foo2{
                        preventDefault();
                        a: integer = 1;
                        readInteger();
                        printInteger(1);
                        readFloat();
                        writeFloat(2.0);
                    }
                    foo2: function void(inherit a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 471))
    
    def test_callstmt_8(self):

        input = """
                    a: integer;
                    foo : function auto( b: integer) inherit foo2{
                        preventDefault();
                        a: integer = 1;
                        readInteger();
                        printInteger(1);
                        readFloat();
                        writeFloat(2);
                        readBoolean();
                        printBoolean(true);
                        readString();
                        printString("Hello");
                    }
                    foo2: function void(inherit a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test_array_0(self):

        input = """
                    a: integer;
                    arr: array [2] of integer = {1,2,3};
                    foo : function auto( b: integer) inherit foo2{
                        preventDefault();
                        a: integer = 1;
                        readInteger();
                        printInteger(1);
                        readFloat();
                        writeFloat(2);
                        readBoolean();
                        printBoolean(true);
                        readString();
                        printString("Hello");
                    }
                    foo2: function void(inherit a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 473))
    
    def test_array_1(self):

        input = """
                    a: integer;
                    arr: array [2] of integer = {1.0,2};
                    foo : function auto( b: integer) inherit foo2{
                        preventDefault();
                        a: integer = 1;
                        a = arr[1];
                        readInteger();
                        printInteger(1);
                        readFloat();
                        writeFloat(2);
                        readBoolean();
                        printBoolean(true);
                        readString();
                        printString("Hello");
                    }
                    foo2: function void(inherit a: integer, b: float){}
                    foo3: function void(){}
                """
        expect = "Illegal array literal: ArrayLit([FloatLit(1.0), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 474))
    
    # def test_array_2(self):

    #     input = """
    #                 a: integer;
    #                 arr: array [2,3] of integer = {{1,2,3},{1,2,3}};
    #                 foo : function auto( b: integer) inherit foo2{
                        
    #                 }
    #                 foo2: function void(inherit a: integer, b: float){}
    #                 foo3: function void(){}
    #             """
    #     expect = "Illegal array literal: ArrayLit([FloatLit(1.0), IntegerLit(2)])"
    #     self.assertTrue(TestChecker.test(input, expect, 475))