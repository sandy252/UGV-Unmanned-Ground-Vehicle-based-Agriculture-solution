
# UGV (Unmanned Ground Vehicle) based Agriculture solution

UGVs can be operated with or without human presence. UGVs can be used in different areas including agriculture. Here we are focusing only on agriculture. There are a variety of purposes where it can be helpful in agriculture such as soil sampling, irrigation management, precision spraying, mechanical weeding, crop harvesting, and disease detection, etc.

Main objective is: -
1. Consider one use case such as tomato crop disease detection i.e., you will collect the different data samples for healthy and infected crops, then you will use those image samples for training our deep learning model.
2. Once the model is ready, you will deploy that model using UGV which will collect the images from the field and classify the crops into various categories i.e., whether that crop is healthy or infected with a certain disease.
3. The other one is weather prediction; this will forecast the weather of that area which will help farmers to give the information about temperature, moisture, rain forecast, etc., and will help to make decisions accordingly.

# About the Models
## CNN Architecture
![model](https://user-images.githubusercontent.com/66490787/219868725-9701133d-2f97-4fac-8f8b-c6108811dbdf.jpg)





## ScreenShots
### Home 
![Screenshot (63)](https://user-images.githubusercontent.com/66490787/219869302-ef00bf04-9bb4-4f20-94fb-35120788ae8f.png)
### predictor
![Screenshot (64)](https://user-images.githubusercontent.com/66490787/219869310-f15f7b73-4792-4145-9a5e-fc0268a6804c.png)


## Run Locally

Clone the project

```bash
  git clone https://github.com/sandy252/Potato_Disease_Classifier.git
```

Go to the project directory

```bash
  cd Potato_Disease_Classifier
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run main.py
```




## Authors

- [Sandeep Kashyap](https://www.linkedin.com/in/sandeep-kashyap-aa1545170/)


## Deployment
[Classifier](https://sandy252-potato-disease-classifier-main-lpuiqn.streamlit.app/)





## Lessons Learned

- Working of API and API keys
- Integrating API's to a system.
- Creating and Deploying web apps.

## Support

For support, email kashyapsandeep252@gmail.com or join our Slack channel.
