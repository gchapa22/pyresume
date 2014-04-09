#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, datetime

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def title(s):
	return color.UNDERLINE + color.BOLD + s + color.END


class Element(object):
	def __init__(self,name,where,date_start,date_end):
		self.name = name
		self.where = where
		self.date_start = date_start
		self.date_end = date_end

	def attributes_list(self):
		return self.__dict__.values()

	def printing(self):
		return color.BOLD + self.name + color.END + " " + str(self.date_start) + "-" + str(self.date_end) + "\n" + self.where

class Education(Element):
	pass

class Experience(Element):
	def set_function(self,function):
		self.function = function

	def printing(self):
		return color.BOLD + self.where + color.END + " " + str(self.date_start.year) + "-" + str(self.date_end.year) + "\n" + self.name +": "+ self.function

class Project(Element):
	def set_description(self,description):
		self.description = description
	def printing(self):
		return color.BOLD + self.name + color.END + " " + str(self.date_start.year) + "\n" + self.description


class Event(Element):
	def set_description(self,description):
		self.description = description
	def printing(self):
		return color.BOLD + self.name + color.END + " " + str(self.date_start.year) + "\n" + self.description

def main(argv):
	print argv
	# Change argv list elements to cppercase
	argv = map(lambda x: x.upper(), argv)
	# COVER LETTER
	if "C" in argv or "COVER" in argv or len(argv)==0:
		c_letter=""

	# CONTACT INFO
	if "CI" in argv or "CONTACT INFO" in argv or len(argv)==0:
		contact = {"Name":"Gerardo Chapa Quiroga","email":"gerardo.chapa.q@gmail.com","github":"http://github.com/gchapa22"}
		print title("Contact Information")
		for key,value in contact.iteritems():
			print color.BOLD + key + color.END,":",value 

	# EDUCATION
	if "EDU" in argv or "EDUCATION" in argv or len(argv)==0:
		education_list=[]
		college = Education("Bachelor of Science in Computer Systems Engineering","ITESM",datetime.date(2007, 8, 17),datetime.date(2013, 12, 21))
		lean_bootcamp = Education("Lean Startup Bootcamp","Naranya* Labs",datetime.date(2013, 5, 27),datetime.date(2013, 6, 27))
		education_list.append(college)
		education_list.append(lean_bootcamp)
		print color.UNDERLINE + color.BOLD + "Education" + color.END
		for edu in education_list:
			print edu.printing()

	# WORK EXPERIENCE
	if "EXP" in argv or "WORK EXPERIENCE" in argv or len(argv)==0:
		experience_list = []
		# SICAF
		sicaf = Experience("Database Admin and Software Engineer","SICAF",datetime.date(2011, 11, 1),datetime.date(2012, 7, 20))
		sicaf.set_function("Stored Procedures developer, native Android development, C# web service.")
		# DTI
		dti_se = Experience("Software Engineer","Disitem Tecnologías de Información",datetime.date(2010, 2, 1),datetime.date(2011, 11, 1))
		dti_se.set_function("Development on C#, Visual Basic .NET, Visual Basic 6, web development on Classic ASP, HTML, CSS and javascript.")
		dti_pa = Experience("Process Automation","Disitem Tecnologías de Información",datetime.date(2009, 7, 1),datetime.date(2010, 2, 1))
		dti_pa.set_function("Creating advance MS SQL Server queries for information extraction.")
		dti_di = Experience("Data Internship","Disitem Tecnologías de Información",datetime.date(2008, 7, 1),datetime.date(2009, 7, 1))
		dti_di.set_function("Data capture, and creation of reports from MS SQL Server queries.")
		# Hispanic Teleservices Corp
		htc = Experience("Bilingual Representative","Hispanic Teleservices Corporation",datetime.date(2007, 7, 1),datetime.date(2008, 7, 1))
		htc.set_function("Customer service, to english speaking customers, via telephone.")
		experience_list=[sicaf,dti_se,dti_pa,dti_di,htc]
		print title("Work Experience")
		for exp in experience_list:
			print exp.printing()

	# PROJECTS
	if "P" in argv or "PROJECTS" in argv or len(argv)==0:
		# College
		college_p = []
		sna = Project("Pygephi Social Network Analysis Script","College",datetime.date(2013, 10, 1),datetime.date(2013, 12, 15))
		sna.set_description("Python script that reads a Google Spreadsheet, and creates a social network xml file with gexf.")
		compi = Project("CACHACA Programming Language","College",datetime.date(2013, 2, 1),datetime.date(2013, 5, 19))
		compi.set_description("Development of a programming language on Python, PLY, and Google App Engine.")
		android = Project("Agenda Medica Android","College",datetime.date(2012, 9, 1),datetime.date(2012, 12, 1))	
		android.set_description("Development of an Android native application for doctors to keep a record of appointments and patients.")
		cloud = Project("Storeathon","College",datetime.date(2011, 10, 1),datetime.date(2011, 12, 1))
		cloud.set_description("Development of a shopify-like web application on Google App Engine using Django NonRel framework.")
		silab = Project("SILAB","College",datetime.date(2011, 8, 20),datetime.date(2011, 12, 1))
		silab.set_description("Development of a web application on php and MySQL, for registrations to lab classes, that read a Google Document with the students’ lists and dynamically created the groups and schedules he students can register to.")  
		college_p=[sna,compi,android,cloud,silab]
		# Personal Projects
		personal_p=[]
		senador = Project("Faltaste Senador Web Crawler","Personal",datetime.date(2014, 1, 1),datetime.date(2014, 2, 20))
		senador.set_description("Python script that scrapes the mexican senate web site to identify the senators that missed the sessions.")
		personal_p.append(senador)
		print title("Projects")
		for x in college_p:
			print x.printing()
		for x in personal_p:
			print x.printing()

	# EVENTS
	if "E" in argv or "EVENTS" in argv or len(argv)==0:

		workshop = Event("Python Workshop","SISCTI 39 Tech Symposium",datetime.date(2014, 4, 4),datetime.date(2014, 4, 6))
		workshop.set_description("Taught an Introduction to Python Programming Workshop.")
		angel = Event("AngelHack","AngelHack",datetime.date(2013, 4, 1),datetime.date(2013, 4, 2))
		angel.set_description("Development of a social network based on achievements and goals (Django framework).")
		acm = Event("ACM-Mty Hackathon","ITESM",datetime.date(2012, 10, 1),datetime.date(2012, 10, 2))
		acm.set_description("Development of a work marketplace for college students (Django framework).")
		event_list=[workshop,angel,acm]
		print title("Events")
		for x in event_list:
			print x.printing()



if __name__=="__main__":
	main(sys.argv[1:])