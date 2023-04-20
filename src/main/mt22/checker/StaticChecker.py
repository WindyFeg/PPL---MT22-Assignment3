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

class FunctionType(Type):
    def __str__(self):
        return self.__class__.__name__
    

    

@dataclass
class Symbol:
    name: str
    mtype: Type #@dimensions: list[int], typ: Type
    
    def __repr__(self) -> str:
        return (
            "Symbol("
            + str(self.name)
            + ", "
            + str(self.mtype)
            + ")"
        )
    
    def __eq__(self, other) -> bool:
        if type(self) is not type(other):
            return False
        return self.name == other.name and self.mtype == other.mtype
    
    def ChangeType(self, typ):
        self.mtype = typ

    def GetType(self):
        return self.mtype
    
    def GetName(self):
        return self.name
    
@dataclass
class FunctionSymbol:
    name: str
    returnType: Type
    params: List[Symbol]
    inheritParams: List[Symbol] = None

    def __repr__(self) -> str:
        return (
            "FunctionSymbol(" 
            + self.name
            + ", "
            + str(self.returnType)
            + ", "
            + str(self.params)
            + ", "
            + str(self.inheritParams)
            + ")"
        )
    
    def __eq__(self, other) -> bool:
        if type(self) is not type(other):
            return False
        return self.name == other.name and self.mtype == other.mtype
    
    def GetParams(self):
        return self.params
    
    def GetInheritParams(self):
        return self.inheritParams

    def ChangeReturnType(self, typ):
        self.returnType = typ

    def ChangeParamsType(self, index, typ):
        self.params[index].ChangeType(typ)

    def GetName(self):
        return self.name
    
    def GetReturnType(self):
        return self.returnType
    
