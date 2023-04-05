grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

// main function is unique => mean appear only once or none
program: decls EOF;
// program: expression EOF;

// ! --------------PARSER RULE--------------

arr: LCB expressionlist? RCB;

vartype: atomictype | arraytype ;
atomictype:AUTO| STRING | BOOLEAN | FLOAT | INTEGER ;
arithmetricop: MINU | PLUS | MUTI | DIVI | MODU;
booleanop: NOT | AND | OR;
stringop: SCOPE;
relationalop: EQUL | NEQ | LESS | GREA | LOEQ | GOEQ;
dimension: INT COMA dimension | INT;

// ?testing expression
operator: arithmetricop| booleanop | stringop | relationalop | indexexpression;
// *Two operation type
// *Two expression (condition expression & typical expression)
operand: constant | functioncall | ID |subexpression ;

//* Expression
subexpression:LB expression RB ;

expression: expression_relat stringop expression_relat | expression_relat;
expression_relat: expression_logic relationalop expression_logic |expression_logic ;
expression_logic: expression_logic (AND|OR) expression_bina1|expression_bina1;
expression_bina1: expression_bina1 (PLUS|MINU) expression_bina2|expression_bina2;
expression_bina2: expression_bina2 (MUTI|DIVI|MODU) expression_unary | expression_unary;
expression_unary: NOT expression_unary
| MINU expression_unary
| indexexpression
| operand
;

constant: STR | BOOL | FLO | INT | arr;
functioncall: ID LB arguementlist? RB;

indexexpression: ID indexop;

// ?testing expression


// *--------part of things--------
parameter: INHERIT? OUT? ID COL vartype;

// indexop []
indexop:LSB expressionlist RSB;

//? arguement add-on
arguement: expression;
functionmainprot:MAIN COL FUNCTION (VOID|vartype) LB parameterlist? RB (INHERIT ID)?;
functionprot: ID COL FUNCTION (VOID|vartype) LB parameterlist? RB (INHERIT ID)?;
// ?add-on not found in mt22
functionbody: blockstatement;

// *Statement
scalarvar: ID;
lhs: scalarvar | indexexpression;

statement: assignstatement 
| ifstatement 
| forstatement 
| whilestatement
| dowhilestatement
| breakstatement
| continuestatement
| returnstatement
| callstatement
| blockstatement
;

assignstatement: lhs EQU expression SEM;

ifstatement: IF LB expression RB statement (ELSE statement)? ;
// ?I put expression for init-express and condition-express
// ? statement should be statement list


forhead:FOR LB lhs EQU expression COMA expression COMA expression RB;
// modified
forstatement: forhead statement;

whilecondition:WHILE LB expression RB;

whilestatement:whilecondition statement;

dowhilestatement: DO blockstatement whilecondition SEM;

breakstatement: BREAK SEM;


continuestatement: CONTINUE SEM;

returnstatement: RETURN expression? SEM;

callstatement: ID LB arguementlist? RB SEM;

blockstatement: LCB (statementlist|variabledecl)*? RCB;

// *--------List of ...--------
idlist: ID  COMA idlist | ID;
expressionlist: expression COMA expressionlist| expression SEM?;
parameterlist: parameter COMA parameterlist| parameter;
arguementlist: arguement COMA arguementlist | arguement;
statementlist: statement SEM statementlist | statement SEM?;
// *--------Declare--------
variabledecl: (variabledeclassign|variabledecls) SEM;
variabledeclassign: ID COMA variabledeclassign COMA expression
| ID COL vartype EQU expression;
variabledecls:idlist COL vartype;

functiondecl: functionprot functionbody;

// ?unique function, whose name is main without any parameter and return nothing (type void).
mainfunction: functionmainprot functionbody;
// ?Is arrray type here?
arraytype:ARRAY (LSB dimension RSB OF atomictype)?;

// * MAIN PROGRAM
decls: decl decls | decl;
decl: functiondecl |variabledecl | statementlist |mainfunction;
// decl:arraydecl;
// !--------------LEXER RULE----------------

// * --------Comment--------
COMMENT_C : '/*' .*? '*/' -> skip ;
COMMENT_CPP : '//' ~[\r\n]* -> skip ;

// * --------String--------
fragment ESCAPE: '\\' ( 'b' | 'f' | 'n' | 'r' | 't' | '\'' | DB | '\\'| '"' );
fragment STR_CHAR: ESCAPE|~[\\'"\r\n];
STR: (DB STR_CHAR*  DB) {self.text = self.text[1:-1]};
fragment STRTYP: SCOPE;

// * --------Keyword--------
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';
MAIN:'main';

// *--------Boolean--------
BOOL: FALSE | TRUE;
FALSE: 'false';
TRUE: 'true';

// *--------Float--------
fragment DECIMAL:  DIGIT+;
fragment EXPONENT: ('e'|'E') ('+'|'-')? DIGIT+;
FLO:  ((POSINT | ZERO)+ DOT DECIMAL EXPONENT?
		| (POSINT | ZERO)+ DOT? EXPONENT
		| DOT DECIMAL EXPONENT){self.text = self.text.replace('_','')};

// *--------Integer--------
fragment POSINT: [1-9] (UNDE+ DIGIT | DIGIT)*;
INT: (POSINT | ZERO){self.text = self.text.replace('_','')} ;

// *--------Identifier--------
fragment DIGIT: [0-9];
fragment LETTER: ([a-z] | [A-Z]);
ID: (LETTER | UNDE) (LETTER | UNDE | DIGIT)*;


// *--------Array--------


//*--------Seprator--------
COMA: ',';
COL: ':';
SEM: ';';
DOT: '.';
LSB: '[';
RSB: ']';
LB: '(';
RB: ')';
LCB: '{';
RCB: '}';
EQU:'=';

// *--------Tokens--------
DB: '"';
fragment ZERO: '0';
UNDE: '_';
PLUS: '+';
MINU: '-';
MUTI: '*';
DIVI: '/';
MODU: '%';
NOT: '!'; 
// *--------Operator--------
AND: '&&';
OR: '||';
EQUL: '==';
NEQ: '!=';
LESS: '<';
LOEQ: '<=';
GREA: '>';
GOEQ: '>=';
SCOPE: '::';


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .{raise ErrorToken(self.text)};

fragment ESCAPE_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;
UNCLOSE_STRING: DB STR_CHAR* ( [\b\t\n\f\r"'\\] | EOF ) {raise UncloseString(self.text[1:])};

ILLEGAL_ESCAPE: DB STR_CHAR* ESCAPE_ILLEGAL{raise IllegalEscape(self.text[1:])};