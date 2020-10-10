# Advertising-Sales-ML-Model-Flask-Deployment
## ML-Model-Flask-Deployment
This is a project to elaborate how Machine Learn Models are deployed on production using Flask API
<img src="https://github.com/vaibhavhariaramani/advertising-Sales-ML-Model-Flask-Deployment/blob/main/images/columns/tv.png" alt="Illustration"/> 
### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) pre-installed.

### Project Structure
This project has four major parts :
1. model.py - This contains code fot our Machine Learning model to predict employee salaries absed on trainign data in 'hiring.csv' file.
2. app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
3. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4. templates - This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee salary.

### Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

You should be able to view the homepage as below :
![alt text](http://www.thepythonblog.com/wp-content/uploads/2019/02/Homepage.png)

Enter valid numerical values in all 3 input boxes and hit Predict.

| Column Name | Range | feature description |  |
| --- | --- | --- | --- |
|  TV | [0,296] | [here](https://www.kaggle.com/ashydv/advertising-dataset) | <img src="/images/columns/tv.png" alt="Illustration"/> |
| Radio | [0,50] | [here](https://www.kaggle.com/ashydv/advertising-dataset) | <img src="/images/columns/Radio.png" alt="Illustration"/> |
| Newspaper | [0,114] | [here](https://www.kaggle.com/ashydv/advertising-dataset) | <img src="/images/columns/Newspaper.png" alt="Illustration"/> |
| [sckit-learn](https://scikit-learn.org/stable/) |  | [linreg3](https://maelfabien.github.io/statistics/linreg3/) | [here]() |



If everything goes well, you should  be able to see the predcited salary vaule on the HTML page!
![alt text](http://www.thepythonblog.com/wp-content/uploads/2019/02/Result.png)

4. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to send the request with some pre-popuated values -
```
python request.py
```
