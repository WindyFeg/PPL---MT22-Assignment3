from Visitor import Visitor
from Utils import *
from StaticChecker import *
from AST import *
from functools import *
from StaticError import *
from dataclasses import dataclass
from typing import List
class NoType:
    pass

class Type(AST):
    pass


@dataclass
class Symbol:
    name: str
    mtype: Type #@dimensions: list[int], typ: Type
    paramTypes: List[Type] = None
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
    
    def __eq__(self, other) -> bool:
        if type(self) is not type(other):
            return False
        return self.name == other.name and self.mtype == other.mtype
    
# @dataclass
# class ArraySymbol(Type):
#     name: str
#     mtype: Type
#     dimension: list[int]

#     def __eq__(self, other) :
#         if type(self) is not type(other):
#             return False
#         return self.dimension == other.dimension and self.typeArray == other.typeArray

#     def __repr__(self) -> str:
#         return ("ArraySymbol(" 
#                 + str(self.name) 
#                 + ',' 
#                 + str(self.dimension) 
#                 + ',' 
#                 + str(self.mtype) 
#                 + ')' )
class Tool:
    def CheckRedeclare(self, name, o):
        for symbol in o:
            if symbol.name == name:
                raise Redeclared(Variable(), name)
            
    def CheckArrayType(dimen):
        for item in dimen:
            if not item.isdigit():
                return False
        return True

    def FindSymbol( name, o):
        for symbol in o:
            if symbol.name == name:
                return symbol
        raise Undeclared(Identifier(), name)
    
    def CheckType(symbol, type):
        return type == symbol.mtype

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
    
    def visitIntegerLit(self, ctx:IntegerLit, o): 
        return IntegerType()
    
    def visitFloatLit(self, ctx:FloatLit, o): 
        return FloatType()
    
    def visitStringLit(self, ctx:StringLit, o): 
        return StringType()
    
    def visitBooleanLit(self, ctx:BooleanLit, o): 
        return BooleanType()

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

    #% UnExpr: op: str, val: Expr
    def visitUnExpr(self, ctx:UnExpr, o): 
        op = ctx.op
        typeValue = self.visit(ctx.val, o)

        if op == '!':
            if type(typeValue) == BooleanType:
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ctx)
        
        if op == '-':
            if type(typeValue) in [IntegerType, FloatType ]:
                return typeValue
            else:
                raise TypeMismatchInExpression(ctx)

    def visitId(self, ctx, o): 
        #* This will loop from outer to inner
        name = ctx.name
        id = Tool.FindSymbol(name, o)
        return id.mtype
    #% ArrayCell: name: str, cell: List[Expr] 
    #* E1[E2]: E1 is ArrayType, E2 is list of integer
    def visitArrayCell(self, ctx, o): 
        arrayName = ctx.name
        arrayCell = ctx.cell
        symbol = Tool.FindSymbol(arrayName, o)
        #* E1 is ArrayType
        if type(symbol.mtype) == ArrayType:
            #* E2 is list of integer
            for expr in arrayCell:
                typeExpr = self.visit(expr, o)
                if type(typeExpr) != IntegerType:
                    raise TypeMismatchInExpression(ctx)
            return symbol.mtype.typ
        raise TypeMismatchInExpression(ctx)
    
    #% ArrayLit: explist: List[Expr]
    #* {1,2,3}
    def visitArrayLit(self, ctx, o): 
        arrayLitType = self.visit(ctx.explist[0], o)
        for expr in ctx.explist:
            typeExpr = self.visit(expr, o)
            # print(typeExpr , arrayLitType, type(typeExpr) != type(arrayLitType))
            if type(typeExpr) != type(arrayLitType):
                raise TypeMismatchInExpression(ctx)
        return arrayLitType

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
    def visitVarDecl(self, ctx:VarDecl, o): 
        Tool.CheckRedeclare(self, ctx.name, o)

        #* Initialize case
        if ctx.init:
            initType = self.visit(ctx.init, o)
            print("-----------------------------")
            print(ctx)
            print(type(ctx.typ))
            print(type(initType))

            #* AutoType
            if type(ctx.typ) == AutoType: 
                return Symbol(ctx.name, initType)

            #* Auto ArrayType & ArrayType
            if type(ctx.typ) == ArrayType:
                typeArrayLit = ctx.typ
                if type(typeArrayLit.typ) == type(initType):
                    return Symbol(ctx.name, ctx.typ)
                elif type(typeArrayLit.typ) == AutoType:
                    typeArrayLit.typ = initType
                    return Symbol(ctx.name, typeArrayLit)

            #* FloatType = IntegerType
            if type(ctx.typ) == FloatType and type(initType) == IntegerType:
                #! Convert Integer to Float
                return Symbol(ctx.name, FloatType())
            
            #* LeftType = RightType
            if type(initType) == type(ctx.typ):
                return Symbol(ctx.name, initType)
            else:
                raise TypeMismatchInVarDecl(ctx)
        
        #* No initialize 
        #* AutoType
        elif type(ctx.typ) == AutoType or type(ctx.typ.typ) == AutoType:
            raise Invalid(Variable(),ctx)
        
        #* Array 
        # VarDecl(n, ArrayType([1, 2], IntegerType))
        #* Check "array [int]"
        if ctx.typ.dimensions and type(ctx.typ) == ArrayType:
            return Symbol(ctx.name, ctx.typ)
        elif ctx.typ.dimensions and type(ctx.typ) != ArrayType:
            raise TypeMismatchInExpression(ctx)
        
        #* Arithmetic 
        return Symbol(ctx.name,ctx.typ)

    def visitParamDecl(self, ctx, o): pass

    #% FuncDecl: # 
    #% name: str, 
    #% return_type: Type, 
    #% params: List[ParamDecl], 
    #% inherit: str or None, 
    #% body: BlockStmt
    def visitFuncDecl(self, ctx, o):
        Tool.CheckRedeclare(self, ctx.name, o)
        
        #* Check return type
        return Symbol(ctx.name, ctx.return_type)

    #$ PROGRAM 
    #% program: #decls: List[Decl] 
    def visitProgram(self, ctx:Program, o):
        #* o will have a list of Symbol(name, mtype)
        o = []
        #! has two loop to loop through vardecl and funcdecl
        for decl in ctx.decls:
            o.append(self.visit(decl, o))
        
        for i in o:
            print("----------------------------")
            print("print Sym")
            print(repr(i))
        #! check if there is a main function
        raise NoEntryPoint()
        