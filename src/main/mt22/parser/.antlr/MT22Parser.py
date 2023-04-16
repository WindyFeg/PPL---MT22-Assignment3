# Generated from f:\Univercity\S2Y3\PRINCIPLES OF PROGRAMMING LANGUAGES\Assignment\assignment3\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u01cd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2\3\3\3")
        buf.write("\3\5\3v\n\3\3\3\3\3\3\4\3\4\5\4|\n\4\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\5\n\u008c\n\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\5\13\u0093\n\13\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u0099\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\5\16\u00a4\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00ab")
        buf.write("\n\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00b3\n\20\f")
        buf.write("\20\16\20\u00b6\13\20\3\21\3\21\3\21\3\21\3\21\3\21\7")
        buf.write("\21\u00be\n\21\f\21\16\21\u00c1\13\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\7\22\u00c9\n\22\f\22\16\22\u00cc\13\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\5\23\u00d4\n\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\5\24\u00db\n\24\3\25\3\25\3\25\5\25\u00e0")
        buf.write("\n\25\3\25\3\25\3\26\3\26\3\26\3\27\5\27\u00e8\n\27\3")
        buf.write("\27\5\27\u00eb\n\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\32\3\32\3\32\5\32\u00fc\n")
        buf.write("\32\3\32\3\32\5\32\u0100\n\32\3\32\3\32\3\32\5\32\u0105")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\33\5\33\u010c\n\33\3\33\3")
        buf.write("\33\5\33\u0110\n\33\3\33\3\33\3\33\5\33\u0115\n\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\5\36\u011d\n\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0129\n\37")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\5!\u0137\n!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$")
        buf.write("\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3)\3)\5)\u015c\n)\3)\3)\3*\3*\3*\5*\u0163\n*\3*\3*\3")
        buf.write("*\3+\3+\3+\7+\u016b\n+\f+\16+\u016e\13+\3+\3+\3,\3,\3")
        buf.write(",\3,\5,\u0176\n,\3-\3-\3-\3-\3-\3-\5-\u017e\n-\5-\u0180")
        buf.write("\n-\3.\3.\3.\3.\3.\5.\u0187\n.\3/\3/\3/\3/\3/\5/\u018e")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u0196\n\60\5\60")
        buf.write("\u0198\n\60\3\61\3\61\5\61\u019c\n\61\3\61\3\61\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\5\62\u01ac\n\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3")
        buf.write("\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66")
        buf.write("\u01bf\n\66\3\67\3\67\3\67\3\67\5\67\u01c5\n\67\38\38")
        buf.write("\38\38\58\u01cb\n8\38\3\u016c\5\36 \"9\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjln\2\t\7\2\6\6\b\b\13\13\17\17\21\21")
        buf.write("\3\2-\61\3\2\62\64\3\2\65:\3\2\63\64\3\2-.\3\2/\61\2\u01d1")
        buf.write("\2p\3\2\2\2\4s\3\2\2\2\6{\3\2\2\2\b}\3\2\2\2\n\177\3\2")
        buf.write("\2\2\f\u0081\3\2\2\2\16\u0083\3\2\2\2\20\u0085\3\2\2\2")
        buf.write("\22\u008b\3\2\2\2\24\u0092\3\2\2\2\26\u0098\3\2\2\2\30")
        buf.write("\u009a\3\2\2\2\32\u00a3\3\2\2\2\34\u00aa\3\2\2\2\36\u00ac")
        buf.write("\3\2\2\2 \u00b7\3\2\2\2\"\u00c2\3\2\2\2$\u00d3\3\2\2\2")
        buf.write("&\u00da\3\2\2\2(\u00dc\3\2\2\2*\u00e3\3\2\2\2,\u00e7\3")
        buf.write("\2\2\2.\u00f0\3\2\2\2\60\u00f4\3\2\2\2\62\u00f6\3\2\2")
        buf.write("\2\64\u0106\3\2\2\2\66\u0116\3\2\2\28\u0118\3\2\2\2:\u011c")
        buf.write("\3\2\2\2<\u0128\3\2\2\2>\u012a\3\2\2\2@\u012f\3\2\2\2")
        buf.write("B\u0138\3\2\2\2D\u0143\3\2\2\2F\u0146\3\2\2\2H\u014b\3")
        buf.write("\2\2\2J\u014e\3\2\2\2L\u0153\3\2\2\2N\u0156\3\2\2\2P\u0159")
        buf.write("\3\2\2\2R\u015f\3\2\2\2T\u0167\3\2\2\2V\u0175\3\2\2\2")
        buf.write("X\u017f\3\2\2\2Z\u0186\3\2\2\2\\\u018d\3\2\2\2^\u0197")
        buf.write("\3\2\2\2`\u019b\3\2\2\2b\u01ab\3\2\2\2d\u01ad\3\2\2\2")
        buf.write("f\u01b1\3\2\2\2h\u01b4\3\2\2\2j\u01b7\3\2\2\2l\u01c4\3")
        buf.write("\2\2\2n\u01ca\3\2\2\2pq\5l\67\2qr\7\2\2\3r\3\3\2\2\2s")
        buf.write("u\7(\2\2tv\5X-\2ut\3\2\2\2uv\3\2\2\2vw\3\2\2\2wx\7)\2")
        buf.write("\2x\5\3\2\2\2y|\5\b\5\2z|\5j\66\2{y\3\2\2\2{z\3\2\2\2")
        buf.write("|\7\3\2\2\2}~\t\2\2\2~\t\3\2\2\2\177\u0080\t\3\2\2\u0080")
        buf.write("\13\3\2\2\2\u0081\u0082\t\4\2\2\u0082\r\3\2\2\2\u0083")
        buf.write("\u0084\7;\2\2\u0084\17\3\2\2\2\u0085\u0086\t\5\2\2\u0086")
        buf.write("\21\3\2\2\2\u0087\u0088\7\36\2\2\u0088\u0089\7 \2\2\u0089")
        buf.write("\u008c\5\22\n\2\u008a\u008c\7\36\2\2\u008b\u0087\3\2\2")
        buf.write("\2\u008b\u008a\3\2\2\2\u008c\23\3\2\2\2\u008d\u0093\5")
        buf.write("\n\6\2\u008e\u0093\5\f\7\2\u008f\u0093\5\16\b\2\u0090")
        buf.write("\u0093\5\20\t\2\u0091\u0093\5*\26\2\u0092\u008d\3\2\2")
        buf.write("\2\u0092\u008e\3\2\2\2\u0092\u008f\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0092\u0091\3\2\2\2\u0093\25\3\2\2\2\u0094\u0099")
        buf.write("\5&\24\2\u0095\u0099\5(\25\2\u0096\u0099\7\37\2\2\u0097")
        buf.write("\u0099\5\30\r\2\u0098\u0094\3\2\2\2\u0098\u0095\3\2\2")
        buf.write("\2\u0098\u0096\3\2\2\2\u0098\u0097\3\2\2\2\u0099\27\3")
        buf.write("\2\2\2\u009a\u009b\7&\2\2\u009b\u009c\5\32\16\2\u009c")
        buf.write("\u009d\7\'\2\2\u009d\31\3\2\2\2\u009e\u009f\5\34\17\2")
        buf.write("\u009f\u00a0\5\16\b\2\u00a0\u00a1\5\34\17\2\u00a1\u00a4")
        buf.write("\3\2\2\2\u00a2\u00a4\5\34\17\2\u00a3\u009e\3\2\2\2\u00a3")
        buf.write("\u00a2\3\2\2\2\u00a4\33\3\2\2\2\u00a5\u00a6\5\36\20\2")
        buf.write("\u00a6\u00a7\5\20\t\2\u00a7\u00a8\5\36\20\2\u00a8\u00ab")
        buf.write("\3\2\2\2\u00a9\u00ab\5\36\20\2\u00aa\u00a5\3\2\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\35\3\2\2\2\u00ac\u00ad\b\20\1\2\u00ad")
        buf.write("\u00ae\5 \21\2\u00ae\u00b4\3\2\2\2\u00af\u00b0\f\4\2\2")
        buf.write("\u00b0\u00b1\t\6\2\2\u00b1\u00b3\5 \21\2\u00b2\u00af\3")
        buf.write("\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5")
        buf.write("\3\2\2\2\u00b5\37\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b8")
        buf.write("\b\21\1\2\u00b8\u00b9\5\"\22\2\u00b9\u00bf\3\2\2\2\u00ba")
        buf.write("\u00bb\f\4\2\2\u00bb\u00bc\t\7\2\2\u00bc\u00be\5\"\22")
        buf.write("\2\u00bd\u00ba\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0!\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c2\u00c3\b\22\1\2\u00c3\u00c4\5$\23\2\u00c4")
        buf.write("\u00ca\3\2\2\2\u00c5\u00c6\f\4\2\2\u00c6\u00c7\t\b\2\2")
        buf.write("\u00c7\u00c9\5$\23\2\u00c8\u00c5\3\2\2\2\u00c9\u00cc\3")
        buf.write("\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb#")
        buf.write("\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce\7\62\2\2\u00ce")
        buf.write("\u00d4\5$\23\2\u00cf\u00d0\7.\2\2\u00d0\u00d4\5$\23\2")
        buf.write("\u00d1\u00d4\5*\26\2\u00d2\u00d4\5\26\f\2\u00d3\u00cd")
        buf.write("\3\2\2\2\u00d3\u00cf\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3")
        buf.write("\u00d2\3\2\2\2\u00d4%\3\2\2\2\u00d5\u00db\7\5\2\2\u00d6")
        buf.write("\u00db\7\32\2\2\u00d7\u00db\7\35\2\2\u00d8\u00db\7\36")
        buf.write("\2\2\u00d9\u00db\5\4\3\2\u00da\u00d5\3\2\2\2\u00da\u00d6")
        buf.write("\3\2\2\2\u00da\u00d7\3\2\2\2\u00da\u00d8\3\2\2\2\u00da")
        buf.write("\u00d9\3\2\2\2\u00db\'\3\2\2\2\u00dc\u00dd\7\37\2\2\u00dd")
        buf.write("\u00df\7&\2\2\u00de\u00e0\5\\/\2\u00df\u00de\3\2\2\2\u00df")
        buf.write("\u00e0\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\7\'\2\2")
        buf.write("\u00e2)\3\2\2\2\u00e3\u00e4\7\37\2\2\u00e4\u00e5\5.\30")
        buf.write("\2\u00e5+\3\2\2\2\u00e6\u00e8\7\27\2\2\u00e7\u00e6\3\2")
        buf.write("\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00ea\3\2\2\2\u00e9\u00eb")
        buf.write("\7\24\2\2\u00ea\u00e9\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb")
        buf.write("\u00ec\3\2\2\2\u00ec\u00ed\7\37\2\2\u00ed\u00ee\7!\2\2")
        buf.write("\u00ee\u00ef\5\6\4\2\u00ef-\3\2\2\2\u00f0\u00f1\7$\2\2")
        buf.write("\u00f1\u00f2\5X-\2\u00f2\u00f3\7%\2\2\u00f3/\3\2\2\2\u00f4")
        buf.write("\u00f5\5\32\16\2\u00f5\61\3\2\2\2\u00f6\u00f7\7\31\2\2")
        buf.write("\u00f7\u00f8\7!\2\2\u00f8\u00fb\7\r\2\2\u00f9\u00fc\7")
        buf.write("\23\2\2\u00fa\u00fc\5\6\4\2\u00fb\u00f9\3\2\2\2\u00fb")
        buf.write("\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00ff\7&\2\2")
        buf.write("\u00fe\u0100\5Z.\2\u00ff\u00fe\3\2\2\2\u00ff\u0100\3\2")
        buf.write("\2\2\u0100\u0101\3\2\2\2\u0101\u0104\7\'\2\2\u0102\u0103")
        buf.write("\7\27\2\2\u0103\u0105\7\37\2\2\u0104\u0102\3\2\2\2\u0104")
        buf.write("\u0105\3\2\2\2\u0105\63\3\2\2\2\u0106\u0107\7\37\2\2\u0107")
        buf.write("\u0108\7!\2\2\u0108\u010b\7\r\2\2\u0109\u010c\7\23\2\2")
        buf.write("\u010a\u010c\5\6\4\2\u010b\u0109\3\2\2\2\u010b\u010a\3")
        buf.write("\2\2\2\u010c\u010d\3\2\2\2\u010d\u010f\7&\2\2\u010e\u0110")
        buf.write("\5Z.\2\u010f\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u0111\u0114\7\'\2\2\u0112\u0113\7\27\2\2\u0113")
        buf.write("\u0115\7\37\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2")
        buf.write("\2\u0115\65\3\2\2\2\u0116\u0117\5T+\2\u0117\67\3\2\2\2")
        buf.write("\u0118\u0119\7\37\2\2\u01199\3\2\2\2\u011a\u011d\58\35")
        buf.write("\2\u011b\u011d\5*\26\2\u011c\u011a\3\2\2\2\u011c\u011b")
        buf.write("\3\2\2\2\u011d;\3\2\2\2\u011e\u0129\5> \2\u011f\u0129")
        buf.write("\5@!\2\u0120\u0129\5D#\2\u0121\u0129\5H%\2\u0122\u0129")
        buf.write("\5J&\2\u0123\u0129\5L\'\2\u0124\u0129\5N(\2\u0125\u0129")
        buf.write("\5P)\2\u0126\u0129\5R*\2\u0127\u0129\5T+\2\u0128\u011e")
        buf.write("\3\2\2\2\u0128\u011f\3\2\2\2\u0128\u0120\3\2\2\2\u0128")
        buf.write("\u0121\3\2\2\2\u0128\u0122\3\2\2\2\u0128\u0123\3\2\2\2")
        buf.write("\u0128\u0124\3\2\2\2\u0128\u0125\3\2\2\2\u0128\u0126\3")
        buf.write("\2\2\2\u0128\u0127\3\2\2\2\u0129=\3\2\2\2\u012a\u012b")
        buf.write("\5:\36\2\u012b\u012c\7*\2\2\u012c\u012d\5\32\16\2\u012d")
        buf.write("\u012e\7\"\2\2\u012e?\3\2\2\2\u012f\u0130\7\16\2\2\u0130")
        buf.write("\u0131\7&\2\2\u0131\u0132\5\32\16\2\u0132\u0133\7\'\2")
        buf.write("\2\u0133\u0136\5<\37\2\u0134\u0135\7\n\2\2\u0135\u0137")
        buf.write("\5<\37\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("A\3\2\2\2\u0138\u0139\7\f\2\2\u0139\u013a\7&\2\2\u013a")
        buf.write("\u013b\5:\36\2\u013b\u013c\7*\2\2\u013c\u013d\5\32\16")
        buf.write("\2\u013d\u013e\7 \2\2\u013e\u013f\5\32\16\2\u013f\u0140")
        buf.write("\7 \2\2\u0140\u0141\5\32\16\2\u0141\u0142\7\'\2\2\u0142")
        buf.write("C\3\2\2\2\u0143\u0144\5B\"\2\u0144\u0145\5<\37\2\u0145")
        buf.write("E\3\2\2\2\u0146\u0147\7\22\2\2\u0147\u0148\7&\2\2\u0148")
        buf.write("\u0149\5\32\16\2\u0149\u014a\7\'\2\2\u014aG\3\2\2\2\u014b")
        buf.write("\u014c\5F$\2\u014c\u014d\5<\37\2\u014dI\3\2\2\2\u014e")
        buf.write("\u014f\7\t\2\2\u014f\u0150\5T+\2\u0150\u0151\5F$\2\u0151")
        buf.write("\u0152\7\"\2\2\u0152K\3\2\2\2\u0153\u0154\7\7\2\2\u0154")
        buf.write("\u0155\7\"\2\2\u0155M\3\2\2\2\u0156\u0157\7\25\2\2\u0157")
        buf.write("\u0158\7\"\2\2\u0158O\3\2\2\2\u0159\u015b\7\20\2\2\u015a")
        buf.write("\u015c\5\32\16\2\u015b\u015a\3\2\2\2\u015b\u015c\3\2\2")
        buf.write("\2\u015c\u015d\3\2\2\2\u015d\u015e\7\"\2\2\u015eQ\3\2")
        buf.write("\2\2\u015f\u0160\7\37\2\2\u0160\u0162\7&\2\2\u0161\u0163")
        buf.write("\5\\/\2\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164\u0165\7\'\2\2\u0165\u0166\7\"\2\2")
        buf.write("\u0166S\3\2\2\2\u0167\u016c\7(\2\2\u0168\u016b\5^\60\2")
        buf.write("\u0169\u016b\5`\61\2\u016a\u0168\3\2\2\2\u016a\u0169\3")
        buf.write("\2\2\2\u016b\u016e\3\2\2\2\u016c\u016d\3\2\2\2\u016c\u016a")
        buf.write("\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u016c\3\2\2\2\u016f")
        buf.write("\u0170\7)\2\2\u0170U\3\2\2\2\u0171\u0172\7\37\2\2\u0172")
        buf.write("\u0173\7 \2\2\u0173\u0176\5V,\2\u0174\u0176\7\37\2\2\u0175")
        buf.write("\u0171\3\2\2\2\u0175\u0174\3\2\2\2\u0176W\3\2\2\2\u0177")
        buf.write("\u0178\5\32\16\2\u0178\u0179\7 \2\2\u0179\u017a\5X-\2")
        buf.write("\u017a\u0180\3\2\2\2\u017b\u017d\5\32\16\2\u017c\u017e")
        buf.write("\7\"\2\2\u017d\u017c\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("\u0180\3\2\2\2\u017f\u0177\3\2\2\2\u017f\u017b\3\2\2\2")
        buf.write("\u0180Y\3\2\2\2\u0181\u0182\5,\27\2\u0182\u0183\7 \2\2")
        buf.write("\u0183\u0184\5Z.\2\u0184\u0187\3\2\2\2\u0185\u0187\5,")
        buf.write("\27\2\u0186\u0181\3\2\2\2\u0186\u0185\3\2\2\2\u0187[\3")
        buf.write("\2\2\2\u0188\u0189\5\60\31\2\u0189\u018a\7 \2\2\u018a")
        buf.write("\u018b\5\\/\2\u018b\u018e\3\2\2\2\u018c\u018e\5\60\31")
        buf.write("\2\u018d\u0188\3\2\2\2\u018d\u018c\3\2\2\2\u018e]\3\2")
        buf.write("\2\2\u018f\u0190\5<\37\2\u0190\u0191\7\"\2\2\u0191\u0192")
        buf.write("\5^\60\2\u0192\u0198\3\2\2\2\u0193\u0195\5<\37\2\u0194")
        buf.write("\u0196\7\"\2\2\u0195\u0194\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196\u0198\3\2\2\2\u0197\u018f\3\2\2\2\u0197\u0193\3")
        buf.write("\2\2\2\u0198_\3\2\2\2\u0199\u019c\5b\62\2\u019a\u019c")
        buf.write("\5d\63\2\u019b\u0199\3\2\2\2\u019b\u019a\3\2\2\2\u019c")
        buf.write("\u019d\3\2\2\2\u019d\u019e\7\"\2\2\u019ea\3\2\2\2\u019f")
        buf.write("\u01a0\7\37\2\2\u01a0\u01a1\7 \2\2\u01a1\u01a2\5b\62\2")
        buf.write("\u01a2\u01a3\7 \2\2\u01a3\u01a4\5\32\16\2\u01a4\u01ac")
        buf.write("\3\2\2\2\u01a5\u01a6\7\37\2\2\u01a6\u01a7\7!\2\2\u01a7")
        buf.write("\u01a8\5\6\4\2\u01a8\u01a9\7*\2\2\u01a9\u01aa\5\32\16")
        buf.write("\2\u01aa\u01ac\3\2\2\2\u01ab\u019f\3\2\2\2\u01ab\u01a5")
        buf.write("\3\2\2\2\u01acc\3\2\2\2\u01ad\u01ae\5V,\2\u01ae\u01af")
        buf.write("\7!\2\2\u01af\u01b0\5\6\4\2\u01b0e\3\2\2\2\u01b1\u01b2")
        buf.write("\5\64\33\2\u01b2\u01b3\5\66\34\2\u01b3g\3\2\2\2\u01b4")
        buf.write("\u01b5\5\62\32\2\u01b5\u01b6\5\66\34\2\u01b6i\3\2\2\2")
        buf.write("\u01b7\u01be\7\30\2\2\u01b8\u01b9\7$\2\2\u01b9\u01ba\5")
        buf.write("\22\n\2\u01ba\u01bb\7%\2\2\u01bb\u01bc\7\26\2\2\u01bc")
        buf.write("\u01bd\5\b\5\2\u01bd\u01bf\3\2\2\2\u01be\u01b8\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bfk\3\2\2\2\u01c0\u01c1\5n8\2")
        buf.write("\u01c1\u01c2\5l\67\2\u01c2\u01c5\3\2\2\2\u01c3\u01c5\5")
        buf.write("n8\2\u01c4\u01c0\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5m\3")
        buf.write("\2\2\2\u01c6\u01cb\5f\64\2\u01c7\u01cb\5`\61\2\u01c8\u01cb")
        buf.write("\5^\60\2\u01c9\u01cb\5h\65\2\u01ca\u01c6\3\2\2\2\u01ca")
        buf.write("\u01c7\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01c9\3\2\2\2")
        buf.write("\u01cbo\3\2\2\2*u{\u008b\u0092\u0098\u00a3\u00aa\u00b4")
        buf.write("\u00bf\u00ca\u00d3\u00da\u00df\u00e7\u00ea\u00fb\u00ff")
        buf.write("\u0104\u010b\u010f\u0114\u011c\u0128\u0136\u015b\u0162")
        buf.write("\u016a\u016c\u0175\u017d\u017f\u0186\u018d\u0195\u0197")
        buf.write("\u019b\u01ab\u01be\u01c4\u01ca")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
                     "'float'", "'for'", "'function'", "'if'", "'integer'", 
                     "'return'", "'string'", "'while'", "'void'", "'out'", 
                     "'continue'", "'of'", "'inherit'", "'array'", "'main'", 
                     "<INVALID>", "'false'", "'true'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','", "':'", "';'", "'.'", "'['", "']'", 
                     "'('", "')'", "'{'", "'}'", "'='", "'\"'", "'_'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'" ]

    symbolicNames = [ "<INVALID>", "COMMENT_C", "COMMENT_CPP", "STR", "AUTO", 
                      "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", 
                      "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "WHILE", 
                      "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                      "MAIN", "BOOL", "FALSE", "TRUE", "FLO", "INT", "ID", 
                      "COMA", "COL", "SEM", "DOT", "LSB", "RSB", "LB", "RB", 
                      "LCB", "RCB", "EQU", "DB", "UNDE", "PLUS", "MINU", 
                      "MUTI", "DIVI", "MODU", "NOT", "AND", "OR", "EQUL", 
                      "NEQ", "LESS", "LOEQ", "GREA", "GOEQ", "SCOPE", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_arr = 1
    RULE_vartype = 2
    RULE_atomictype = 3
    RULE_arithmetricop = 4
    RULE_booleanop = 5
    RULE_stringop = 6
    RULE_relationalop = 7
    RULE_dimension = 8
    RULE_operator = 9
    RULE_operand = 10
    RULE_subexpression = 11
    RULE_expression = 12
    RULE_expression_relat = 13
    RULE_expression_logic = 14
    RULE_expression_bina1 = 15
    RULE_expression_bina2 = 16
    RULE_expression_unary = 17
    RULE_constant = 18
    RULE_functioncall = 19
    RULE_indexexpression = 20
    RULE_parameter = 21
    RULE_indexop = 22
    RULE_arguement = 23
    RULE_functionmainprot = 24
    RULE_functionprot = 25
    RULE_functionbody = 26
    RULE_scalarvar = 27
    RULE_lhs = 28
    RULE_statement = 29
    RULE_assignstatement = 30
    RULE_ifstatement = 31
    RULE_forhead = 32
    RULE_forstatement = 33
    RULE_whilecondition = 34
    RULE_whilestatement = 35
    RULE_dowhilestatement = 36
    RULE_breakstatement = 37
    RULE_continuestatement = 38
    RULE_returnstatement = 39
    RULE_callstatement = 40
    RULE_blockstatement = 41
    RULE_idlist = 42
    RULE_expressionlist = 43
    RULE_parameterlist = 44
    RULE_arguementlist = 45
    RULE_statementlist = 46
    RULE_variabledecl = 47
    RULE_variabledeclassign = 48
    RULE_variabledecls = 49
    RULE_functiondecl = 50
    RULE_mainfunction = 51
    RULE_arraytype = 52
    RULE_decls = 53
    RULE_decl = 54

    ruleNames =  [ "program", "arr", "vartype", "atomictype", "arithmetricop", 
                   "booleanop", "stringop", "relationalop", "dimension", 
                   "operator", "operand", "subexpression", "expression", 
                   "expression_relat", "expression_logic", "expression_bina1", 
                   "expression_bina2", "expression_unary", "constant", "functioncall", 
                   "indexexpression", "parameter", "indexop", "arguement", 
                   "functionmainprot", "functionprot", "functionbody", "scalarvar", 
                   "lhs", "statement", "assignstatement", "ifstatement", 
                   "forhead", "forstatement", "whilecondition", "whilestatement", 
                   "dowhilestatement", "breakstatement", "continuestatement", 
                   "returnstatement", "callstatement", "blockstatement", 
                   "idlist", "expressionlist", "parameterlist", "arguementlist", 
                   "statementlist", "variabledecl", "variabledeclassign", 
                   "variabledecls", "functiondecl", "mainfunction", "arraytype", 
                   "decls", "decl" ]

    EOF = Token.EOF
    COMMENT_C=1
    COMMENT_CPP=2
    STR=3
    AUTO=4
    BREAK=5
    BOOLEAN=6
    DO=7
    ELSE=8
    FLOAT=9
    FOR=10
    FUNCTION=11
    IF=12
    INTEGER=13
    RETURN=14
    STRING=15
    WHILE=16
    VOID=17
    OUT=18
    CONTINUE=19
    OF=20
    INHERIT=21
    ARRAY=22
    MAIN=23
    BOOL=24
    FALSE=25
    TRUE=26
    FLO=27
    INT=28
    ID=29
    COMA=30
    COL=31
    SEM=32
    DOT=33
    LSB=34
    RSB=35
    LB=36
    RB=37
    LCB=38
    RCB=39
    EQU=40
    DB=41
    UNDE=42
    PLUS=43
    MINU=44
    MUTI=45
    DIVI=46
    MODU=47
    NOT=48
    AND=49
    OR=50
    EQUL=51
    NEQ=52
    LESS=53
    LOEQ=54
    GREA=55
    GOEQ=56
    SCOPE=57
    WS=58
    ERROR_CHAR=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decls(self):
            return self.getTypedRuleContext(MT22Parser.DeclsContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.decls()
            self.state = 111
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arr




    def arr(self):

        localctx = MT22Parser.ArrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_arr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(MT22Parser.LCB)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.STR) | (1 << MT22Parser.BOOL) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.ID) | (1 << MT22Parser.LB) | (1 << MT22Parser.LCB) | (1 << MT22Parser.MINU) | (1 << MT22Parser.NOT))) != 0):
                self.state = 114
                self.expressionlist()


            self.state = 117
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomictype(self):
            return self.getTypedRuleContext(MT22Parser.AtomictypeContext,0)


        def arraytype(self):
            return self.getTypedRuleContext(MT22Parser.ArraytypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vartype




    def vartype(self):

        localctx = MT22Parser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vartype)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.atomictype()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.arraytype()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomictypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomictype




    def atomictype(self):

        localctx = MT22Parser.AtomictypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atomictype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.AUTO) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmetricopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINU(self):
            return self.getToken(MT22Parser.MINU, 0)

        def PLUS(self):
            return self.getToken(MT22Parser.PLUS, 0)

        def MUTI(self):
            return self.getToken(MT22Parser.MUTI, 0)

        def DIVI(self):
            return self.getToken(MT22Parser.DIVI, 0)

        def MODU(self):
            return self.getToken(MT22Parser.MODU, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arithmetricop




    def arithmetricop(self):

        localctx = MT22Parser.ArithmetricopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arithmetricop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.PLUS) | (1 << MT22Parser.MINU) | (1 << MT22Parser.MUTI) | (1 << MT22Parser.DIVI) | (1 << MT22Parser.MODU))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_booleanop




    def booleanop(self):

        localctx = MT22Parser.BooleanopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_booleanop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.NOT) | (1 << MT22Parser.AND) | (1 << MT22Parser.OR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCOPE(self):
            return self.getToken(MT22Parser.SCOPE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_stringop




    def stringop(self):

        localctx = MT22Parser.StringopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stringop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(MT22Parser.SCOPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUL(self):
            return self.getToken(MT22Parser.EQUL, 0)

        def NEQ(self):
            return self.getToken(MT22Parser.NEQ, 0)

        def LESS(self):
            return self.getToken(MT22Parser.LESS, 0)

        def GREA(self):
            return self.getToken(MT22Parser.GREA, 0)

        def LOEQ(self):
            return self.getToken(MT22Parser.LOEQ, 0)

        def GOEQ(self):
            return self.getToken(MT22Parser.GOEQ, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_relationalop




    def relationalop(self):

        localctx = MT22Parser.RelationalopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_relationalop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUL) | (1 << MT22Parser.NEQ) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LOEQ) | (1 << MT22Parser.GREA) | (1 << MT22Parser.GOEQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MT22Parser.INT, 0)

        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def dimension(self):
            return self.getTypedRuleContext(MT22Parser.DimensionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimension




    def dimension(self):

        localctx = MT22Parser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dimension)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(MT22Parser.INT)
                self.state = 134
                self.match(MT22Parser.COMA)
                self.state = 135
                self.dimension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(MT22Parser.INT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetricop(self):
            return self.getTypedRuleContext(MT22Parser.ArithmetricopContext,0)


        def booleanop(self):
            return self.getTypedRuleContext(MT22Parser.BooleanopContext,0)


        def stringop(self):
            return self.getTypedRuleContext(MT22Parser.StringopContext,0)


        def relationalop(self):
            return self.getTypedRuleContext(MT22Parser.RelationalopContext,0)


        def indexexpression(self):
            return self.getTypedRuleContext(MT22Parser.IndexexpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_operator




    def operator(self):

        localctx = MT22Parser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operator)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.PLUS, MT22Parser.MINU, MT22Parser.MUTI, MT22Parser.DIVI, MT22Parser.MODU]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.arithmetricop()
                pass
            elif token in [MT22Parser.NOT, MT22Parser.AND, MT22Parser.OR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.booleanop()
                pass
            elif token in [MT22Parser.SCOPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.stringop()
                pass
            elif token in [MT22Parser.EQUL, MT22Parser.NEQ, MT22Parser.LESS, MT22Parser.LOEQ, MT22Parser.GREA, MT22Parser.GOEQ]:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.relationalop()
                pass
            elif token in [MT22Parser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 143
                self.indexexpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(MT22Parser.ConstantContext,0)


        def functioncall(self):
            return self.getTypedRuleContext(MT22Parser.FunctioncallContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def subexpression(self):
            return self.getTypedRuleContext(MT22Parser.SubexpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_operand




    def operand(self):

        localctx = MT22Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operand)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.constant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.functioncall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.match(MT22Parser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.subexpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_subexpression




    def subexpression(self):

        localctx = MT22Parser.SubexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_subexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(MT22Parser.LB)
            self.state = 153
            self.expression()
            self.state = 154
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_relat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expression_relatContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Expression_relatContext,i)


        def stringop(self):
            return self.getTypedRuleContext(MT22Parser.StringopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression




    def expression(self):

        localctx = MT22Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.expression_relat()
                self.state = 157
                self.stringop()
                self.state = 158
                self.expression_relat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.expression_relat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_relatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_logic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expression_logicContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Expression_logicContext,i)


        def relationalop(self):
            return self.getTypedRuleContext(MT22Parser.RelationalopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression_relat




    def expression_relat(self):

        localctx = MT22Parser.Expression_relatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression_relat)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.expression_logic(0)
                self.state = 164
                self.relationalop()
                self.state = 165
                self.expression_logic(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.expression_logic(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_logicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_bina1(self):
            return self.getTypedRuleContext(MT22Parser.Expression_bina1Context,0)


        def expression_logic(self):
            return self.getTypedRuleContext(MT22Parser.Expression_logicContext,0)


        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression_logic



    def expression_logic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expression_logicContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression_logic, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.expression_bina1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expression_logicContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_logic)
                    self.state = 173
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 174
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 175
                    self.expression_bina1(0) 
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_bina1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_bina2(self):
            return self.getTypedRuleContext(MT22Parser.Expression_bina2Context,0)


        def expression_bina1(self):
            return self.getTypedRuleContext(MT22Parser.Expression_bina1Context,0)


        def PLUS(self):
            return self.getToken(MT22Parser.PLUS, 0)

        def MINU(self):
            return self.getToken(MT22Parser.MINU, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression_bina1



    def expression_bina1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expression_bina1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression_bina1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.expression_bina2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expression_bina1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_bina1)
                    self.state = 184
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 185
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.PLUS or _la==MT22Parser.MINU):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 186
                    self.expression_bina2(0) 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_bina2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_unary(self):
            return self.getTypedRuleContext(MT22Parser.Expression_unaryContext,0)


        def expression_bina2(self):
            return self.getTypedRuleContext(MT22Parser.Expression_bina2Context,0)


        def MUTI(self):
            return self.getToken(MT22Parser.MUTI, 0)

        def DIVI(self):
            return self.getToken(MT22Parser.DIVI, 0)

        def MODU(self):
            return self.getToken(MT22Parser.MODU, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression_bina2



    def expression_bina2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expression_bina2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression_bina2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.expression_unary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expression_bina2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_bina2)
                    self.state = 195
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 196
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUTI) | (1 << MT22Parser.DIVI) | (1 << MT22Parser.MODU))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 197
                    self.expression_unary() 
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_unaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def expression_unary(self):
            return self.getTypedRuleContext(MT22Parser.Expression_unaryContext,0)


        def MINU(self):
            return self.getToken(MT22Parser.MINU, 0)

        def indexexpression(self):
            return self.getTypedRuleContext(MT22Parser.IndexexpressionContext,0)


        def operand(self):
            return self.getTypedRuleContext(MT22Parser.OperandContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression_unary




    def expression_unary(self):

        localctx = MT22Parser.Expression_unaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression_unary)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(MT22Parser.NOT)
                self.state = 204
                self.expression_unary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(MT22Parser.MINU)
                self.state = 206
                self.expression_unary()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.indexexpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 208
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(MT22Parser.STR, 0)

        def BOOL(self):
            return self.getToken(MT22Parser.BOOL, 0)

        def FLO(self):
            return self.getToken(MT22Parser.FLO, 0)

        def INT(self):
            return self.getToken(MT22Parser.INT, 0)

        def arr(self):
            return self.getTypedRuleContext(MT22Parser.ArrContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_constant




    def constant(self):

        localctx = MT22Parser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_constant)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.STR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(MT22Parser.STR)
                pass
            elif token in [MT22Parser.BOOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(MT22Parser.BOOL)
                pass
            elif token in [MT22Parser.FLO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.match(MT22Parser.FLO)
                pass
            elif token in [MT22Parser.INT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 214
                self.match(MT22Parser.INT)
                pass
            elif token in [MT22Parser.LCB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 215
                self.arr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def arguementlist(self):
            return self.getTypedRuleContext(MT22Parser.ArguementlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functioncall




    def functioncall(self):

        localctx = MT22Parser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_functioncall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(MT22Parser.ID)
            self.state = 219
            self.match(MT22Parser.LB)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.STR) | (1 << MT22Parser.BOOL) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.ID) | (1 << MT22Parser.LB) | (1 << MT22Parser.LCB) | (1 << MT22Parser.MINU) | (1 << MT22Parser.NOT))) != 0):
                self.state = 220
                self.arguementlist()


            self.state = 223
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def indexop(self):
            return self.getTypedRuleContext(MT22Parser.IndexopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_indexexpression




    def indexexpression(self):

        localctx = MT22Parser.IndexexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_indexexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MT22Parser.ID)
            self.state = 226
            self.indexop()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COL(self):
            return self.getToken(MT22Parser.COL, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_parameter




    def parameter(self):

        localctx = MT22Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 228
                self.match(MT22Parser.INHERIT)


            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 231
                self.match(MT22Parser.OUT)


            self.state = 234
            self.match(MT22Parser.ID)
            self.state = 235
            self.match(MT22Parser.COL)
            self.state = 236
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionlistContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_indexop




    def indexop(self):

        localctx = MT22Parser.IndexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_indexop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MT22Parser.LSB)
            self.state = 239
            self.expressionlist()
            self.state = 240
            self.match(MT22Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArguementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arguement




    def arguement(self):

        localctx = MT22Parser.ArguementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arguement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionmainprotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(MT22Parser.MAIN, 0)

        def COL(self):
            return self.getToken(MT22Parser.COL, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def parameterlist(self):
            return self.getTypedRuleContext(MT22Parser.ParameterlistContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_functionmainprot




    def functionmainprot(self):

        localctx = MT22Parser.FunctionmainprotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_functionmainprot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(MT22Parser.MAIN)
            self.state = 245
            self.match(MT22Parser.COL)
            self.state = 246
            self.match(MT22Parser.FUNCTION)
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.VOID]:
                self.state = 247
                self.match(MT22Parser.VOID)
                pass
            elif token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING, MT22Parser.ARRAY]:
                self.state = 248
                self.vartype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 251
            self.match(MT22Parser.LB)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.OUT) | (1 << MT22Parser.INHERIT) | (1 << MT22Parser.ID))) != 0):
                self.state = 252
                self.parameterlist()


            self.state = 255
            self.match(MT22Parser.RB)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 256
                self.match(MT22Parser.INHERIT)
                self.state = 257
                self.match(MT22Parser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionprotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COL(self):
            return self.getToken(MT22Parser.COL, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def parameterlist(self):
            return self.getTypedRuleContext(MT22Parser.ParameterlistContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_functionprot




    def functionprot(self):

        localctx = MT22Parser.FunctionprotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_functionprot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(MT22Parser.ID)
            self.state = 261
            self.match(MT22Parser.COL)
            self.state = 262
            self.match(MT22Parser.FUNCTION)
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.VOID]:
                self.state = 263
                self.match(MT22Parser.VOID)
                pass
            elif token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING, MT22Parser.ARRAY]:
                self.state = 264
                self.vartype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 267
            self.match(MT22Parser.LB)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.OUT) | (1 << MT22Parser.INHERIT) | (1 << MT22Parser.ID))) != 0):
                self.state = 268
                self.parameterlist()


            self.state = 271
            self.match(MT22Parser.RB)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 272
                self.match(MT22Parser.INHERIT)
                self.state = 273
                self.match(MT22Parser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockstatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockstatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functionbody




    def functionbody(self):

        localctx = MT22Parser.FunctionbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_functionbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.blockstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_scalarvar




    def scalarvar(self):

        localctx = MT22Parser.ScalarvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_scalarvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(MT22Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarvar(self):
            return self.getTypedRuleContext(MT22Parser.ScalarvarContext,0)


        def indexexpression(self):
            return self.getTypedRuleContext(MT22Parser.IndexexpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_lhs




    def lhs(self):

        localctx = MT22Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_lhs)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.scalarvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.indexexpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstatement(self):
            return self.getTypedRuleContext(MT22Parser.AssignstatementContext,0)


        def ifstatement(self):
            return self.getTypedRuleContext(MT22Parser.IfstatementContext,0)


        def forstatement(self):
            return self.getTypedRuleContext(MT22Parser.ForstatementContext,0)


        def whilestatement(self):
            return self.getTypedRuleContext(MT22Parser.WhilestatementContext,0)


        def dowhilestatement(self):
            return self.getTypedRuleContext(MT22Parser.DowhilestatementContext,0)


        def breakstatement(self):
            return self.getTypedRuleContext(MT22Parser.BreakstatementContext,0)


        def continuestatement(self):
            return self.getTypedRuleContext(MT22Parser.ContinuestatementContext,0)


        def returnstatement(self):
            return self.getTypedRuleContext(MT22Parser.ReturnstatementContext,0)


        def callstatement(self):
            return self.getTypedRuleContext(MT22Parser.CallstatementContext,0)


        def blockstatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockstatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_statement)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.assignstatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.ifstatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 286
                self.forstatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 287
                self.whilestatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 288
                self.dowhilestatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 289
                self.breakstatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 290
                self.continuestatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 291
                self.returnstatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 292
                self.callstatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 293
                self.blockstatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def EQU(self):
            return self.getToken(MT22Parser.EQU, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignstatement




    def assignstatement(self):

        localctx = MT22Parser.AssignstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assignstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.lhs()
            self.state = 297
            self.match(MT22Parser.EQU)
            self.state = 298
            self.expression()
            self.state = 299
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_ifstatement




    def ifstatement(self):

        localctx = MT22Parser.IfstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_ifstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(MT22Parser.IF)
            self.state = 302
            self.match(MT22Parser.LB)
            self.state = 303
            self.expression()
            self.state = 304
            self.match(MT22Parser.RB)
            self.state = 305
            self.statement()
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 306
                self.match(MT22Parser.ELSE)
                self.state = 307
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForheadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def EQU(self):
            return self.getToken(MT22Parser.EQU, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMA)
            else:
                return self.getToken(MT22Parser.COMA, i)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_forhead




    def forhead(self):

        localctx = MT22Parser.ForheadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_forhead)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(MT22Parser.FOR)
            self.state = 311
            self.match(MT22Parser.LB)
            self.state = 312
            self.lhs()
            self.state = 313
            self.match(MT22Parser.EQU)
            self.state = 314
            self.expression()
            self.state = 315
            self.match(MT22Parser.COMA)
            self.state = 316
            self.expression()
            self.state = 317
            self.match(MT22Parser.COMA)
            self.state = 318
            self.expression()
            self.state = 319
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forhead(self):
            return self.getTypedRuleContext(MT22Parser.ForheadContext,0)


        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forstatement




    def forstatement(self):

        localctx = MT22Parser.ForstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_forstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.forhead()
            self.state = 322
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileconditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_whilecondition




    def whilecondition(self):

        localctx = MT22Parser.WhileconditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_whilecondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(MT22Parser.WHILE)
            self.state = 325
            self.match(MT22Parser.LB)
            self.state = 326
            self.expression()
            self.state = 327
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def whilecondition(self):
            return self.getTypedRuleContext(MT22Parser.WhileconditionContext,0)


        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_whilestatement




    def whilestatement(self):

        localctx = MT22Parser.WhilestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_whilestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.whilecondition()
            self.state = 330
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DowhilestatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def blockstatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockstatementContext,0)


        def whilecondition(self):
            return self.getTypedRuleContext(MT22Parser.WhileconditionContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dowhilestatement




    def dowhilestatement(self):

        localctx = MT22Parser.DowhilestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_dowhilestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(MT22Parser.DO)
            self.state = 333
            self.blockstatement()
            self.state = 334
            self.whilecondition()
            self.state = 335
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_breakstatement




    def breakstatement(self):

        localctx = MT22Parser.BreakstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_breakstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(MT22Parser.BREAK)
            self.state = 338
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continuestatement




    def continuestatement(self):

        localctx = MT22Parser.ContinuestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_continuestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(MT22Parser.CONTINUE)
            self.state = 341
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returnstatement




    def returnstatement(self):

        localctx = MT22Parser.ReturnstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_returnstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(MT22Parser.RETURN)
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.STR) | (1 << MT22Parser.BOOL) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.ID) | (1 << MT22Parser.LB) | (1 << MT22Parser.LCB) | (1 << MT22Parser.MINU) | (1 << MT22Parser.NOT))) != 0):
                self.state = 344
                self.expression()


            self.state = 347
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def arguementlist(self):
            return self.getTypedRuleContext(MT22Parser.ArguementlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_callstatement




    def callstatement(self):

        localctx = MT22Parser.CallstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_callstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(MT22Parser.ID)
            self.state = 350
            self.match(MT22Parser.LB)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.STR) | (1 << MT22Parser.BOOL) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.ID) | (1 << MT22Parser.LB) | (1 << MT22Parser.LCB) | (1 << MT22Parser.MINU) | (1 << MT22Parser.NOT))) != 0):
                self.state = 351
                self.arguementlist()


            self.state = 354
            self.match(MT22Parser.RB)
            self.state = 355
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def statementlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementlistContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementlistContext,i)


        def variabledecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.VariabledeclContext)
            else:
                return self.getTypedRuleContext(MT22Parser.VariabledeclContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_blockstatement




    def blockstatement(self):

        localctx = MT22Parser.BlockstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_blockstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(MT22Parser.LCB)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 360
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        self.state = 358
                        self.statementlist()
                        pass

                    elif la_ == 2:
                        self.state = 359
                        self.variabledecl()
                        pass

             
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 365
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_idlist




    def idlist(self):

        localctx = MT22Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_idlist)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.match(MT22Parser.ID)
                self.state = 368
                self.match(MT22Parser.COMA)
                self.state = 369
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionlistContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expressionlist




    def expressionlist(self):

        localctx = MT22Parser.ExpressionlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expressionlist)
        self._la = 0 # Token type
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.expression()
                self.state = 374
                self.match(MT22Parser.COMA)
                self.state = 375
                self.expressionlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.expression()
                self.state = 379
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MT22Parser.SEM:
                    self.state = 378
                    self.match(MT22Parser.SEM)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(MT22Parser.ParameterContext,0)


        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(MT22Parser.ParameterlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_parameterlist




    def parameterlist(self):

        localctx = MT22Parser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_parameterlist)
        try:
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.parameter()
                self.state = 384
                self.match(MT22Parser.COMA)
                self.state = 385
                self.parameterlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArguementlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arguement(self):
            return self.getTypedRuleContext(MT22Parser.ArguementContext,0)


        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def arguementlist(self):
            return self.getTypedRuleContext(MT22Parser.ArguementlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arguementlist




    def arguementlist(self):

        localctx = MT22Parser.ArguementlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arguementlist)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.arguement()
                self.state = 391
                self.match(MT22Parser.COMA)
                self.state = 392
                self.arguementlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.arguement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def statementlist(self):
            return self.getTypedRuleContext(MT22Parser.StatementlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statementlist




    def statementlist(self):

        localctx = MT22Parser.StatementlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_statementlist)
        self._la = 0 # Token type
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.statement()
                self.state = 398
                self.match(MT22Parser.SEM)
                self.state = 399
                self.statementlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.statement()
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MT22Parser.SEM:
                    self.state = 402
                    self.match(MT22Parser.SEM)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariabledeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def variabledeclassign(self):
            return self.getTypedRuleContext(MT22Parser.VariabledeclassignContext,0)


        def variabledecls(self):
            return self.getTypedRuleContext(MT22Parser.VariabledeclsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_variabledecl




    def variabledecl(self):

        localctx = MT22Parser.VariabledeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_variabledecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 407
                self.variabledeclassign()
                pass

            elif la_ == 2:
                self.state = 408
                self.variabledecls()
                pass


            self.state = 411
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariabledeclassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMA)
            else:
                return self.getToken(MT22Parser.COMA, i)

        def variabledeclassign(self):
            return self.getTypedRuleContext(MT22Parser.VariabledeclassignContext,0)


        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def COL(self):
            return self.getToken(MT22Parser.COL, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def EQU(self):
            return self.getToken(MT22Parser.EQU, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_variabledeclassign




    def variabledeclassign(self):

        localctx = MT22Parser.VariabledeclassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_variabledeclassign)
        try:
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(MT22Parser.ID)
                self.state = 414
                self.match(MT22Parser.COMA)
                self.state = 415
                self.variabledeclassign()
                self.state = 416
                self.match(MT22Parser.COMA)
                self.state = 417
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.match(MT22Parser.ID)
                self.state = 420
                self.match(MT22Parser.COL)
                self.state = 421
                self.vartype()
                self.state = 422
                self.match(MT22Parser.EQU)
                self.state = 423
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariabledeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COL(self):
            return self.getToken(MT22Parser.COL, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_variabledecls




    def variabledecls(self):

        localctx = MT22Parser.VariabledeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_variabledecls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.idlist()
            self.state = 428
            self.match(MT22Parser.COL)
            self.state = 429
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctiondeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionprot(self):
            return self.getTypedRuleContext(MT22Parser.FunctionprotContext,0)


        def functionbody(self):
            return self.getTypedRuleContext(MT22Parser.FunctionbodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functiondecl




    def functiondecl(self):

        localctx = MT22Parser.FunctiondeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_functiondecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.functionprot()
            self.state = 432
            self.functionbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainfunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionmainprot(self):
            return self.getTypedRuleContext(MT22Parser.FunctionmainprotContext,0)


        def functionbody(self):
            return self.getTypedRuleContext(MT22Parser.FunctionbodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_mainfunction




    def mainfunction(self):

        localctx = MT22Parser.MainfunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_mainfunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.functionmainprot()
            self.state = 435
            self.functionbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def dimension(self):
            return self.getTypedRuleContext(MT22Parser.DimensionContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomictype(self):
            return self.getTypedRuleContext(MT22Parser.AtomictypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arraytype




    def arraytype(self):

        localctx = MT22Parser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_arraytype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(MT22Parser.ARRAY)
            self.state = 444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.LSB:
                self.state = 438
                self.match(MT22Parser.LSB)
                self.state = 439
                self.dimension()
                self.state = 440
                self.match(MT22Parser.RSB)
                self.state = 441
                self.match(MT22Parser.OF)
                self.state = 442
                self.atomictype()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(MT22Parser.DeclsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decls




    def decls(self):

        localctx = MT22Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_decls)
        try:
            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.decl()
                self.state = 447
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functiondecl(self):
            return self.getTypedRuleContext(MT22Parser.FunctiondeclContext,0)


        def variabledecl(self):
            return self.getTypedRuleContext(MT22Parser.VariabledeclContext,0)


        def statementlist(self):
            return self.getTypedRuleContext(MT22Parser.StatementlistContext,0)


        def mainfunction(self):
            return self.getTypedRuleContext(MT22Parser.MainfunctionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_decl)
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.functiondecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.variabledecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
                self.statementlist()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 455
                self.mainfunction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression_logic_sempred
        self._predicates[15] = self.expression_bina1_sempred
        self._predicates[16] = self.expression_bina2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_logic_sempred(self, localctx:Expression_logicContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression_bina1_sempred(self, localctx:Expression_bina1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression_bina2_sempred(self, localctx:Expression_bina2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




