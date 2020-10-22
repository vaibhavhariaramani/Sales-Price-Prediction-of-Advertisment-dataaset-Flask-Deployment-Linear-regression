# [Advertising-Sales-ML-Model-Flask-Deployment](https://sales-predictionapi.herokuapp.com/)
## [Checkout Live Model Api at ](https://sales-predictionapi.herokuapp.com/):[https://sales-predictionapi.herokuapp.com/](https://sales-predictionapi.herokuapp.com/)
```
[https://sales-predictionapi.herokuapp.com/]
```
[![Deployed Model](https://3kllhk1ibq34qk6sp3bhtox1-wpengine.netdna-ssl.com/wp-content/uploads/continuous-delivery-default.png)](https://sales-predictionapi.herokuapp.com/)

### Problem : [Advertising Dataset](https://www.kaggle.com/ashydv/advertising-dataset)

## Single Linear Regression (SLR)

We will explore [Advertising Dataset](https://www.kaggle.com/ashydv/advertising-dataset) and predict sales by performing the Single Linear Regression (SLR)and then will deploy model for global access. The major topics to be covered are below:

- [Reading and Understanding the Data](https://nbviewer.jupyter.org/github/vaibhavhariaramani/advertising-Sales-ML-Model-Flask-Deployment-Linear-regression/blob/main/sales-prediction-simple-linear-regression.ipynb#text_cell_render%20border-box-sizing%20rendered_html)
- Data Inspection
- Data Cleaning
- Exploratory Data Analysis
- Univariate Analysis
- Bivariate Analysis
- Model Building
- Model Evaluation
- Model Deployment Using Flask and Heroku


## For better understanding about Single Linear Regression (SLR) checkout my blog [My personal data science blog on EDA](https://vaibhavhariaramani.github.io/blogs/) 


## ML-Model-Flask-Deployment
This is a project to elaborate how Machine Learn Models are deployed on production using Flask API
<img src="https://github.com/vaibhavhariaramani/advertising-Sales-ML-Model-Flask-Deployment/blob/main/images/columns/tv.png"> 
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




If everything goes well, you should  be able to see the predcited salary vaule on the HTML page!
![alt text](http://www.thepythonblog.com/wp-content/uploads/2019/02/Result.png)

## Deploying ML model on HEROKU
1. Sign up or Login to [HEROKU](https://www.heroku.com/)
2. Go to [heroku dashboard](https://dashboard.heroku.com/apps)
3. Click on create on new apps
4. Give a name to your model app such as 'Linear-Regression'
5. Connect app with your ML model Github Repo
6. Click on deploy model
Hence your model is deployed.....
Checkout my model [https://sales-predictionapi.herokuapp.com/](https://sales-predictionapi.herokuapp.com/)

=========================================================================================================================================================
# Resources 

To learn more about these Resources you can Refer to some of these articles written by Me:-

- [Medium](https://medium.com/geeky-bawa)
- [geeky Traveller](https://sites.google.com/view/geeky-traveller/)
- [Blogs](https://github.com/vaibhavhariaramani/blogs)
- [Youtube](https://www.youtube.com/channel/UCy7amUpLnsRLEMIaJGGBYog)[![Youtube Badge](https://img.shields.io/badge/-Geeky_Bawa-1ca0f1?style=flat-circle&labelColor=d54b3d&logo=youtube&logoColor=white&link=https://www.youtube.com/channel/UCy7amUpLnsRLEMIaJGGBYog)](https://www.youtube.com/channel/UCy7amUpLnsRLEMIaJGGBYog)

### Don't forget to tag us

if you use this repo in  your project don't forget to mention us as Contributer in it . And Don't forget to tag us [Linkedin](https://www.linkedin.com/in/vaibhav-hariramani-087488186/),[ instagram](https://www.instagram.com/geeky_baba_/?hl=en),[ facebook](https://www.facebook.com/jayesh.hariramani.3) ,[ twitter](https://www.linkedin.com/in/vaibhav-hariramani-087488186/), [ Github](https://github.com/vaibhavhariaramani) 

============================================================================
# Made with ❤️by Vaibhav Hariramani
#### About me

I am a Machine Learning enthusiast, an Actions on Google, Internet of things, Alexa Skills, and Image processing developer.
I have a keen interest in Image processing and Andriod development.
I am Currently studying at  Chandigarh University, Punjab.

[My PortFolio](https://vaibhavhariaramani.github.io/)
You can find me at:-
[Linkedin](https://www.linkedin.com/in/vaibhav-hariramani-087488186/) or [Github](https://github.com/vaibhavhariaramani) .

Email: [vaibhav.hariramani01@gmail.com](mailto:vaibhav.hariramani01@gmail.com)


# Download [THE VAIBHAV HARIRAMANI APP](https://github.com/vaibhavhariaramani/The-Vaibhav-Hariramani-App/raw/master/vaibhav%20hariramani%20app.apk)

# [<img src="https://github.com/vaibhavhariaramani/vaibhavhariaramani/blob/master/icon/gh-bannner-light.png">](https://github.com/vaibhavhariaramani/The-Vaibhav-Hariramani-App/raw/master/vaibhav%20hariramani%20app.apk) 
<p align='center'>
<a href="https://www.linkedin.com/in/vaibhav-hariramani-087488186/"><img height="30" src="https://github.com/vaibhavhariaramani/vaibhavhariaramani/blob/master/icon/linkedin.png"></a>&nbsp;&nbsp;
<a href="https://twitter.com/vaibhavhariram2"><img height="30" src="https://github.com/vaibhavhariaramani/vaibhavhariaramani/blob/master/icon/twitter.png"></a>&nbsp;&nbsp;
<a href="https://www.instagram.com/vaibhav.hariramani/?hl=en"><img height="30" src="https://github.com/vaibhavhariaramani/vaibhavhariaramani/blob/master/icon/instagram.jpg"></a>&nbsp;&nbsp;
<a href="https://www.buymeacoffee.com/vaibhavJii"><img height="30" src="https://github.com/vaibhavhariaramani/vaibhavhariaramani/blob/master/icon/by-me-a-coffee.png"></a>
<a href="https://wa.me/+917790991077"><img height="30" src="https://github.com/vaibhavhariaramani/vaibhavhariaramani/blob/master/icon/whatsapp.png"></a>&nbsp;&nbsp;
<a href="mailto:vaibhav.hariramani01@gmail.com"><img height="30" src="https://github.com/vaibhavhariaramani/vaibhavhariaramani/blob/master/icon/email.png"></a>&nbsp;&nbsp;
</p>


[<img width="150" align='center' src="https://archive.org/download/download-button-png/download-button-png.png">The Vaibhav Hariramani App (Latest Version) ](https://github.com/vaibhavhariaramani/The-Vaibhav-Hariramani-App/raw/master/vaibhav%20hariramani%20app.apk)

Download [THE VAIBHAV HARIRAMANI APP](https://github.com/vaibhavhariaramani/The-Vaibhav-Hariramani-App/raw/master/vaibhav%20hariramani%20app.apk) consist of Tutorials,Projects,Blogs and Vlogs of our Site developed Using Android Studio with Web View try installing it in your android device.

Happy coding ❤️ .

### Follow me
  
[![Linkedin Badge](https://img.shields.io/badge/-VaibhavHariramani-blue?style=flat-circle&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/vaibhav-hariramani-087488186/)](https://www.linkedin.com/in/vaibhav-hariramani-087488186/) [![Instagram Badge](https://img.shields.io/badge/-VaibhavHariramani-e02c73?style=flat-circle&labelColor=e02c73&logo=Instagram&logoColor=white&link=https://www.instagram.com/vaibhav.hariramani/?hl=en)](https://www.instagram.com/vaibhav.hariramani/?hl=en) [![Twitter Badge](https://img.shields.io/badge/-VaibhavHariramani-1ca0f1?style=flat-circle&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/vaibhavhariram2)](https://twitter.com/vaibhavhariram2) [![GitHub Badge](https://img.shields.io/badge/-@Vaibhavhariaramani-24292e?style=flat-circle&labelColor=24292e&logo=github&logoColor=white&link=https://github.com/vaibhavhariaramani)](https://github.com/vaibhavhariaramani) [![Gmail Badge](https://img.shields.io/badge/-VaibhavHariramani-d54b3d?style=flat-circle&labelColor=d54b3d&logo=gmail&logoColor=white&link=mailto:vaibhav.hariramani01@gmail.com)](mailto:vaibhav.hariramani01@gmail.com) [![Medium Badge](https://img.shields.io/badge/-VaibhavHariramani-d54b3d?style=flat-circle&labelColor=d54b3d&logo=medium&logoColor=white&link=https://medium.com/geeky-bawa)](https://medium.com/geeky-bawa) 
