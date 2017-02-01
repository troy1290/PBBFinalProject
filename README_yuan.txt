=======Reformat the soap output file==========

#orignal file: bsanew-soap-out.txt.

step one:
delete the first three columns by regular expression in Jedit
search term: 
replacement term:

infile:bsanew-soap-out.txt
output file:bsanew-soap-out-1.txt

stop two:

every three columns as a unit(clone name-tagNO, scafold, position), and start a new line;

use python regular expresssion to reforamt

code(bsanew-soap-out1.py):
#!/usr/bin/env python
import re
def rep():
        InFileName = "bsanew-soap-out-1.txt"
        InFile = open(InFileName, 'r')
        Outfile = open(InFileName[0:-4] + "regular.txt", "w")
        for Line in InFile:
                pattern = '\w+\-(\w+\-)\d\-([A-Z]\d*)([A-Z]\d*)(\-\d)(\t[a-z]*\d+\t\d+\t)'
                substitute = '\\1\\3\\2\\4\\5\\n'
                formatted_line = re.sub(pattern, substitute, Line)
                print formatted_line
                Outfile.write(formatted_line)
               
        InFile.close()
rep()

infile:bsanew-soap-out-1.txt
output:bsanew-soap-out-1regular.txt

some emmpty lines in output bsanew-soap-out-1regular.txt file which produced by last python code
when the line only has a single unit, after repalce "\n", there is a new single line

step three: 
delete empty lines

code(bsanew-soap-out-del.py):
#!/usr/bin/env python

InFileName="bsanew-soap-out-1regular.txt"
InFile=open(InFileName,'r')
Outfile=open(InFileName[0:-4] + "del.txt", "w")
for Line in InFlie:
        if Line=="\n":
                continue
        print Line
        Outfile.write(Line)
InFile.close()

infile:bsanew-soap-out-1regular.txt
output:bsanew-soap-out-1regulardel.txt

step four:

in file "bsanew-soap-out-1regulardel.txt", the first column bsaNo.+PNo. can determine the colony from which palte. 
According to the fosmid form repalce the bsaNO.+Pno. with the plate No.

fosmid.xls
	P1	P2	P3	P4	P5	P6	P7	P8	P9	P10	P11	P12	P13	P14	P15	P16
Bsa4	P1001	P1002	P1003	P1004												
Bsa8	P105	P106	P107	P108	P109	P110	P111	P112								
Bsa12	P113	P114	P115	P116	P117	P118	P119	P120	P9	P10	P11	P12	 	 		
																
Bsa16	P121	P122	P123	P124	P125	P126	P127	P128	P129	P130	P131	P132	P133	P134	P135	P136
																

make a dictionary, bsaNo. + PNo. as the key, the Pxx as the value.
write python code():

#!/usr/bin/env python
import re
def rep():
    InFileName = "bsanew-soap-out-1regulardel.txt"
    outfile = open(InFileName[0:-4] + "-repl.txt", "w")
    FosmidDict = {
'bsa4P1':'P1001','bsa4P2':'P1002','bsa4P3':'P1003','bsa4P4':'P1004','bsa8P1':'P105','bsa8P2':'P106','bsa8P3':'P107', 'bsa8P4':'P108', \
'bsa8P5':'P109', 'bsa8P6':'P110', 'bsa8P7':'P111', 'bsa8P8':'P112', 'bsa12P1':'P113', 'bsa12P2':'P114', 'bsa12P3':'P115', 'bsa12P4':'\
P116', 'bsa12P5':'P117', 'bsa12P6':'P118', 'bsa12P7':'P119', 'bsa12P8':'P120', 'bsa12P9':'P9', 'bsa12P10':'P10', 'bsa12P11':'P11',\
 'bsa12P12':'P12', 'bsa16P1':'P121', 'bsa16P2':'P122', 'bsa16P3':'P123', 'bsa16P4':'P124', 'bsa16P5':'P125', 'bsa16P6':'P126', 'bsa16P7':'P127',
 'bsa16P8':'P128', 'bsa16P9':'P129', 'bsa16P10':'P130', 'bsa16P11':'P131', 'bsa16P12':'P132', 'bsa16P13':'P133', 'bsa16P14':'P134','bsa16P15':'P135','bsa16P16':'P136'}
    keylist = FosmidDict.keys()
    with open(InFileName, 'r') as f:
        for line in f:
            printed = False
            for key in keylist:
                if (key) == line[0:(len(key))]:
                    linesplit = line.split("\t")
                    linesplit[0] = FosmidDict[key] + linesplit[0][len(key):]
                    outfile.write("\t".join(linesplit))
                    printed = True


rep()

infile:bsanew-soap-out-1regulardel.txt
output:bsanew-soap-out-1regulardel-repl.txt

step five:

in the bsanew-soap-out-1regulardel-repl.txt, '\-\d'of the first column is the the tag No, delete the tag No, and combine the same colony in the same line

a,delete the tag No.
code(dele--.py): 
#!/usr/bin/env python
import re
Infilename='bsanew-soap-out-1regulardel-repl.txt'
Infile=open(Infilename,'r')
Outfile=open('BSAsamplied.txt','w')
for line in Infile:
        pattern='(\w+)\-\d*(.*)'
        substitute='\\1\\2'
        BSA=re.sub(pattern,substitute,line)
        Outfile.write(BSA)
Infile.close()
 
infile:bsanew-soap-out-1regulardel-repl.txt
output:BSAsamplied.txt

sort the BSAsamplied.txt (command: sort BSAsamplied.txt ) to get BSAsamplied2.txt

b,Combine the same colony and scaffold number,

code(BSAsamplied1.py):

#!/usr/bin/env python
Infilename='BSAsamplied2.txt'
File=open(Infilename,'r')
Output=open('BSAsamplied3.txt','w')

Firstline=File.readline()
Prev_conent=Firstline.split("\t")
Prev_conent = Prev_conent[0:-1]

for Line in File:
        content=Line.split("\t")
        if Prev_conent[0]==content[0]:
                Prev_conent.append(content[2])
        else:
                text = "\t".join(Prev_conent)
                Output.write(text + "\n")
                Prev_conent=content[0:-1]
Output.write(text)
 
infile:BSAsamplied2.txt
output:BSAsamplied3.txt

c,sort the position from low number to large number 

code(sort.py):

!/usr/bin/env python
Infilename='BSAsamplied3.txt'
File=open(Infilename,'r')
Output=open('BSAsamplied4.txt','w')

for Line in File:
        Line = Line.replace("\n","")
        content=Line.split("\t")
        for index in range(2,len(content)):
                content[index] = int(content[index])
        content[2:] = sorted(content[2:])
        #text="\t".join(content)
        for sorted_content in content:
                Output.write(str(sorted_content))
                if sorted_content != content[-1]:
                        Output.write("\t")
                else:
                        Output.write("\n")
        #print text
        #Output.write(text)

Output.close()
File.close()

infile:BSAsamplied3.txt
outfile:BSAsamplied4.txt

d,
keep the lowest(third column) and the largest number(last column)

Search : ^(\w+\s\w+\s\w+).*(\s\w+)$
Replace: $1$2

e, delete the single poistion line 

^(\w+\s\w+\s\w+)\n

Replace :


final output:TEST_BSAsimplified.txt

