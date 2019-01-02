# Starter Data Science Project: The Quantified Self
## Part 1: enter the python

For this series I'm going to approach introducing the tools and techniques of Data Science, in a manner I've so far not seen online yet.
Most introductions to Data Science revolve around datasets that are already well known and with the foreknowledge of what can and cannot be extracted from it. A certain 20th century tragedy and various flower specimens come to mind. While there's not exactly wrong with learning data science through these kinds of examples, I think it removes the element of data science I personally love the most: discovery!

I personally first learned Python in order to explore complex sets of data I encountered during my Peace Corps tour back in 2014. Being able to transform what I was learning through blogs, online courses, and books into actionable insights. Helped create a virtuous cycle of seeing a technique and immediately applying it to a personal project that grew in scope on a almost daily basis.

It's my aim to try to give some guidance on how to recreate that same experience with this blog series. While I'd encourage anyone interested in getting into Data Science to start with data that they are familiar with and care enough about to what to analyze. But for many it's hard to think of something. What I'll be laying out is a data source that is

* definitely unique
* relevant and actionable  

We'll be using health data collected from our own iphones or wearables as a guide towards learning python for data analysis all the while
steadily building up our own understanding of ourselves and our habits. Hopefully you'll end up with a enough python knowledge to be dangerous, and have an experience that will serve as a framework when working with data in the future.

