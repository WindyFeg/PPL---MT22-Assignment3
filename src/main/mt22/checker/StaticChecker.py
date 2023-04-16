from Visitor import Visitor
from Utils import *
from StaticChecker import *
from AST import *
from functools import *
from StaticError import *

class NoType:
    pass
class Symbol:
    def __init__(self, name, mtype):
        self.name = name
        self.mtype = mtype

class StaticChecker(Visitor):
    def __init__(self, ast): 
        self.ast = ast

    def check(self): 
        level = 0
        return self.ast.accept(self,level)

    #$ ATOMIC TYPE
    def visitIntegerType(self, ctx, o): 
        return IntegerType()
    
    def visitFloatType(self, ctx, o): 
        return FloatType()
    
    def visitBooleanType(self, ctx, o):
        return BooleanType()

    #$ TYPE
    def visitStringType(self, ctx, o):
        return StringType()
    
    def visitArrayType(self, ctx, o):
        return ArrayType()
            
    def visitAutoType(self, ctx, o):
        return AutoType()
    
    def visitVoidType(self, ctx, o):
        return VoidType()

    def visitBinExpr(self, ctx, o): pass
    def visitUnExpr(self, ctx:UnExpr, o): pass

    def visitId(self, ctx, o): 
        #* This will loop from outer to inner
        name = ctx.name
        for symbol in o:
            if symbol.name == name:
                return symbol.mtype
        raise Undeclared(Identifier(), name)

    def visitArrayCell(self, ctx, o): pass

    def visitIntegerLit(self, ctx:IntegerLit, o): 
        return IntegerType()
    
    def visitFloatLit(self, ctx:FloatLit, o): 
        return FloatType()
    
    def visitStringLit(self, ctx:StringLit, o): 
        return StringType()
    
    def visitBooleanLit(self, ctx:BooleanLit, o): 
        return BooleanType()
    
    def visitArrayLit(self, ctx, o): pass
    def visitFuncCall(self, ctx, o): pass

    #$ STATEMENT 
    def visitAssignStmt(self, ctx, o): pass
    def visitBlockStmt(self, ctx, o): pass
    def visitIfStmt(self, ctx, o): pass
    def visitForStmt(self, ctx, o): pass
    def visitWhileStmt(self, ctx, o): pass
    def visitDoWhileStmt(self, ctx, o): pass
    def visitBreakStmt(self, ctx, o): pass
    def visitContinueStmt(self, ctx, o): pass
    def visitReturnStmt(self, ctx, o): pass
    def visitCallStmt(self, ctx, o): pass

    #$ DECLARE
    #% Vardecl: #name: str, typ: Type, init: Expr or None = None)
    def visitVarDecl(self, ctx:Program, o): 
        for symbol in o:
            if symbol.name == ctx.name:
                raise Redeclared(Variable(),ctx.name)
            
        if ctx.init:
            initType = self.visit(ctx.init, o)
            print("-----------------------------")
            print(ctx)
            print(type(ctx.typ))
            print(type(initType))

            #* AutoType
            if type(ctx.typ) == AutoType:
                return Symbol(ctx.name, initType)

            #* FloatType = IntegerType
            if type(ctx.typ) == FloatType and type(initType) == IntegerType:
                #! Convert Integer to Float
                return Symbol(ctx.name, FloatType())
            
            #* LeftType = RightType
            if type(initType) == type(ctx.typ):
                return Symbol(ctx.name, initType)
            else:
                raise TypeMismatchInVarDecl(ctx)
        return Symbol(ctx.name,ctx.typ)

    def visitParamDecl(self, ctx, o): pass
    def visitFuncDecl(self, ctx, o): pass

    #$ PROGRAM 
    #% program: #decls: List[Decl] 
    def visitProgram(self, ctx, o):
        #* o will have a list of Symbol(name, mtype)
        o = []
        for decl in ctx.decls:
            o.append(self.visit(decl, o))
        return ""