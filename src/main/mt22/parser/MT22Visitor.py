# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arr.
    def visitArr(self, ctx:MT22Parser.ArrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vartype.
    def visitVartype(self, ctx:MT22Parser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomictype.
    def visitAtomictype(self, ctx:MT22Parser.AtomictypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arithmetricop.
    def visitArithmetricop(self, ctx:MT22Parser.ArithmetricopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#booleanop.
    def visitBooleanop(self, ctx:MT22Parser.BooleanopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stringop.
    def visitStringop(self, ctx:MT22Parser.StringopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relationalop.
    def visitRelationalop(self, ctx:MT22Parser.RelationalopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension.
    def visitDimension(self, ctx:MT22Parser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operator.
    def visitOperator(self, ctx:MT22Parser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexpression.
    def visitSubexpression(self, ctx:MT22Parser.SubexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_relat.
    def visitExpression_relat(self, ctx:MT22Parser.Expression_relatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_logic.
    def visitExpression_logic(self, ctx:MT22Parser.Expression_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_bina1.
    def visitExpression_bina1(self, ctx:MT22Parser.Expression_bina1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_bina2.
    def visitExpression_bina2(self, ctx:MT22Parser.Expression_bina2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_unary.
    def visitExpression_unary(self, ctx:MT22Parser.Expression_unaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#constant.
    def visitConstant(self, ctx:MT22Parser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functioncall.
    def visitFunctioncall(self, ctx:MT22Parser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexexpression.
    def visitIndexexpression(self, ctx:MT22Parser.IndexexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexop.
    def visitIndexop(self, ctx:MT22Parser.IndexopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arguement.
    def visitArguement(self, ctx:MT22Parser.ArguementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionmainprot.
    def visitFunctionmainprot(self, ctx:MT22Parser.FunctionmainprotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionprot.
    def visitFunctionprot(self, ctx:MT22Parser.FunctionprotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionbody.
    def visitFunctionbody(self, ctx:MT22Parser.FunctionbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalarvar.
    def visitScalarvar(self, ctx:MT22Parser.ScalarvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignstatement.
    def visitAssignstatement(self, ctx:MT22Parser.AssignstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifstatement.
    def visitIfstatement(self, ctx:MT22Parser.IfstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forhead.
    def visitForhead(self, ctx:MT22Parser.ForheadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forstatement.
    def visitForstatement(self, ctx:MT22Parser.ForstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilecondition.
    def visitWhilecondition(self, ctx:MT22Parser.WhileconditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilestatement.
    def visitWhilestatement(self, ctx:MT22Parser.WhilestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhilestatement.
    def visitDowhilestatement(self, ctx:MT22Parser.DowhilestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakstatement.
    def visitBreakstatement(self, ctx:MT22Parser.BreakstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continuestatement.
    def visitContinuestatement(self, ctx:MT22Parser.ContinuestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnstatement.
    def visitReturnstatement(self, ctx:MT22Parser.ReturnstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstatement.
    def visitCallstatement(self, ctx:MT22Parser.CallstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstatement.
    def visitBlockstatement(self, ctx:MT22Parser.BlockstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expressionlist.
    def visitExpressionlist(self, ctx:MT22Parser.ExpressionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameterlist.
    def visitParameterlist(self, ctx:MT22Parser.ParameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arguementlist.
    def visitArguementlist(self, ctx:MT22Parser.ArguementlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statementlist.
    def visitStatementlist(self, ctx:MT22Parser.StatementlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variabledecl.
    def visitVariabledecl(self, ctx:MT22Parser.VariabledeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variabledeclassign.
    def visitVariabledeclassign(self, ctx:MT22Parser.VariabledeclassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variabledecls.
    def visitVariabledecls(self, ctx:MT22Parser.VariabledeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functiondecl.
    def visitFunctiondecl(self, ctx:MT22Parser.FunctiondeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#mainfunction.
    def visitMainfunction(self, ctx:MT22Parser.MainfunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraytype.
    def visitArraytype(self, ctx:MT22Parser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)



del MT22Parser