## Gathering our data
[QS Access](https://itunes.apple.com/us/app/qs-access/id920297614?mt=8) is a simple iphone app that accesses the health app in your iphone. You'll want to allow the health app to have read access to all of the other apps on your phone tracking your calories, exercise, meditation minutes, etc. because QS Access only works with the health app directly.  

I would recommend first downloading your data as days since that will include the most metrics coming from your devices. From there you can upload this csv file to your own personal computer either via dropbox, icloud, google drive or by email. Now that our data has been captured, we can transform it into something comprehensible. Sometimes health tracking apps

If you're brand new to Python, I would highly recommend downloading and installing the [Anaconda](https://www.anaconda.com/download/) distribution. There's a part in the installation process that asks weather or not you want to put Anaconda on your PATH variable. If this is your first time using Python, I'd recommend putting checking that box and putting Python on your PATH. I know the installer says this isn't recommended but really unless your managing multiple python interpreters (if you don't know what that means your probably not). Then putting Anaconda on your PATH will make things smoother moving forward. By downloading Anaconda, we'll have pretty much all the tools we'll need to make it through the series plus at the time of writing this post Anaconda comes with the option of downloading VS Code, a great text editor for writing code, and the Jupyter project which is ubiquitous tool in the Data Science world, as well as being a rather beginner friendly environment to learn python in.

# Beyond Helloworld: Loading a csv file
Place your csv file in a dedicated folder for example in a folder called *Quant_yourself* on your C: drive or Home directory if you're using mac. If your using Linux then you know what your doing.

```
C:\Quant_yourself\health_data.csv
```

We'll be using this Quant_yourself folder as our project directory. If I say put x y or z file in your project directory this is the folder I'm talking about.

Next we'll get started with our python script that'll extract, load, and transfor our dataset.

While many beginner python tutorials shy away from using external packages, I say if they make life easier let them make life easier.

If you installed anaconda then the following should work. If you didn't for some reason then go to the command line and use pip to install the following to install pandas, a very widely used and robust python package for data analysis and processing.

```bash
pip install pandas
```

Once that's done or you already have anaconda installed (which includes pandas)
create a file called **main.py**

#### Note for those new to programming:
In programming generally specific languages use specific file endings to denote a file that is meant to be processed in that language. Technically you could call your python script in this case anything: main.py, app.py, myscript.py, or not_a_python_script.py.
what's important is important for our purposes is that the file contains the ending **.py** which tells python and your operating system that it's working with a python file. If you're using a programming oriented text editor (sublime text, atom, VS Code, emacs, notepad, etc) it's enough to just save the file as **script.py** for this to be done correctly. Also note how I named our csv file with a name without any spaces,
using a underscore "_" instead of a space. For reasons outside the scope of this tutorial, spaces in file names makes pathing a hassle and unpredictable. In laymans
terms, the computer has *creative* ways of understanding spaces that we humans
don't find necessarily intuitive.

## Extracting the Data

Ok so in our main.py script start the script with the following:

```Python
yimport pandas as pd
import numpy as np

import os

df = pd.read_csv("health_data.csv")

```

The first line of python code simply tells python to import in the code for pandas
and then tells python to use the alias pd to refer to pandas.

Generally people use the alias, pd for pandas so if you happen across some python code
where you see **pd** you can mostly assume it's referring to pandas.

The same goes for the next line which imports the python package **numpy** or numerical python.

note: if you installed pandas you should have also gotten numpy since it's a dependency for pandas

The fourth line is where we encounter something interesting. This line will load
our csv file named *health_data.csv* and store it in a variable called **df**
which is the convention for people working in pandas to call variables that hold a
pandas **dataframe** which you can think of as being analgous to a excel spreadsheet.
"health_data.csv" is as you may see the name of the csv file saved in our folder, if you're csv file of health data is named something else, change that part to what you have on your machine. 

## Reading out information about our dataset

Next add these lines to the script
```Python
print("information about your dataset")
print(df.info())
print("first 5 rows of the data")
print(df.head(5))

```
These next few lines will output general information about the dataframe and list out the first five lines of the dataset. 
The **print** statments that each command is wrapped it tells python to read out whatever is placed between the parenthesis to into the terminal which we'll touch on shortly. Generally python functions are invoked pretty much in the same way as you would say an excel function:

```
function(parameter, parameter,...)
```

The first print function will simply read out the statement "information about your dataset" to the terminal. Anything written between single quotes or double quotes will be interpretted as a string by python. A *string* is simply text that isn't meant to be interpretted as code, pretty much all programming languages support string datatypes.

The next print statement doesn't contain a string but instead calls a method from our **df** object. A method tells python to activate a particular action from an object. methods in python are accessed with a period or what is sometimes refered to as dot notation.

```
object.method()
```

In this case and in the **df.head()** method we are telling python to access the **.info()** and **.head()** methods of a pandas dataframe. .info() will provide a simple read out of what pandas is interpretting as our dataframe. It's a good idea to always call this method and check it's read out when performing data analysis to make sure that the computer is seeing things the same way we are. .head serves a similar function, as it prints out the first **n** rows of a dataframe, where **n** is the number placed within the method's parameters. In this example that would be 5. Something useful to keep in my when programming is that while the computer is very obedient and fast, it's not as clever as we may often hope. Pandas is pretty robust but you should expect to encounter some issues eventually especially when say tweaking the pd.read_csv command to only access specific parts of the original csv file.

## Running our first python script 

At this point it's worthwhile to give our python script a test to run to see that we've set everything up correctly. 
This means that you'll have to access the command line. On mac or linux that's going to be the terminal program. On windows I'd highly recommend installing git and using the git bash terminal, which will come included when you install git. If for some reason you cannot install git then use Windows powershell, not the cmd.exe unless you know what you're doing. 

Once you have the command line open you'll need to navigate to the folder where you have your csv file and .py file. The conventional way to do this is to use the **cd** command which stands for "change directory" in unix based systems. Macs are unix based while the git bash terminal on windows mimics one. Powershell contains some but not all unix commands luckily it does have the cd command

```
cd Quant_yourself
```

this assumes that you placed your Quant_yourself folder in either your home directory on mac or C: drive on windows. If you put it someplace else say within a folder in your home directory, then you'll have to prefix the file path like this:

```
cd projects/Quant_yourself
```
Once you've navigated to your project directory, you should see something like this in your terminal

```
YourComputer:~/Quant_yourself$ 
```
The specifics will be different between operating systems and terminal programs but generally you should see the Quant_yourself text to the left of your cursor. 

Next you'll call python and have it run your first script. Type in the following command: 

```
YourComputer:~/Quant_yourself$ python main.py
```
press enter and you should see the following being read out 

```
yourcomputer:Quant_yourself$ python main.py
information on your dataset
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 510 entries, 0 to 509
Data columns (total 8 columns):
Unnamed: 0                510 non-null int64
Unnamed: 0.1              510 non-null int64
Start                     510 non-null object
Finish                    510 non-null object
Distance (mi)             510 non-null float64
Steps (count)             510 non-null float64
Weight (lb)               510 non-null float64
Dietary Calories (cal)    510 non-null float64
dtypes: float64(4), int64(2), object(2)
memory usage: 32.0+ KB
first 5 rows of the data
   Unnamed: 0  Unnamed: 0.1          ...           Weight (lb) Dietary Calories (cal)
0           0             0          ...                 197.6                 2240.9
1           1             1          ...                 200.8                 2319.7
2           2             2          ...                 200.4                 2369.7
3           3             3          ...                 201.6                 2188.8
4           4             4          ...                 202.9                 2555.0


```
If you got something similar to the above, then congradulations you just ran your first python script!!

This may not be much but it's a start. In this next section we'll start to move beyond what we frankly could have just done in excel. 


# Quantify Yourself part 2: Open up a can of Statistics

In my previous post we started with downloading and installing the Anaconda python distribution and loaded our health data csv into a Python interpretter. I know that a lot of that installation work and perhaps figuring out pathing may have been frustrating. But like anything new we do, those intial challenges and frustrations are what build experience. 
Now that we have our data loaded it's time to start extracting insights. 

Open up the script from the previous part in your prefered text editor. 
When we finished last our script should look like this:

```python
import pandas as pd
import numpy as np

import os

df = pd.read_csv("health_data.csv")
print("information about your dataset")
print(df.info())
print("first 5 rows of the data")
print(df.head(5))

```

In this script the methods **.info()** and **.head()** just gave us some very bare bones but necessary information about our dataset. Next we'll go over some more sophisticated 
things we can do with our dataset such as descriptive statistics, correlation tables, and regression analysis. We'll also go over how to export these statistics to both a text file and an excel file. 

## Descriptive Stats
Pandas has a number of built in methods that make drawing up stats extremely easy. In this first part of this tutorial series we read out information about our dataset that I would almost always check upon loading a new dataset. From both .info() and .head() I'd be checking to make sure that each column has the expected number of non-null rows and that python had interpretted numbers as numbers and words as strings. That's what the ```print(df.info())``` line is for. And for good measure I always like to actually read out a sub-section of the dataset so I can see what python is actually seeing, and that's the purpose of this line: ```print(df.head(5))```. These steps are there just to make sure our data exists as we expect it to exist, but don't necessarily help us extract insights from our data. 

add the following lines to the bottom of your script:

```python
descriptive_stats = df.describe()
correlation_table = df.corr()

print("Descriptive Statistics")
print(descriptive_stats)

print('Correlation Table')
print(correlation_table)
```

In the above we are calling two new pandas.DataFrame methods and storing the results into variables that are again printed out into the console

When you run this script from the terminal, you should now have output that will look something like this:

```python
Descriptive Statistics
       Distance (mi)  Steps (count)  Weight (lb)  Dietary Calories (cal)
count     510.000000     510.000000   510.000000              510.000000
mean        3.732590    9558.945098   202.065882             2486.992941
std         2.517266    6084.983156     1.705974              254.538844
min         0.020139      56.000000   196.200000             1696.500000
25%         1.731280    4741.000000   201.000000             2313.775000
50%         3.182276    8140.379652   202.400000             2478.300000
75%         5.236160   13392.750000   203.200000             2652.575000
max        14.480813   32873.096151   206.700000             3283.600000
Correlation Table
                        Distance (mi)  Steps (count)  Weight (lb)  Dietary Calories (cal)
Distance (mi)                1.000000       0.990703    -0.827025               -0.070965
Steps (count)                0.990703       1.000000    -0.833593               -0.069348
Weight (lb)                 -0.827025      -0.833593     1.000000                0.608575
Dietary Calories (cal)      -0.070965      -0.069348     0.608575                1.000000
-


```
So first let's go over what the .describe method outputed. 

The columns list out the columns we have in our dataset while the rows store stats for the associated column. 
* **count** simply the number of non-null values in a given column, my dataset is complete so each column has the same number of non-null rows: 510

* **mean** is just another word for the average, on average I have walked 3.73 miles in a given day.

* **std** short hand for standard deviation. In laymans terms a standard deviation is the range from which a value can be considered to be atypical in a probablistic context. The standard deviation for the distance I walked over this given timeframe is 2.5 miles, so a day in which I walked a signifcantly greater distance than normal would be 6.2 miles (2.5 + 3.7) while a day in which I walked significantly less would be 1.2 miles (3.7 - 2.5). For the most part the standard deviation is useful for giving context to your datapoints. 

* **25% , 50%, and 75%** these are all just shorthand for the 25th, 50th, and 75th percentiles. Percentiles points are representations of point within the data that a proportion of the values are bellow that given point. So for example 25% of the values in the distance column are 1.7 miles or less. The 50th percentile is the point where half of our data is above this point and half is bellow. This is also the definition of the *median*. Our 75th percentile is 5.23 miles so for three quarters of this given time frame I walked less that 5.23 miles but walked that amount or more for one quarter of this given timeframe. 

* **max** this is just shorthand for the maximum.  

You can see the documenation for .describe() [here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html)

After our stats output we have our correlations table. Correlation tables are IMO an essential part of data exploration. I almost always use one as a guide for whatever next steps I take in performing data analysis and when properly visualized they can be great analytical products in their own right. A correlation table is typically presented as a matrix with identical labels on both the columns and rows. The numbers that make up the matrix are the correlation values between the corresponding row and column labels. Correlation essentially is the degree in which two phenomena appear to act in concert. If a correlation is a positive number then we can say that when **A** increases **B** also increases, on average, by the degree of the correlation value. With my dataset Step Counts and Distance in miles  


## Data Exploration and Cleaning in Jupyter Notebooks

While Jupyter notebooks were conceived of as a portable means of combining code and written research, I find them to be an excellent environment for exploring data and toying around with different data engineering operations. You can load a datasource in one cell and then write any number of cells that perform different operations on this datasource without having to go into our terminal and rerun different versions of our program. I also use the markdown cells to write nicely formatted notes about what each cell does or store links to online resources that are relevant to what ever I'm doing with a certain project. In this next section we'll go over the basics of running jupyter notebooks by doing some basic data processing. 

* Firing up Jupyter Lab
* Filling missing values
* splitting up our dataframes 
* converting to markdown or html see: https://www.blog.pythonlibrary.org/2018/10/09/how-to-export-jupyter-notebooks-into-other-formats/ 
