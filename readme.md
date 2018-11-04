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
Place your csv file
