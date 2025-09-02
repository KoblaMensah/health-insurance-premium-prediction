# 📊 Health Insurance Premium Predictor

Predict health insurance premiums based on user demographics and lifestyle factors using a machine learning model deployed with Streamlit.

---

## 📖 Project Overview
This project demonstrates how machine learning can be used to estimate health insurance premiums.  
It includes:
- **Exploratory Data Analysis (EDA)**  
- **Model training** with XGBoost  
- **Model deployment** on Streamlit Cloud  
- **Interactive UI** where users can input their data and get predictions instantly  



## For a Live Demo, try the app here:  
[Health Insurance Premium Predictor](https://health-insurance-premium-prediction-fmensah.streamlit.app)



For a detailed explanation of the project background, dataset, and methodology, see the full report:
[Click to view the report(PDF)](./report.pdf)



## How to Run the app Locally(On your own computer) in bash 

1. Clone the repo:
 ```bash
   git clone https://github.com/KoblaMensah/health-insurance-premium-prediction.git
   cd health-insurance-premium-prediction
```
2. Create a Virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
3. Install all dependancies
```bash
pip install -r requirements.txt
```
4. To run the app:
```bash
streamlit run app.py 
```

