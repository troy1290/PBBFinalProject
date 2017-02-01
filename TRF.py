#!/usr/bin/env python
#NAME: XUAN LI & YUAN ZOU
#P NUMBER: P277920 & P275022
#DATE: 20170126

#Python 2.7.6

import re     #load regular expression module

#the following part of the script is aiming for reformating the TRF output file
InFileName="TEST_TRFoutput.txt"     #set input file name

OutFileName="TRFreformatted.txt"     #set output file name

WriteOutFile=True     #give the option to write to a file or just print to screen

InFile=open(InFileName,'r')     #open the input file for reading

Headstring='''ScaffoldNum	StartPos	EndPos	TRNum	TRSize	CopyNum	TRLength'''     #set the header for the output file

if WriteOutFile:
  OutFile=open(OutFileName,'w')
  OutFile.write(Headstring)
else:
  print Headstring

LineNumber=0     #initialize the counter used to keep track of line number

for Line in InFile:     #loop through each line in the file

  if LineNumber > 0:     #to skip the header line
    Line=Line.strip('\n')     #get rid of the carriage returen at the end of each line
    ElementList=Line.split('\t')     #split the line into different elements using \t as delimiter
    Scaffold=ElementList[0]
    Start=int(ElementList[3])
    End=int(ElementList[4])
    Number=ElementList[8]
    Size=int(ElementList[9])
    Copy=ElementList[10]
    Length=int(End-Start)
    ChangedLine='''
%s	%d	%d	%s	%d	%s	%d'''%(Scaffold,Start,End,Number,Size,Copy,Length)     #change the format of the line

    if WriteOutFile:
      OutFile.write(ChangedLine)     #write refoematted line into the out put file
    else:
      print PlaceLine

  LineNumber += 1

InFile.close()
if WriteOutFile:
  print "Reformatted",LineNumber,"records from",InFileName,"as",OutFileName     #print changing information on the screen
  OutFile.close()

#the following part of the script is aiming for removing the redundant items
InFileName2="TRFreformatted.txt"

OutFileName2="TRFsimplified.txt"

InFile2=open(InFileName2,'r')

OutFile2=open(OutFileName2,'w')

Headstring='''ScaffoldNum	StartPos	EndPos	TRNum	TRSize	CopyNum	TRLength
'''     #set the header for the output file

OutFile2.write(Headstring)

LineNumber2=0

BufferedLine=str(InFile2.readlines()[1])

InFile2.close()
InFile2=open(InFileName2,'r')     #close the input file and open it again for the "for loop" to read

for Line2 in InFile2:

  if LineNumber2>0:
    ElementList2=Line2.split('\t')     #to split Line2 and BufferedLine to extract saffold number, start position and end position
    Scaffold2=str(ElementList2[0])
    Start2=int(ElementList2[1])
    End2=int(ElementList2[2])
    ElementList3=BufferedLine.split('\t')
    Scaffold3=str(ElementList3[0])
    Start3=int(ElementList3[1])
    End3=int(ElementList3[2])

    if Scaffold2==Scaffold3:     #when comparaing the BufferedLine and the newly read line when one is including in the other
      if Start2==Start3:     #meaning in the same scaffold and positioning on the same parts then wirte newly read line into 
        if End2>=End3:     #BufferedLine and go to the next loop otherwise output the BufferedLine
          BufferedLine=Line2
        else:
          BufferedLine=BufferedLine
      else:
        OutFile2.write(BufferedLine)
        BufferedLine=Line2
    else:
      BufferedLine=Line2
      OutFile2.write(BufferedLine)

  LineNumber2+=1

InFile2.close()
if WriteOutFile:
  print "Repetitive items are removed, records from",InFileName2,"are saved in",OutFileName2
  OutFile2.close()

#the following part of the script is aiming for print general information on the screen
InFileName3="TRFsimplified.txt"

InFile3=open(InFileName3,'r')

LineNumber3=0

SSR=0

VNTR=0

satelliteDNA=0

TotalLength=0

for Line3 in InFile3:

  if LineNumber3>0:
    ElementList3=Line3.split('\t')     #to split Line3 to extract period size
    Size3=int(ElementList3[4])
    Length3=int(ElementList3[6])
    if Size3>65:
      satelliteDNA+=1
    else:
      if Size3>15:
        VNTR+=1
      else:
        if Size3<6:
          SSR+=1
    TotalLength+=Length3

  LineNumber3+=1

print "There are",LineNumber3,"tandem repeats in total. Including",SSR," microsatellite DNA;",VNTR," minisatellite DNA;",satelliteDNA,"satellite DNA. The total length of the tandem repeats are",TotalLength,"."

InFile3.close()


















