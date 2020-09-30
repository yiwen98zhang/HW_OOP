# OOP homework for Statistical Computing
## Instructions
In your local repository, type the following command in your terminal:
```
python3 src/main.py
```
Then this message would show up:
```
Please type in the dataset you want to see (Counties, States, or US):
```
For displaying the data in us-counties.csv, type 'Counties'.  
For displaying the data in us-states.csv, type 'States'.  
For displaying the data in us.csv, type 'US'.  
Then the first 10 rows of each dataset would be printed on your screen.

## OOP concepts implemented
class *ReadGeneral*, class *ReadCounties*, class *ReadStates*, and class *ReadUS* are classes.  
class *ReadCounties* is-a class *ReadGeneral*.  
class *ReadStates* is-a class *ReadGeneral*.  
class *ReadUS* is-a class *ReadGeneral*.  
class *ReadGeneral* is an abstract class.  
Initializer is utilized in class ReadCounties, class *ReadStates*, and class *ReadUS*.  
Method *read_all()* is implemented in all the classes above.  
*data* is an object of class ReadCounties, class *ReadStates*, or class *ReadUS*.  

## Additional Requirements
We utilized the *os* module to get the path of local path, so make sure this module has been installed.  
We utilized the *csv* module to load our datasets, which is in .csv format, so make sure this module has been installed.  
We utilized the *abc* module to create the abstract class, so make sure this module has been installed.  


## Result of SonarQube
![Image text](https://github.com/yiwen98zhang/HW_OOP/blob/master/Docs/SonarQubeScreenshot.png)
