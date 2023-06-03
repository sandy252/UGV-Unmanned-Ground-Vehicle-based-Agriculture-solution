
# UGV (Unmanned Ground Vehicle) based Agriculture solution

UGVs can be operated with or without human presence. UGVs can be used in different areas including agriculture. Here we are focusing only on agriculture. There are a variety of purposes where it can be helpful in agriculture such as soil sampling, irrigation management, precision spraying, mechanical weeding, crop harvesting, and disease detection, etc.

Main objective is: -
1. Collecting different data samples for healthy and infected crops, then using those image samples for training our deep learning model(CNN).
2. Once the model is ready, I will be creating a web app and then deploying the same to cloud. It will be deployed in cloud which will collect the images from the field and classify the crops into various categories i.e., whether that crop is healthy or infected with a certain disease.
3. The other one is crop recommender. this will predict the suitable crop to grow in perticular weather of that area which will help farmers to make decisions accordingly.

## About the Models
### CNN Architecture
![model](https://user-images.githubusercontent.com/66490787/219868725-9701133d-2f97-4fac-8f8b-c6108811dbdf.jpg)


## ScreenShots
### Disease classifier 
![Screenshot (e79)](https://github.com/sandy252/UGV-Unmanned-Ground-Vehicle-based-Agriculture-solution/assets/66490787/c7275a42-c17e-432a-a190-801179471d34)
![Screenshot (80)](https://github.com/sandy252/UGV-Unmanned-Ground-Vehicle-based-Agriculture-solution/assets/66490787/70377a71-8097-415b-8d0e-814f8ac83098)


### crop recommender
![Screenshot e(81)](https://github.com/sandy252/UGV-Unmanned-Ground-Vehicle-based-Agriculture-solution/assets/66490787/8dc46319-7d05-4229-a247-08868a9f092c)


## Run Locally

Clone the project

```bash
  git clone https://github.com/sandy252/UGV-Unmanned-Ground-Vehicle-based-Agriculture-solution.git
```

Go to the project directory

```bash
  cd UGV-Unmanned-Ground-Vehicle-based-Agriculture-solution
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run main.py
```




## Author

- [Sandeep Kashyap](https://www.linkedin.com/in/sandeep-kashyap-aa1545170/)


## Deployment
[Classifier](https://sandy252-potato-disease-classifier-main-lpuiqn.streamlit.app/)





## Lessons Learned

- Working of API and API keys
- Integrating API's to a system.
- Creating and Deploying web apps.

## Support

For support, email kashyapsandeep252@gmail.com or join our Slack channel.