class Tool:
    def CheckRedeclare(self,name, mtype, o):
        seen = set()
        for symbol in o:
            if symbol.GetName() in seen:
                if symbol.GetName() == name:
                    raise Redeclared(mtype, symbol.GetName())
                return
            seen.add(symbol.GetName())

    def CheckParamsInvalid(self,name, mtype, o):
        for symbol in o:
            if symbol.GetName() == name:
                raise Invalid(mtype, symbol.GetName())
        return
            
    def CheckArrayType(dimen):
        for item in dimen:
            if not item.isdigit():
                return False
        return True

    def FindSymbol( name,type, o):
        for symbol in o:
            if symbol.GetName() == name:
                return symbol
        raise Undeclared(type, name)
    
    def CheckType(symbol, type):
        return type == symbol.mtype

    #* Check dimension of array literal
    def CheckArrayLitDimension(exprList):
        return [len(exprList)] + Tool.CheckArrayLitDimension(exprList[0]) if type(exprList) == list else []
    
    def flatten(arr):
        result = []
        for item in arr:
            if isinstance(item, list):
                result.extend(Tool.flatten(item))
            else:
                result.append(item)
        return result
    
    def int_to_str(arr):
        return [str(i) for i in arr]

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
    
    #%ArrayType #self.dimensions = dimensions
    #% self.typ = typ
    def visitArrayType(self, ctx: ArrayType, o):
        return ctx
            
    def visitAutoType(self, ctx:AutoType, o):
        return AutoType()
    
    def visitVoidType(self, ctx:VoidType, o):
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

            #* Auto type
            elif typeLeft in [IntegerType, FloatType] and typeRight == AutoType:
                symbol = Tool.FindSymbol(ctx.right.name, Function(), o)
                symbol.ChangeReturnType(left)
                return left
            else:
                raise TypeMismatchInExpression(ctx)
        
        #* Boolean operators
        if op in ['&&', '||']:
            if typeLeft == typeRight and typeLeft == BooleanType:
                return BooleanType()
            #* Auto type
            if typeLeft == BooleanType and typeRight == AutoType:
                symbol = Tool.FindSymbol(ctx.right.name, Function(), o)
                symbol.ChangeReturnType(left)
                return left
            else:
                raise TypeMismatchInExpression(ctx)

        #* String operators
        if op == '::':
            if typeLeft == typeRight and typeLeft == StringType:
                return StringType()
            if typeLeft == StringType and typeRight == AutoType:
                symbol = Tool.FindSymbol(ctx.right.name, Function(), o)
                symbol.ChangeReturnType(left)
                return left
            else:
                raise TypeMismatchInExpression(ctx)
            
        #* Relational operators
        if op in ['<', '>', '<=', '>=']:
            if typeLeft in [IntegerType, FloatType] and typeRight in [IntegerType, FloatType]:
                return BooleanType()
            
            #* Auto type
            if typeLeft in [IntegerType, FloatType] and typeRight == AutoType:
                symbol = Tool.FindSymbol(ctx.right.name, Function(), o)
                symbol.ChangeReturnType(left)
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ctx)
        
        if op in ['==', '!=']:
            if typeLeft == typeRight and typeLeft in [IntegerType, BooleanType]:
                return BooleanType()
            
            #* Auto type
            if typeLeft in [IntegerType, BooleanType] and typeRight == AutoType:
                symbol = Tool.FindSymbol(ctx.right.name, Function(), o)
                symbol.ChangeReturnType(left)
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
        return Tool.FindSymbol(ctx.name,Identifier(), o).GetType()
    
    #% ArrayCell: name: str, cell: List[Expr] 
    #* E1[E2]: E1 is ArrayType, E2 is list of integer
    def visitArrayCell(self, ctx, o): 
        symbol = Tool.FindSymbol(ctx.name, Identifier(), o)
        #* E1 is ArrayType
        if type(symbol.mtype) == ArrayType:
            #* E2 is list of integer
            for expr in ctx.cell:
                typeExpr = self.visit(expr, o)
                if type(typeExpr) != IntegerType:
                    raise TypeMismatchInExpression(ctx)
            return symbol.mtype.typ
        raise TypeMismatchInExpression(ctx)
    
    

    #% ArrayLit: explist: List[Expr]
    #* {1,2,3}
    #* Check if all expr in array are the same type and return that type
    def visitArrayLit(self, ctx:ArrayLit, o):
        dimension = len(ctx.explist)
        # print("dimension check " + str(dimension))
        #* Go to the deepest array and get it dimension
        if type(ctx.explist[0]) == ArrayLit:

            #* Check case {{a,b},{c}}
            for expr in ctx.explist[1:]:
                if len(ctx.explist[0].explist) != len(expr.explist):
                    return [], None

            child_dimension, arrayLitType = self.visit(ctx.explist[0], o)
            for expr in ctx.explist[1:]:
                child_dimension2, arrayLitType2 = self.visit(expr, o)
                if child_dimension != child_dimension2:
                    return [], None
                if type(arrayLitType) != type(arrayLitType2):
                    return [], None
                
            return [dimension] + child_dimension, arrayLitType
        else:
        #* Get type of expr in array
        #* Check if all expr in array are the same type
            arrayLitType = self.visit(ctx.explist[0], o)
            for expr in ctx.explist:
                typeExpr = self.visit(expr, o)
                if type(typeExpr) != type(arrayLitType):
                    raise IllegalArrayLiteral(ctx)
            return [dimension] ,arrayLitType

    #% FuncCall: #name: str, args: List[Expr] 
    def visitFuncCall(self, ctx: FuncCall, o):
        #* Get symbol of function
        symbol = Tool.FindSymbol(ctx.name, Identifier(), o)
        
        #* Check if symbol is function
        if type(symbol) != FunctionSymbol:
            raise Undeclared(Function(), ctx.name)

        #* Check if number of args is correct
        if len(symbol.GetParams()) != len(ctx.args):
            raise TypeMismatchInExpression(ctx)
        
        #* Check Type of args
        for i in range(len(ctx.args)):
            arguementType = self.visit(ctx.args[i], o)
            paramType = symbol.GetParams()[i].GetType()
            if type(arguementType) != type(paramType):

                #* AutoType
                if type(paramType) == AutoType:
                    symbol.ChangeParamsType(i, arguementType)
                    continue

                #* IntegerType = FloatType
                if type(arguementType) == IntegerType and type(paramType) == FloatType:
                    continue
                raise TypeMismatchInExpression(ctx)
        return symbol.GetReturnType()

    #$ STATEMENT 
    #%AssignStmt: lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ctx, o):
        if o[0] == "env": 
            return 
        lhs = self.visit(ctx.lhs, o)
        rhs = self.visit(ctx.rhs, o)

        print("------------ASSIGN-STMT------------")
        print(type(lhs), type(rhs))
        #* Check if lsh is VoidType or ArrayType
        if type(lhs) in [VoidType, ArrayType]:
            raise TypeMismatchInStatement(ctx)

        #* Check if lsh is same type as rhs
        if type(lhs) != type(rhs):
            #* Check if lsh is FloatType
            if type(lhs) == FloatType and type(rhs) == IntegerType:
                return None
            raise TypeMismatchInStatement(ctx)

    #% BlockStmt: #body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ctx:BlockStmt, o):
        functionParams = []
        #* Function Body
        if type(o[len(o)-1]) == type(""):
            #* Get all params of function
            thisFunction = Tool.FindSymbol(o.pop(), Identifier(), o)
            functionParams = thisFunction.GetParams()

        print(functionParams)
        #* Normal body
        o_temp = ["env", functionParams] + o
        for i in ctx.body:
            if type(i) == VarDecl:
                o_temp[1].append(self.visit(i, o_temp))
        
        for i in ctx.body:
            self.visit(i, o_temp[1])
        




    #%IfStmt: #cond: Expr, 
    #% tstmt: Stmt, 
    #% fstmt: Stmt or None = None 
    def visitIfStmt(self, ctx, o): pass

    #% ForStmt: #init: AssignStmt, 
    #% cond: Expr, 
    #% upd: Expr, 
    #% stmt: Stmt
    def visitForStmt(self, ctx, o): pass

    #% WhileStmt: #cond: Expr, stmt: Stmt 
    def visitWhileStmt(self, ctx, o): pass

    #% DowhileStmt: #cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ctx, o): pass

    def visitBreakStmt(self, ctx:BreakStmt, o): 
        return BreakStmt()
    
    def visitContinueStmt(self, ctx:ContinueStmt, o): 
        return ContinueStmt()

    #% ReturnStmt: expr: Expr
    def visitReturnStmt(self, ctx: ReturnStmt, o):
        return self.visit(ctx.expr, o) 
    
    def visitCallStmt(self, ctx, o): pass

    #$ DECLARE
    #% Vardecl: #name: str, typ: Type, init: Expr or None = None)
    def visitVarDecl(self, ctx:VarDecl, o): 
        if o[0] == "env":
            return Symbol(ctx.name, self.visit(ctx.typ, o))
        else:
            Tool.CheckRedeclare(self, ctx.name, Variable(), o)
            symbol = Tool.FindSymbol(ctx.name, Identifier(), o)

            #* Initialize case
            if ctx.init:
                try:
                    dimensionArrayLit, typeInit = self.visit(ctx.init,o)
                except:
                    typeInit = self.visit(ctx.init,o)

                print("-------------VAR-DECLARE----------------")
                print(ctx)
                print(type(ctx.typ))
                print(type(typeInit))

                #* AutoType
                if type(ctx.typ) == AutoType: 
                    symbol.ChangeType(typeInit)
                    return None

                #* Auto ArrayType & ArrayType
                if type(ctx.typ) == ArrayType:
                    #* {{a,b}, {c}}
                    if dimensionArrayLit == [] and typeInit == None:
                        raise TypeMismatchInVarDecl(ctx)

                    typeArrayLit = ctx.typ
                    dimensionArrayLit = Tool.int_to_str(Tool.flatten(dimensionArrayLit))

                    #* ArrayDimension [i,j] = ArrayLitDimension [i,j] 
                    # print(typeArrayLit.dimensions)
                    # print(dimensionArrayLit)
                    if typeArrayLit.dimensions != dimensionArrayLit:
                        raise TypeMismatchInVarDecl(ctx)

                    if type(typeArrayLit.typ) == type(typeInit):
                        symbol.ChangeType(ctx.typ)
                        return None
                    
                    #* Auto ArrayType
                    elif type(typeArrayLit.typ) == AutoType:
                        typeArrayLit.typ = typeInit
                        symbol.ChangeType(ctx.typ)
                        return None

                #* FloatType = IntegerType
                if type(ctx.typ) == FloatType and type(typeInit) == IntegerType:
                    symbol.ChangeType(FloatType())
                    return None
                
                #* RightType = AutoType
                if type(typeInit) == AutoType:
                    if type(ctx.init) == FuncCall:
                        functionCall = Tool.FindSymbol(ctx.init.name, Identifier(), o)
                        functionCall.ChangeReturnType(ctx.typ)
                    else:
                        symbol.ChangeType(ctx.typ)
                    return None
                
                #* LeftType = RightType
                if type(typeInit) == type(ctx.typ):
                    symbol.ChangeType(typeInit)
                    return None
                else:
                    raise TypeMismatchInVarDecl(ctx)
            
            #* No initialize 
            #* AutoType
            elif type(ctx.typ) == AutoType:
                raise Invalid(Variable(),ctx)
            
            # VarDecl(n, ArrayType([1, 2], IntegerType))
            #* ArrayType
            elif type(ctx.typ) == ArrayType: 
                if type(ctx.typ.typ) == AutoType:
                    raise Invalid(Variable(),ctx)
                #* Array 
                #* Check "array [int]"
                if ctx.typ.dimensions:
                    symbol.ChangeType(ctx.typ)
                    return None
            
            #* Arithmetic 
            symbol.ChangeType(ctx.typ)
            return None

    #% name: str, 
    #% typ: Type, 
    #% out: bool = False, 
    #% inherit: bool = False
    def visitParamDecl(self, ctx, o): 
        if o[0] == "env":
            if ctx.inherit:
                return Symbol(ctx.name, ctx.typ), True
            return Symbol(ctx.name, ctx.typ), False
        else:
            functionSymbol = Tool.FindSymbol(ctx.name, Identifier(), o)
            Tool.CheckRedeclare(self, ctx.name, Parameter(), functionSymbol.GetParams())
            functionSymbol.ChangeReturnType(ctx.typ)
            return True if ctx.name == "main" else None

    #% FuncDecl: # 
    #% name: str, 
    #% return_type: Type, 
    #% params: List[ParamDecl], 
    #% inherit: str or None, 
    #% body: BlockStmt
    #* name: function <return-type> (<parameter-list>) [inherit <function-name>]?
    def visitFuncDecl(self, ctx, o):
        if o[0] == "env":
            inheritParams, params = [], []
            for param in ctx.params:
                par, isIhr = self.visit(param, o)
                if isIhr:
                    inheritParams.append(par)
                params.append(par)
            return FunctionSymbol(ctx.name, ctx.return_type, params, inheritParams)
        else:
            #* Check redeclare
            Tool.CheckRedeclare(self, ctx.name, Function(), o)

            #* Check redeclare in params
            thisFunction = Tool.FindSymbol(ctx.name, Function(), o)
            functionParams = thisFunction.GetParams()
            for param in ctx.params:
                Tool.CheckRedeclare(self, param.name, Parameter(), functionParams)

            #* Check inherit 
            if ctx.inherit:
                inheritFunction = Tool.FindSymbol(ctx.inherit, Function(), o)

                #* Check if Child has params like Father inherit params
                for param in functionParams:
                    Tool.CheckParamsInvalid(self, param.GetName(), Parameter(), inheritFunction.GetInheritParams())
                
                #* Father inherit params + Son params
                inheritFunctionParams_FunctionParams = inheritFunction.GetInheritParams() + functionParams
                
                self.visit(ctx.body, o + [ctx.name])
                return None
            else:
                
                self.visit(ctx.body, o + [ctx.name])
                return None
            


    #$ PROGRAM 
    #% program: #decls: List[Decl] 
    #$ o = [Symbol(name, mtype),...]
    def visitProgram(self, ctx:Program, o):
        o = ["env", []]

        #* Get all declaration
        for decl in ctx.decls:
            if self.visit(decl, o) is not None:
                o[1].append(self.visit(decl, o))
        o = o[1]

        print("------------ROUND1----------------")
        for i in o:
            print(repr(i))

        for decl in ctx.decls:
            self.visit(decl, o)
        
        print("--------------ROUND2--------------")
        for i in o:
            print(repr(i))

        #* Check main function
        # if mainFunction:
        raise NoEntryPoint()

        