# R
### Learing Note In Udacity:
#### 1.Run R code of file into R studio Console:
1. Open the R code file in R studdio;
2. Select the R code part you want to run;
3. Command + Enter to Run R code into R R studio Console:

### 2.Look for help in R:
In console, type:? + Term, for  exmple
```
?mean
```
You will find the exmplation in R help in R studio

### 3.Read CSV file in R studio:
1. Open the R code file in R studdio;
2.Locate the current directoty:
```
getwd()
```
3. Move to R file directry:
```
setwd('/Users/zhanghuiqiao/Downloads/eda-course-materials/lesson2')
```
4. Run the file:
```
stattesinfo <- read.csv('stateData.csv')
```
5. You will see the data logs in Enviroment, then Click the sheet symbol to see the data content

### 4. Subset data :
```
subset(stattesinfo, state.region == 1)
stattesinfo[stattesinfo$state.region ==1,]
```
Note :1. Select the R code part you want to run;
      <br>2. Command + Enter to Run R code into R R studio Console


## R Learning Resources
### Video:
1.Data Analysis with R
<br>https://www.udacity.com/course/data-analysis-with-r--ud651
<br>2.Anwarvic/Data-Analysis-with-R--Udacity
<br>https://github.com/Anwarvic/Data-Analysis-with-R--Udacity
<br>3. Data Science Specialization
<br>https://www.coursera.org/specializations/jhu-data-science
<br>4. Professional Certificate inData Science
<br>https://www.edx.org/professional-certificate/harvardx-data-science
<br>5.Harvard University is offering FREE 14 Online Data Science Courses
<br>https://medium.com/@brenspiration/harvard-university-is-offering-free-14-online-data-science-courses-fd10e35a925c

### Data Camp Note:
GlennOu66304/Data-Sciences-in-R
<br>https://github.com/GlennOu66304/Data-Sciences-in-R

### Book:
Learning R
<br>https://learning.oreilly.com/library/view/learning-r/9781449357160/
<br>Introduction to Data Science with R
<br>https://learning.oreilly.com/videos/introduction-to-data/9781491915028
<br>R for Data Science
<br>https://learning.oreilly.com/library/view/r-for-data/9781491910382/
<br>https://r4ds.had.co.nz/
<br>OReilly_HandsOn_Programming_with_R_2014
<br>https://d1b10bmlvqabco.cloudfront.net/attach/ighbo26t3ua52t/igp9099yy4v10/igz7vp4w5su9/OReilly_HandsOn_Programming_with_R_2014.pdf
