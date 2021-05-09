# Setup
For this project the method was tested on a hadoop 3.2.2 cluster with a namenode and three datanodes, with spark as 
a runner. The used operating system is Ubuntu 18.04. To be able to replicate the results, spark and the necessary
libraries have to be installed.

Libraries: sklearn, mrjob, pandas, jsonpickle, numpy

Also the ratings.csv and the movies_metadata.csv should be present on your system.
They can be obtained here: https://www.kaggle.com/rounakbanik/the-movies-dataset

# Running the code
* First specify the locations of the ratings.csv and the movies_metadata.csv in merge_datasets.py file and the run it
as a simple python script. It will generate the merged_data.csv. 
* The preprocessing.py script should then be run in the same directory in the same fashion. It will generate the
train_set.csv and the test_set.csv files.
* Next, specify the path to the train_set.csv file in the train_rf.py script and run it on your hadoop cluster, with the
nun_trees.txt as an input. This file can be altered to reflect how many trees should be generated. Also specify an output
file for the models. In my case this looked like this:

`python3 train_rf.py -r spark num_trees.txt > models.txt`

* Now specify the path to your test_set.csv in the eval_rf.py and then run it with the models.txt as input:

`python3 eval_rf.py -r spark models.txt`


