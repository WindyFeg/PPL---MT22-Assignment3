# Generated from f:\Univercity\S2Y3\PRINCIPLES OF PROGRAMMING LANGUAGES\Assignment\assignment3\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01fc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\7\2\u0096")
        buf.write("\n\2\f\2\16\2\u0099\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\7\3\u00a4\n\3\f\3\16\3\u00a7\13\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\5\4\u00af\n\4\3\5\3\5\5\5\u00b3\n\5\3\6\3\6")
        buf.write("\7\6\u00b7\n\6\f\6\16\6\u00ba\13\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\5\34\u0139\n\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\6\37")
        buf.write("\u0147\n\37\r\37\16\37\u0148\3 \3 \5 \u014d\n \3 \6 \u0150")
        buf.write("\n \r \16 \u0151\3!\3!\6!\u0156\n!\r!\16!\u0157\3!\3!")
        buf.write("\3!\5!\u015d\n!\3!\3!\6!\u0161\n!\r!\16!\u0162\3!\5!\u0166")
        buf.write("\n!\3!\3!\3!\3!\3!\3!\5!\u016e\n!\3!\3!\3\"\3\"\6\"\u0174")
        buf.write("\n\"\r\"\16\"\u0175\3\"\3\"\3\"\7\"\u017b\n\"\f\"\16\"")
        buf.write("\u017e\13\"\3#\3#\5#\u0182\n#\3#\3#\3$\3$\3%\5%\u0189")
        buf.write("\n%\3&\3&\5&\u018d\n&\3&\3&\3&\7&\u0192\n&\f&\16&\u0195")
        buf.write("\13&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3")
        buf.write(";\3;\3;\3<\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3@\3@\3@\3A\3")
        buf.write("A\3B\3B\3B\3C\3C\3C\3D\6D\u01d9\nD\rD\16D\u01da\3D\3D")
        buf.write("\3E\3E\3E\3F\3F\3F\5F\u01e5\nF\3G\3G\7G\u01e9\nG\fG\16")
        buf.write("G\u01ec\13G\3G\5G\u01ef\nG\3G\3G\3H\3H\7H\u01f5\nH\fH")
        buf.write("\16H\u01f8\13H\3H\3H\3H\3\u0097\2I\3\3\5\4\7\2\t\2\13")
        buf.write("\5\r\2\17\6\21\7\23\b\25\t\27\n\31\13\33\f\35\r\37\16")
        buf.write("!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67")
        buf.write("\329\33;\34=\2?\2A\35C\2E\36G\2I\2K\37M O!Q\"S#U$W%Y&")
        buf.write("[\'](_)a*c+e\2g,i-k.m/o\60q\61s\62u\63w\64y\65{\66}\67")
        buf.write("\1778\u00819\u0083:\u0085;\u0087<\u0089=\u008b\2\u008d")
        buf.write(">\u008f?\3\2\17\4\2\f\f\17\17\b\2))ddhhppttvv\4\2$$^^")
        buf.write("\7\2\f\f\17\17$$))^^\4\2GGgg\4\2--//\3\2\63;\3\2\62;\4")
        buf.write("\2C\\c|\5\2\13\f\17\17\"\"\n\2$$))^^ddhhppttvv\3\2^^\7")
        buf.write("\3\n\f\16\17$$))^^\2\u020f\2\3\3\2\2\2\2\5\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2A\3\2\2\2\2E\3\2\2\2\2K\3\2\2\2\2")
        buf.write("M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2")
        buf.write("\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2")
        buf.write("\2\2a\3\2\2\2\2c\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\3\u0091\3\2\2\2\5\u009f\3\2\2\2\7\u00aa\3\2\2")
        buf.write("\2\t\u00b2\3\2\2\2\13\u00b4\3\2\2\2\r\u00bf\3\2\2\2\17")
        buf.write("\u00c1\3\2\2\2\21\u00c6\3\2\2\2\23\u00cc\3\2\2\2\25\u00d4")
        buf.write("\3\2\2\2\27\u00d7\3\2\2\2\31\u00dc\3\2\2\2\33\u00e2\3")
        buf.write("\2\2\2\35\u00e6\3\2\2\2\37\u00ef\3\2\2\2!\u00f2\3\2\2")
        buf.write("\2#\u00fa\3\2\2\2%\u0101\3\2\2\2\'\u0108\3\2\2\2)\u010e")
        buf.write("\3\2\2\2+\u0113\3\2\2\2-\u0117\3\2\2\2/\u0120\3\2\2\2")
        buf.write("\61\u0123\3\2\2\2\63\u012b\3\2\2\2\65\u0131\3\2\2\2\67")
        buf.write("\u0138\3\2\2\29\u013a\3\2\2\2;\u0140\3\2\2\2=\u0146\3")
        buf.write("\2\2\2?\u014a\3\2\2\2A\u016d\3\2\2\2C\u0171\3\2\2\2E\u0181")
        buf.write("\3\2\2\2G\u0185\3\2\2\2I\u0188\3\2\2\2K\u018c\3\2\2\2")
        buf.write("M\u0196\3\2\2\2O\u0198\3\2\2\2Q\u019a\3\2\2\2S\u019c\3")
        buf.write("\2\2\2U\u019e\3\2\2\2W\u01a0\3\2\2\2Y\u01a2\3\2\2\2[\u01a4")
        buf.write("\3\2\2\2]\u01a6\3\2\2\2_\u01a8\3\2\2\2a\u01aa\3\2\2\2")
        buf.write("c\u01ac\3\2\2\2e\u01ae\3\2\2\2g\u01b0\3\2\2\2i\u01b2\3")
        buf.write("\2\2\2k\u01b4\3\2\2\2m\u01b6\3\2\2\2o\u01b8\3\2\2\2q\u01ba")
        buf.write("\3\2\2\2s\u01bc\3\2\2\2u\u01be\3\2\2\2w\u01c1\3\2\2\2")
        buf.write("y\u01c4\3\2\2\2{\u01c7\3\2\2\2}\u01ca\3\2\2\2\177\u01cc")
        buf.write("\3\2\2\2\u0081\u01cf\3\2\2\2\u0083\u01d1\3\2\2\2\u0085")
        buf.write("\u01d4\3\2\2\2\u0087\u01d8\3\2\2\2\u0089\u01de\3\2\2\2")
        buf.write("\u008b\u01e4\3\2\2\2\u008d\u01e6\3\2\2\2\u008f\u01f2\3")
        buf.write("\2\2\2\u0091\u0092\7\61\2\2\u0092\u0093\7,\2\2\u0093\u0097")
        buf.write("\3\2\2\2\u0094\u0096\13\2\2\2\u0095\u0094\3\2\2\2\u0096")
        buf.write("\u0099\3\2\2\2\u0097\u0098\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0098\u009a\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009b\7")
        buf.write(",\2\2\u009b\u009c\7\61\2\2\u009c\u009d\3\2\2\2\u009d\u009e")
        buf.write("\b\2\2\2\u009e\4\3\2\2\2\u009f\u00a0\7\61\2\2\u00a0\u00a1")
        buf.write("\7\61\2\2\u00a1\u00a5\3\2\2\2\u00a2\u00a4\n\2\2\2\u00a3")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7\u00a5\3")
        buf.write("\2\2\2\u00a8\u00a9\b\3\2\2\u00a9\6\3\2\2\2\u00aa\u00ae")
        buf.write("\7^\2\2\u00ab\u00af\t\3\2\2\u00ac\u00af\5c\62\2\u00ad")
        buf.write("\u00af\t\4\2\2\u00ae\u00ab\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00ae\u00ad\3\2\2\2\u00af\b\3\2\2\2\u00b0\u00b3\5\7\4")
        buf.write("\2\u00b1\u00b3\n\5\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1")
        buf.write("\3\2\2\2\u00b3\n\3\2\2\2\u00b4\u00b8\5c\62\2\u00b5\u00b7")
        buf.write("\5\t\5\2\u00b6\u00b5\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00bb\3\2\2\2")
        buf.write("\u00ba\u00b8\3\2\2\2\u00bb\u00bc\5c\62\2\u00bc\u00bd\3")
        buf.write("\2\2\2\u00bd\u00be\b\6\3\2\u00be\f\3\2\2\2\u00bf\u00c0")
        buf.write("\5\u0085C\2\u00c0\16\3\2\2\2\u00c1\u00c2\7c\2\2\u00c2")
        buf.write("\u00c3\7w\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5\7q\2\2\u00c5")
        buf.write("\20\3\2\2\2\u00c6\u00c7\7d\2\2\u00c7\u00c8\7t\2\2\u00c8")
        buf.write("\u00c9\7g\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb\7m\2\2\u00cb")
        buf.write("\22\3\2\2\2\u00cc\u00cd\7d\2\2\u00cd\u00ce\7q\2\2\u00ce")
        buf.write("\u00cf\7q\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7g\2\2\u00d1")
        buf.write("\u00d2\7c\2\2\u00d2\u00d3\7p\2\2\u00d3\24\3\2\2\2\u00d4")
        buf.write("\u00d5\7f\2\2\u00d5\u00d6\7q\2\2\u00d6\26\3\2\2\2\u00d7")
        buf.write("\u00d8\7g\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da\7u\2\2\u00da")
        buf.write("\u00db\7g\2\2\u00db\30\3\2\2\2\u00dc\u00dd\7h\2\2\u00dd")
        buf.write("\u00de\7n\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7c\2\2\u00e0")
        buf.write("\u00e1\7v\2\2\u00e1\32\3\2\2\2\u00e2\u00e3\7h\2\2\u00e3")
        buf.write("\u00e4\7q\2\2\u00e4\u00e5\7t\2\2\u00e5\34\3\2\2\2\u00e6")
        buf.write("\u00e7\7h\2\2\u00e7\u00e8\7w\2\2\u00e8\u00e9\7p\2\2\u00e9")
        buf.write("\u00ea\7e\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec\7k\2\2\u00ec")
        buf.write("\u00ed\7q\2\2\u00ed\u00ee\7p\2\2\u00ee\36\3\2\2\2\u00ef")
        buf.write("\u00f0\7k\2\2\u00f0\u00f1\7h\2\2\u00f1 \3\2\2\2\u00f2")
        buf.write("\u00f3\7k\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7v\2\2\u00f5")
        buf.write("\u00f6\7g\2\2\u00f6\u00f7\7i\2\2\u00f7\u00f8\7g\2\2\u00f8")
        buf.write("\u00f9\7t\2\2\u00f9\"\3\2\2\2\u00fa\u00fb\7t\2\2\u00fb")
        buf.write("\u00fc\7g\2\2\u00fc\u00fd\7v\2\2\u00fd\u00fe\7w\2\2\u00fe")
        buf.write("\u00ff\7t\2\2\u00ff\u0100\7p\2\2\u0100$\3\2\2\2\u0101")
        buf.write("\u0102\7u\2\2\u0102\u0103\7v\2\2\u0103\u0104\7t\2\2\u0104")
        buf.write("\u0105\7k\2\2\u0105\u0106\7p\2\2\u0106\u0107\7i\2\2\u0107")
        buf.write("&\3\2\2\2\u0108\u0109\7y\2\2\u0109\u010a\7j\2\2\u010a")
        buf.write("\u010b\7k\2\2\u010b\u010c\7n\2\2\u010c\u010d\7g\2\2\u010d")
        buf.write("(\3\2\2\2\u010e\u010f\7x\2\2\u010f\u0110\7q\2\2\u0110")
        buf.write("\u0111\7k\2\2\u0111\u0112\7f\2\2\u0112*\3\2\2\2\u0113")
        buf.write("\u0114\7q\2\2\u0114\u0115\7w\2\2\u0115\u0116\7v\2\2\u0116")
        buf.write(",\3\2\2\2\u0117\u0118\7e\2\2\u0118\u0119\7q\2\2\u0119")
        buf.write("\u011a\7p\2\2\u011a\u011b\7v\2\2\u011b\u011c\7k\2\2\u011c")
        buf.write("\u011d\7p\2\2\u011d\u011e\7w\2\2\u011e\u011f\7g\2\2\u011f")
        buf.write(".\3\2\2\2\u0120\u0121\7q\2\2\u0121\u0122\7h\2\2\u0122")
        buf.write("\60\3\2\2\2\u0123\u0124\7k\2\2\u0124\u0125\7p\2\2\u0125")
        buf.write("\u0126\7j\2\2\u0126\u0127\7g\2\2\u0127\u0128\7t\2\2\u0128")
        buf.write("\u0129\7k\2\2\u0129\u012a\7v\2\2\u012a\62\3\2\2\2\u012b")
        buf.write("\u012c\7c\2\2\u012c\u012d\7t\2\2\u012d\u012e\7t\2\2\u012e")
        buf.write("\u012f\7c\2\2\u012f\u0130\7{\2\2\u0130\64\3\2\2\2\u0131")
        buf.write("\u0132\7o\2\2\u0132\u0133\7c\2\2\u0133\u0134\7k\2\2\u0134")
        buf.write("\u0135\7p\2\2\u0135\66\3\2\2\2\u0136\u0139\59\35\2\u0137")
        buf.write("\u0139\5;\36\2\u0138\u0136\3\2\2\2\u0138\u0137\3\2\2\2")
        buf.write("\u01398\3\2\2\2\u013a\u013b\7h\2\2\u013b\u013c\7c\2\2")
        buf.write("\u013c\u013d\7n\2\2\u013d\u013e\7u\2\2\u013e\u013f\7g")
        buf.write("\2\2\u013f:\3\2\2\2\u0140\u0141\7v\2\2\u0141\u0142\7t")
        buf.write("\2\2\u0142\u0143\7w\2\2\u0143\u0144\7g\2\2\u0144<\3\2")
        buf.write("\2\2\u0145\u0147\5G$\2\u0146\u0145\3\2\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149")
        buf.write(">\3\2\2\2\u014a\u014c\t\6\2\2\u014b\u014d\t\7\2\2\u014c")
        buf.write("\u014b\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014f\3\2\2\2")
        buf.write("\u014e\u0150\5G$\2\u014f\u014e\3\2\2\2\u0150\u0151\3\2")
        buf.write("\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152@\3")
        buf.write("\2\2\2\u0153\u0156\5C\"\2\u0154\u0156\5e\63\2\u0155\u0153")
        buf.write("\3\2\2\2\u0155\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157")
        buf.write("\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159\u015a\5S*\2\u015a\u015c\5=\37\2\u015b\u015d\5?")
        buf.write(" \2\u015c\u015b\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u016e")
        buf.write("\3\2\2\2\u015e\u0161\5C\"\2\u015f\u0161\5e\63\2\u0160")
        buf.write("\u015e\3\2\2\2\u0160\u015f\3\2\2\2\u0161\u0162\3\2\2\2")
        buf.write("\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0165\3")
        buf.write("\2\2\2\u0164\u0166\5S*\2\u0165\u0164\3\2\2\2\u0165\u0166")
        buf.write("\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\5? \2\u0168\u016e")
        buf.write("\3\2\2\2\u0169\u016a\5S*\2\u016a\u016b\5=\37\2\u016b\u016c")
        buf.write("\5? \2\u016c\u016e\3\2\2\2\u016d\u0155\3\2\2\2\u016d\u0160")
        buf.write("\3\2\2\2\u016d\u0169\3\2\2\2\u016e\u016f\3\2\2\2\u016f")
        buf.write("\u0170\b!\4\2\u0170B\3\2\2\2\u0171\u017c\t\b\2\2\u0172")
        buf.write("\u0174\5g\64\2\u0173\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\3")
        buf.write("\2\2\2\u0177\u0178\5G$\2\u0178\u017b\3\2\2\2\u0179\u017b")
        buf.write("\5G$\2\u017a\u0173\3\2\2\2\u017a\u0179\3\2\2\2\u017b\u017e")
        buf.write("\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write("D\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0182\5C\"\2\u0180")
        buf.write("\u0182\5e\63\2\u0181\u017f\3\2\2\2\u0181\u0180\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183\u0184\b#\5\2\u0184F\3\2\2\2")
        buf.write("\u0185\u0186\t\t\2\2\u0186H\3\2\2\2\u0187\u0189\t\n\2")
        buf.write("\2\u0188\u0187\3\2\2\2\u0189J\3\2\2\2\u018a\u018d\5I%")
        buf.write("\2\u018b\u018d\5g\64\2\u018c\u018a\3\2\2\2\u018c\u018b")
        buf.write("\3\2\2\2\u018d\u0193\3\2\2\2\u018e\u0192\5I%\2\u018f\u0192")
        buf.write("\5g\64\2\u0190\u0192\5G$\2\u0191\u018e\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0191\u0190\3\2\2\2\u0192\u0195\3\2\2\2\u0193")
        buf.write("\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194L\3\2\2\2\u0195")
        buf.write("\u0193\3\2\2\2\u0196\u0197\7.\2\2\u0197N\3\2\2\2\u0198")
        buf.write("\u0199\7<\2\2\u0199P\3\2\2\2\u019a\u019b\7=\2\2\u019b")
        buf.write("R\3\2\2\2\u019c\u019d\7\60\2\2\u019dT\3\2\2\2\u019e\u019f")
        buf.write("\7]\2\2\u019fV\3\2\2\2\u01a0\u01a1\7_\2\2\u01a1X\3\2\2")
        buf.write("\2\u01a2\u01a3\7*\2\2\u01a3Z\3\2\2\2\u01a4\u01a5\7+\2")
        buf.write("\2\u01a5\\\3\2\2\2\u01a6\u01a7\7}\2\2\u01a7^\3\2\2\2\u01a8")
        buf.write("\u01a9\7\177\2\2\u01a9`\3\2\2\2\u01aa\u01ab\7?\2\2\u01ab")
        buf.write("b\3\2\2\2\u01ac\u01ad\7$\2\2\u01add\3\2\2\2\u01ae\u01af")
        buf.write("\7\62\2\2\u01aff\3\2\2\2\u01b0\u01b1\7a\2\2\u01b1h\3\2")
        buf.write("\2\2\u01b2\u01b3\7-\2\2\u01b3j\3\2\2\2\u01b4\u01b5\7/")
        buf.write("\2\2\u01b5l\3\2\2\2\u01b6\u01b7\7,\2\2\u01b7n\3\2\2\2")
        buf.write("\u01b8\u01b9\7\61\2\2\u01b9p\3\2\2\2\u01ba\u01bb\7\'\2")
        buf.write("\2\u01bbr\3\2\2\2\u01bc\u01bd\7#\2\2\u01bdt\3\2\2\2\u01be")
        buf.write("\u01bf\7(\2\2\u01bf\u01c0\7(\2\2\u01c0v\3\2\2\2\u01c1")
        buf.write("\u01c2\7~\2\2\u01c2\u01c3\7~\2\2\u01c3x\3\2\2\2\u01c4")
        buf.write("\u01c5\7?\2\2\u01c5\u01c6\7?\2\2\u01c6z\3\2\2\2\u01c7")
        buf.write("\u01c8\7#\2\2\u01c8\u01c9\7?\2\2\u01c9|\3\2\2\2\u01ca")
        buf.write("\u01cb\7>\2\2\u01cb~\3\2\2\2\u01cc\u01cd\7>\2\2\u01cd")
        buf.write("\u01ce\7?\2\2\u01ce\u0080\3\2\2\2\u01cf\u01d0\7@\2\2\u01d0")
        buf.write("\u0082\3\2\2\2\u01d1\u01d2\7@\2\2\u01d2\u01d3\7?\2\2\u01d3")
        buf.write("\u0084\3\2\2\2\u01d4\u01d5\7<\2\2\u01d5\u01d6\7<\2\2\u01d6")
        buf.write("\u0086\3\2\2\2\u01d7\u01d9\t\13\2\2\u01d8\u01d7\3\2\2")
        buf.write("\2\u01d9\u01da\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01db")
        buf.write("\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01dd\bD\2\2\u01dd")
        buf.write("\u0088\3\2\2\2\u01de\u01df\13\2\2\2\u01df\u01e0\bE\6\2")
        buf.write("\u01e0\u008a\3\2\2\2\u01e1\u01e2\7^\2\2\u01e2\u01e5\n")
        buf.write("\f\2\2\u01e3\u01e5\n\r\2\2\u01e4\u01e1\3\2\2\2\u01e4\u01e3")
        buf.write("\3\2\2\2\u01e5\u008c\3\2\2\2\u01e6\u01ea\5c\62\2\u01e7")
        buf.write("\u01e9\5\t\5\2\u01e8\u01e7\3\2\2\2\u01e9\u01ec\3\2\2\2")
        buf.write("\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ee\3")
        buf.write("\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01ef\t\16\2\2\u01ee")
        buf.write("\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1\bG\7\2")
        buf.write("\u01f1\u008e\3\2\2\2\u01f2\u01f6\5c\62\2\u01f3\u01f5\5")
        buf.write("\t\5\2\u01f4\u01f3\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6\u01f4")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f9\3\2\2\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f9\u01fa\5\u008bF\2\u01fa\u01fb\bH\b")
        buf.write("\2\u01fb\u0090\3\2\2\2 \2\u0097\u00a5\u00ae\u00b2\u00b8")
        buf.write("\u0138\u0148\u014c\u0151\u0155\u0157\u015c\u0160\u0162")
        buf.write("\u0165\u016d\u0175\u017a\u017c\u0181\u0188\u018c\u0191")
        buf.write("\u0193\u01da\u01e4\u01ea\u01ee\u01f6\t\b\2\2\3\6\2\3!")
        buf.write("\3\3#\4\3E\5\3G\6\3H\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_C = 1
    COMMENT_CPP = 2
    STR = 3
    AUTO = 4
    BREAK = 5
    BOOLEAN = 6
    DO = 7
    ELSE = 8
    FLOAT = 9
    FOR = 10
    FUNCTION = 11
    IF = 12
    INTEGER = 13
    RETURN = 14
    STRING = 15
    WHILE = 16
    VOID = 17
    OUT = 18
    CONTINUE = 19
    OF = 20
    INHERIT = 21
    ARRAY = 22
    MAIN = 23
    BOOL = 24
    FALSE = 25
    TRUE = 26
    FLO = 27
    INT = 28
    ID = 29
    COMA = 30
    COL = 31
    SEM = 32
    DOT = 33
    LSB = 34
    RSB = 35
    LB = 36
    RB = 37
    LCB = 38
    RCB = 39
    EQU = 40
    DB = 41
    UNDE = 42
    PLUS = 43
    MINU = 44
    MUTI = 45
    DIVI = 46
    MODU = 47
    NOT = 48
    AND = 49
    OR = 50
    EQUL = 51
    NEQ = 52
    LESS = 53
    LOEQ = 54
    GREA = 55
    GOEQ = 56
    SCOPE = 57
    WS = 58
    ERROR_CHAR = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'float'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'main'", "'false'", "'true'", "','", "':'", "';'", 
            "'.'", "'['", "']'", "'('", "')'", "'{'", "'}'", "'='", "'\"'", 
            "'_'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_C", "COMMENT_CPP", "STR", "AUTO", "BREAK", "BOOLEAN", 
            "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
            "STRING", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
            "ARRAY", "MAIN", "BOOL", "FALSE", "TRUE", "FLO", "INT", "ID", 
            "COMA", "COL", "SEM", "DOT", "LSB", "RSB", "LB", "RB", "LCB", 
            "RCB", "EQU", "DB", "UNDE", "PLUS", "MINU", "MUTI", "DIVI", 
            "MODU", "NOT", "AND", "OR", "EQUL", "NEQ", "LESS", "LOEQ", "GREA", 
            "GOEQ", "SCOPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT_C", "COMMENT_CPP", "ESCAPE", "STR_CHAR", "STR", 
                  "STRTYP", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                  "MAIN", "BOOL", "FALSE", "TRUE", "DECIMAL", "EXPONENT", 
                  "FLO", "POSINT", "INT", "DIGIT", "LETTER", "ID", "COMA", 
                  "COL", "SEM", "DOT", "LSB", "RSB", "LB", "RB", "LCB", 
                  "RCB", "EQU", "DB", "ZERO", "UNDE", "PLUS", "MINU", "MUTI", 
                  "DIVI", "MODU", "NOT", "AND", "OR", "EQUL", "NEQ", "LESS", 
                  "LOEQ", "GREA", "GOEQ", "SCOPE", "WS", "ERROR_CHAR", "ESCAPE_ILLEGAL", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[4] = self.STR_action 
            actions[31] = self.FLO_action 
            actions[33] = self.INT_action 
            actions[67] = self.ERROR_CHAR_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def FLO_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace('_','')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise IllegalEscape(self.text[1:])
     


