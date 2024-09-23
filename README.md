# Restaurant Rating Prediction

### Summary:

In this project, the primary objective was to predict restaurant ratings based on various features from the Zomato dataset. The approach involved classic machine learning tasks such as Data Exploration, Data Cleaning, Feature Engineering, and Model Building. Extensive Exploratory Data Analysis (EDA) was performed to understand the dataset and draw insights for building the model.

Key insights from the EDA revealed that:
- **Online orders** are more frequent compared to offline orders, with around 30,000 online orders versus 23,000 offline orders.
- **Delivery** is the most preferred type of service (50.2%), followed by **Dine-out** (34.4%).
- Locations like **BTM** and **Koramangala** have the most restaurants compared to other areas.
- **North Indian**, **Chinese**, and **South Indian** cuisines are the most popular choices.
- The most common restaurant types are **Quick Bites** and **Casual Dining**.
- The top 20 restaurant locations and top 20 famous restaurants in the city were identified.
- The preferred cost for two people is **₹300**, with around 7,000 orders in that range.

Following the data analysis, the data was encoded and prepared for machine learning model building. Various regression models were implemented, including:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost
- XGBoost with Cross-Validation (CV)

Among these models, **XGBoost with Cross-Validation** performed the best and was chosen for deployment. The final model and label encoders were saved as pickle files, and the solution was deployed using Flask.

### Conclusion:

This project successfully built a predictive model for restaurant ratings based on features such as online order availability, type of service, location, cuisine, and cost for two people. The insights gained from EDA helped in understanding customer preferences and trends in the restaurant industry. The **XGBoost with Cross-Validation** model was found to be the most effective and was deployed to provide rating predictions. This solution could help Zomato restaurants better understand the factors influencing their ratings and make data-driven decisions to improve their services.
