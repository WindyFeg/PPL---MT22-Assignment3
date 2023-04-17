from Visitor import Visitor
from Utils import *
from StaticChecker import *
from AST import *
from functools import *
from StaticError import *
from dataclasses import dataclass

class NoType:
    pass

class Type(AST):
    pass


@dataclass
class Symbol:
    name: str
    mtype: Type
    paramTypes: list[Type] = None
    returnType: Type = None
    
    def __repr__(self) -> str:
        return (
            "Symbol("
            + str(self.name)
            + ", "
            + str(self.mtype)
            # + str(self.params_to_str())
            # + str(self.return_to_str())
            + ")"
        )

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

    #% BinExpr: #op: str, left: Expr, right: Expr
    def visitBinExpr(self, ctx: BinExpr, o): 
        op = ctx.op
        left = self.visit(ctx.left, o)
        right = self.visit(ctx.right, o)
        typeLeft = type(left)
        typeRight = type(right)

        print("-----------------------------")
        print(ctx)
        print(typeLeft)
        print(typeRight)

        #* Arithmetic operators
        if op == '%':
            if typeLeft == typeRight and typeLeft == IntegerType:
                return IntegerType()
            else:
                raise TypeMismatchInExpression(ctx)

        if op in ['+', '-', '*', '/']:
            if typeLeft == typeRight and typeLeft in [IntegerType, FloatType]:
                return left
            elif typeLeft == IntegerType and typeRight == FloatType:
                return FloatType()
            elif typeLeft == FloatType and typeRight == IntegerType:
                return FloatType()
            
            else:
                raise TypeMismatchInExpression(ctx)
        
        #* Boolean operators
        if op in ['&&', '||']:
            if typeLeft == typeRight and typeLeft == BooleanType:
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ctx)

        #* String operators
        if op == '::':
            if typeLeft == typeRight and typeLeft == StringType:
                return StringType()
            else:
                raise TypeMismatchInExpression(ctx)
            
        #* Relational operators
        if op in ['<', '>', '<=', '>=']:
            if typeLeft in [IntegerType, FloatType] and typeRight in [IntegerType, FloatType]:
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ctx)
        
        if op in ['==', '!=']:
            if typeLeft == typeRight and typeLeft in [IntegerType, BooleanType]:
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ctx)

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
        
        #* No init for AutoType
        elif type(ctx.typ) == AutoType:
            raise Invalid(Variable(),ctx)
        return Symbol(ctx.name,ctx.typ)

    def visitParamDecl(self, ctx, o): pass

    #% FuncDecl: # 
    #% name: str, 
    #% return_type: Type, 
    #% params: List[ParamDecl], 
    #% inherit: str or None, 
    #% body: BlockStmt
    def visitFuncDecl(self, ctx, o):
        for symbol in o:
            if symbol.name == ctx.name:
                raise Redeclared(Function(),ctx.name)
        
        #* Check return type
        return Symbol(ctx.name, ctx.return_type)

    #$ PROGRAM 
    #% program: #decls: List[Decl] 
    def visitProgram(self, ctx, o):
        #* o will have a list of Symbol(name, mtype)
        o = []
        #! has two loop to loop through vardecl and funcdecl
        for decl in ctx.decls:
            o.append(self.visit(decl, o))
        
        #! check if there is a main function
        raise NoEntryPoint()
        