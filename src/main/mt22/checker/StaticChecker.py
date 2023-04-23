from Visitor import Visitor
from Utils import *
from StaticChecker import *
from AST import *
from functools import *
from StaticError import *
from typing import List
class NoType:
    pass

class Type(AST):
    pass

class FunctionType(Type):
    def __str__(self):
        return self.__class__.__name__
    

    

class Symbol:
    def __init__(self, name: str, mtype: Type, array: Type = None):
        self.name = name
        self.mtype = mtype
        self.array = array 
    
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
    
class FunctionSymbol:
    def __init__(self, name: str, returnType: Type, params: List[Symbol], inheritParams: List[Symbol] = None):
        self.name = name
        self.returnType = returnType
        self.params = params
        self.inheritParams = inheritParams

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
    
    def GetIndexParams(self, index):
        return self.params[index]
    
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
    
    def CheckArgsInFunction(self, name, args, ctx, o):
        func = Tool.FindSymbol(name, Function(), o[1] + o[2])
        if type(func) != FunctionSymbol:
            raise Undeclared(Function(), func.GetName())
        
        if len(func.GetParams()) != len(args):
            raise TypeMismatchInStatement(ctx)
        
        for i in range(len(args)):
            arg = self.visit(args[i], [1] + o[2])
            # print("CHECK this aloooo")
            # print(func.GetIndexParams(i))
            if type(arg) != type(func.GetIndexParams(i).GetType()):
                raise TypeMismatchInExpression(ctx)
    
    #* return x;
    def CheckReturnAndFunction(self ,ctxReturn, o):
        if type(ctxReturn) == ReturnStmt:
            returnType = self.visit(ctxReturn, o)
            thisFunction = Tool.FindSymbol(o[3][1], Identifier(), o[1] + o[2])
            #*Function is autoType
            if type(thisFunction.GetReturnType()) == AutoType:
                thisFunction.ChangeReturnType(returnType)
            elif type(thisFunction.GetReturnType()) != type(returnType):
                raise TypeMismatchInStatement(ctxReturn)

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

        # print("-----------------------------")
        # print(ctx)
        # print(typeLeft)
        # print(typeRight)

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
            if typeRight in [IntegerType, BooleanType] and typeLeft in [IntegerType, BooleanType]:
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
        if symbol.array == True:
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
                raise TypeMismatchInExpression(ctx.args[i])
        return symbol.GetReturnType()

    #$ STATEMENT 
    #%AssignStmt: lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ctx, o):
        if o[0] == "envi": 
            return 
        
        #! ["check/func",[current], [father]] 
        lhs = self.visit(ctx.lhs, o[1] + o[2])
        rhs = self.visit(ctx.rhs, o[1] + o[2])

        # print("------------ASSIGN-STMT------------")
        # print(type(lhs), type(rhs))
        #* Check if lsh is VoidType or ArrayType
        if type(lhs) in [VoidType, ArrayType]:
            raise TypeMismatchInStatement(ctx)

        #* Check if lsh is same type as rhs
        if type(lhs) != type(rhs):
            #* Check if lsh is FloatType
            if type(lhs) == FloatType and type(rhs) == IntegerType:
                return None
            
            #* Check id = functionCall() -> AutoType
            if type(rhs) == AutoType and type(ctx.rhs) != VoidType:
                symbol = Tool.FindSymbol(ctx.rhs.name, Function(), o[1] + o[2])
                if type(ctx.rhs) == FuncCall:
                    symbol.ChangeReturnType(lhs)
                else:
                    symbol.ChangeType(lhs)
                return None
            
            #* Check id  -> AutoType = functionCall() 
            if type(lhs) == AutoType and type(ctx.rhs) != VoidType:
                symbol = Tool.FindSymbol(ctx.lhs.name, Identifier(), o[1] + o[2])
                symbol.ChangeType(rhs)
                return None

            raise TypeMismatchInStatement(ctx)

    #% BlockStmt: #body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ctx:BlockStmt, o):
        #$ ["typeOfChecker", [current], [father], [function]]
        functionParams = []
        body = ctx.body
        TypeOfchecker = "none"
        
        #* For Body
        if  "loop" in o[0]:
            TypeOfchecker = o[0]

        #* Function Body
        if len(o) == 4:
            TypeOfchecker = "func" if o[0] == "func" else TypeOfchecker
            #$ o[3] = ["inheritFunctionName", "thisFunctionName" ]
            inheritFunctionName = o[3][0]
            thisFunctionName = o[3][1]

            #* Get all params of function
            thisFunction = Tool.FindSymbol(thisFunctionName, Identifier(), o[1] + o[2])

            #* Get all params of inherit function 
            if inheritFunctionName is not None:
                inheritFunction = Tool.FindSymbol(inheritFunctionName, Identifier(), o[1] + o[2])
                functionParams = inheritFunction.GetInheritParams() 

                #* Check if first callStmt is callStmt
                if type(body[0]) != CallStmt :
                    raise InvalidStatementInFunction(thisFunction.GetName())  

                #* Check if first callStmt is super or PreventDefault
                if  body[0].name == "super" :
                    body[0].name = inheritFunction.GetName()
                    
                    self.visit(body[0], o + [inheritFunction.GetName()])
                    body = body[1:]
                elif body[0].name == "preventDefault":
                    if body[0].args != []:
                        raise TypeMismatchInStatement(body[0]) 
                    body = body[1:]
                else:
                    #* Add super()
                    if inheritFunction.GetParams() == []:
                        return
                    raise InvalidStatementInFunction(inheritFunction.GetName())   
            
            #* Load params
            functionParams += thisFunction.GetParams()
        
        # print("THIS IS PARAMS")
        # print(functionParams)
        #* Normal body
        #! issue when declare outside function 
        o_temp = ["envi", functionParams, o[1] + o[2], o[3]]
        # print(o_temp)
        for i in body:
            if type(i) == VarDecl:
                item = self.visit(i, o_temp)
                if item is not None:
                    o_temp[1].append(item)
        
        o_temp[0] = TypeOfchecker
        for i in body:
            if type(i) == ReturnStmt:
                functionReturnType = thisFunction.GetReturnType()
                returnStmtType = self.visit(i, o_temp[1] + o_temp[2])
                
                #* Void Void
                if type(functionReturnType) == VoidType and type(returnStmtType) == VoidType:
                    continue

                elif type(functionReturnType) == AutoType:
                    thisFunction.ChangeReturnType(returnStmtType)
                    continue

                #* FloatType = IntegerType
                elif type(functionReturnType) == FloatType and type(returnStmtType) == IntegerType:
                    continue
                
                #* Check if return type is same
                elif type(functionReturnType) == type(returnStmtType):
                    continue

                else:
                    raise TypeMismatchInStatement(i)
                
            self.visit(i, o_temp)

        #$ ["typeOfChecker", [current], [father]]
        if TypeOfchecker== "func":
            o.pop()
        

    #%IfStmt: #cond: Expr, 
    #% tstmt: Stmt, 
    #% fstmt: Stmt or None = None 
    def visitIfStmt(self, ctx, o): 
        typeOfChecker = o[0]
        if typeOfChecker == "envi":
            return
        
        #* Check cond
        typeOfCond = self.visit(ctx.cond, o[1] + o[2])
        if type(typeOfCond) != BooleanType:
            raise TypeMismatchInStatement(ctx)

        o[0] = "elif"
        #* Check blockStmt
        if type(ctx.tstmt) == BlockStmt:
            self.visit(ctx.tstmt, o)
        elif type(ctx.tstmt) == ReturnStmt:
            Tool.CheckReturnAndFunction(self, ctx.tstmt, o)
        else:
            self.visit(ctx.tstmt, o)

        #* Check fstmt
        if ctx.fstmt is not None:
            if type(ctx.fstmt) == BlockStmt:
                self.visit(ctx.fstmt, o)
            elif type(ctx.fstmt) == ReturnStmt:
                Tool.CheckReturnAndFunction(self, ctx.fstmt, o)
            else:
                self.visit(ctx.fstmt, o)

        o[0] = typeOfChecker

    #% ForStmt: #init: AssignStmt, 
    #% cond: Expr, 
    #% upd: Expr, 
    #% stmt: Stmt
    def visitForStmt(self, ctx, o): 
        typeOfChecker = o[0]
        if typeOfChecker == "envi":
            return
        
        #* Check init
        typeOfScalar = self.visit(ctx.init.lhs, o[1] + o[2])
        if type(typeOfScalar) != IntegerType:
            raise TypeMismatchInStatement(ctx)
        #* Check AssignStmt
        self.visit(ctx.init, o)

        #* Check cond
        typeOfCond = self.visit(ctx.cond, o[1] + o[2])
        if type(typeOfCond) != BooleanType:
            raise TypeMismatchInStatement(ctx)
        
        #* Check upd
        typeOfUpd = self.visit(ctx.upd, o[1] + o[2])
        if type(typeOfUpd) != IntegerType:
            raise TypeMismatchInStatement(ctx)

        
        if typeOfChecker in ["chec", "func"]:
            o[0] = "loop"
        else:
            #* Loop in loop
            o[0] = o[0] + "loop"


        #* Check stmt
        self.visit(ctx.stmt, o)

        #* End loop
        o[0] = typeOfChecker



    #% WhileStmt: #cond: Expr, stmt: Stmt 
    def visitWhileStmt(self, ctx, o): 
        typeOfChecker = o[0]
        if typeOfChecker == "envi":
            return
        
        #* Check cond
        typeOfCond = self.visit(ctx.cond, o[1] + o[2])
        if type(typeOfCond) != BooleanType:
            raise TypeMismatchInStatement(ctx)

        if typeOfChecker in ["chec", "func"]:
            o[0] = "loop"
        else:
            #* Loop in loop
            o[0] = o[0] + "loop"

        #* Check stmt
        self.visit(ctx.stmt, o)

        #* End loop
        o[0] = typeOfChecker

    #% DowhileStmt: #cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ctx, o): 
        typeOfChecker = o[0]
        if typeOfChecker == "envi":
            return
        
        if typeOfChecker in ["chec", "func"]:
            o[0] = "loop"
        else:
            #* Loop in loop
            o[0] = o[0] + "loop"

        #* Check blockStmt
        self.visit(ctx.stmt, o)

        #* Check cond
        typeOfCond = self.visit(ctx.cond, o[1] + o[2])
        if type(typeOfCond) != BooleanType:
            raise TypeMismatchInStatement(ctx.cond)

        #* End loop
        o[0] = typeOfChecker

    def visitBreakStmt(self, ctx:BreakStmt, o): 
        if type(o[0]) == "envi":
            return
        typeOfChecker = o[0]
        if typeOfChecker in  ["chec", "func"]:
            raise MustInLoop(ctx)
        return None
    
    def visitContinueStmt(self, ctx:ContinueStmt, o): 
        if type(o[0]) == "envi":
            return
        typeOfChecker = o[0]
        if typeOfChecker in ["chec", "func"]:
            raise MustInLoop(ctx)
        return None

    #% ReturnStmt: expr: Expr
    def visitReturnStmt(self, ctx: ReturnStmt, o):
        if ctx.expr is None:
            return VoidType()
        return self.visit(ctx.expr, o) 
    
    #% CallStmt: # name: str, args: List[Expr]
    def visitCallStmt(self, ctx:CallStmt, o): 
        if o[0] == "envi":
            return
        
        #* PreventDefault
        if ctx.name == "preventDefault":
            return 
        
        #! FIX THIS
        #* super
        #$ [Symbol, "inheritFunctionName"]
        if ctx.name == "super" and type(o[len(o)-1]) == type(""):
            fatherFunction = Tool.FindSymbol(o.pop(), Identifier(), o[1] + o[2])
            self.visit(fatherFunction, o)
            return 

        #* Call normal statement
        Tool.CheckArgsInFunction(self, ctx.name, ctx.args, ctx, o)

        #* Case function auto
        thisFunction = Tool.FindSymbol(ctx.name, Identifier(), o[1] + o[2])
        if type(thisFunction.GetReturnType()) == AutoType:
            thisFunction.ChangeReturnType(VoidType())

        # elif type(thisFunction.GetReturnType()) != VoidType:
        #     raise TypeMismatchInStatement(ctx)

        return 
    

    #$ DECLARE
    #% Vardecl: #name: str, typ: Type, init: Expr or None = None)
    def visitVarDecl(self, ctx:VarDecl, o): 
        if o[0] == "envi":

            return Symbol(ctx.name, self.visit(ctx.typ, o), True if type(ctx.typ) is ArrayType else False)  
        else:
            #!Check on current scope then check on father scope
            #! ["envi",[current], [father]] 
            #! redeclare only check current, find symbol check current then father
            #! o = ["chec", [current], [father]] 
            Tool.CheckRedeclare(self, ctx.name, Variable(), o[1])
            symbol = Tool.FindSymbol(ctx.name, Identifier(), o[1] + o[2])

            #* Initialize case
            if ctx.init:
                try:
                    dimensionArrayLit, typeInit = self.visit(ctx.init,o[1] + o[2])
                except:
                    typeInit = self.visit(ctx.init,o[1] + o[2])

                # print("-------------VAR-DECLARE----------------")
                # print(ctx)
                # print(type(ctx.typ))
                # print(type(typeInit))

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
                        functionCall = Tool.FindSymbol(ctx.init.name, Identifier(), o[1] + o[2])
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
                raise Invalid(Variable(),ctx.name)
            
            # VarDecl(n, ArrayType([1, 2], IntegerType))
            #* ArrayType
            elif type(ctx.typ) == ArrayType: 
                if type(ctx.typ.typ) == AutoType:
                    raise Invalid(Variable(),ctx.name)
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
        if o[0] == "envi":
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
        if o[0] == "envi":
            inheritParams, params = [], []
            for param in ctx.params:
                par, isIhr = self.visit(param, o)
                if isIhr:
                    if par is not None:
                        inheritParams.append(par)
                if par is not None:
                    params.append(par)
            return FunctionSymbol(ctx.name, ctx.return_type, params, inheritParams)
        else:
            o[0] = "func"
            #! ["func",[current], [father]] 
            #* Check redeclare
            Tool.CheckRedeclare(self, ctx.name, Function(), o[1])

            #* Check redeclare in params
            thisFunction = Tool.FindSymbol(ctx.name, Function(), o[1])
            functionParams = thisFunction.GetParams()
            for param in ctx.params:
                Tool.CheckRedeclare(self, param.name, Parameter(), functionParams)

            #* Check inherit 
            if ctx.inherit:
                inheritFunction = Tool.FindSymbol(ctx.inherit, Function(), o[1])

                #* Check if Child has params like Father inherit params
                for param in functionParams:
                    Tool.CheckParamsInvalid(self, param.GetName(), Parameter(), inheritFunction.GetInheritParams())
                
                #* Father inherit params + Son params
                inheritFunctionParams_FunctionParams = inheritFunction.GetInheritParams() + functionParams
                
                self.visit(ctx.body, o + [[ctx.inherit,ctx.name]])
                return None
            else:
                
                self.visit(ctx.body, o + [[None, ctx.name]])
                return None
            
            o[0] = "chec"


    #$ PROGRAM 
    #% program: #decls: List[Decl] 
    #$ o = [Symbol(name, mtype),...]
    def visitProgram(self, ctx:Program, o):
        o = ["envi", [], []]

        #* ["typeOfChecker",CurrentScope, FatherScope]
        #* Get all declaration
        for decl in ctx.decls:
            item = self.visit(decl, o)
            if item is not None:
                o[1].append(item)
        

        # print("------------ROUND1----------------")
        # for i in o:
        #     print(repr(i))

        o[0] = "chec"
        for decl in ctx.decls:
            self.visit(decl, o)
        
        # print("--------------ROUND2--------------")
        # for i in o:
        #     print(repr(i))

        #* Check main function
        hasMain = False
        for decl in o[1]:
            if decl.GetName() == "main":
                hasMain = True
        if hasMain == False:
            raise NoEntryPoint()

        