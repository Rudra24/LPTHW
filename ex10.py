__author__ = 'rudragouda'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* abc
\t* pqr
\t* xyz\n\t* ABC
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

'''
        ESCAPE	    WHAT IT DOES.

          \\	        Backslash ()
          \'	        Single-quote (')
          \"	        Double-quote (")
          \a	        ASCII bell (BEL)
          \b	        ASCII backspace (BS)
          \f	        ASCII formfeed (FF)
          \n	        ASCII linefeed (LF)
        \N{name}	Character named name in the Unicode database (Unicode only)
        \r ASCII	Carriage Return (CR)
        \t ASCII	Horizontal Tab (TAB)
        \uxxxx	    Character with 16-bit hex value xxxx (Unicode only)
        \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
          \v	        ASCII vertical tab (VT)
         \ooo	    Character with octal value ooo
         \hh	    Character with hex value hh
'''