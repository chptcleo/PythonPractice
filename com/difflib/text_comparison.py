import difflib

text1 = '''text1: line1
           text1: line2
           text1: line3
'''
text1_lines = text1.splitlines()

text2 = '''text2: line1
           text2: line2
           text2:line3
'''
text2_lines = text2.splitlines()

# d = difflib.Differ()
# diff = d.compare(text1_lines, text2_lines)
# print '\n'.join(list(diff))
d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines)
