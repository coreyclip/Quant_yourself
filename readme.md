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
import pandas as pd
import numpy as np

import os

df = pd.read_csv(os.getcwd() + "/health_data.csv")

```

The first line of python code simply tells python to import in the code for pandas
and then tells python to use the alias pd to refer to pandas.

Generally people use the alias, pd for pandas so if you happen across some python code
where you see **pd** you can mostly assume it's referring to pandas.

The same goes for the next line which imports the python package **numpy** or numerical python.

note: if you installed pandas you should have also gotten numpy since it's a dependency for pandas

The third line import the python package **os** which stands for Operating System
an extremely handy package that I believe beginners to python should become familiar
with ASAP.

The fourth line is where we encounter something interesting. This line will load
our csv file named *health_data.csv* and store it in a variable called **df**
which is the convention for people working in pandas to call variables that hold a
pandas **dataframe** which you can think of as being analgous to a excel spreadsheet.


## Reading out information about our dataset

Next add these lines to the script
```Python
print("-"*15 + "information on your dataset" + "-"*15)
df.info()
print("-"*15 + "first 5 rows of the data" + "-"*15)
print(df.head(5))

```
