# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/3 10:20'
import survey
table = survey.Pregnancies()
table.ReadRecords()
print("Number of pregnancies",len(table.records))