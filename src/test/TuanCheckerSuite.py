import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = Program([VarDecl("x", IntegerType())])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_full_vardecl(self):
        input = """x : integer;
        x : float;
        main: function void (){}"""
        expect = """Redeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_short_vardecl_1(self):
        input = """x : integer = y + 1;
        main: function void (){}"""
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_short_vardecl_2(self):
        input = """x : integer = 1.234;
        main: function void (){}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FloatLit(1.234))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_short_vardecl_3(self):
        input = """x : integer = true;
        main: function void (){}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_short_vardecl_4(self):
        input = """x : integer = "string";
        main: function void (){}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_short_vardecl_5(self):
        input = """x : integer = "string";
        main: function void (){}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_short_vardecl_6(self):
        input = """x : integer = 1+1;
        main: function void (){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_short_vardecl_7(self):
        input = """x : integer = true + true;
        main: function void (){}"""
        expect = "Type mismatch in expression: BinExpr(+, BooleanLit(True), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_short_vardecl_8(self):
        input = """x, y : integer = 1, 2;
        main: function void (){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_short_vardecl_9(self):
        input = """x, y : integer = 1, true;
        main: function void (){}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(y, IntegerType, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_short_vardecl_10(self):
        input = """x: boolean = true;
        main: function void (){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_short_vardecl_11(self):
        input = """x: boolean = 1 < 2;
        main: function void (){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_short_vardecl_12(self):
        input = """x: boolean = 1 < true;
        main: function void (){}"""
        expect = "Type mismatch in expression: BinExpr(<, IntegerLit(1), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_short_vardecl_13(self):
        input = """x: boolean = 1 < 2.12;
        main: function void (){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_short_vardecl_14(self):
        input = """x: boolean = 1 == 2.12;
        main: function void (){}"""
        expect = "Type mismatch in expression: BinExpr(==, IntegerLit(1), FloatLit(2.12))"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_short_vardecl_15(self):
        input = """x: string = 1 :: 2.12;
        main: function void (){}"""
        expect = "Type mismatch in expression: BinExpr(::, IntegerLit(1), FloatLit(2.12))"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_short_vardecl_16(self):
        input = """x: string = "Hello" :: "World";
        main: function void (){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_short_vardecl_17(self):
        input = """x: boolean = "Hello" && "World";
        main: function void (){}"""
        expect = "Type mismatch in expression: BinExpr(&&, StringLit(Hello), StringLit(World))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_short_vardecl_18(self):
        input = """x: boolean = ! true;
        main: function void (){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_short_vardecl_19(self):
        input = """x: integer = -3;
        main: function void (){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_short_vardecl_20(self):
        input = """x: auto = 3;
        main: function void (){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_short_vardecl_21(self):
        input = """x: auto = 3;
        a : integer = x;
        main: function void (){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_short_vardecl_22(self):
        input = """x: auto = 3;
        a : boolean = x;
        main: function void (){}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, BooleanType, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_short_vardecl_23(self):
        input = """x: auto = 3;
        main: function void (){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_short_vardecl_24(self):
        input = """x: auto = 3;
        main: function void (a: integer){}"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_short_vardecl_25(self):
        input = """x: auto = 3;
        foo: function void (a:integer){}
        main: function void (){}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_short_vardecl_26(self):
        input = """x: auto = 3;
        foo: function void (a:integer, a: boolean){}
        main: function void (){}"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_short_vardecl_27(self):
        input = """x: auto = 3;
        foo: function void (a:integer){}
        foo: function void (){}
        main: function void (){}"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_short_vardecl_28(self):
        input = """x: auto = 3;
        main: function void (){
            a:integer = 1;
        }"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_short_vardecl_29(self):
        input = """x: auto = 3;
        main: function void (){
            a:integer = 1;
        }
        foo: function void (){
            a : integer = 1;
            a : float = 1.2;
        }
        """
        expect = "Redeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_short_vardecl_30(self):
        input = """x: auto = 3;
        main: function void (){
            a:integer = 1;
        }
        foo: function void (a:integer){
            a : integer = 1;
        }
        """
        expect = "Redeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_short_vardecl_31(self):
        input = """x: void = 3;
        main: function void (){
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, VoidType, IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_short_vardecl_32(self):
        input = """main: function void (){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_short_vardecl_33(self):
        input = """main: function void (){
            a : integer = 2;
            a = 3;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_short_vardecl_34(self):
        input = """main: function void (){
            a : integer = 2;
            a = true;
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_short_vardecl_35(self):
        input = """main: function void (){
            a : integer = 2.1;
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(2.1))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_short_vardecl_36(self):
        input = """main: function void (){
            a : float = 2.1;
            a = 1;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_short_vardecl_37(self):
        input = """main: function void (){
            a : integer;
            if (a > 0) a = 1;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_short_vardecl_38(self):
        input = """main: function void (){
            a : integer;
            if (a + 0) testCondOnly = 1;
        }
        """
        expect = "Type mismatch in statement: IfStmt(BinExpr(+, Id(a), IntegerLit(0)), AssignStmt(Id(testCondOnly), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_short_vardecl_39(self):
        input = """main: function void (){
            a : integer;
            if (a == 0) b = 1;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_short_vardecl_40(self):
        input = """b:integer;
        main: function void (){
            a : integer;
            if (a == 0) b = 1;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_short_vardecl_41(self):
        input = """b:integer;
        main: function void (){
            a : integer;
            if (a == 0){
                a : integer;
                b = 1;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_short_vardecl_42(self):
        input = """b:integer;
        main: function void (){
            a : integer = 1;
            while (a < 1){
                b = 1;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_short_vardecl_43(self):
        input = """b:integer;
        main: function void (){
            a : integer = 1;
            do {
                b = 1;
            }
            while (a < 1);
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_short_vardecl_44(self):
        input = """b:integer;
        main: function void (){
            a : integer = 1;
            do {
                b = 1;
                a : integer;
            }
            while (a < 1);
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_short_vardecl_45(self):
        input = """b:integer;
        main: function void (){
            a : integer = 1;
            do {
                b = 1;
                a : integer;
                c : float;
                d : integer;
            }
            while (a < 1);
            do {
                c : integer;
                do {
                    c = 1;
                    b = 1;
                }
                while (d < 1);
            }
            while (a < 1);
        }
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_short_vardecl_46(self):
        input = """b:integer;
        main: function void (){
            a : integer;
            if (a == 0) {
                a : integer;
                c : integer;
                if (a == 0) {
                    a : integer;
                    c = 1;
                    b = 1;
                    d : float;
                }
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_short_vardecl_47(self):
        input = """b:integer;
        main: function void (){
            a : integer;
            for (a = 1, a < 10, a + 1){
                a = 1 + 1;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_short_vardecl_48(self):
        input = """b:integer;
        main: function void (){
            for (a = 1, a < 10, a + 1){
                a = 1 + 1;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_short_vardecl_49(self):
        input = """b:integer;
        main: function void (){
            a : boolean;
            for (a = true, a < 10, a + 1){
                a = 1 + 1;
            }
        }
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(a), BooleanLit(True)), BinExpr(<, Id(a), IntegerLit(10)), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, IntegerLit(1), IntegerLit(1)))]))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_short_vardecl_50(self):
        input = """b:integer;
        main: function void (){
            a : integer;
            for (a = true, a < 10, a + 1){
                a = 1 + 1;
            }
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_short_vardecl_51(self):
        input = """b:integer;
        main: function void (){
            a : integer;
            for (a = 1, a < 10, a + 1.2){
                a = 1 + 1;
            }
        }
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(<, Id(a), IntegerLit(10)), BinExpr(+, Id(a), FloatLit(1.2)), BlockStmt([AssignStmt(Id(a), BinExpr(+, IntegerLit(1), IntegerLit(1)))]))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_short_vardecl_52(self):
        input = """b : integer;
        main: function void (){
            a : integer;
            for (a = 1, a < 10, a + 1){
                b : string;
                for (a = 2, a < 10, a + 1){
                    b = 1;
                }
            }
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(b), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_short_vardecl_53(self):
        input = """b : integer;
        main: function void (){
            a : integer;
            break;
        }
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_short_vardecl_54(self):
        input = """b:integer;
        main: function void (){
            a : integer;
            if (a == 0) {
                a : integer;
                c : integer;
                if (a == 0) {
                    a : integer;
                    c = 1;
                    b = 1;
                    d : float;
                    continue;
                }
            }
        }
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_short_vardecl_55(self):
        input = """b:integer;
        main: function void (){
            a : integer;
            if (a == 0) {
                a : integer;
                c : integer;
                while (a == 0) {
                    a : integer;
                    c = 1;
                    b = 1;
                    d : float;
                    continue;
                }
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_short_vardecl_56(self):
        input = """b:integer;
        foo : function integer (a : integer){
            a = 1;
        }
        foo1 : function float (a : integer){
            foo = 1;
        }
        main: function void (){
            a : integer;
        }
        """
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_short_vardecl_57(self):
        input = """b:integer;
        foo : function integer (){
            a : integer;
        }
        foo1 : function float (a : integer){
            a = 1;
        }
        main: function void (){
            a : integer;
            foo();
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_short_vardecl_58(self):
        input = """b:integer;
        main: function void (){
            a : integer;
            a = 1;
            foo();
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_short_vardecl_59(self):
        input = """b:integer;
        foo1 : function float (a : integer){
            a = 1;
        }
        main: function void (){
            a : integer;
            foo();
        }
        foo : function integer (){
            a : integer;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_short_vardecl_60(self):
        input = """x: auto;
        main: function void (){}"""
        expect = "Invalid Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_short_vardecl_61(self):
        input = """b:integer;
        foo1 : function float (a : integer){
            a = 1;
        }
        main: function void (){
            a : integer;
            foo1();
        }
        foo : function integer (){
            a : integer;
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, )"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_short_vardecl_62(self):
        input = """b:integer;
        foo1 : function float (a : integer){
            a = 1;
        }
        main: function void (){
            a : integer;
            foo1(1);
        }
        foo : function integer (){
            a : integer;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_short_vardecl_63(self):
        input = """b:integer;
        foo1 : function float (a : integer){
            a = 1;
        }
        main: function void (){
            a : integer;
            foo1(1, 2);
        }
        foo : function integer (){
            a : integer;
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_short_vardecl_64(self):
        input = """b:integer;
        foo1 : function float (a : integer){
            a = 1;
        }
        main: function void (){
            a : integer;
            foo1(true);
        }
        foo : function integer (){
            a : integer;
        }
        """
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_short_vardecl_65(self):
        input = """b:integer;
        foo1 : function float (a : integer, b : float){
            a = 1;
        }
        main: function void (){
            a : integer;
            foo1(1);
        }
        foo : function integer (){
            a : integer;
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_short_vardecl_66(self):
        input = """b:integer;
        foo1 : function float (a : integer, b : float){
            a = 1;
        }
        main: function void (){
            a : integer;
            foo1(1, 1.2);
        }
        foo : function integer (){
            a : integer;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_short_vardecl_67(self):
        input = """b:integer;
        foo1 : function float (a : integer, b : float){
            a = 1;
        }
        main: function void (){
            a : integer;
            foo1(1, 1);
        }
        foo : function integer (){
            a : integer;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_short_vardecl_68(self):
        input = """b:integer;
        foo1 : function integer (a : integer, b : float){
            a = 1;
        }
        main: function void (){
            a : integer;
            a = foo1(1, 1);
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_short_vardecl_69(self):
        input = """b:integer;
        foo1 : function float (a : integer, b : float, c : integer){
            a = 1;
        }
        main: function void (){
            a : integer;
            foo1(1, 1, true);
        }
        foo : function integer (){
            a : integer;
        }
        """
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_short_vardecl_70(self):
        input = """b:integer;
        foo1 : function integer (a : integer, b : float){
            a = 1;
        }
        main: function void (){
            a : boolean;
            a = foo1(1, 1);
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), FuncCall(foo1, [IntegerLit(1), IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_short_vardecl_71(self):
        input = """b:integer;
        foo1 : function integer (a : integer, b : float){
            a = 1;
        }
        main: function void (){
            a : integer;
            a = foo1(1, 1) + 1;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_short_vardecl_72(self):
        input = """b:integer;
        foo1 : function void (a : integer, b : float){
            a = 1;
        }
        main: function void (){
            a : integer;
            a = foo1(1, 1) + 1;
        }
        """
        expect = "Type mismatch in expression: BinExpr(+, FuncCall(foo1, [IntegerLit(1), IntegerLit(1)]), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_short_vardecl_73(self):
        input = """b:integer;
        foo1 : function void (a : integer, b : float){
            a = 1;
        }
        main: function void (){
            a : integer;
            a = foo(1, 1) + 1;
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_short_vardecl_74(self):
        input = """b:integer;
        foo1 : function auto (a : integer, b : float){
            a = 1;
        }
        main: function void (){
            a : integer;
            a = foo1(1, 1) + 1;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_short_vardecl_75(self):
        input = """b:integer;
        foo1 : function auto (a : integer, b : float){
            a = 1;
        }
        main: function void (){
            a : integer;
            b : boolean;
            a = foo1(1, 1) + 1;
            b = foo1(1, 1);
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(b), FuncCall(foo1, [IntegerLit(1), IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_short_vardecl_76(self):
        input = """b:integer;
        foo1 : function auto (a : integer, b : float){
            a = 1;
        }
        main: function void (){
            a : string;
            b : string;
            b = foo1(1, 1) :: "hello";
            a = foo1(1, 1);
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_short_vardecl_77(self):
        input = """b:integer;
        foo1 : function auto (a : integer, b : float){
            a = 1;
        }
        main: function void (){
            a : string;
            b : string;
            b = foo1(1, 1);
            a = foo1(1, 1)  :: "hello";
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_short_vardecl_78(self):
        input = """b:integer;
        foo1 : function auto (a : integer, b : float){
            a = 1;
        }
        main: function void (){
            foo1(1, 1);
            a : integer = foo1(1, 1);
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_short_vardecl_79(self):
        input = """b:integer;
        foo1 : function auto (a : integer, b : float){
            a = 1;
        }
        main: function void (){
            a : integer = foo1(1, 1);
            a = 1 + foo1(1, 1);
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_short_vardecl_80(self):
        input = """b : array [1, 2] of integer;
        main: function void (){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_short_vardecl_81(self):
        input = """b : array [1, 2] of integer = {{1, 2}};
        main: function void (){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_short_vardecl_82(self):
        input = """b : array [1, 2] of integer = {1, true};
        main: function void (){
        }
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_short_vardecl_83(self):
        input = """b : array [1, 2] of integer = {false, true};
        main: function void (){
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayLit([BooleanLit(False), BooleanLit(True)]))"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_short_vardecl_84(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        main: function void (){
            a : integer = b[1, 1];
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_short_vardecl_85(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        main: function void (){
            a : integer = c[1];
        }
        """
        expect = "Type mismatch in expression: ArrayCell(c, [IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_short_vardecl_86(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        main: function void (){
            a : integer = c[1];
        }
        """
        expect = "Type mismatch in expression: ArrayCell(c, [IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_short_vardecl_87(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        main: function void (){
            a : boolean = b[1, 2];
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, BooleanType, ArrayCell(b, [IntegerLit(1), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_short_vardecl_88(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        main: function void (){
            c : integer;
            a : boolean = c[1];
        }
        """
        expect = "Type mismatch in expression: ArrayCell(c, [IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_short_vardecl_89(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        main: function void (){
            b : integer = b[1+1, 1];
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_short_vardecl_90(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        main: function void (){
            b : integer = b[1+1, 1] + 2 + 3;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_short_vardecl_91(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        main: function void (){
            b : integer = b[true] + 2 + 3;
        }
        """
        expect = "Type mismatch in expression: ArrayCell(b, [BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_short_vardecl_92(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        main: function void (){
            b : integer = b[1,2,3] + 2 + 3;
        }
        """
        expect = "Type mismatch in expression: ArrayCell(b, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_short_vardecl_93(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        foo: function void(){
            a : integer;
        }
        foo1: function void(){
            a = 1;
        }
        main: function void (){
            b : integer = b[1,2,3] + 2 + 3;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_short_vardecl_94(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        foo: function void(){
            a : integer;
        }
        foo1: function void(){
        }
        main: function void (){
            b : integer = b[1,2] + 2 + 3;
            return;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_short_vardecl_95(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        foo: function void(){
            a : integer;
        }
        foo1: function integer(){
            return 1;
        }
        main: function void (){
            b : integer = b[1,2] + 2 + 3;
            return;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_short_vardecl_96(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        foo: function void(){
            a : integer;
            return a;
        }
        foo1: function integer(){
            return 1;
        }
        main: function void (){
            b : integer = b[1,2] + 2 + 3;
            return;
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_short_vardecl_97(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        main: function void (){
            b : integer = b[1,2] + 2 + 3;
            if (b == 1) return;
            return;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_short_vardecl_98(self):
        input = """b : array [1, 2] of integer = {{1, 1}};
        main: function void (){
            b : integer = b[1,2] + 2 + 3;
            if (b == 1) return "lol";
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(lol))"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_short_vardecl_99(self):
        input = """b : array [1, 3] of integer = {{1, 2, 3}};
        main: function void (){
            b : integer = b[1,2] + 2 + 3;
            if (b == 1) return;
            else return;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 500))

    def test_short_vardecl_100(self):
        input = """b : array [1, 2] of integer = {{1, 2}};
        main: function void (){
            b : integer = b[1,2] + 2 + 3;
            if (b == 1) return;
            else return 1;
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 501))

    def test_short_vardecl_101(self):
        input = """b : array [1, 2] of integer = {{1, 2}};
        foo : function integer (a : auto){
            a = 1;
        }
        main: function void (){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 502))

    def test_short_vardecl_102(self):
        input = """b : array [1, 2] of integer = {{1, 2}};
        main: function void (){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 503))

    def test_short_vardecl_103(self):
        input = """b : array [1, 2] of integer = {{1, 2}};
        main: function void (){
            b = 1;
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(b), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 504))

    def test_short_vardecl_104(self):
        input = """b : array [1, 2] of integer = {{1, 2}};
        main: function void (){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 505))

    def test_short_vardecl_105(self):
        input = """b : array [1, 2] of integer = {{1, 2}};
        foo : function void (){
            super();
        }
        main: function void (){
        }
        """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 506))

    def test_short_vardecl_106(self):
        input = """b : array [1, 2] of integer = {{1, 2}};
        foo : function void (a : integer){
        }
        main: function void (){
            foo(true);
        }
        """
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker.test(input, expect, 507))

    def test_short_vardecl_107(self):
        input = """b : array [1, 2] of integer = {{1, 2}};
        foo : function integer (a : integer){
        }
        main: function void (){
            a : integer = foo(true) + 1;
        }
        """
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker.test(input, expect, 508))

    def test_short_vardecl_108(self):
        input = """b : array [1, 2] of integer = 1;
        foo : function integer (a : integer){
        }
        main: function void (){
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 509))

    def test_short_vardecl_109(self):
        input = """b : array [3, 2] of integer = {{1,2},{1,2},{1,2}};
        foo : function integer (a : integer){
        }
        main: function void (){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 510))

    def test_short_vardecl_110(self):
        input = """b : array [3, 2] of integer = {{1,2},{1,2},{1,2}};
        foo : function integer (a : integer){
            super();
        }
        main: function void (){
        }
        """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 511))

    def test_short_vardecl_111(self):
        input = """b : array [3, 2] of integer = {{1,2},{1,2},{1,2}};
        foo1 : function integer (a : integer){}
        foo : function integer (a : integer) inherit foo1 {
            super();
        }
        main: function void (){
        }
        """
        expect = "Type mismatch in statement: CallStmt(super, )"
        self.assertTrue(TestChecker.test(input, expect, 512))

    def test_short_vardecl_112(self):
        input = """b : array [3, 2] of integer = {{1,2},{1,2},{1,2}};
        foo1 : function integer (a : integer){}
        foo : function integer (a : integer) inherit foo1 {
        }
        main: function void (){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 513))

    def test_short_vardecl_113(self):
        input = """b : array [3, 2] of integer = {{1,2},{1,2},{1,2}};
        foo1 : function integer (a : integer){}
        foo : function integer (a : integer) inherit foo3 {
        }
        main: function void (){
        }
        """
        expect = "Undeclared Identifier: foo3"
        self.assertTrue(TestChecker.test(input, expect, 514))

    def test_short_vardecl_114(self):
        input = """b : array [3, 2] of integer = {{1,2},{1,2},{1,2}};
        foo1 : function integer (a : integer){}
        foo : function integer (a : integer) inherit foo1 {
            super();
        }
        main: function void (){
        }
        """
        expect = "Type mismatch in statement: CallStmt(super, )"
        self.assertTrue(TestChecker.test(input, expect, 515))

    def test_short_vardecl_115(self):
        input = """b : array [3, 2] of integer = {{1,2},{1,2},{1,2}};
        foo1 : function integer (a : integer){}
        foo : function integer (a : integer) inherit foo1 {
            super(true);
        }
        main: function void (){
        }
        """
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker.test(input, expect, 516))

    def test_short_vardecl_116(self):
        input = """b : array [3, 2] of integer = {{1,2},{1,2},{1,2}};
        foo1 : function integer (a : integer){}
        foo : function integer (a : integer) inherit foo1 {
            super(1);
        }
        main: function void (){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 517))

    def test_short_vardecl_117(self):
        input = """b : array [3, 2] of integer = {{1,2},{1,2},{1,2}};
        foo1 : function integer (a : integer){}
        foo : function integer (a : integer) inherit foo1 {
            b : integer;
        }
        main: function void (){
        }
        """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 518))

    def test_short_vardecl_118(self):
        input = """b : array [3, 2] of integer = {{1,2},{1,2},{1,2}};
        foo1 : function void (a : integer){}
        foo : function integer (a : integer) inherit foo1 {
            foo1(1);
            b : integer;
        }
        main: function void (){
        }
        """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 519))

    def test_short_vardecl_119(self):
        input = """b : array [3, 2] of integer = {{1,2},{1,2},{1,2}};
        foo1 : function void (a : integer){}
        foo : function integer (a : integer) inherit foo1 {
            preventDefault();
            b : integer;
        }
        main: function void (){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 520))

    def test_short_vardecl_120(self):
        input = """b : integer;
        foo1 : function void (a : integer){
            b = 1;
        }
        foo : function integer (a : integer){
            b : integer;
        }
        main: function void (){
            b = 1;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 521))

    def test_short_vardecl_121(self):
        input = """b : float = 1;
        main: function void (){
            b = 1 + 1.0;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 522))

    def test_short_vardecl_122(self):
        input = """b : integer;
        foo1 : function void (inherit a : integer){
            b = 1;
        }
        foo : function integer (b : integer) inherit foo1{
            super(1);
        }
        main: function void (){
            b = 1;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 523))

    def test_short_vardecl_123(self):
        input = """b : integer;
        foo1 : function void (inherit a : integer){
            b = 1;
        }
        foo : function integer (a : integer) inherit foo1{
            super(1);
        }
        main: function void (){
            b = 1;
        }
        """
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 524))

    def test_short_vardecl_124(self):
        input = """b : integer;
        foo1 : function void (inherit a : integer){
            b = 1;
        }
        foo : function integer (b : integer) inherit foo1{
            super(1);
            a : integer;
        }
        main: function void (){
            b = 1;
        }
        """
        expect = "Redeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 525))

    def test_short_vardecl_125(self):
        input = """foo: function void () {}
            main: function void() {
                foo: integer = 1;
                x: integer = foo();
                x = foo;
    }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 526))

    def test_short_vardecl_126(self):
        input = """foo: function integer (a : auto, b : auto, c: auto) {
            a = 1;
            b = 1;
            c = 1;
            return a + b + c;
        }
            main: function void() {
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 527))

    def test_short_vardecl_127(self):
        input = """foo: function integer (a : auto, b : auto, c: auto) {
            d : integer = a;
            return a;
        }
            main: function void() {
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 528))

    def test_short_vardecl_128(self):
        input = """foo: function integer (a : auto, b : auto, c: auto) {
            a = 1;
            b = a + 1 - 3;
            c = 1;
            return a + b + c;
        }
            main: function void() {
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 529))

    def test_short_vardecl_129(self):
        input = """foo: function auto () {
            return 1;
        }
            main: function void() {
                a : integer = foo();
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 530))

    def test_short_vardecl_130(self):
        input = """foo: function auto () {
            return 1;
        }
            main: function void() {
                foo();
                a : integer = foo();
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 531))

    def test_short_vardecl_131(self):
        input = """foo: function auto () {
        }
            main: function void() {
                foo();
                a : integer = foo();
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 532))

    def test_short_vardecl_132(self):
        input = """foo : integer = 1;
            foo: function auto () {
            }
            main: function void() {
                foo();
                foo : integer = 1;
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 533))

    def test_short_vardecl_133(self):
        input = """foo : array [1,2] of integer = {};
            main: function void() {
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(foo, IntegerType, ArrayLit([]))"
        self.assertTrue(TestChecker.test(input, expect, 534))

    def test_short_vardecl_134(self):
        input = """foo : array [2,2] of integer = {{1,2},{2,2}};
            main: function void() {
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 535))

    def test_short_vardecl_135(self):
        input = """foo : array [2,2] of integer = {{1,true},{2,2}};
            main: function void() {
        }
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 536))

    def test_short_vardecl_136(self):
        input = """foo : array [2,2] of integer = {{1,1},{2,2,3}};
            main: function void() {
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(foo, IntegerType, ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(1)]), ArrayLit([IntegerLit(2), IntegerLit(2), IntegerLit(3)])]))"
        self.assertTrue(TestChecker.test(input, expect, 537))

    def test_short_vardecl_137(self):
        input = """foo : array [3] of integer = {1,2,3};
            main: function void() {
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 538))

    def test_short_vardecl_138(self):
        input = """b : integer;
        foo1 : function void (a : integer){
            b = 1;
        }
        foo : function integer (a : integer) inherit foo1{
            super(1);
        }
        main: function void (){
            b = 1;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 539))

    def test_short_vardecl_139(self):
        input = """foo : array [3] of float = {1,2,3};
            main: function void() {
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 540))

    def test_short_vardecl_140(self):
        input = """b : integer;
        foo1 : function void (inherit a : integer){
            b = 1;
        }
        foo : function integer (b : integer) inherit foo1{
            super(1);
            a : integer;
        }
        main: function void (){
            b = 1;
        }
        """
        expect = "Redeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 541))

    def test_short_vardecl_141(self):
        input = """b : integer;
        a : array[3] of integer;
        main: function void (){
            a[1] = 1;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 542))
