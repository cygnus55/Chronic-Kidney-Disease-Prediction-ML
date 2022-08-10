# Notes

## Preprocessing

- Converted arff files to csv using:
[https://pulipulichen.github.io/jieba-js/weka/arff2csv/](https://pulipulichen.github.io/jieba-js/weka/arff2csv/)
- Renamed csv file to `chronic_kidney_disease_full.csv`
- Detected error in csv file (Some rows contain addtional columns)

When above process didn't work, we followed following procedures:

- We study the arff file and we get to know that arff file have following error:
	- There are unwanted tabs.
	- There are unwanted commas (,) and spaces in the rows.

- We remove the tabs using find and replace feature of text editor.
- We remove unwanted space in line 60.
- We remove unwanted comma in line 399.
- After cleaning arff file, we import it using arff method of `scipy` library.
- The imported data is then converted to pandas Dataframe.
- We then proceed to clean the dataframe.

### Cleaning procedures

- The datatypes of some attributes were in byte strings. So, the datatype was recoded to string or float datatype which was appropriate.
- Some values of attributes were `?`. Those were replaced by NaN.

### Load data for working on it

- The data was loaded in the form of pandas dataframe and its shape and features were studied
- The id column was dropped
- The class attribute had all its values converted in numeric format
- The column names were changed to more descriptive names
