#                                         Notes from cheat sheet.

-> If  you want to write the heading(with bold and big text) use # for it, and add # as your heading number increases. Eg.
# Subjects (heading1)
## Course  (heading2)
.
.
##### Teachers (heading5)

-> If you want to write anything in bold, use ** f ** without space. f= text which you want to see in bold.
**DS690**.

-> If you want to write anything in italics, use * italicized text * without space.
*Data science*

-> To create a blockquote, add a > in front of a paragraph.
> Today is my first class of DS690.

-> Ordered List
1. First item.
2. Second item.
3. Third item.

-> Unordered List
- First item.
- Second item.
- Third item.

-> To denote a word or phrase as code,we should enclose that in backticks (`).

->To create a horizontal rule, use three or more asterisks (***), dashes (---), or underscores (___) on a line by themselves.
*** , ___ , ---

-> To create a link, enclose the link text in brackets and then follow it immediately with the URL in parentheses.
[title](https. whatever the link is).

-> To add an image, add an exclamation mark (!), followed by alt text in brackets, and the path or URL to the image asset in parentheses.
In this way we can add image with some description on it.


_____________________________________________________________________________________________

Little info about github and how to use it.
How to create a repository.
How to add a new file and wriite the description for it

_________________________________________________________________________________________________________________________________________________________________________
                                          **Python for Data Analysis**
                                                 **Chapter1**

# common data types
 - Integer
 - Float
 - Boolean
 - String
 
# Libraries

# Installation and setup
 Go to python.organd download it from there After that, to install jupyter notebook go to command prompt and type the command through which you want to download(given in jupyter notebook website)
 
# Basic idea on what python is and for what it is used.
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

___________________________________________________________________________________________________________________________________________________________________________

                                                   **chapter 2**

# common binary operators

a + b Add a and b
a - b Subtract b from a
a * b Multiply a by b
a / b Divide a by b
a // b Floor-divide a by b, dropping any fractional remainder
a ** b Raise a to the b power

Python is one of the most popular languages used by data scientists and software developers alike for data science tasks. It can be used to predict outcomes, automate tasks, streamline processes, and offer business intelligence insights. 

It’s possible to work with data in vanilla Python, but there are quite a few open-source libraries that make Python data tasks much, much easier.

You’ve certainly heard of some of these, but is there a helpful library you might be missing? Here's a line-up of the most important Python libraries for data science tasks, covering areas such as data processing, modeling, and visualization.

Data Mining
1. Scrapy
One of the most popular Python data science libraries, Scrapy helps to build crawling programs (spider bots) that can retrieve structured data from the web – for example, URLs or contact info. It's a great tool for scraping data used in, for example, Python machine learning models. 

Developers use it for gathering data from APIs. This full-fledged framework follows the Don't Repeat Yourself principle in the design of its interface. As a result, the tool inspires users to write universal code that can be reused for building and scaling large crawlers.

2. BeautifulSoup
BeautifulSoup is another really popular library for web crawling and data scraping. If you want to collect data that’s available on some website but not via a proper CSV or API, BeautifulSoup can help you scrape it and arrange it into the format you need.

Data Processing and Modeling
3. NumPy
NumPy (Numerical Python) is a perfect tool for scientific computing and performing basic and advanced array operations.

The library offers many handy features performing operations on n-arrays and matrices in Python. It helps to process arrays that store values of the same data type and makes performing math operations on arrays (and their vectorization) easier. In fact, the vectorization of mathematical operations on the NumPy array type increases performance and accelerates the execution time.

4. SciPy
This useful library includes modules for linear algebra, integration, optimization, and statistics. Its main functionality was built upon NumPy, so its arrays make use of this library. SciPy works great for all kinds of scientific programming projects (science, mathematics, and engineering). It offers efficient numerical routines such as numerical optimization, integration, and others in submodules. The extensive documentation makes working with this library really easy.

5. Pandas
Pandas is a library created to help developers work with "labeled" and "relational" data intuitively. It's based on two main data structures: "Series" (one-dimensional, like a list of items) and "Data Frames" (two-dimensional, like a table with multiple columns). Pandas allows converting data structures to DataFrame objects, handling missing data, and adding/deleting columns from DataFrame, imputing missing files, and plotting data with histogram or plot box. It’s a must-have for data wrangling, manipulation, and visualization.

(Want to learn pandas? Check out Dataquest's NumPy and Pandas fundamentals course, or one of our many free pandas tutorials.)

6. Keras
Keras is a great library for building neural networks and modeling. It's very straightforward to use and provides developers with a good degree of extensibility. The library takes advantage of other packages, (Theano or TensorFlow) as its backends. Moreover, Microsoft integrated CNTK (Microsoft Cognitive Toolkit) to serve as another backend. It's a great pick if you want to experiment quickly using compact systems – the minimalist approach to design really pays off!

7. SciKit-Learn
This is an industry-standard for data science projects based in Python. Scikits is a group of packages in the SciPy Stack that were created for specific functionalities – for example, image processing. Scikit-learn uses the math operations of SciPy to expose a concise interface to the most common machine learning algorithms. 

Data scientists use it for handling standard machine learning and data mining tasks such as clustering, regression, model selection, dimensionality reduction, and classification. Another advantage? It comes with quality documentation and offers high performance. 

8. PyTorch
PyTorch is a framework that is perfect for data scientists who want to perform deep learning tasks easily. The tool allows performing tensor computations with GPU acceleration. It's also used for other tasks – for example, for creating dynamic computational graphs and calculating gradients automatically. PyTorch is based on Torch, which is an open-source deep learning library implemented in C, with a wrapper in Lua. 

9. TensorFlow
TensorFlow is a popular Python framework for machine learning and deep learning, which was developed at Google Brain. It's the best tool for tasks like object identification, speech recognition, and many others. It helps in working with artificial neural networks that need to handle multiple data sets. The library includes various layer-helpers (tflearn, tf-slim, skflow), which make it even more functional. TensorFlow is constantly expanded with its new releases – including fixes in potential security vulnerabilities or improvements in the integration of TensorFlow and GPU.

10. XGBoost
Use this library to implement machine learning algorithms under the Gradient Boosting framework. XGBoost is portable, flexible, and efficient. It offers parallel tree boosting that helps teams to resolve many data science problems. Another advantage is that developers can run the same code on major distributed environments such as Hadoop, SGE, and MPI.

Data Visualization
11. Matplotlib
This is a standard data science library that helps to generate data visualizations such as two-dimensional diagrams and graphs (histograms, scatterplots, non-Cartesian coordinates graphs). Matplotlib is one of those plotting libraries that are really useful in data science projects — it  provides an object-oriented API for embedding plots into applications. 

It's thanks to this library that Python can compete with scientific tools like MatLab or Mathematica. However, developers need to write more code than usual while using this library for generating advanced visualizations. Note that popular plotting libraries work seamlessly with Matplotlib. 

12. Seaborn
Seaborn is based on Matplotlib and serves as a useful Python machine learning tool for visualizing statistical models – heatmaps and other types of visualizations that summarize data and depict the overall distributions. When using this library, you get to benefit from an extensive gallery of visualizations (including complex ones like time series, joint plots, and violin diagrams).

13. Bokeh
This library is a great tool for creating interactive and scalable visualizations inside browsers using JavaScript widgets. Bokeh is fully independent of Matplotlib. It focuses on interactivity and presents visualizations through modern browsers – similarly to Data-Driven Documents (d3.js). It offers a set of graphs, interaction abilities (like linking plots or adding JavaScript widgets), and styling.

14. Plotly
This web-based tool for data visualization that offers many useful out-of-box graphics – you can find them on the Plot.ly website. The library works very well in interactive web applications. Its creators are busy expanding the library with new graphics and features for supporting multiple linked views, animation, and crosstalk integration.

15. pydot
This library helps to generate oriented and non-oriented graphs. It serves as an interface to Graphviz (written in pure Python). You can easily show the structure of graphs with the help of this library. That comes in handy when you're developing algorithms based on neural networks and decision trees.

                                              --------> got this from https://www.dataquest.io/blog/15-python-libraries-for-data-science/
                                              
                                              
**SOME OF THE BASIC PROGRAMS ARE ATTACHED IN THE FILE**

















