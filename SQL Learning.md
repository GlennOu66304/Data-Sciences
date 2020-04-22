# SQL Learning
### SQL Real Lfe Using:

1.SQL CHEAT SHEET
<br>https://cdn.sqltutorial.org/wp-content/uploads/2016/04/SQL-cheat-sheet.pdf
<br>2.SQL COMMANDS
<br>https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf




### 1.Enviroment To Run your SQL Code:
PostgreSQL
<br>1,Interactive installer by EnterpriseDB
<br>https://www.postgresql.org/download/macosx/
<br>2.PostgreSQL Database Download
<br>https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
<br>3.Installation of PostgreSQL on Mac OS
<br>https://www.enterprisedb.com/postgres-tutorials/installation-postgresql-mac-os
<br>4.The PostgreSQL documentation
<br>https://www.enterprisedb.com/edb-docs/p/postgresql
<br>5.Connecting PostgreSQL using psql and pgAdmin
<br>https://www.enterprisedb.com/postgres-tutorials/connecting-postgresql-using-psql-and-pgadmin

### 2.Run PostgreSQL DVD Rental sample in Postgre Sql Pgadmin4
1.downlaod the DVD Rental sample :
<br>https://www.postgresqltutorial.com/postgresql-sample-database/

2.Extract the DVD Rental sample  Zip file into tar file
<br>https://extract.me/

3.Make sure that data format was chosen to all file, if you meet "no file was found" warning while you restore the data.
<br>How to load database to PostgreSQL
<br>https://www.youtube.com/watch?v=8bENMPsFepg

4.printable postgresql sample database digram.psd
<br>https://sp.postgresqltutorial.com/wp-content/uploads/2018/03/printable-postgresql-sample-database-diagram.pdf

5.To launch the web version of pgadmin4, you need to click the pgadmin4 file first then find the elephant icon in mac header bar to choose New pgadmin4 window.

### 4. Run Udacity CSV FILE in Postgre Sql Pgadmin4
1. CREAT A TABLER region :
```CREATE TABLE public.region
( 
    id integer NOT NULL,
	name character varying(25) COLLATE pg_catalog."default" NOT NULL,
	CONSTRAINT region_pkey PRIMARY KEY(id)
)

  SELECT * FROM region;
CREATE TABLE public.region
( 
    id integer NOT NULL,
	name character varying(25) COLLATE pg_catalog."default" NOT NULL,
	CONSTRAINT region_pkey PRIMARY KEY(id)
)

  SELECT * FROM region;
```
<br>Create the Parch & Posey DB
<br>https://medium.com/@gauravinthevalley/run-the-parch-posey-db-locally-in-postgres-8a0c2fde0c2e

2. Utilize Postgre Sql Pgadmin4 to Import a CVS File
<br>Import CSV file into a table using pgAdmin
<br>https://www.postgresqltutorial.com/import-csv-file-into-posgresql-table/

Test the result:
```
SELECT * FROM Region;
```

3.parchposey Dataset
<br>parchposey
<br>https://github.com/jdbarillas/parchposey

## 3.Run your SQL commands in Mode.
1. Install the Bridge connector
<br>https://app.mode.com/udacity_data_sciences/data_sources/bridges/setup/default/postgresql?flow=create_org

2. Choose the connect page to Connecting through Bridge Connector page
<br>https://app.mode.com/udacity_data_sciences/data_sources/bridges/default/default/postgresql
3. input required information
```
Server [localhost]: 
Database [postgres]: 
Port [5432]: 
Username [postgres]: 
Password for user postgres: 
```
<br>https://app.mode.com/udacity_data_sciences/data_sources/bridges/8a84b988d6b3/default/postgresql/new

4. Don't choose the encryption option then you are able to connect your Mode with Postgre SQl

## References
1.Oreilly Book:
<br>Learning SQL, 2nd Edition
<br>https://learning.oreilly.com/library/view/learning-sql-2nd/9780596801847/ad_files/strata-ad.html

2.Udacity Video:
<br>1.SQL for Data Analysis
<br>https://classroom.udacity.com/courses/ud198

2.ayushi-b / SQL-for-Data-Analysis
<br>https://github.com/ayushi-b/SQL-for-Data-Analysis

3.Intro to Relational Databases
<br>https://www.udacity.com/course/intro-to-relational-databases--ud197

4.<br>Mode
<br>https://app.mode.com/home/glenn_ou/search


