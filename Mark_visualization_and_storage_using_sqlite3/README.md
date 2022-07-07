# Mark visualization and storage using sqlite3

## About
<img src="https://www.cyanous.com/img/data2.gif" align="right" width="40%" height="40%">
<p>&emsp; This project aims to visualize,store and compare marks in a database. This project provides login/sign up facility,secured sign in using password, entering of marks for all exams, compare and visualize marks and store it in a database for furthur reference. Students can visit the program and register themselves with the required information that is expected by the system.<br><br>
	&emsp; This project is very helpful for students to analyze their marks in all the subjects in all the exams and compare it. It makes the students to identify their weakness and strenghts so that they can focus on that subject.<br><br>
	&emsp; Since this project uses the database concept, students can view and analyse their marks instantly without entering all the details again. This program is useful to store multiple student’s marks such that many of the students can make use of it.</p>

## Module Description

Here, in this project we use differenty kinds of modules that integrate with the source code and run effectiely.

### 1.sqlite3

<p>&emsp; SQLite is a C library that provides a lightweight disk-based databse that doesn’t require a separate server processs and allowes accessing the databse using a nonstandard variant of the SQL query language.</p>

### 2.matplotlib

<p>&emsp; Matplotlib is a plotting library for the Python programing langauge and its numerical mathematics  extension NumPy. It provides an object-oriented API for emdeddding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython,Qt, or GTK.</p>

## How to use the output terminal

<ol>
  <li>If you are a new user, then signup by entering user id and password or login using your user id and password.</li>
  <li>Enter your marks out of 100 for CAT-1,CAT-2,CAT-3,Semester respectively. If already entered, then ignore this step.</li>
  <li>For visualising your marks, select <b>visualization</b> and then select the exam you want to visualize.</li>
  <li>For comparing your CAT and Semester marks, select <b>compare CAT vs semesteer</b>
</ol>

## Working

<ol>
  <li>At first, the modules and packages <b>sqlite3</b> and <b>matplotlib.pyplot</b> is imported into the program.</li>
  <li>A database <b>student_details</b> is created if there is no database else it is opened from the directory.</li>
  <li>When ever the user enters their user id and password, a new table with user id as name will be created and password is stored in password column.</li>
  <li>During login, when the user enters their user id and password, their corresponding table is accessed and the password column is accessed and checks if it is same as enters.</li>
  <li>If the login is successfull, main menu is displayed.</li>
  <li>For entering the marks, the entered marks is stored in the corresponding exam row with subject as column in the user's table</li>
  <li>For visualization and comparing, the user enters the exam to be visualized.</li>
  <li>The entered exam choice is received and the corresponding data is accessed from the user's table and with the help of <b>matplotlib</b> module, the data is displayed as histogram.</li>
  <li>This procedure is continued until the user exits from the output terminal.</li>
</ol>

### NOTE: This is a initial version of the project. Lots of improvements and more functions will be added ASAP.


