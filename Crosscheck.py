#!/usr/bin/env python
#NAME: XUAN LI & YUAN ZOU
#P NUMBER: P277920 & P275022
#DATE: 20170126

#Python 2.7.6

import re

InFileName1="TRFsimplified.txt"

InFileName2="TEST_BSAsimplified.txt"

OutFileName="TRF-BSAcrosschecked.txt"

InFile1=open(InFileName1,'r')

OutFile=open(OutFileName,'w')

LineNumber1=0

LineNumber2=0

Headstring='''CloneNum	ScaffoldNum	CStart	CEnd	TRNum	TRStart	TREnd	TRLength'''

OutFile.write(Headstring)     #add new header

for Line1 in InFile1:     #read simplified file line by line

  if LineNumber1>0:     #extract elements from the line for further compraison
    Line1=Line1.strip('\n')
    ElementList1=Line1.split('\t')
    Scaffold1=ElementList1[0]
    Start1=int(ElementList1[1])
    End1=int(ElementList1[2])
    Number1=ElementList1[3]
    Size1=int(ElementList1[4])
    Copy1=ElementList1[5]
    Length1=int(ElementList1[6])
    List=[]     #built a empty list
    InFile2=open(InFileName2,'r')

    for Line2 in InFile2:     #read bas simplified file line by line and store the line in to the list when it has the same
      if LineNumber2>0:     #scaffold number as the TRF line
        Line2=Line2.strip('\n')
        ElementList2=Line2.split('\t')
        Scaffold2=ElementList2[1]
        Start2=int(ElementList2[2])
        End2=int(ElementList2[3])
        if Scaffold2==Scaffold1:
          List.append(Line2)
          for Item in List:     #go throught the lise and to see whether the TRF position is include in the clone position
            ElementList3=Item.split('\t')
            Clone=ElementList3[0]
            Scaffold3=ElementList3[1]
            Start3=int(ElementList3[2])
            End3=int(ElementList3[3])
            if Start3<=Start1 and End1<=End3:
              JointLine='''
%s	%s	%d	%d	%s	%d	%d	%d''' %(Clone,Scaffold3,Start3,End3,Number1,Start1,End1,Length1)
              OutFile.write(JointLine)     #reformat and joint the lines, write them in to output file

    InFile2.close()

  LineNumber1+=1
  LineNumber2+=1

InFile1.close()
OutFile.close()



















