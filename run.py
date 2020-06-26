from dataset import Dataset

'''
number :

Set the number of training sound files

The actual number of files generated in the dataset
will be 6*number
as each song will be generated in 6 instruments a,b,c,d,e,p

These files will be generated in the data directory

Below number is 10, thus no. of files in data directory = 6*10 = 60
'''


number = 10

Number of training sound file
dataset = Dataset()
dataset.generate_dataset(number,1)
