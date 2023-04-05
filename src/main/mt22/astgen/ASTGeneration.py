from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    #@ 1. Program

    #% program: decls;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decls()))

    #% decls: decl decls | decl;
    # ! Return a list 
    def visitDecls(self, ctx: MT22Parser.decls):
        if ctx.decls():
            return self.visit(ctx.decl()) + self.visit(ctx.decls())
        return self.visit(ctx.decl())
    
    #% decl: functiondecl |variabledecl | statementlist |mainfunction;
    def visitDecl(self, ctx: MT22Parser.decl):
        if ctx.functiondecl():
            return self.visit(ctx.functiondecl())
        elif ctx.variabledecl():
            return self.visit(ctx.variabledecl())
        elif ctx.statementlist():
            return self.visit(ctx.statementlist())
        return self.visit(ctx.mainfunction())

    #@ 2. Declaration
    #@ 2.1 Function declare

    #@ 2.1.1 Main function
    #% mainfunction: functionmainprot functionbody;
    def visitMainfunction(self, ctx: MT22Parser.mainfunction):
        mf = self.visit(ctx.functionmainprot())
        return [FuncDecl(
            mf[0],
            mf[1],
            mf[2],
            mf[3],
            self.visit(ctx.functionbody()) # BlockStmt
        )]
    
    #% functionmainprot:MAIN COL FUNCTION (VOID|vartype) LB parameterlist? RB (INHERIT ID)?;
    def visitFunctionmainprot(self, ctx: MT22Parser.functionmainprot):
        mf_name = ctx.MAIN().getText()
        mf_return_type = VoidType() if ctx.VOID() else self.visit(ctx.vartype()) 
        mf_params = self.visit(ctx.parameterlist()) if ctx.parameterlist() else []
        mf_inherit = ctx.ID().getText() if ctx.ID() else None
        return (mf_name, mf_return_type, mf_params, mf_inherit)
    
    #@ 2.1.2 Normal function
    #% functiondecl: functionprot functionbody;
    def visitFunctiondecl(self, ctx: MT22Parser.functiondecl):
        f_name, f_return_type, f_params, f_inherit = self.visit(ctx.functionprot())
        return [FuncDecl(
            f_name,
            f_return_type,
            f_params,
            f_inherit,
            self.visit(ctx.functionbody()) # BlockStmt
        )]
    
    #% functionprot: ID COL FUNCTION (VOID|vartype) LB parameterlist? RB (INHERIT ID)?;
    def visitFunctionprot(self, ctx: MT22Parser.functionprot):
        f_name = ctx.ID(0).getText()
        f_return_type = VoidType() if ctx.VOID() else self.visit(ctx.vartype()) 
        f_params = self.visit(ctx.parameterlist()) if ctx.parameterlist() else []
        f_inherit = ctx.ID(1).getText() if ctx.ID(1) else None
        return f_name, f_return_type, f_params, f_inherit

    #@ 2.1.3 Function body
    #% functionbody: blockstatement;
    def visitFunctionbody(self, ctx: MT22Parser.functionbody):
        return self.visit(ctx.blockstatement())

    #@ 2.2 Variable declare
    #%variabledecl: (variabledeclassign|variabledecls) SEM;
    def visitVariabledecl(self, ctx: MT22Parser.variabledecl):
        if ctx.variabledeclassign():
            # [("a", 3), ("b", 2), ("c", 1), type]
            ListTuple = self.visit(ctx.variabledeclassign())
            Type = ListTuple.pop()
            idList, expList = [], []
            for tup in ListTuple:
                idList.append(tup[0])
                expList.append(tup[1])
            ReverseExp = zip(idList, expList[::-1])
            return [VarDecl(var[0], Type, var[1]) for var in ReverseExp]
        return self.visit(ctx.variabledecls())

    #% variabledecls:idlist COL vartype;
    def visitVariabledecls(self, ctx: MT22Parser.variabledecls):
        idList = self.visit(ctx.idlist())
        varType = self.visit(ctx.vartype())
        return [VarDecl(id, varType) for id in idList]

    #% variabledeclassign: ID COMA variabledeclassign COMA expression
    #% | ID COL vartype EQU expression;
    def visitVariabledeclassign(self, ctx: MT22Parser.variabledeclassign):
        if ctx.vartype():
            return [(ctx.ID().getText(),self.visit(ctx.expression()) ) , self.visit(ctx.vartype())]
        return [(ctx.ID().getText(), self.visit(ctx.expression()))] + self.visit(ctx.variabledeclassign())
    
    #@ 3. LIST
    #@ 3.1. Parameter list
    #% parameterlist: parameter COMA parameterlist| parameter;
    def visitParameterlist(self, ctx: MT22Parser.parameterlist):
        #! return a list of parameter
        if ctx.parameterlist():
            return [self.visit(ctx.parameter())] + self.visit(ctx.parameterlist())
        return [self.visit(ctx.parameter())]

    #% parameter: INHERIT? OUT? ID COL vartype;
    def visitParameter(self, ctx: MT22Parser.parameter):
        return ParamDecl(
            str(ctx.ID().getText()),
            self.visit(ctx.vartype()),
            True if ctx.OUT() else False,
            True if ctx.INHERIT() else False
        )
    
    #@ 3.2. ID list
    #% idlist: ID  COMA idlist | ID;
    def visitIdlist(self, ctx: MT22Parser.idlist):
        if ctx.idlist():
            return [ctx.ID().getText()] + self.visit(ctx.idlist())
        return [ctx.ID().getText()]
    
    #@ 3.3. Expression list
    #% expressionlist: expression COMA expressionlist| expression SEM?;
    def visitExpressionlist(self, ctx: MT22Parser.expressionlist):
        if ctx.expressionlist():
            return [self.visit(ctx.expression())] + self.visit(ctx.expressionlist())
        return [self.visit(ctx.expression())]

    #@ 3.4. Statement list
    #% statementlist: statement SEM statementlist | statement SEM?;
    def visitStatementlist(self, ctx: MT22Parser.statementlist):
        if ctx.statementlist():
            return [self.visit(ctx.statement())] + self.visit(ctx.statementlist())
        return [self.visit(ctx.statement())]

    #@ 3.5. Argument list
    #% arguementlist: arguement COMA arguementlist | arguement;
    def visitArguementlist(self, ctx: MT22Parser.arguementlist):
        if ctx.arguementlist():
            return [self.visit(ctx.arguement())] + self.visit(ctx.arguementlist())
        return [self.visit(ctx.arguement())]
    
    # % arguement: expression;
    def visitArguement(self, ctx: MT22Parser.arguement):
        return self.visit(ctx.expression())


    #@ 4. STATEMENT
    #%statement: assignstatement 
    #% | ifstatement 
    #% | forstatement 
    #% | whilestatement
    #% | dowhilestatement
    #% | breakstatement
    #% | continuestatement
    #% | returnstatement
    #% | callstatement
    #% | blockstatement
    #% ;
    def visitStatement(self, ctx: MT22Parser.statement):
        if ctx.assignstatement():
            return self.visit(ctx.assignstatement())
        elif ctx.ifstatement():
            return self.visit(ctx.ifstatement())
        elif ctx.forstatement():
            return self.visit(ctx.forstatement())
        elif ctx.whilestatement():
            return self.visit(ctx.whilestatement())
        elif ctx.dowhilestatement():
            return self.visit(ctx.dowhilestatement())
        elif ctx.breakstatement():
            return self.visit(ctx.breakstatement())
        elif ctx.continuestatement():
            return self.visit(ctx.continuestatement())
        elif ctx.returnstatement():
            return self.visit(ctx.returnstatement())
        elif ctx.callstatement():
            return self.visit(ctx.callstatement())
        elif ctx.blockstatement():
            return self.visit(ctx.blockstatement())
        return None
    #@ 4.1. Assign statement
    #% assignstatement: lhs EQU expression SEM;
    def visitAssignstatement(self, ctx: MT22Parser.assignstatement):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expression()))
      
    #% lhs: scalarvar | indexexpression;
    def visitLhs(self, ctx: MT22Parser.lhs):
        if ctx.scalarvar():
            return Id(ctx.scalarvar().getText())
        return self.visit(ctx.indexexpression())
    
    #@ 4.2. If statement
    #% ifstatement: IF LB expression RB statement (ELSE statement)? ;
    def visitIfstatement(self, ctx: MT22Parser.ifstatement):
        return IfStmt(self.visit(ctx.expression()), self.visit(ctx.statement(0)), self.visit(ctx.statement(1)) if ctx.ELSE() else None)
    
    #@ 4.3. For statement
    #% forstatement: forhead statement;
    def visitForstatement(self, ctx: MT22Parser.forstatement):
        forHead = self.visit(ctx.forhead())
        return ForStmt(
            forHead[0],
            forHead[1],
            forHead[2],
            self.visit(ctx.statement())
        )
    
    #% forhead:FOR LB lhs EQU expression COMA expression COMA expression RB;
    def visitForhead(self, ctx: MT22Parser.forhead):
        return (AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expression(0))), 
                self.visit(ctx.expression(1)), 
                self.visit(ctx.expression(2))) 
    #@ 4.4. While statement
    #% whilestatement:whilecondition statement;
    def visitWhilestatement(self, ctx: MT22Parser.whilestatement):
        return WhileStmt(self.visit(ctx.whilecondition()), self.visit(ctx.statement()))

    #%whilecondition:WHILE LB expression RB;
    def visitWhilecondition(self, ctx: MT22Parser.whilecondition):
        return self.visit(ctx.expression())
    
    #@ 4.5. Do-while statement
    #%dowhilestatement: DO blockstatement whilecondition SEM;
    def visitDowhilestatement(self, ctx: MT22Parser.dowhilestatement):
        return DoWhileStmt(self.visit(ctx.whilecondition()), self.visit(ctx.blockstatement()))
    
    #@ 4.6. Break statement
    #% breakstatement: BREAK SEM;
    def visitBreakstatement(self, ctx: MT22Parser.breakstatement):
        return BreakStmt()

    #@ 4.7. Continue statement
    #% continuestatement: CONTINUE SEM;
    def visitContinuestatement(self, ctx: MT22Parser.continuestatement):
        return ContinueStmt()

    #@ 4.8. Return statement
    #% returnstatement: RETURN expression? SEM;
    def visitReturnstatement(self, ctx: MT22Parser.returnstatement):
        return ReturnStmt(self.visit(ctx.expression()) if ctx.expression() else None)

    #@ 4.9. Call statement
    #% callstatement: ID LB arguementlist? RB SEM;
    def visitCallstatement(self, ctx: MT22Parser.callstatement):
        return CallStmt(
            ctx.ID().getText(),
            self.visit(ctx.arguementlist()) if ctx.arguementlist() else []
        )

    #% functioncall: ID LB arguementlist? RB;
    def visitFunctioncall(self, ctx: MT22Parser.functioncall):
        return FuncCall(
            ctx.ID().getText(),
            self.visit(ctx.arguementlist()) if ctx.arguementlist() else []
        )

    #@ 4.10. Block statement
    #% blockstatement: LCB (statementlist|variabledecl)*? RCB;
    def visitBlockstatement(self, ctx: MT22Parser.blockstatement):
        listStmtVarDecl = []
        for item in range(1, ctx.getChildCount() - 1):
            if ctx.statementlist():
                listStmtVarDecl += self.visit(ctx.getChild(item))
            elif ctx.variabledecl():
                listStmtVarDecl += self.visit(ctx.getChild(item))
        return BlockStmt(listStmtVarDecl)

    #@ 5. EXPRESSION
    #%  stringop: SCOPE;
    def visitStringop(self, ctx: MT22Parser.stringop):
        return str(ctx.SCOPE().getText())
    
    #% relationalop: EQUL | NEQ | LESS | GREA | LOEQ | GOEQ;
    def visitRelationalop(self, ctx: MT22Parser.relationalop):
        return str(ctx.getText())

    #% indexexpression: ID indexop;
    def visitIndexexpression(self, ctx: MT22Parser.indexexpression):
        return ArrayCell(
            ctx.ID().getText(),
            #! return Expr list
            self.visit(ctx.indexop())
        )
    
    #%indexop:LSB expressionlist RSB;
    def visitIndexop(self, ctx: MT22Parser.indexop):
        return self.visit(ctx.expressionlist())

    #% operand: constant | functioncall | ID |subexpression ;
    def visitOperand(self, ctx: MT22Parser.operand):
        if ctx.constant():
            return self.visit(ctx.constant())
        if ctx.functioncall():
            return self.visit(ctx.functioncall())
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.subexpression())

    #% constant: STR | BOOL | FLO | INT | arr;
    def visitConstant(self, ctx: MT22Parser.constant):
        if ctx.STR():
            return StringLit(ctx.STR().getText())
        elif ctx.BOOL():
            return BooleanLit(True if ctx.BOOL().getText() == "true" else False)
        elif ctx.FLO():
            return FloatLit(float(ctx.FLO().getText()))
        elif ctx.INT():
            return IntegerLit(int(ctx.INT().getText()))
        return self.visit(ctx.arr())
    
    #% arr: LCB expressionlist? RCB;
    def visitArr(self, ctx: MT22Parser.arr):
        return ArrayLit(self.visit(ctx.expressionlist()) if ctx.expressionlist() else [])

    #% subexpression:LB expression RB ;
    def visitSubexpression(self, ctx: MT22Parser.subexpression):
        return self.visit(ctx.expression())

    #@ 5.1. Binary expression
    #% expression: expression_relat stringop expression_relat | expression_relat;
    def visitExpression(self, ctx: MT22Parser.expression):
        if ctx.stringop(): 
            return BinExpr(
                self.visit(ctx.stringop()),
                self.visit(ctx.expression_relat(0)),
                self.visit(ctx.expression_relat(1))
            )
        return self.visit(ctx.expression_relat(0))

    #% expression_relat: expression_logic relationalop expression_logic |expression_logic ;
    def visitExpression_relat(self, ctx: MT22Parser.expression_relat):
        if ctx.relationalop():
            return BinExpr(
                self.visit(ctx.relationalop()),
                self.visit(ctx.expression_logic(0)),
                self.visit(ctx.expression_logic(1))
            )
        return self.visit(ctx.expression_logic(0))
    
    #% expression_logic: expression_logic (AND|OR) expression_bina1|expression_bina1;
    def visitExpression_logic(self, ctx: MT22Parser.expression_logic):
        if ctx.AND() or ctx.OR():
            return BinExpr(
                str(ctx.getChild(1).getText()),
                self.visit(ctx.expression_logic()),
                self.visit(ctx.expression_bina1())
            )
        return self.visit(ctx.expression_bina1())

    #% expression_bina1: expression_bina1 (PLUS|MINU) expression_bina2|expression_bina2;
    def visitExpression_bina1(self, ctx: MT22Parser.expression_bina1):
        if ctx.PLUS() or ctx.MINU():
            return BinExpr(
                str(ctx.getChild(1).getText()),
                self.visit(ctx.expression_bina1()),
                self.visit(ctx.expression_bina2())
            )
        return self.visit(ctx.expression_bina2())

    #%expression_bina2: expression_bina2 (MUTI|DIVI|MODU) expression_unary | expression_unary;
    def visitExpression_bina2(self, ctx: MT22Parser.expression_bina2):
        if ctx.MUTI() or ctx.DIVI() or ctx.MODU():
            return BinExpr(
                str(ctx.getChild(1).getText()),
                self.visit(ctx.expression_bina2()),
                self.visit(ctx.expression_unary())
            )
        return self.visit(ctx.expression_unary())
    
    #@ 5.2. Unary expression
    #% expression_unary: NOT expression_unary
    #% | MINU expression_unary
    #% | indexexpression
    #% | operand;
    def visitExpression_unary(self, ctx: MT22Parser.expression_unary):
        if ctx.NOT():
            return UnExpr(
                str(ctx.NOT().getText()),
                self.visit(ctx.expression_unary())
            )
        elif ctx.MINU():
            return UnExpr(
                str(ctx.MINU().getText()),
                self.visit(ctx.expression_unary())
            )
        # a[1,2,3]
        elif ctx.indexexpression():
            #! return arrayCell
            return self.visit(ctx.indexexpression())
        elif ctx.operand():
            #! return Expr type
            return self.visit(ctx.operand())
        return None

    #@ TYPE & ARRAY
    #% vartype: atomictype | arraytype ;
    def visitVartype(self, ctx: MT22Parser.vartype):
        if ctx.atomictype():
            return self.visit(ctx.atomictype())
        return self.visit(ctx.arraytype())

    #@ Array
    #% arraytype:ARRAY (LSB dimension RSB OF atomictype)?;
    def visitArraytype(self, ctx: MT22Parser.arraytype):
        return ArrayType(self.visit(ctx.dimension()), 
                         self.visit(ctx.atomictype()))
    
    #% dimension: INT COMA dimension | INT;
    def visitDimension(self, ctx: MT22Parser.dimension):
        if ctx.dimension():
            return [ctx.INT().getText()] + self.visit(ctx.dimension())
        return [ctx.INT().getText()]

    #% atomictype: AUTO| STRING | BOOLEAN | FLOAT | INTEGER ;
    def visitAtomictype(self, ctx: MT22Parser.atomictype):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.AUTO():
            return AutoType()
        else:
            return None
    
    #@ Type
    # @ ID & LITERAL
    # just .getText() and set it type
    #% ID: (LETTER | UNDE) (LETTER | UNDE | DIGIT)*;
    # def visitId(self, ctx: MT22Parser.ID):
    #     return Id(str(ctx.getText()))

    #% INT: (POSINT | ZERO){self.text = self.text.replace('_','')} ;
    # def visitInt(self, ctx: MT22Parser.INT):
    #     return IntegerLit(int(ctx.getText()))

    #% BOOL: FALSE | TRUE;
    # def visitBool(self, ctx: MT22Parser.BOOL):
    #     return BooleanLit(True if ctx.TRUE() else False)
    
    #% FLO:  ((POSINT | ZERO)+ DOT DECIMAL EXPONENT?
	#% | (POSINT | ZERO)+ DOT? EXPONENT
	#% | DOT DECIMAL EXPONENT){self.text = self.text.replace('_','')};
    # def visitFlo(self, ctx: MT22Parser.FLO):
    #     return FloatLit(float(str(ctx.getText())))
    
    #% STR: (DB STR_CHAR*  DB) {self.text = self.text[1:-1]};
    # def visitStr(self, ctx: MT22Parser.STR):
    #     return StringLit(str(ctx.getText()))

