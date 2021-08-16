"""
File: TexLogger.py
Author: Jackson Bates
Created: 11/7/2019 6:13 PM 
"""

# Set empty to begin, must be set with init_logger()

__REALPRINT = print
__OUTFILE
# maybe a bit of "magic" here with the format() calls being auto run on key check.
# can break if incorrect number of parameters are given for that specific key.

TEX = {
    "Negation":"\\neg {}".format,
    "Conditional":"{} \\rightarrow {}".format,
    "Biconditional":"{} \\leftrightarrow {}".format,
    "Conjunction":"{} \\wedge {}".format,
    "Disjunction":"{} \\vee {}".format
}

print(TEX["Conditional"]("a","b"))

def init_doc(filename):

    __OUTFILE = open(filename,"w")
    __OUTFILE.writelines(["\\documentclass{article}\n",
                          "\\usepackage{geometry}\n",
                          "\\usepackage{amsmath}\n",
                          "\\usepackage{amssymb}\n",
                          "\\begin{document}\n"])

def tex(msg):
    __OUTFILE.write(msg+"\n")

def end_doc():
    __OUTFILE.write("\\end{document}")
    __OUTFILE.close()


init_doc("test.tex")
tex(TEX["Conditional"]("a","b"))
tex(TEX["Negation"]("({})".format(TEX["Disjunction"]("a","b"))))
end_doc()

