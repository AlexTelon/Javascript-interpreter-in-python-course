# Generated from java-escape by ANTLR 4.4
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .ECMAScriptListener import ECMAScriptListener
    from .ECMAScriptVisitor import ECMAScriptVisitor
else:
    from ECMAScriptListener import ECMAScriptListener
    from ECMAScriptVisitor import ECMAScriptVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3k")
        buf.write("\u025a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\5\2f\n\2\3\2\3")
        buf.write("\2\3\3\6\3k\n\3\r\3\16\3l\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4~\n\4\3\5\3\5\5\5")
        buf.write("\u0082\n\5\3\5\3\5\3\6\6\6\u0087\n\6\r\6\16\6\u0088\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\7\b\u0092\n\b\f\b\16\b\u0095")
        buf.write("\13\b\3\t\3\t\5\t\u0099\n\t\3\n\3\n\3\n\3\13\3\13\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00a9\n\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\5\16\u00bc\n\16\3\16\3\16\5")
        buf.write("\16\u00c0\n\16\3\16\3\16\5\16\u00c4\n\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\5\16\u00ce\n\16\3\16\3\16\5")
        buf.write("\16\u00d2\n\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00e8\n\16\3\17\3\17\5\17\u00ec\n\17\3\17\3")
        buf.write("\17\3\20\3\20\5\20\u00f2\n\20\3\20\3\20\3\21\3\21\5\21")
        buf.write("\u00f8\n\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\6\24\u010b")
        buf.write("\n\24\r\24\16\24\u010c\3\24\3\24\3\25\3\25\3\25\3\25\5")
        buf.write("\25\u0115\n\25\3\26\3\26\3\26\5\26\u011a\n\26\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0131\n")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\7\35\u0142\n\35\f\35\16\35\u0145")
        buf.write("\13\35\3\36\5\36\u0148\n\36\3\37\3\37\5\37\u014c\n\37")
        buf.write("\3\37\5\37\u014f\n\37\3\37\5\37\u0152\n\37\3\37\3\37\3")
        buf.write(" \5 \u0157\n \3 \3 \3 \5 \u015c\n \3 \7 \u015f\n \f \16")
        buf.write(" \u0162\13 \3!\6!\u0165\n!\r!\16!\u0166\3\"\3\"\3\"\3")
        buf.write("\"\7\"\u016d\n\"\f\"\16\"\u0170\13\"\5\"\u0172\n\"\3\"")
        buf.write("\5\"\u0175\n\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0194")
        buf.write("\n#\3$\3$\3$\5$\u0199\n$\3%\3%\5%\u019d\n%\3%\3%\3&\3")
        buf.write("&\3&\7&\u01a4\n&\f&\16&\u01a7\13&\3\'\3\'\3\'\7\'\u01ac")
        buf.write("\n\'\f\'\16\'\u01af\13\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\5(\u01c2\n(\3(\3(\5(\u01c6\n(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\5(\u01ef\n(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\7(\u0236\n(\f(\16(\u0239\13(\3)\3)\3*\3*\3")
        buf.write("+\3+\5+\u0241\n+\3,\3,\3-\3-\5-\u0247\n-\3.\3.\3.\5.\u024c")
        buf.write("\n.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\5\61\u0256\n\61")
        buf.write("\3\62\3\62\3\62\2\3N\63\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("\2\20\3\2\27\31\3\2\23\24\3\2\32\34\3\2\35 \3\2!$\3\2")
        buf.write("%\'\3\2()\3\2\21\22\4\2\r\r*\64\5\2\3\3\678gg\3\29;\3")
        buf.write("\2\678\3\2<U\3\2Ve\u0292\2e\3\2\2\2\4j\3\2\2\2\6}\3\2")
        buf.write("\2\2\b\177\3\2\2\2\n\u0086\3\2\2\2\f\u008a\3\2\2\2\16")
        buf.write("\u008e\3\2\2\2\20\u0096\3\2\2\2\22\u009a\3\2\2\2\24\u009d")
        buf.write("\3\2\2\2\26\u009f\3\2\2\2\30\u00a1\3\2\2\2\32\u00e7\3")
        buf.write("\2\2\2\34\u00e9\3\2\2\2\36\u00ef\3\2\2\2 \u00f5\3\2\2")
        buf.write("\2\"\u00fb\3\2\2\2$\u0101\3\2\2\2&\u0107\3\2\2\2(\u0110")
        buf.write("\3\2\2\2*\u0116\3\2\2\2,\u011b\3\2\2\2.\u011f\3\2\2\2")
        buf.write("\60\u0130\3\2\2\2\62\u0132\3\2\2\2\64\u0138\3\2\2\2\66")
        buf.write("\u013b\3\2\2\28\u013e\3\2\2\2:\u0147\3\2\2\2<\u0149\3")
        buf.write("\2\2\2>\u0156\3\2\2\2@\u0164\3\2\2\2B\u0168\3\2\2\2D\u0193")
        buf.write("\3\2\2\2F\u0198\3\2\2\2H\u019a\3\2\2\2J\u01a0\3\2\2\2")
        buf.write("L\u01a8\3\2\2\2N\u01ee\3\2\2\2P\u023a\3\2\2\2R\u023c\3")
        buf.write("\2\2\2T\u0240\3\2\2\2V\u0242\3\2\2\2X\u0246\3\2\2\2Z\u024b")
        buf.write("\3\2\2\2\\\u024d\3\2\2\2^\u024f\3\2\2\2`\u0255\3\2\2\2")
        buf.write("b\u0257\3\2\2\2df\5\4\3\2ed\3\2\2\2ef\3\2\2\2fg\3\2\2")
        buf.write("\2gh\7\2\2\3h\3\3\2\2\2ik\5\6\4\2ji\3\2\2\2kl\3\2\2\2")
        buf.write("lj\3\2\2\2lm\3\2\2\2m\5\3\2\2\2n~\5\b\5\2o~\5\f\7\2p~")
        buf.write("\5\24\13\2q~\5\26\f\2r~\5\30\r\2s~\5\32\16\2t~\5\34\17")
        buf.write("\2u~\5\36\20\2v~\5 \21\2w~\5\"\22\2x~\5,\27\2y~\5$\23")
        buf.write("\2z~\5.\30\2{~\5\60\31\2|~\5\66\34\2}n\3\2\2\2}o\3\2\2")
        buf.write("\2}p\3\2\2\2}q\3\2\2\2}r\3\2\2\2}s\3\2\2\2}t\3\2\2\2}")
        buf.write("u\3\2\2\2}v\3\2\2\2}w\3\2\2\2}x\3\2\2\2}y\3\2\2\2}z\3")
        buf.write("\2\2\2}{\3\2\2\2}|\3\2\2\2~\7\3\2\2\2\177\u0081\7\t\2")
        buf.write("\2\u0080\u0082\5\n\6\2\u0081\u0080\3\2\2\2\u0081\u0082")
        buf.write("\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084\7\n\2\2\u0084")
        buf.write("\t\3\2\2\2\u0085\u0087\5\6\4\2\u0086\u0085\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\13\3\2\2\2\u008a\u008b\7C\2\2\u008b\u008c\5\16")
        buf.write("\b\2\u008c\u008d\5`\61\2\u008d\r\3\2\2\2\u008e\u0093\5")
        buf.write("\20\t\2\u008f\u0090\7\f\2\2\u0090\u0092\5\20\t\2\u0091")
        buf.write("\u008f\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2")
        buf.write("\u0093\u0094\3\2\2\2\u0094\17\3\2\2\2\u0095\u0093\3\2")
        buf.write("\2\2\u0096\u0098\7f\2\2\u0097\u0099\5\22\n\2\u0098\u0097")
        buf.write("\3\2\2\2\u0098\u0099\3\2\2\2\u0099\21\3\2\2\2\u009a\u009b")
        buf.write("\7\r\2\2\u009b\u009c\5N(\2\u009c\23\3\2\2\2\u009d\u009e")
        buf.write("\7\13\2\2\u009e\25\3\2\2\2\u009f\u00a0\5L\'\2\u00a0\27")
        buf.write("\3\2\2\2\u00a1\u00a2\7Q\2\2\u00a2\u00a3\7\7\2\2\u00a3")
        buf.write("\u00a4\5L\'\2\u00a4\u00a5\7\b\2\2\u00a5\u00a8\5\6\4\2")
        buf.write("\u00a6\u00a7\7A\2\2\u00a7\u00a9\5\6\4\2\u00a8\u00a6\3")
        buf.write("\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\31\3\2\2\2\u00aa\u00ab")
        buf.write("\7=\2\2\u00ab\u00ac\5\6\4\2\u00ac\u00ad\7K\2\2\u00ad\u00ae")
        buf.write("\7\7\2\2\u00ae\u00af\5L\'\2\u00af\u00b0\7\b\2\2\u00b0")
        buf.write("\u00b1\5`\61\2\u00b1\u00e8\3\2\2\2\u00b2\u00b3\7K\2\2")
        buf.write("\u00b3\u00b4\7\7\2\2\u00b4\u00b5\5L\'\2\u00b5\u00b6\7")
        buf.write("\b\2\2\u00b6\u00b7\5\6\4\2\u00b7\u00e8\3\2\2\2\u00b8\u00b9")
        buf.write("\7I\2\2\u00b9\u00bb\7\7\2\2\u00ba\u00bc\5L\'\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00bf\7\13\2\2\u00be\u00c0\5L\'\2\u00bf\u00be\3\2\2\2")
        buf.write("\u00bf\u00c0\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\7")
        buf.write("\13\2\2\u00c2\u00c4\5L\'\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\7\b\2\2\u00c6")
        buf.write("\u00e8\5\6\4\2\u00c7\u00c8\7I\2\2\u00c8\u00c9\7\7\2\2")
        buf.write("\u00c9\u00ca\7C\2\2\u00ca\u00cb\5\16\b\2\u00cb\u00cd\7")
        buf.write("\13\2\2\u00cc\u00ce\5L\'\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce")
        buf.write("\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1\7\13\2\2\u00d0")
        buf.write("\u00d2\5L\'\2\u00d1\u00d0\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2\u00d3\3\2\2\2\u00d3\u00d4\7\b\2\2\u00d4\u00d5\5")
        buf.write("\6\4\2\u00d5\u00e8\3\2\2\2\u00d6\u00d7\7I\2\2\u00d7\u00d8")
        buf.write("\7\7\2\2\u00d8\u00d9\5N(\2\u00d9\u00da\7T\2\2\u00da\u00db")
        buf.write("\5L\'\2\u00db\u00dc\7\b\2\2\u00dc\u00dd\5\6\4\2\u00dd")
        buf.write("\u00e8\3\2\2\2\u00de\u00df\7I\2\2\u00df\u00e0\7\7\2\2")
        buf.write("\u00e0\u00e1\7C\2\2\u00e1\u00e2\5\20\t\2\u00e2\u00e3\7")
        buf.write("T\2\2\u00e3\u00e4\5L\'\2\u00e4\u00e5\7\b\2\2\u00e5\u00e6")
        buf.write("\5\6\4\2\u00e6\u00e8\3\2\2\2\u00e7\u00aa\3\2\2\2\u00e7")
        buf.write("\u00b2\3\2\2\2\u00e7\u00b8\3\2\2\2\u00e7\u00c7\3\2\2\2")
        buf.write("\u00e7\u00d6\3\2\2\2\u00e7\u00de\3\2\2\2\u00e8\33\3\2")
        buf.write("\2\2\u00e9\u00eb\7H\2\2\u00ea\u00ec\7f\2\2\u00eb\u00ea")
        buf.write("\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed")
        buf.write("\u00ee\5`\61\2\u00ee\35\3\2\2\2\u00ef\u00f1\7<\2\2\u00f0")
        buf.write("\u00f2\7f\2\2\u00f1\u00f0\3\2\2\2\u00f1\u00f2\3\2\2\2")
        buf.write("\u00f2\u00f3\3\2\2\2\u00f3\u00f4\5`\61\2\u00f4\37\3\2")
        buf.write("\2\2\u00f5\u00f7\7F\2\2\u00f6\u00f8\5L\'\2\u00f7\u00f6")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9")
        buf.write("\u00fa\5`\61\2\u00fa!\3\2\2\2\u00fb\u00fc\7O\2\2\u00fc")
        buf.write("\u00fd\7\7\2\2\u00fd\u00fe\5L\'\2\u00fe\u00ff\7\b\2\2")
        buf.write("\u00ff\u0100\5\6\4\2\u0100#\3\2\2\2\u0101\u0102\7J\2\2")
        buf.write("\u0102\u0103\7\7\2\2\u0103\u0104\5L\'\2\u0104\u0105\7")
        buf.write("\b\2\2\u0105\u0106\5&\24\2\u0106%\3\2\2\2\u0107\u010a")
        buf.write("\7\t\2\2\u0108\u010b\5(\25\2\u0109\u010b\5*\26\2\u010a")
        buf.write("\u0108\3\2\2\2\u010a\u0109\3\2\2\2\u010b\u010c\3\2\2\2")
        buf.write("\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010e\3")
        buf.write("\2\2\2\u010e\u010f\7\n\2\2\u010f\'\3\2\2\2\u0110\u0111")
        buf.write("\7@\2\2\u0111\u0112\5L\'\2\u0112\u0114\7\17\2\2\u0113")
        buf.write("\u0115\5\n\6\2\u0114\u0113\3\2\2\2\u0114\u0115\3\2\2\2")
        buf.write("\u0115)\3\2\2\2\u0116\u0117\7P\2\2\u0117\u0119\7\17\2")
        buf.write("\2\u0118\u011a\5\n\6\2\u0119\u0118\3\2\2\2\u0119\u011a")
        buf.write("\3\2\2\2\u011a+\3\2\2\2\u011b\u011c\7f\2\2\u011c\u011d")
        buf.write("\7\17\2\2\u011d\u011e\5\6\4\2\u011e-\3\2\2\2\u011f\u0120")
        buf.write("\7R\2\2\u0120\u0121\5L\'\2\u0121\u0122\5`\61\2\u0122/")
        buf.write("\3\2\2\2\u0123\u0124\7U\2\2\u0124\u0125\5\b\5\2\u0125")
        buf.write("\u0126\5\62\32\2\u0126\u0131\3\2\2\2\u0127\u0128\7U\2")
        buf.write("\2\u0128\u0129\5\b\5\2\u0129\u012a\5\64\33\2\u012a\u0131")
        buf.write("\3\2\2\2\u012b\u012c\7U\2\2\u012c\u012d\5\b\5\2\u012d")
        buf.write("\u012e\5\62\32\2\u012e\u012f\5\64\33\2\u012f\u0131\3\2")
        buf.write("\2\2\u0130\u0123\3\2\2\2\u0130\u0127\3\2\2\2\u0130\u012b")
        buf.write("\3\2\2\2\u0131\61\3\2\2\2\u0132\u0133\7D\2\2\u0133\u0134")
        buf.write("\7\7\2\2\u0134\u0135\7f\2\2\u0135\u0136\7\b\2\2\u0136")
        buf.write("\u0137\5\b\5\2\u0137\63\3\2\2\2\u0138\u0139\7E\2\2\u0139")
        buf.write("\u013a\5\b\5\2\u013a\65\3\2\2\2\u013b\u013c\7L\2\2\u013c")
        buf.write("\u013d\5`\61\2\u013d\67\3\2\2\2\u013e\u0143\7f\2\2\u013f")
        buf.write("\u0140\7\f\2\2\u0140\u0142\7f\2\2\u0141\u013f\3\2\2\2")
        buf.write("\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3")
        buf.write("\2\2\2\u01449\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0148")
        buf.write("\5\4\3\2\u0147\u0146\3\2\2\2\u0147\u0148\3\2\2\2\u0148")
        buf.write(";\3\2\2\2\u0149\u014b\7\5\2\2\u014a\u014c\5> \2\u014b")
        buf.write("\u014a\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014e\3\2\2\2")
        buf.write("\u014d\u014f\7\f\2\2\u014e\u014d\3\2\2\2\u014e\u014f\3")
        buf.write("\2\2\2\u014f\u0151\3\2\2\2\u0150\u0152\5@!\2\u0151\u0150")
        buf.write("\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0153\3\2\2\2\u0153")
        buf.write("\u0154\7\6\2\2\u0154=\3\2\2\2\u0155\u0157\5@!\2\u0156")
        buf.write("\u0155\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158\u0160\5N(\2\u0159\u015b\7\f\2\2\u015a\u015c\5@")
        buf.write("!\2\u015b\u015a\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d")
        buf.write("\3\2\2\2\u015d\u015f\5N(\2\u015e\u0159\3\2\2\2\u015f\u0162")
        buf.write("\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161")
        buf.write("?\3\2\2\2\u0162\u0160\3\2\2\2\u0163\u0165\7\f\2\2\u0164")
        buf.write("\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0164\3\2\2\2")
        buf.write("\u0166\u0167\3\2\2\2\u0167A\3\2\2\2\u0168\u0171\7\t\2")
        buf.write("\2\u0169\u016e\5D#\2\u016a\u016b\7\f\2\2\u016b\u016d\5")
        buf.write("D#\2\u016c\u016a\3\2\2\2\u016d\u0170\3\2\2\2\u016e\u016c")
        buf.write("\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0172\3\2\2\2\u0170")
        buf.write("\u016e\3\2\2\2\u0171\u0169\3\2\2\2\u0171\u0172\3\2\2\2")
        buf.write("\u0172\u0174\3\2\2\2\u0173\u0175\7\f\2\2\u0174\u0173\3")
        buf.write("\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177")
        buf.write("\7\n\2\2\u0177C\3\2\2\2\u0178\u0179\5F$\2\u0179\u017a")
        buf.write("\7\17\2\2\u017a\u017b\5N(\2\u017b\u0194\3\2\2\2\u017c")
        buf.write("\u017d\7\65\2\2\u017d\u017e\7\17\2\2\u017e\u0194\5N(\2")
        buf.write("\u017f\u0180\7\65\2\2\u0180\u0181\7f\2\2\u0181\u0182\7")
        buf.write("\7\2\2\u0182\u0183\7\b\2\2\u0183\u0184\7\t\2\2\u0184\u0185")
        buf.write("\5:\36\2\u0185\u0186\7\n\2\2\u0186\u0194\3\2\2\2\u0187")
        buf.write("\u0188\7\66\2\2\u0188\u0189\7\17\2\2\u0189\u0194\5N(\2")
        buf.write("\u018a\u018b\7\66\2\2\u018b\u018c\7f\2\2\u018c\u018d\7")
        buf.write("\7\2\2\u018d\u018e\7f\2\2\u018e\u018f\7\b\2\2\u018f\u0190")
        buf.write("\7\t\2\2\u0190\u0191\5:\36\2\u0191\u0192\7\n\2\2\u0192")
        buf.write("\u0194\3\2\2\2\u0193\u0178\3\2\2\2\u0193\u017c\3\2\2\2")
        buf.write("\u0193\u017f\3\2\2\2\u0193\u0187\3\2\2\2\u0193\u018a\3")
        buf.write("\2\2\2\u0194E\3\2\2\2\u0195\u0199\5X-\2\u0196\u0199\7")
        buf.write("g\2\2\u0197\u0199\5V,\2\u0198\u0195\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0197\3\2\2\2\u0199G\3\2\2\2\u019a\u019c")
        buf.write("\7\7\2\2\u019b\u019d\5J&\2\u019c\u019b\3\2\2\2\u019c\u019d")
        buf.write("\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019f\7\b\2\2\u019f")
        buf.write("I\3\2\2\2\u01a0\u01a5\5N(\2\u01a1\u01a2\7\f\2\2\u01a2")
        buf.write("\u01a4\5N(\2\u01a3\u01a1\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6K\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a8\u01ad\5N(\2\u01a9\u01aa\7\f\2\2\u01aa")
        buf.write("\u01ac\5N(\2\u01ab\u01a9\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad")
        buf.write("\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01aeM\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01b0\u01b1\b(\1\2\u01b1\u01b2\7S\2\2\u01b2")
        buf.write("\u01ef\5N(\37\u01b3\u01b4\7G\2\2\u01b4\u01ef\5N(\36\u01b5")
        buf.write("\u01b6\7?\2\2\u01b6\u01ef\5N(\35\u01b7\u01b8\7\23\2\2")
        buf.write("\u01b8\u01ef\5N(\31\u01b9\u01ba\7\24\2\2\u01ba\u01ef\5")
        buf.write("N(\30\u01bb\u01bc\7\25\2\2\u01bc\u01ef\5N(\27\u01bd\u01be")
        buf.write("\7\26\2\2\u01be\u01ef\5N(\26\u01bf\u01c1\7M\2\2\u01c0")
        buf.write("\u01c2\7f\2\2\u01c1\u01c0\3\2\2\2\u01c1\u01c2\3\2\2\2")
        buf.write("\u01c2\u01c3\3\2\2\2\u01c3\u01c5\7\7\2\2\u01c4\u01c6\5")
        buf.write("8\35\2\u01c5\u01c4\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7")
        buf.write("\3\2\2\2\u01c7\u01c8\7\b\2\2\u01c8\u01c9\7\t\2\2\u01c9")
        buf.write("\u01ca\5:\36\2\u01ca\u01cb\7\n\2\2\u01cb\u01ef\3\2\2\2")
        buf.write("\u01cc\u01cd\7B\2\2\u01cd\u01ce\5N(\2\u01ce\u01cf\5H%")
        buf.write("\2\u01cf\u01ef\3\2\2\2\u01d0\u01d1\7f\2\2\u01d1\u01d2")
        buf.write("\6(\2\2\u01d2\u01ef\5P)\2\u01d3\u01d4\5P)\2\u01d4\u01d5")
        buf.write("\7f\2\2\u01d5\u01ef\3\2\2\2\u01d6\u01d7\5P)\2\u01d7\u01d8")
        buf.write("\5N(\2\u01d8\u01d9\7\20\2\2\u01d9\u01da\5X-\2\u01da\u01ef")
        buf.write("\3\2\2\2\u01db\u01dc\5P)\2\u01dc\u01dd\5N(\2\u01dd\u01de")
        buf.write("\7\5\2\2\u01de\u01df\5L\'\2\u01df\u01e0\7\6\2\2\u01e0")
        buf.write("\u01ef\3\2\2\2\u01e1\u01e2\7f\2\2\u01e2\u01e3\5R*\2\u01e3")
        buf.write("\u01e4\5L\'\2\u01e4\u01ef\3\2\2\2\u01e5\u01ef\7N\2\2\u01e6")
        buf.write("\u01ef\7f\2\2\u01e7\u01ef\5T+\2\u01e8\u01ef\5<\37\2\u01e9")
        buf.write("\u01ef\5B\"\2\u01ea\u01eb\7\7\2\2\u01eb\u01ec\5L\'\2\u01ec")
        buf.write("\u01ed\7\b\2\2\u01ed\u01ef\3\2\2\2\u01ee\u01b0\3\2\2\2")
        buf.write("\u01ee\u01b3\3\2\2\2\u01ee\u01b5\3\2\2\2\u01ee\u01b7\3")
        buf.write("\2\2\2\u01ee\u01b9\3\2\2\2\u01ee\u01bb\3\2\2\2\u01ee\u01bd")
        buf.write("\3\2\2\2\u01ee\u01bf\3\2\2\2\u01ee\u01cc\3\2\2\2\u01ee")
        buf.write("\u01d0\3\2\2\2\u01ee\u01d3\3\2\2\2\u01ee\u01d6\3\2\2\2")
        buf.write("\u01ee\u01db\3\2\2\2\u01ee\u01e1\3\2\2\2\u01ee\u01e5\3")
        buf.write("\2\2\2\u01ee\u01e6\3\2\2\2\u01ee\u01e7\3\2\2\2\u01ee\u01e8")
        buf.write("\3\2\2\2\u01ee\u01e9\3\2\2\2\u01ee\u01ea\3\2\2\2\u01ef")
        buf.write("\u0237\3\2\2\2\u01f0\u01f1\f\25\2\2\u01f1\u01f2\t\2\2")
        buf.write("\2\u01f2\u0236\5N(\26\u01f3\u01f4\f\24\2\2\u01f4\u01f5")
        buf.write("\t\3\2\2\u01f5\u0236\5N(\25\u01f6\u01f7\f\23\2\2\u01f7")
        buf.write("\u01f8\t\4\2\2\u01f8\u0236\5N(\24\u01f9\u01fa\f\22\2\2")
        buf.write("\u01fa\u01fb\t\5\2\2\u01fb\u0236\5N(\23\u01fc\u01fd\f")
        buf.write("\21\2\2\u01fd\u01fe\7>\2\2\u01fe\u0236\5N(\22\u01ff\u0200")
        buf.write("\f\20\2\2\u0200\u0201\7T\2\2\u0201\u0236\5N(\21\u0202")
        buf.write("\u0203\f\17\2\2\u0203\u0204\t\6\2\2\u0204\u0236\5N(\20")
        buf.write("\u0205\u0206\f\16\2\2\u0206\u0207\t\7\2\2\u0207\u0236")
        buf.write("\5N(\17\u0208\u0209\f\r\2\2\u0209\u020a\t\b\2\2\u020a")
        buf.write("\u0236\5N(\16\u020b\u020c\f\f\2\2\u020c\u020d\7\16\2\2")
        buf.write("\u020d\u020e\5N(\2\u020e\u020f\7\17\2\2\u020f\u0210\5")
        buf.write("N(\r\u0210\u0236\3\2\2\2\u0211\u0212\f&\2\2\u0212\u0213")
        buf.write("\7\5\2\2\u0213\u0214\5L\'\2\u0214\u0215\7\6\2\2\u0215")
        buf.write("\u0236\3\2\2\2\u0216\u0217\f%\2\2\u0217\u0218\7\20\2\2")
        buf.write("\u0218\u0236\5X-\2\u0219\u021a\f$\2\2\u021a\u0236\5H%")
        buf.write("\2\u021b\u021c\f!\2\2\u021c\u021d\7\20\2\2\u021d\u021e")
        buf.write("\5X-\2\u021e\u021f\6(\21\2\u021f\u0220\5P)\2\u0220\u0236")
        buf.write("\3\2\2\2\u0221\u0222\f \2\2\u0222\u0223\7\5\2\2\u0223")
        buf.write("\u0224\5L\'\2\u0224\u0225\7\6\2\2\u0225\u0226\6(\23\2")
        buf.write("\u0226\u0227\5P)\2\u0227\u0236\3\2\2\2\u0228\u0229\f\n")
        buf.write("\2\2\u0229\u022a\7\20\2\2\u022a\u022b\5X-\2\u022b\u022c")
        buf.write("\5R*\2\u022c\u022d\5L\'\2\u022d\u0236\3\2\2\2\u022e\u022f")
        buf.write("\f\t\2\2\u022f\u0230\7\5\2\2\u0230\u0231\5L\'\2\u0231")
        buf.write("\u0232\7\6\2\2\u0232\u0233\5R*\2\u0233\u0234\5L\'\2\u0234")
        buf.write("\u0236\3\2\2\2\u0235\u01f0\3\2\2\2\u0235\u01f3\3\2\2\2")
        buf.write("\u0235\u01f6\3\2\2\2\u0235\u01f9\3\2\2\2\u0235\u01fc\3")
        buf.write("\2\2\2\u0235\u01ff\3\2\2\2\u0235\u0202\3\2\2\2\u0235\u0205")
        buf.write("\3\2\2\2\u0235\u0208\3\2\2\2\u0235\u020b\3\2\2\2\u0235")
        buf.write("\u0211\3\2\2\2\u0235\u0216\3\2\2\2\u0235\u0219\3\2\2\2")
        buf.write("\u0235\u021b\3\2\2\2\u0235\u0221\3\2\2\2\u0235\u0228\3")
        buf.write("\2\2\2\u0235\u022e\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235")
        buf.write("\3\2\2\2\u0237\u0238\3\2\2\2\u0238O\3\2\2\2\u0239\u0237")
        buf.write("\3\2\2\2\u023a\u023b\t\t\2\2\u023bQ\3\2\2\2\u023c\u023d")
        buf.write("\t\n\2\2\u023dS\3\2\2\2\u023e\u0241\t\13\2\2\u023f\u0241")
        buf.write("\5V,\2\u0240\u023e\3\2\2\2\u0240\u023f\3\2\2\2\u0241U")
        buf.write("\3\2\2\2\u0242\u0243\t\f\2\2\u0243W\3\2\2\2\u0244\u0247")
        buf.write("\7f\2\2\u0245\u0247\5Z.\2\u0246\u0244\3\2\2\2\u0246\u0245")
        buf.write("\3\2\2\2\u0247Y\3\2\2\2\u0248\u024c\5\\/\2\u0249\u024c")
        buf.write("\5^\60\2\u024a\u024c\t\r\2\2\u024b\u0248\3\2\2\2\u024b")
        buf.write("\u0249\3\2\2\2\u024b\u024a\3\2\2\2\u024c[\3\2\2\2\u024d")
        buf.write("\u024e\t\16\2\2\u024e]\3\2\2\2\u024f\u0250\t\17\2\2\u0250")
        buf.write("_\3\2\2\2\u0251\u0256\7\13\2\2\u0252\u0256\7\2\2\3\u0253")
        buf.write("\u0256\6\61\26\2\u0254\u0256\6\61\27\2\u0255\u0251\3\2")
        buf.write("\2\2\u0255\u0252\3\2\2\2\u0255\u0253\3\2\2\2\u0255\u0254")
        buf.write("\3\2\2\2\u0256a\3\2\2\2\u0257\u0258\7\2\2\3\u0258c\3\2")
        buf.write("\2\2\62el}\u0081\u0088\u0093\u0098\u00a8\u00bb\u00bf\u00c3")
        buf.write("\u00cd\u00d1\u00e7\u00eb\u00f1\u00f7\u010a\u010c\u0114")
        buf.write("\u0119\u0130\u0143\u0147\u014b\u014e\u0151\u0156\u015b")
        buf.write("\u0160\u0166\u016e\u0171\u0174\u0193\u0198\u019c\u01a5")
        buf.write("\u01ad\u01c1\u01c5\u01ee\u0235\u0237\u0240\u0246\u024b")
        buf.write("\u0255")
        return buf.getvalue()
		

class ECMAScriptParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    RegularExpressionLiteral=1
    LineTerminator=2
    OpenBracket=3
    CloseBracket=4
    OpenParen=5
    CloseParen=6
    OpenBrace=7
    CloseBrace=8
    SemiColon=9
    Comma=10
    Assign=11
    QuestionMark=12
    Colon=13
    Dot=14
    PlusPlus=15
    MinusMinus=16
    Plus=17
    Minus=18
    BitNot=19
    Not=20
    Multiply=21
    Divide=22
    Modulus=23
    RightShiftArithmetic=24
    LeftShiftArithmetic=25
    RightShiftLogical=26
    LessThan=27
    MoreThan=28
    LessThanEquals=29
    GreaterThanEquals=30
    Equals=31
    NotEquals=32
    IdentityEquals=33
    IdentityNotEquals=34
    BitAnd=35
    BitXOr=36
    BitOr=37
    And=38
    Or=39
    MultiplyAssign=40
    DivideAssign=41
    ModulusAssign=42
    PlusAssign=43
    MinusAssign=44
    LeftShiftArithmeticAssign=45
    RightShiftArithmeticAssign=46
    RightShiftLogicalAssign=47
    BitAndAssign=48
    BitXorAssign=49
    BitOrAssign=50
    Get=51
    Set=52
    NullLiteral=53
    BooleanLiteral=54
    DecimalLiteral=55
    HexIntegerLiteral=56
    OctalIntegerLiteral=57
    Break=58
    Do=59
    Instanceof=60
    Typeof=61
    Case=62
    Else=63
    New=64
    Var=65
    Catch=66
    Finally=67
    Return=68
    Void=69
    Continue=70
    For=71
    Switch=72
    While=73
    Debugger=74
    Function=75
    This=76
    With=77
    Default=78
    If=79
    Throw=80
    Delete=81
    In=82
    Try=83
    Class=84
    Enum=85
    Extends=86
    Super=87
    Const=88
    Export=89
    Import=90
    Implements=91
    Let=92
    Private=93
    Public=94
    Interface=95
    Package=96
    Protected=97
    Static=98
    Yield=99
    Identifier=100
    StringLiteral=101
    WhiteSpaces=102
    MultiLineComment=103
    SingleLineComment=104
    UnexpectedCharacter=105

    tokenNames = [ "<INVALID>", "RegularExpressionLiteral", "LineTerminator", 
                   "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "','", 
                   "'='", "'?'", "':'", "'.'", "'++'", "'--'", "'+'", "'-'", 
                   "'~'", "'!'", "'*'", "'/'", "'%'", "'>>'", "'<<'", "'>>>'", 
                   "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'==='", 
                   "'!=='", "'&'", "'^'", "'|'", "'&&'", "'||'", "'*='", 
                   "'/='", "'%='", "'+='", "'-='", "'<<='", "'>>='", "'>>>='", 
                   "'&='", "'^='", "'|='", "'get'", "'set'", "'null'", "BooleanLiteral", 
                   "DecimalLiteral", "HexIntegerLiteral", "OctalIntegerLiteral", 
                   "'break'", "'do'", "'instanceof'", "'typeof'", "'case'", 
                   "'else'", "'new'", "'var'", "'catch'", "'finally'", "'return'", 
                   "'void'", "'continue'", "'for'", "'switch'", "'while'", 
                   "'debugger'", "'function'", "'this'", "'with'", "'default'", 
                   "'if'", "'throw'", "'delete'", "'in'", "'try'", "'class'", 
                   "'enum'", "'extends'", "'super'", "'const'", "'export'", 
                   "'import'", "Implements", "Let", "Private", "Public", 
                   "Interface", "Package", "Protected", "Static", "Yield", 
                   "Identifier", "StringLiteral", "WhiteSpaces", "MultiLineComment", 
                   "SingleLineComment", "UnexpectedCharacter" ]

    RULE_program = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_block = 3
    RULE_statementList = 4
    RULE_variableStatement = 5
    RULE_variableDeclarationList = 6
    RULE_variableDeclaration = 7
    RULE_initialiser = 8
    RULE_emptyStatement = 9
    RULE_expressionStatement = 10
    RULE_ifStatement = 11
    RULE_iterationStatement = 12
    RULE_continueStatement = 13
    RULE_breakStatement = 14
    RULE_returnStatement = 15
    RULE_withStatement = 16
    RULE_switchStatement = 17
    RULE_caseBlock = 18
    RULE_caseClause = 19
    RULE_defaultClause = 20
    RULE_labelledStatement = 21
    RULE_throwStatement = 22
    RULE_tryStatement = 23
    RULE_catchProduction = 24
    RULE_finallyProduction = 25
    RULE_debuggerStatement = 26
    RULE_formalParameterList = 27
    RULE_functionBody = 28
    RULE_arrayLiteral = 29
    RULE_elementList = 30
    RULE_elision = 31
    RULE_objectLiteral = 32
    RULE_propertyAssignment = 33
    RULE_propertyName = 34
    RULE_arguments = 35
    RULE_argumentList = 36
    RULE_expressionSequence = 37
    RULE_singleExpression = 38
    RULE_incrementOperator = 39
    RULE_assignmentOperator = 40
    RULE_literal = 41
    RULE_numericLiteral = 42
    RULE_identifierName = 43
    RULE_reservedWord = 44
    RULE_keyword = 45
    RULE_futureReservedWord = 46
    RULE_eos = 47
    RULE_eof = 48

    ruleNames =  [ "program", "statements", "statement", "block", "statementList", 
                   "variableStatement", "variableDeclarationList", "variableDeclaration", 
                   "initialiser", "emptyStatement", "expressionStatement", 
                   "ifStatement", "iterationStatement", "continueStatement", 
                   "breakStatement", "returnStatement", "withStatement", 
                   "switchStatement", "caseBlock", "caseClause", "defaultClause", 
                   "labelledStatement", "throwStatement", "tryStatement", 
                   "catchProduction", "finallyProduction", "debuggerStatement", 
                   "formalParameterList", "functionBody", "arrayLiteral", 
                   "elementList", "elision", "objectLiteral", "propertyAssignment", 
                   "propertyName", "arguments", "argumentList", "expressionSequence", 
                   "singleExpression", "incrementOperator", "assignmentOperator", 
                   "literal", "numericLiteral", "identifierName", "reservedWord", 
                   "keyword", "futureReservedWord", "eos", "eof" ]

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ECMAScriptParser.EOF, 0)

        def statements(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementsContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ECMAScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RegularExpressionLiteral) | (1 << self.OpenBracket) | (1 << self.OpenParen) | (1 << self.OpenBrace) | (1 << self.SemiColon) | (1 << self.PlusPlus) | (1 << self.MinusMinus) | (1 << self.Plus) | (1 << self.Minus) | (1 << self.BitNot) | (1 << self.Not) | (1 << self.NullLiteral) | (1 << self.BooleanLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.New - 64)) | (1 << (self.Var - 64)) | (1 << (self.Return - 64)) | (1 << (self.Void - 64)) | (1 << (self.Continue - 64)) | (1 << (self.For - 64)) | (1 << (self.Switch - 64)) | (1 << (self.While - 64)) | (1 << (self.Debugger - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.With - 64)) | (1 << (self.If - 64)) | (1 << (self.Throw - 64)) | (1 << (self.Delete - 64)) | (1 << (self.Try - 64)) | (1 << (self.Identifier - 64)) | (1 << (self.StringLiteral - 64)))) != 0):
                self.state = 98 
                self.statements()


            self.state = 101
            self.match(self.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = ECMAScriptParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 103 
                self.statement()
                self.state = 106 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RegularExpressionLiteral) | (1 << self.OpenBracket) | (1 << self.OpenParen) | (1 << self.OpenBrace) | (1 << self.SemiColon) | (1 << self.PlusPlus) | (1 << self.MinusMinus) | (1 << self.Plus) | (1 << self.Minus) | (1 << self.BitNot) | (1 << self.Not) | (1 << self.NullLiteral) | (1 << self.BooleanLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.New - 64)) | (1 << (self.Var - 64)) | (1 << (self.Return - 64)) | (1 << (self.Void - 64)) | (1 << (self.Continue - 64)) | (1 << (self.For - 64)) | (1 << (self.Switch - 64)) | (1 << (self.While - 64)) | (1 << (self.Debugger - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.With - 64)) | (1 << (self.If - 64)) | (1 << (self.Throw - 64)) | (1 << (self.Delete - 64)) | (1 << (self.Try - 64)) | (1 << (self.Identifier - 64)) | (1 << (self.StringLiteral - 64)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tryStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.TryStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.SwitchStatementContext,0)


        def withStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.WithStatementContext,0)


        def debuggerStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.DebuggerStatementContext,0)


        def labelledStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.LabelledStatementContext,0)


        def emptyStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.EmptyStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.BreakStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.IfStatementContext,0)


        def variableStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionStatementContext,0)


        def throwStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ThrowStatementContext,0)


        def iterationStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.IterationStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ContinueStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ECMAScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 123
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108 
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109 
                self.variableStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110 
                self.emptyStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 111 
                self.expressionStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 112 
                self.ifStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 113 
                self.iterationStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 114 
                self.continueStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 115 
                self.breakStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 116 
                self.returnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 117 
                self.withStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 118 
                self.labelledStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 119 
                self.switchStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 120 
                self.throwStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 121 
                self.tryStatement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 122 
                self.debuggerStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ECMAScriptParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(self.OpenBrace)
            self.state = 127
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RegularExpressionLiteral) | (1 << self.OpenBracket) | (1 << self.OpenParen) | (1 << self.OpenBrace) | (1 << self.SemiColon) | (1 << self.PlusPlus) | (1 << self.MinusMinus) | (1 << self.Plus) | (1 << self.Minus) | (1 << self.BitNot) | (1 << self.Not) | (1 << self.NullLiteral) | (1 << self.BooleanLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.New - 64)) | (1 << (self.Var - 64)) | (1 << (self.Return - 64)) | (1 << (self.Void - 64)) | (1 << (self.Continue - 64)) | (1 << (self.For - 64)) | (1 << (self.Switch - 64)) | (1 << (self.While - 64)) | (1 << (self.Debugger - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.With - 64)) | (1 << (self.If - 64)) | (1 << (self.Throw - 64)) | (1 << (self.Delete - 64)) | (1 << (self.Try - 64)) | (1 << (self.Identifier - 64)) | (1 << (self.StringLiteral - 64)))) != 0):
                self.state = 126 
                self.statementList()


            self.state = 129
            self.match(self.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitStatementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = ECMAScriptParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 131 
                self.statement()
                self.state = 134 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RegularExpressionLiteral) | (1 << self.OpenBracket) | (1 << self.OpenParen) | (1 << self.OpenBrace) | (1 << self.SemiColon) | (1 << self.PlusPlus) | (1 << self.MinusMinus) | (1 << self.Plus) | (1 << self.Minus) | (1 << self.BitNot) | (1 << self.Not) | (1 << self.NullLiteral) | (1 << self.BooleanLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.New - 64)) | (1 << (self.Var - 64)) | (1 << (self.Return - 64)) | (1 << (self.Void - 64)) | (1 << (self.Continue - 64)) | (1 << (self.For - 64)) | (1 << (self.Switch - 64)) | (1 << (self.While - 64)) | (1 << (self.Debugger - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.With - 64)) | (1 << (self.If - 64)) | (1 << (self.Throw - 64)) | (1 << (self.Delete - 64)) | (1 << (self.Try - 64)) | (1 << (self.Identifier - 64)) | (1 << (self.StringLiteral - 64)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def variableDeclarationList(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationListContext,0)


        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_variableStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterVariableStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitVariableStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitVariableStatement(self)
            else:
                return visitor.visitChildren(self)




    def variableStatement(self):

        localctx = ECMAScriptParser.VariableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(self.Var)
            self.state = 137 
            self.variableDeclarationList()
            self.state = 138 
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_variableDeclarationList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterVariableDeclarationList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitVariableDeclarationList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitVariableDeclarationList(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarationList(self):

        localctx = ECMAScriptParser.VariableDeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableDeclarationList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140 
            self.variableDeclaration()
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 141
                    self.match(self.Comma)
                    self.state = 142 
                    self.variableDeclaration() 
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def initialiser(self):
            return self.getTypedRuleContext(ECMAScriptParser.InitialiserContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = ECMAScriptParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(self.Identifier)
            self.state = 150
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 149 
                self.initialiser()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitialiserContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_initialiser

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterInitialiser(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitInitialiser(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitInitialiser(self)
            else:
                return visitor.visitChildren(self)




    def initialiser(self):

        localctx = ECMAScriptParser.InitialiserContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_initialiser)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(self.Assign)
            self.state = 153 
            self.singleExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EmptyStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SemiColon(self):
            return self.getToken(ECMAScriptParser.SemiColon, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_emptyStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitEmptyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitEmptyStatement(self)
            else:
                return visitor.visitChildren(self)




    def emptyStatement(self):

        localctx = ECMAScriptParser.EmptyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_emptyStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(self.SemiColon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = ECMAScriptParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157 
            self.expressionSequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def Else(self):
            return self.getToken(ECMAScriptParser.Else, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.StatementContext,i)


        def If(self):
            return self.getToken(ECMAScriptParser.If, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = ECMAScriptParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(self.If)
            self.state = 160
            self.match(self.OpenParen)
            self.state = 161 
            self.expressionSequence()
            self.state = 162
            self.match(self.CloseParen)
            self.state = 163 
            self.statement()
            self.state = 166
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 164
                self.match(self.Else)
                self.state = 165 
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IterationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_iterationStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DoStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.IterationStatementContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def While(self):
            return self.getToken(ECMAScriptParser.While, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def Do(self):
            return self.getToken(ECMAScriptParser.Do, 0)
        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterDoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitDoStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitDoStatement(self)
            else:
                return visitor.visitChildren(self)


    class WhileStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.IterationStatementContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def While(self):
            return self.getToken(ECMAScriptParser.While, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)


    class ForStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.IterationStatementContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def variableDeclarationList(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationListContext,0)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)

        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)
        def expressionSequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)


    class ForInStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.IterationStatementContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def variableDeclaration(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationContext,0)

        def In(self):
            return self.getToken(ECMAScriptParser.In, 0)
        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterForInStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitForInStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitForInStatement(self)
            else:
                return visitor.visitChildren(self)



    def iterationStatement(self):

        localctx = ECMAScriptParser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 229
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.DoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(self.Do)
                self.state = 169 
                self.statement()
                self.state = 170
                self.match(self.While)
                self.state = 171
                self.match(self.OpenParen)
                self.state = 172 
                self.expressionSequence()
                self.state = 173
                self.match(self.CloseParen)
                self.state = 174 
                self.eos()
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(self.While)
                self.state = 177
                self.match(self.OpenParen)
                self.state = 178 
                self.expressionSequence()
                self.state = 179
                self.match(self.CloseParen)
                self.state = 180 
                self.statement()
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.match(self.For)
                self.state = 183
                self.match(self.OpenParen)
                self.state = 185
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RegularExpressionLiteral) | (1 << self.OpenBracket) | (1 << self.OpenParen) | (1 << self.OpenBrace) | (1 << self.PlusPlus) | (1 << self.MinusMinus) | (1 << self.Plus) | (1 << self.Minus) | (1 << self.BitNot) | (1 << self.Not) | (1 << self.NullLiteral) | (1 << self.BooleanLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.New - 64)) | (1 << (self.Void - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.Delete - 64)) | (1 << (self.Identifier - 64)) | (1 << (self.StringLiteral - 64)))) != 0):
                    self.state = 184 
                    self.expressionSequence()


                self.state = 187
                self.match(self.SemiColon)
                self.state = 189
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RegularExpressionLiteral) | (1 << self.OpenBracket) | (1 << self.OpenParen) | (1 << self.OpenBrace) | (1 << self.PlusPlus) | (1 << self.MinusMinus) | (1 << self.Plus) | (1 << self.Minus) | (1 << self.BitNot) | (1 << self.Not) | (1 << self.NullLiteral) | (1 << self.BooleanLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.New - 64)) | (1 << (self.Void - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.Delete - 64)) | (1 << (self.Identifier - 64)) | (1 << (self.StringLiteral - 64)))) != 0):
                    self.state = 188 
                    self.expressionSequence()


                self.state = 191
                self.match(self.SemiColon)
                self.state = 193
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RegularExpressionLiteral) | (1 << self.OpenBracket) | (1 << self.OpenParen) | (1 << self.OpenBrace) | (1 << self.PlusPlus) | (1 << self.MinusMinus) | (1 << self.Plus) | (1 << self.Minus) | (1 << self.BitNot) | (1 << self.Not) | (1 << self.NullLiteral) | (1 << self.BooleanLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.New - 64)) | (1 << (self.Void - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.Delete - 64)) | (1 << (self.Identifier - 64)) | (1 << (self.StringLiteral - 64)))) != 0):
                    self.state = 192 
                    self.expressionSequence()


                self.state = 195
                self.match(self.CloseParen)
                self.state = 196 
                self.statement()
                pass

            elif la_ == 4:
                localctx = ECMAScriptParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 197
                self.match(self.For)
                self.state = 198
                self.match(self.OpenParen)
                self.state = 199
                self.match(self.Var)
                self.state = 200 
                self.variableDeclarationList()
                self.state = 201
                self.match(self.SemiColon)
                self.state = 203
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RegularExpressionLiteral) | (1 << self.OpenBracket) | (1 << self.OpenParen) | (1 << self.OpenBrace) | (1 << self.PlusPlus) | (1 << self.MinusMinus) | (1 << self.Plus) | (1 << self.Minus) | (1 << self.BitNot) | (1 << self.Not) | (1 << self.NullLiteral) | (1 << self.BooleanLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.New - 64)) | (1 << (self.Void - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.Delete - 64)) | (1 << (self.Identifier - 64)) | (1 << (self.StringLiteral - 64)))) != 0):
                    self.state = 202 
                    self.expressionSequence()


                self.state = 205
                self.match(self.SemiColon)
                self.state = 207
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RegularExpressionLiteral) | (1 << self.OpenBracket) | (1 << self.OpenParen) | (1 << self.OpenBrace) | (1 << self.PlusPlus) | (1 << self.MinusMinus) | (1 << self.Plus) | (1 << self.Minus) | (1 << self.BitNot) | (1 << self.Not) | (1 << self.NullLiteral) | (1 << self.BooleanLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.New - 64)) | (1 << (self.Void - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.Delete - 64)) | (1 << (self.Identifier - 64)) | (1 << (self.StringLiteral - 64)))) != 0):
                    self.state = 206 
                    self.expressionSequence()


                self.state = 209
                self.match(self.CloseParen)
                self.state = 210 
                self.statement()
                pass

            elif la_ == 5:
                localctx = ECMAScriptParser.ForInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 212
                self.match(self.For)
                self.state = 213
                self.match(self.OpenParen)
                self.state = 214 
                self.singleExpression(0)
                self.state = 215
                self.match(self.In)
                self.state = 216 
                self.expressionSequence()
                self.state = 217
                self.match(self.CloseParen)
                self.state = 218 
                self.statement()
                pass

            elif la_ == 6:
                localctx = ECMAScriptParser.ForInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 220
                self.match(self.For)
                self.state = 221
                self.match(self.OpenParen)
                self.state = 222
                self.match(self.Var)
                self.state = 223 
                self.variableDeclaration()
                self.state = 224
                self.match(self.In)
                self.state = 225 
                self.expressionSequence()
                self.state = 226
                self.match(self.CloseParen)
                self.state = 227 
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContinueStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def Continue(self):
            return self.getToken(ECMAScriptParser.Continue, 0)

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitContinueStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = ECMAScriptParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(self.Continue)
            self.state = 233
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 232
                self.match(self.Identifier)


            self.state = 235 
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BreakStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def Break(self):
            return self.getToken(ECMAScriptParser.Break, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitBreakStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = ECMAScriptParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(self.Break)
            self.state = 239
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 238
                self.match(self.Identifier)


            self.state = 241 
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def Return(self):
            return self.getToken(ECMAScriptParser.Return, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = ECMAScriptParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(self.Return)
            self.state = 245
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 244 
                self.expressionSequence()


            self.state = 247 
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WithStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


        def With(self):
            return self.getToken(ECMAScriptParser.With, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_withStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterWithStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitWithStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitWithStatement(self)
            else:
                return visitor.visitChildren(self)




    def withStatement(self):

        localctx = ECMAScriptParser.WithStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_withStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(self.With)
            self.state = 250
            self.match(self.OpenParen)
            self.state = 251 
            self.expressionSequence()
            self.state = 252
            self.match(self.CloseParen)
            self.state = 253 
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SwitchStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def Switch(self):
            return self.getToken(ECMAScriptParser.Switch, 0)

        def caseBlock(self):
            return self.getTypedRuleContext(ECMAScriptParser.CaseBlockContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitSwitchStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = ECMAScriptParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_switchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(self.Switch)
            self.state = 256
            self.match(self.OpenParen)
            self.state = 257 
            self.expressionSequence()
            self.state = 258
            self.match(self.CloseParen)
            self.state = 259 
            self.caseBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CaseBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def defaultClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.DefaultClauseContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.DefaultClauseContext,i)


        def caseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.CaseClauseContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.CaseClauseContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_caseBlock

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterCaseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitCaseBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitCaseBlock(self)
            else:
                return visitor.visitChildren(self)




    def caseBlock(self):

        localctx = ECMAScriptParser.CaseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_caseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(self.OpenBrace)
            self.state = 264 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 264
                token = self._input.LA(1)
                if token in [self.Case]:
                    self.state = 262 
                    self.caseClause()

                elif token in [self.Default]:
                    self.state = 263 
                    self.defaultClause()

                else:
                    raise NoViableAltException(self)

                self.state = 266 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECMAScriptParser.Case or _la==ECMAScriptParser.Default):
                    break

            self.state = 268
            self.match(self.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CaseClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def statementList(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementListContext,0)


        def Case(self):
            return self.getToken(ECMAScriptParser.Case, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_caseClause

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterCaseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitCaseClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitCaseClause(self)
            else:
                return visitor.visitChildren(self)




    def caseClause(self):

        localctx = ECMAScriptParser.CaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_caseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(self.Case)
            self.state = 271 
            self.expressionSequence()
            self.state = 272
            self.match(self.Colon)
            self.state = 274
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RegularExpressionLiteral) | (1 << self.OpenBracket) | (1 << self.OpenParen) | (1 << self.OpenBrace) | (1 << self.SemiColon) | (1 << self.PlusPlus) | (1 << self.MinusMinus) | (1 << self.Plus) | (1 << self.Minus) | (1 << self.BitNot) | (1 << self.Not) | (1 << self.NullLiteral) | (1 << self.BooleanLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.New - 64)) | (1 << (self.Var - 64)) | (1 << (self.Return - 64)) | (1 << (self.Void - 64)) | (1 << (self.Continue - 64)) | (1 << (self.For - 64)) | (1 << (self.Switch - 64)) | (1 << (self.While - 64)) | (1 << (self.Debugger - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.With - 64)) | (1 << (self.If - 64)) | (1 << (self.Throw - 64)) | (1 << (self.Delete - 64)) | (1 << (self.Try - 64)) | (1 << (self.Identifier - 64)) | (1 << (self.StringLiteral - 64)))) != 0):
                self.state = 273 
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DefaultClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Default(self):
            return self.getToken(ECMAScriptParser.Default, 0)

        def statementList(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_defaultClause

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterDefaultClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitDefaultClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitDefaultClause(self)
            else:
                return visitor.visitChildren(self)




    def defaultClause(self):

        localctx = ECMAScriptParser.DefaultClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_defaultClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(self.Default)
            self.state = 277
            self.match(self.Colon)
            self.state = 279
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RegularExpressionLiteral) | (1 << self.OpenBracket) | (1 << self.OpenParen) | (1 << self.OpenBrace) | (1 << self.SemiColon) | (1 << self.PlusPlus) | (1 << self.MinusMinus) | (1 << self.Plus) | (1 << self.Minus) | (1 << self.BitNot) | (1 << self.Not) | (1 << self.NullLiteral) | (1 << self.BooleanLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.New - 64)) | (1 << (self.Var - 64)) | (1 << (self.Return - 64)) | (1 << (self.Void - 64)) | (1 << (self.Continue - 64)) | (1 << (self.For - 64)) | (1 << (self.Switch - 64)) | (1 << (self.While - 64)) | (1 << (self.Debugger - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.With - 64)) | (1 << (self.If - 64)) | (1 << (self.Throw - 64)) | (1 << (self.Delete - 64)) | (1 << (self.Try - 64)) | (1 << (self.Identifier - 64)) | (1 << (self.StringLiteral - 64)))) != 0):
                self.state = 278 
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelledStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_labelledStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterLabelledStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitLabelledStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitLabelledStatement(self)
            else:
                return visitor.visitChildren(self)




    def labelledStatement(self):

        localctx = ECMAScriptParser.LabelledStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_labelledStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(self.Identifier)
            self.state = 282
            self.match(self.Colon)
            self.state = 283 
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ThrowStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def Throw(self):
            return self.getToken(ECMAScriptParser.Throw, 0)

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_throwStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterThrowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitThrowStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitThrowStatement(self)
            else:
                return visitor.visitChildren(self)




    def throwStatement(self):

        localctx = ECMAScriptParser.ThrowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_throwStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(self.Throw)
            self.state = 286 
            self.expressionSequence()
            self.state = 287 
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TryStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def catchProduction(self):
            return self.getTypedRuleContext(ECMAScriptParser.CatchProductionContext,0)


        def finallyProduction(self):
            return self.getTypedRuleContext(ECMAScriptParser.FinallyProductionContext,0)


        def Try(self):
            return self.getToken(ECMAScriptParser.Try, 0)

        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_tryStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterTryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitTryStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitTryStatement(self)
            else:
                return visitor.visitChildren(self)




    def tryStatement(self):

        localctx = ECMAScriptParser.TryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_tryStatement)
        try:
            self.state = 302
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.match(self.Try)
                self.state = 290 
                self.block()
                self.state = 291 
                self.catchProduction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.match(self.Try)
                self.state = 294 
                self.block()
                self.state = 295 
                self.finallyProduction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 297
                self.match(self.Try)
                self.state = 298 
                self.block()
                self.state = 299 
                self.catchProduction()
                self.state = 300 
                self.finallyProduction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CatchProductionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Catch(self):
            return self.getToken(ECMAScriptParser.Catch, 0)

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_catchProduction

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterCatchProduction(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitCatchProduction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitCatchProduction(self)
            else:
                return visitor.visitChildren(self)




    def catchProduction(self):

        localctx = ECMAScriptParser.CatchProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_catchProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(self.Catch)
            self.state = 305
            self.match(self.OpenParen)
            self.state = 306
            self.match(self.Identifier)
            self.state = 307
            self.match(self.CloseParen)
            self.state = 308 
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FinallyProductionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Finally(self):
            return self.getToken(ECMAScriptParser.Finally, 0)

        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_finallyProduction

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFinallyProduction(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFinallyProduction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitFinallyProduction(self)
            else:
                return visitor.visitChildren(self)




    def finallyProduction(self):

        localctx = ECMAScriptParser.FinallyProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_finallyProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(self.Finally)
            self.state = 311 
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DebuggerStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def Debugger(self):
            return self.getToken(ECMAScriptParser.Debugger, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_debuggerStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterDebuggerStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitDebuggerStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitDebuggerStatement(self)
            else:
                return visitor.visitChildren(self)




    def debuggerStatement(self):

        localctx = ECMAScriptParser.DebuggerStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_debuggerStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(self.Debugger)
            self.state = 314 
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormalParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(ECMAScriptParser.Identifier)
            else:
                return self.getToken(ECMAScriptParser.Identifier, i)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_formalParameterList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFormalParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFormalParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitFormalParameterList(self)
            else:
                return visitor.visitChildren(self)




    def formalParameterList(self):

        localctx = ECMAScriptParser.FormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(self.Identifier)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.Comma:
                self.state = 317
                self.match(self.Comma)
                self.state = 318
                self.match(self.Identifier)
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementsContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_functionBody

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFunctionBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitFunctionBody(self)
            else:
                return visitor.visitChildren(self)




    def functionBody(self):

        localctx = ECMAScriptParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RegularExpressionLiteral) | (1 << self.OpenBracket) | (1 << self.OpenParen) | (1 << self.OpenBrace) | (1 << self.SemiColon) | (1 << self.PlusPlus) | (1 << self.MinusMinus) | (1 << self.Plus) | (1 << self.Minus) | (1 << self.BitNot) | (1 << self.Not) | (1 << self.NullLiteral) | (1 << self.BooleanLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.New - 64)) | (1 << (self.Var - 64)) | (1 << (self.Return - 64)) | (1 << (self.Void - 64)) | (1 << (self.Continue - 64)) | (1 << (self.For - 64)) | (1 << (self.Switch - 64)) | (1 << (self.While - 64)) | (1 << (self.Debugger - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.With - 64)) | (1 << (self.If - 64)) | (1 << (self.Throw - 64)) | (1 << (self.Delete - 64)) | (1 << (self.Try - 64)) | (1 << (self.Identifier - 64)) | (1 << (self.StringLiteral - 64)))) != 0):
                self.state = 324 
                self.statements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elision(self):
            return self.getTypedRuleContext(ECMAScriptParser.ElisionContext,0)


        def elementList(self):
            return self.getTypedRuleContext(ECMAScriptParser.ElementListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitArrayLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = ECMAScriptParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(self.OpenBracket)
            self.state = 329
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 328 
                self.elementList()


            self.state = 332
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 331
                self.match(self.Comma)


            self.state = 335
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Comma:
                self.state = 334 
                self.elision()


            self.state = 337
            self.match(self.CloseBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elision(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.ElisionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.ElisionContext,i)


        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_elementList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterElementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitElementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitElementList(self)
            else:
                return visitor.visitChildren(self)




    def elementList(self):

        localctx = ECMAScriptParser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_elementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Comma:
                self.state = 339 
                self.elision()


            self.state = 342 
            self.singleExpression(0)
            self.state = 350
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 343
                    self.match(self.Comma)
                    self.state = 345
                    _la = self._input.LA(1)
                    if _la==ECMAScriptParser.Comma:
                        self.state = 344 
                        self.elision()


                    self.state = 347 
                    self.singleExpression(0) 
                self.state = 352
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElisionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_elision

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterElision(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitElision(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitElision(self)
            else:
                return visitor.visitChildren(self)




    def elision(self):

        localctx = ECMAScriptParser.ElisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_elision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 353
                self.match(self.Comma)
                self.state = 356 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECMAScriptParser.Comma):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjectLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def propertyAssignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.PropertyAssignmentContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.PropertyAssignmentContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_objectLiteral

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterObjectLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitObjectLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitObjectLiteral(self)
            else:
                return visitor.visitChildren(self)




    def objectLiteral(self):

        localctx = ECMAScriptParser.ObjectLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_objectLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(self.OpenBrace)
            self.state = 367
            _la = self._input.LA(1)
            if ((((_la - 51)) & ~0x3f) == 0 and ((1 << (_la - 51)) & ((1 << (self.Get - 51)) | (1 << (self.Set - 51)) | (1 << (self.NullLiteral - 51)) | (1 << (self.BooleanLiteral - 51)) | (1 << (self.DecimalLiteral - 51)) | (1 << (self.HexIntegerLiteral - 51)) | (1 << (self.OctalIntegerLiteral - 51)) | (1 << (self.Break - 51)) | (1 << (self.Do - 51)) | (1 << (self.Instanceof - 51)) | (1 << (self.Typeof - 51)) | (1 << (self.Case - 51)) | (1 << (self.Else - 51)) | (1 << (self.New - 51)) | (1 << (self.Var - 51)) | (1 << (self.Catch - 51)) | (1 << (self.Finally - 51)) | (1 << (self.Return - 51)) | (1 << (self.Void - 51)) | (1 << (self.Continue - 51)) | (1 << (self.For - 51)) | (1 << (self.Switch - 51)) | (1 << (self.While - 51)) | (1 << (self.Debugger - 51)) | (1 << (self.Function - 51)) | (1 << (self.This - 51)) | (1 << (self.With - 51)) | (1 << (self.Default - 51)) | (1 << (self.If - 51)) | (1 << (self.Throw - 51)) | (1 << (self.Delete - 51)) | (1 << (self.In - 51)) | (1 << (self.Try - 51)) | (1 << (self.Class - 51)) | (1 << (self.Enum - 51)) | (1 << (self.Extends - 51)) | (1 << (self.Super - 51)) | (1 << (self.Const - 51)) | (1 << (self.Export - 51)) | (1 << (self.Import - 51)) | (1 << (self.Implements - 51)) | (1 << (self.Let - 51)) | (1 << (self.Private - 51)) | (1 << (self.Public - 51)) | (1 << (self.Interface - 51)) | (1 << (self.Package - 51)) | (1 << (self.Protected - 51)) | (1 << (self.Static - 51)) | (1 << (self.Yield - 51)) | (1 << (self.Identifier - 51)) | (1 << (self.StringLiteral - 51)))) != 0):
                self.state = 359 
                self.propertyAssignment()
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 360
                        self.match(self.Comma)
                        self.state = 361 
                        self.propertyAssignment() 
                    self.state = 366
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)



            self.state = 370
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Comma:
                self.state = 369
                self.match(self.Comma)


            self.state = 372
            self.match(self.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_propertyAssignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PropertyExpressionAssignmentContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.PropertyAssignmentContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def Set(self):
            return self.getToken(ECMAScriptParser.Set, 0)
        def Get(self):
            return self.getToken(ECMAScriptParser.Get, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def propertyName(self):
            return self.getTypedRuleContext(ECMAScriptParser.PropertyNameContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertyExpressionAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertyExpressionAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitPropertyExpressionAssignment(self)
            else:
                return visitor.visitChildren(self)


    class PropertySetterContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.PropertyAssignmentContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(ECMAScriptParser.Identifier)
            else:
                return self.getToken(ECMAScriptParser.Identifier, i)
        def functionBody(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionBodyContext,0)

        def Set(self):
            return self.getToken(ECMAScriptParser.Set, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertySetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertySetter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitPropertySetter(self)
            else:
                return visitor.visitChildren(self)


    class PropertyGetterContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.PropertyAssignmentContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)
        def functionBody(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionBodyContext,0)

        def Get(self):
            return self.getToken(ECMAScriptParser.Get, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertyGetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertyGetter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitPropertyGetter(self)
            else:
                return visitor.visitChildren(self)



    def propertyAssignment(self):

        localctx = ECMAScriptParser.PropertyAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_propertyAssignment)
        try:
            self.state = 401
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.PropertyExpressionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 374 
                self.propertyName()
                self.state = 375
                self.match(self.Colon)
                self.state = 376 
                self.singleExpression(0)
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.PropertyExpressionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.match(self.Get)
                self.state = 379
                self.match(self.Colon)
                self.state = 380 
                self.singleExpression(0)
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.PropertyGetterContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 381
                self.match(self.Get)
                self.state = 382
                self.match(self.Identifier)
                self.state = 383
                self.match(self.OpenParen)
                self.state = 384
                self.match(self.CloseParen)
                self.state = 385
                self.match(self.OpenBrace)
                self.state = 386 
                self.functionBody()
                self.state = 387
                self.match(self.CloseBrace)
                pass

            elif la_ == 4:
                localctx = ECMAScriptParser.PropertyExpressionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 389
                self.match(self.Set)
                self.state = 390
                self.match(self.Colon)
                self.state = 391 
                self.singleExpression(0)
                pass

            elif la_ == 5:
                localctx = ECMAScriptParser.PropertySetterContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 392
                self.match(self.Set)
                self.state = 393
                self.match(self.Identifier)
                self.state = 394
                self.match(self.OpenParen)
                self.state = 395
                self.match(self.Identifier)
                self.state = 396
                self.match(self.CloseParen)
                self.state = 397
                self.match(self.OpenBrace)
                self.state = 398 
                self.functionBody()
                self.state = 399
                self.match(self.CloseBrace)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.NumericLiteralContext,0)


        def StringLiteral(self):
            return self.getToken(ECMAScriptParser.StringLiteral, 0)

        def identifierName(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierNameContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_propertyName

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertyName(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertyName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitPropertyName(self)
            else:
                return visitor.visitChildren(self)




    def propertyName(self):

        localctx = ECMAScriptParser.PropertyNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_propertyName)
        try:
            self.state = 406
            token = self._input.LA(1)
            if token in [self.NullLiteral, self.BooleanLiteral, self.Break, self.Do, self.Instanceof, self.Typeof, self.Case, self.Else, self.New, self.Var, self.Catch, self.Finally, self.Return, self.Void, self.Continue, self.For, self.Switch, self.While, self.Debugger, self.Function, self.This, self.With, self.Default, self.If, self.Throw, self.Delete, self.In, self.Try, self.Class, self.Enum, self.Extends, self.Super, self.Const, self.Export, self.Import, self.Implements, self.Let, self.Private, self.Public, self.Interface, self.Package, self.Protected, self.Static, self.Yield, self.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 403 
                self.identifierName()

            elif token in [self.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.match(self.StringLiteral)

            elif token in [self.DecimalLiteral, self.HexIntegerLiteral, self.OctalIntegerLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 405 
                self.numericLiteral()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argumentList(self):
            return self.getTypedRuleContext(ECMAScriptParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = ECMAScriptParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(self.OpenParen)
            self.state = 410
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RegularExpressionLiteral) | (1 << self.OpenBracket) | (1 << self.OpenParen) | (1 << self.OpenBrace) | (1 << self.PlusPlus) | (1 << self.MinusMinus) | (1 << self.Plus) | (1 << self.Minus) | (1 << self.BitNot) | (1 << self.Not) | (1 << self.NullLiteral) | (1 << self.BooleanLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.New - 64)) | (1 << (self.Void - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.Delete - 64)) | (1 << (self.Identifier - 64)) | (1 << (self.StringLiteral - 64)))) != 0):
                self.state = 409 
                self.argumentList()


            self.state = 412
            self.match(self.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = ECMAScriptParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414 
            self.singleExpression(0)
            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.Comma:
                self.state = 415
                self.match(self.Comma)
                self.state = 416 
                self.singleExpression(0)
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionSequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_expressionSequence

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterExpressionSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitExpressionSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitExpressionSequence(self)
            else:
                return visitor.visitChildren(self)




    def expressionSequence(self):

        localctx = ECMAScriptParser.ExpressionSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expressionSequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422 
            self.singleExpression(0)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 423
                    self.match(self.Comma)
                    self.state = 424 
                    self.singleExpression(0) 
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SingleExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_singleExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParenthesizedExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitParenthesizedExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitParenthesizedExpression(self)
            else:
                return visitor.visitChildren(self)


    class TernaryExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitTernaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitTernaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class ObjectLiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def objectLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.ObjectLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterObjectLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitObjectLiteralExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitObjectLiteralExpression(self)
            else:
                return visitor.visitChildren(self)


    class NewExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def New(self):
            return self.getToken(ECMAScriptParser.New, 0)
        def arguments(self):
            return self.getTypedRuleContext(ECMAScriptParser.ArgumentsContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterNewExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitNewExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitNewExpression(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(ECMAScriptParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitLiteralExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitLiteralExpression(self)
            else:
                return visitor.visitChildren(self)


    class ArrayLiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrayLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.ArrayLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterArrayLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitArrayLiteralExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitArrayLiteralExpression(self)
            else:
                return visitor.visitChildren(self)


    class MemberDotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifierName(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierNameContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterMemberDotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitMemberDotExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitMemberDotExpression(self)
            else:
                return visitor.visitChildren(self)


    class UnaryExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def Delete(self):
            return self.getToken(ECMAScriptParser.Delete, 0)
        def Void(self):
            return self.getToken(ECMAScriptParser.Void, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def Typeof(self):
            return self.getToken(ECMAScriptParser.Typeof, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class MemberIndexExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterMemberIndexExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitMemberIndexExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitMemberIndexExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitIdentifierExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitIdentifierExpression(self)
            else:
                return visitor.visitChildren(self)


    class ArgumentsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def arguments(self):
            return self.getTypedRuleContext(ECMAScriptParser.ArgumentsContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterArgumentsExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitArgumentsExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitArgumentsExpression(self)
            else:
                return visitor.visitChildren(self)


    class ThisExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def This(self):
            return self.getToken(ECMAScriptParser.This, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterThisExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitThisExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitThisExpression(self)
            else:
                return visitor.visitChildren(self)


    class FunctionExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)
        def formalParameterList(self):
            return self.getTypedRuleContext(ECMAScriptParser.FormalParameterListContext,0)

        def functionBody(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionBodyContext,0)

        def Function(self):
            return self.getToken(ECMAScriptParser.Function, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFunctionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFunctionExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitFunctionExpression(self)
            else:
                return visitor.visitChildren(self)


    class BinaryExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def Instanceof(self):
            return self.getToken(ECMAScriptParser.Instanceof, 0)
        def In(self):
            return self.getToken(ECMAScriptParser.In, 0)
        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterBinaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitBinaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitBinaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentOperatorExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)
        def identifierName(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierNameContext,0)

        def assignmentOperator(self):
            return self.getTypedRuleContext(ECMAScriptParser.AssignmentOperatorContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def expressionSequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterAssignmentOperatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitAssignmentOperatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitAssignmentOperatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class PostUnaryAssignmentExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)
        def incrementOperator(self):
            return self.getTypedRuleContext(ECMAScriptParser.IncrementOperatorContext,0)

        def identifierName(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierNameContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPostUnaryAssignmentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPostUnaryAssignmentExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitPostUnaryAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)


    class UnaryAssignmentExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ECMAScriptParser.SingleExpressionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def incrementOperator(self):
            return self.getTypedRuleContext(ECMAScriptParser.IncrementOperatorContext,0)

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)
        def identifierName(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierNameContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterUnaryAssignmentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitUnaryAssignmentExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitUnaryAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)



    def singleExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ECMAScriptParser.SingleExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_singleExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.UnaryExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 431
                self.match(self.Delete)
                self.state = 432 
                self.singleExpression(29)
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.UnaryExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 433
                self.match(self.Void)
                self.state = 434 
                self.singleExpression(28)
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.UnaryExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 435
                self.match(self.Typeof)
                self.state = 436 
                self.singleExpression(27)
                pass

            elif la_ == 4:
                localctx = ECMAScriptParser.UnaryExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 437
                self.match(self.Plus)
                self.state = 438 
                self.singleExpression(23)
                pass

            elif la_ == 5:
                localctx = ECMAScriptParser.UnaryExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 439
                self.match(self.Minus)
                self.state = 440 
                self.singleExpression(22)
                pass

            elif la_ == 6:
                localctx = ECMAScriptParser.UnaryExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 441
                self.match(self.BitNot)
                self.state = 442 
                self.singleExpression(21)
                pass

            elif la_ == 7:
                localctx = ECMAScriptParser.UnaryExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 443
                self.match(self.Not)
                self.state = 444 
                self.singleExpression(20)
                pass

            elif la_ == 8:
                localctx = ECMAScriptParser.FunctionExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 445
                self.match(self.Function)
                self.state = 447
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.Identifier:
                    self.state = 446
                    self.match(self.Identifier)


                self.state = 449
                self.match(self.OpenParen)
                self.state = 451
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.Identifier:
                    self.state = 450 
                    self.formalParameterList()


                self.state = 453
                self.match(self.CloseParen)
                self.state = 454
                self.match(self.OpenBrace)
                self.state = 455 
                self.functionBody()
                self.state = 456
                self.match(self.CloseBrace)
                pass

            elif la_ == 9:
                localctx = ECMAScriptParser.NewExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 458
                self.match(self.New)
                self.state = 459 
                self.singleExpression(0)
                self.state = 460 
                self.arguments()
                pass

            elif la_ == 10:
                localctx = ECMAScriptParser.PostUnaryAssignmentExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 462
                self.match(self.Identifier)
                self.state = 463
                if not (not self.here(ECMAScriptParser.LineTerminator)):
                    raise FailedPredicateException(self, "(not self.here(ECMAScriptParser.LineTerminator))")
                self.state = 464 
                self.incrementOperator()
                pass

            elif la_ == 11:
                localctx = ECMAScriptParser.UnaryAssignmentExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 465 
                self.incrementOperator()
                self.state = 466
                self.match(self.Identifier)
                pass

            elif la_ == 12:
                localctx = ECMAScriptParser.UnaryAssignmentExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 468 
                self.incrementOperator()
                self.state = 469 
                self.singleExpression(0)
                self.state = 470
                self.match(self.Dot)
                self.state = 471 
                self.identifierName()
                pass

            elif la_ == 13:
                localctx = ECMAScriptParser.UnaryAssignmentExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 473 
                self.incrementOperator()
                self.state = 474 
                self.singleExpression(0)
                self.state = 475
                self.match(self.OpenBracket)
                self.state = 476 
                self.expressionSequence()
                self.state = 477
                self.match(self.CloseBracket)
                pass

            elif la_ == 14:
                localctx = ECMAScriptParser.AssignmentOperatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 479
                self.match(self.Identifier)
                self.state = 480 
                self.assignmentOperator()
                self.state = 481 
                self.expressionSequence()
                pass

            elif la_ == 15:
                localctx = ECMAScriptParser.ThisExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 483
                self.match(self.This)
                pass

            elif la_ == 16:
                localctx = ECMAScriptParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 484
                self.match(self.Identifier)
                pass

            elif la_ == 17:
                localctx = ECMAScriptParser.LiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 485 
                self.literal()
                pass

            elif la_ == 18:
                localctx = ECMAScriptParser.ArrayLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 486 
                self.arrayLiteral()
                pass

            elif la_ == 19:
                localctx = ECMAScriptParser.ObjectLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 487 
                self.objectLiteral()
                pass

            elif la_ == 20:
                localctx = ECMAScriptParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 488
                self.match(self.OpenParen)
                self.state = 489 
                self.expressionSequence()
                self.state = 490
                self.match(self.CloseParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 565
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 563
                    la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                    if la_ == 1:
                        localctx = ECMAScriptParser.BinaryExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 494
                        if not self.precpred(self._ctx, 19):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 495
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.Multiply) | (1 << self.Divide) | (1 << self.Modulus))) != 0)):
                            self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 496 
                        self.singleExpression(20)
                        pass

                    elif la_ == 2:
                        localctx = ECMAScriptParser.BinaryExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 497
                        if not self.precpred(self._ctx, 18):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 498
                        _la = self._input.LA(1)
                        if not(_la==ECMAScriptParser.Plus or _la==ECMAScriptParser.Minus):
                            self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 499 
                        self.singleExpression(19)
                        pass

                    elif la_ == 3:
                        localctx = ECMAScriptParser.BinaryExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 500
                        if not self.precpred(self._ctx, 17):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 501
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RightShiftArithmetic) | (1 << self.LeftShiftArithmetic) | (1 << self.RightShiftLogical))) != 0)):
                            self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 502 
                        self.singleExpression(18)
                        pass

                    elif la_ == 4:
                        localctx = ECMAScriptParser.BinaryExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 503
                        if not self.precpred(self._ctx, 16):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 504
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.LessThan) | (1 << self.MoreThan) | (1 << self.LessThanEquals) | (1 << self.GreaterThanEquals))) != 0)):
                            self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 505 
                        self.singleExpression(17)
                        pass

                    elif la_ == 5:
                        localctx = ECMAScriptParser.BinaryExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 506
                        if not self.precpred(self._ctx, 15):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 507
                        self.match(self.Instanceof)
                        self.state = 508 
                        self.singleExpression(16)
                        pass

                    elif la_ == 6:
                        localctx = ECMAScriptParser.BinaryExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 509
                        if not self.precpred(self._ctx, 14):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 510
                        self.match(self.In)
                        self.state = 511 
                        self.singleExpression(15)
                        pass

                    elif la_ == 7:
                        localctx = ECMAScriptParser.BinaryExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 512
                        if not self.precpred(self._ctx, 13):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 513
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.Equals) | (1 << self.NotEquals) | (1 << self.IdentityEquals) | (1 << self.IdentityNotEquals))) != 0)):
                            self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 514 
                        self.singleExpression(14)
                        pass

                    elif la_ == 8:
                        localctx = ECMAScriptParser.BinaryExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 515
                        if not self.precpred(self._ctx, 12):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 516
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.BitAnd) | (1 << self.BitXOr) | (1 << self.BitOr))) != 0)):
                            self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 517 
                        self.singleExpression(13)
                        pass

                    elif la_ == 9:
                        localctx = ECMAScriptParser.BinaryExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 518
                        if not self.precpred(self._ctx, 11):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 519
                        _la = self._input.LA(1)
                        if not(_la==ECMAScriptParser.And or _la==ECMAScriptParser.Or):
                            self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 520 
                        self.singleExpression(12)
                        pass

                    elif la_ == 10:
                        localctx = ECMAScriptParser.TernaryExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 521
                        if not self.precpred(self._ctx, 10):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 522
                        self.match(self.QuestionMark)
                        self.state = 523 
                        self.singleExpression(0)
                        self.state = 524
                        self.match(self.Colon)
                        self.state = 525 
                        self.singleExpression(11)
                        pass

                    elif la_ == 11:
                        localctx = ECMAScriptParser.MemberIndexExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 527
                        if not self.precpred(self._ctx, 36):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 36)")
                        self.state = 528
                        self.match(self.OpenBracket)
                        self.state = 529 
                        self.expressionSequence()
                        self.state = 530
                        self.match(self.CloseBracket)
                        pass

                    elif la_ == 12:
                        localctx = ECMAScriptParser.MemberDotExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 532
                        if not self.precpred(self._ctx, 35):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 35)")
                        self.state = 533
                        self.match(self.Dot)
                        self.state = 534 
                        self.identifierName()
                        pass

                    elif la_ == 13:
                        localctx = ECMAScriptParser.ArgumentsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 535
                        if not self.precpred(self._ctx, 34):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 536 
                        self.arguments()
                        pass

                    elif la_ == 14:
                        localctx = ECMAScriptParser.PostUnaryAssignmentExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 537
                        if not self.precpred(self._ctx, 31):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 538
                        self.match(self.Dot)
                        self.state = 539 
                        self.identifierName()
                        self.state = 540
                        if not (not self.here(ECMAScriptParser.LineTerminator)):
                            raise FailedPredicateException(self, "(not self.here(ECMAScriptParser.LineTerminator))")
                        self.state = 541 
                        self.incrementOperator()
                        pass

                    elif la_ == 15:
                        localctx = ECMAScriptParser.PostUnaryAssignmentExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 543
                        if not self.precpred(self._ctx, 30):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 544
                        self.match(self.OpenBracket)
                        self.state = 545 
                        self.expressionSequence()
                        self.state = 546
                        self.match(self.CloseBracket)
                        self.state = 547
                        if not (not self.here(ECMAScriptParser.LineTerminator)):
                            raise FailedPredicateException(self, "(not self.here(ECMAScriptParser.LineTerminator))")
                        self.state = 548 
                        self.incrementOperator()
                        pass

                    elif la_ == 16:
                        localctx = ECMAScriptParser.AssignmentOperatorExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 550
                        if not self.precpred(self._ctx, 8):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 551
                        self.match(self.Dot)
                        self.state = 552 
                        self.identifierName()
                        self.state = 553 
                        self.assignmentOperator()
                        self.state = 554 
                        self.expressionSequence()
                        pass

                    elif la_ == 17:
                        localctx = ECMAScriptParser.AssignmentOperatorExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 556
                        if not self.precpred(self._ctx, 7):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 557
                        self.match(self.OpenBracket)
                        self.state = 558 
                        self.expressionSequence()
                        self.state = 559
                        self.match(self.CloseBracket)
                        self.state = 560 
                        self.assignmentOperator()
                        self.state = 561 
                        self.expressionSequence()
                        pass

             
                self.state = 567
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class IncrementOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_incrementOperator

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterIncrementOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitIncrementOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitIncrementOperator(self)
            else:
                return visitor.visitChildren(self)




    def incrementOperator(self):

        localctx = ECMAScriptParser.IncrementOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_incrementOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            _la = self._input.LA(1)
            if not(_la==ECMAScriptParser.PlusPlus or _la==ECMAScriptParser.MinusMinus):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitAssignmentOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = ECMAScriptParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.Assign) | (1 << self.MultiplyAssign) | (1 << self.DivideAssign) | (1 << self.ModulusAssign) | (1 << self.PlusAssign) | (1 << self.MinusAssign) | (1 << self.LeftShiftArithmeticAssign) | (1 << self.RightShiftArithmeticAssign) | (1 << self.RightShiftLogicalAssign) | (1 << self.BitAndAssign) | (1 << self.BitXorAssign) | (1 << self.BitOrAssign))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.NumericLiteralContext,0)


        def StringLiteral(self):
            return self.getToken(ECMAScriptParser.StringLiteral, 0)

        def NullLiteral(self):
            return self.getToken(ECMAScriptParser.NullLiteral, 0)

        def RegularExpressionLiteral(self):
            return self.getToken(ECMAScriptParser.RegularExpressionLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(ECMAScriptParser.BooleanLiteral, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ECMAScriptParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.state = 574
            token = self._input.LA(1)
            if token in [self.RegularExpressionLiteral, self.NullLiteral, self.BooleanLiteral, self.StringLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 572
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.RegularExpressionLiteral) | (1 << self.NullLiteral) | (1 << self.BooleanLiteral))) != 0) or _la==ECMAScriptParser.StringLiteral):
                    self._errHandler.recoverInline(self)
                self.consume()

            elif token in [self.DecimalLiteral, self.HexIntegerLiteral, self.OctalIntegerLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 573 
                self.numericLiteral()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DecimalLiteral(self):
            return self.getToken(ECMAScriptParser.DecimalLiteral, 0)

        def OctalIntegerLiteral(self):
            return self.getToken(ECMAScriptParser.OctalIntegerLiteral, 0)

        def HexIntegerLiteral(self):
            return self.getToken(ECMAScriptParser.HexIntegerLiteral, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_numericLiteral

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterNumericLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitNumericLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitNumericLiteral(self)
            else:
                return visitor.visitChildren(self)




    def numericLiteral(self):

        localctx = ECMAScriptParser.NumericLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_numericLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ECMAScriptParser.Identifier, 0)

        def reservedWord(self):
            return self.getTypedRuleContext(ECMAScriptParser.ReservedWordContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_identifierName

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterIdentifierName(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitIdentifierName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitIdentifierName(self)
            else:
                return visitor.visitChildren(self)




    def identifierName(self):

        localctx = ECMAScriptParser.IdentifierNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_identifierName)
        try:
            self.state = 580
            token = self._input.LA(1)
            if token in [self.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 578
                self.match(self.Identifier)

            elif token in [self.NullLiteral, self.BooleanLiteral, self.Break, self.Do, self.Instanceof, self.Typeof, self.Case, self.Else, self.New, self.Var, self.Catch, self.Finally, self.Return, self.Void, self.Continue, self.For, self.Switch, self.While, self.Debugger, self.Function, self.This, self.With, self.Default, self.If, self.Throw, self.Delete, self.In, self.Try, self.Class, self.Enum, self.Extends, self.Super, self.Const, self.Export, self.Import, self.Implements, self.Let, self.Private, self.Public, self.Interface, self.Package, self.Protected, self.Static, self.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 579 
                self.reservedWord()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReservedWordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def futureReservedWord(self):
            return self.getTypedRuleContext(ECMAScriptParser.FutureReservedWordContext,0)


        def keyword(self):
            return self.getTypedRuleContext(ECMAScriptParser.KeywordContext,0)


        def NullLiteral(self):
            return self.getToken(ECMAScriptParser.NullLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(ECMAScriptParser.BooleanLiteral, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_reservedWord

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterReservedWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitReservedWord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitReservedWord(self)
            else:
                return visitor.visitChildren(self)




    def reservedWord(self):

        localctx = ECMAScriptParser.ReservedWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_reservedWord)
        self._la = 0 # Token type
        try:
            self.state = 585
            token = self._input.LA(1)
            if token in [self.Break, self.Do, self.Instanceof, self.Typeof, self.Case, self.Else, self.New, self.Var, self.Catch, self.Finally, self.Return, self.Void, self.Continue, self.For, self.Switch, self.While, self.Debugger, self.Function, self.This, self.With, self.Default, self.If, self.Throw, self.Delete, self.In, self.Try]:
                self.enterOuterAlt(localctx, 1)
                self.state = 582 
                self.keyword()

            elif token in [self.Class, self.Enum, self.Extends, self.Super, self.Const, self.Export, self.Import, self.Implements, self.Let, self.Private, self.Public, self.Interface, self.Package, self.Protected, self.Static, self.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 583 
                self.futureReservedWord()

            elif token in [self.NullLiteral, self.BooleanLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 584
                _la = self._input.LA(1)
                if not(_la==ECMAScriptParser.NullLiteral or _la==ECMAScriptParser.BooleanLiteral):
                    self._errHandler.recoverInline(self)
                self.consume()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeywordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Catch(self):
            return self.getToken(ECMAScriptParser.Catch, 0)

        def Throw(self):
            return self.getToken(ECMAScriptParser.Throw, 0)

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)

        def While(self):
            return self.getToken(ECMAScriptParser.While, 0)

        def Continue(self):
            return self.getToken(ECMAScriptParser.Continue, 0)

        def Instanceof(self):
            return self.getToken(ECMAScriptParser.Instanceof, 0)

        def This(self):
            return self.getToken(ECMAScriptParser.This, 0)

        def Void(self):
            return self.getToken(ECMAScriptParser.Void, 0)

        def Try(self):
            return self.getToken(ECMAScriptParser.Try, 0)

        def Finally(self):
            return self.getToken(ECMAScriptParser.Finally, 0)

        def Return(self):
            return self.getToken(ECMAScriptParser.Return, 0)

        def If(self):
            return self.getToken(ECMAScriptParser.If, 0)

        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)

        def Switch(self):
            return self.getToken(ECMAScriptParser.Switch, 0)

        def Do(self):
            return self.getToken(ECMAScriptParser.Do, 0)

        def Default(self):
            return self.getToken(ECMAScriptParser.Default, 0)

        def Delete(self):
            return self.getToken(ECMAScriptParser.Delete, 0)

        def New(self):
            return self.getToken(ECMAScriptParser.New, 0)

        def In(self):
            return self.getToken(ECMAScriptParser.In, 0)

        def Else(self):
            return self.getToken(ECMAScriptParser.Else, 0)

        def Debugger(self):
            return self.getToken(ECMAScriptParser.Debugger, 0)

        def Typeof(self):
            return self.getToken(ECMAScriptParser.Typeof, 0)

        def Break(self):
            return self.getToken(ECMAScriptParser.Break, 0)

        def With(self):
            return self.getToken(ECMAScriptParser.With, 0)

        def Function(self):
            return self.getToken(ECMAScriptParser.Function, 0)

        def Case(self):
            return self.getToken(ECMAScriptParser.Case, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_keyword

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitKeyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitKeyword(self)
            else:
                return visitor.visitChildren(self)




    def keyword(self):

        localctx = ECMAScriptParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            _la = self._input.LA(1)
            if not(((((_la - 58)) & ~0x3f) == 0 and ((1 << (_la - 58)) & ((1 << (self.Break - 58)) | (1 << (self.Do - 58)) | (1 << (self.Instanceof - 58)) | (1 << (self.Typeof - 58)) | (1 << (self.Case - 58)) | (1 << (self.Else - 58)) | (1 << (self.New - 58)) | (1 << (self.Var - 58)) | (1 << (self.Catch - 58)) | (1 << (self.Finally - 58)) | (1 << (self.Return - 58)) | (1 << (self.Void - 58)) | (1 << (self.Continue - 58)) | (1 << (self.For - 58)) | (1 << (self.Switch - 58)) | (1 << (self.While - 58)) | (1 << (self.Debugger - 58)) | (1 << (self.Function - 58)) | (1 << (self.This - 58)) | (1 << (self.With - 58)) | (1 << (self.Default - 58)) | (1 << (self.If - 58)) | (1 << (self.Throw - 58)) | (1 << (self.Delete - 58)) | (1 << (self.In - 58)) | (1 << (self.Try - 58)))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FutureReservedWordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Implements(self):
            return self.getToken(ECMAScriptParser.Implements, 0)

        def Protected(self):
            return self.getToken(ECMAScriptParser.Protected, 0)

        def Let(self):
            return self.getToken(ECMAScriptParser.Let, 0)

        def Private(self):
            return self.getToken(ECMAScriptParser.Private, 0)

        def Class(self):
            return self.getToken(ECMAScriptParser.Class, 0)

        def Static(self):
            return self.getToken(ECMAScriptParser.Static, 0)

        def Const(self):
            return self.getToken(ECMAScriptParser.Const, 0)

        def Super(self):
            return self.getToken(ECMAScriptParser.Super, 0)

        def Import(self):
            return self.getToken(ECMAScriptParser.Import, 0)

        def Enum(self):
            return self.getToken(ECMAScriptParser.Enum, 0)

        def Extends(self):
            return self.getToken(ECMAScriptParser.Extends, 0)

        def Public(self):
            return self.getToken(ECMAScriptParser.Public, 0)

        def Yield(self):
            return self.getToken(ECMAScriptParser.Yield, 0)

        def Export(self):
            return self.getToken(ECMAScriptParser.Export, 0)

        def Package(self):
            return self.getToken(ECMAScriptParser.Package, 0)

        def Interface(self):
            return self.getToken(ECMAScriptParser.Interface, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_futureReservedWord

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFutureReservedWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFutureReservedWord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitFutureReservedWord(self)
            else:
                return visitor.visitChildren(self)




    def futureReservedWord(self):

        localctx = ECMAScriptParser.FutureReservedWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_futureReservedWord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            _la = self._input.LA(1)
            if not(((((_la - 84)) & ~0x3f) == 0 and ((1 << (_la - 84)) & ((1 << (self.Class - 84)) | (1 << (self.Enum - 84)) | (1 << (self.Extends - 84)) | (1 << (self.Super - 84)) | (1 << (self.Const - 84)) | (1 << (self.Export - 84)) | (1 << (self.Import - 84)) | (1 << (self.Implements - 84)) | (1 << (self.Let - 84)) | (1 << (self.Private - 84)) | (1 << (self.Public - 84)) | (1 << (self.Interface - 84)) | (1 << (self.Package - 84)) | (1 << (self.Protected - 84)) | (1 << (self.Static - 84)) | (1 << (self.Yield - 84)))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ECMAScriptParser.EOF, 0)

        def SemiColon(self):
            return self.getToken(ECMAScriptParser.SemiColon, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_eos

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterEos(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitEos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitEos(self)
            else:
                return visitor.visitChildren(self)




    def eos(self):

        localctx = ECMAScriptParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_eos)
        try:
            self.state = 595
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 591
                self.match(self.SemiColon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 592
                self.match(self.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 593
                if not self.lineTerminatorAhead():
                    raise FailedPredicateException(self, "self.lineTerminatorAhead()")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 594
                if not self._input.LT(1).type == self.CloseBrace:
                    raise FailedPredicateException(self, "self._input.LT(1).type == self.CloseBrace")
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EofContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ECMAScriptParser.EOF, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_eof

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterEof(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitEof(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECMAScriptVisitor ):
                return visitor.visitEof(self)
            else:
                return visitor.visitChildren(self)




    def eof(self):

        localctx = ECMAScriptParser.EofContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_eof)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.match(self.EOF)
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
        self._predicates[38] = self.singleExpression_sempred
        self._predicates[47] = self.eos_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def singleExpression_sempred(self, localctx:SingleExpressionContext, predIndex:int):
            if predIndex == 0:
                return (not self.here(ECMAScriptParser.LineTerminator))
         

            if predIndex == 1:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 36)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 35)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 34)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 15:
                return (not self.here(ECMAScriptParser.LineTerminator))
         

            if predIndex == 16:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 17:
                return (not self.here(ECMAScriptParser.LineTerminator))
         

            if predIndex == 18:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 7)
         

    def eos_sempred(self, localctx:EosContext, predIndex:int):
            if predIndex == 20:
                return self.lineTerminatorAhead()
         

            if predIndex == 21:
                return self._input.LT(1).type == self.CloseBrace
         



