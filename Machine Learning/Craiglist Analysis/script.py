# Load libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Set seed
np.random.seed(3)

# Import data
housing = pd.read_csv('craigslist.csv')

# Fit model1
model1 = sm.OLS.from_formula('price ~ type + sqfeet + beds + baths', data=housing).fit()
# Fit model2
model2 = sm.OLS.from_formula('price ~ type + sqfeet + beds + baths + comes_furnished + laundry_options + parking_options + smoking_allowed ', data=housing).fit()
# Fit model3
model3 = sm.OLS.from_formula('price ~ type + sqfeet + beds + baths + comes_furnished + laundry_options + parking_options + smoking_allowed  + cats_allowed + dogs_allowed', data=housing).fit()

# Print R-squared for all models
print("R^2 Model 1: ", model1.rsquared)
print("R^2 Model 2: ", model2.rsquared)
print("R^2 Model 3: ", model3.rsquared)

print("\n")

# Print adjusted R-squared for all models
print("adjusted R^2 Model 1: ", model1.rsquared_adj)
print("adjusted R^2 Model 2: ", model2.rsquared_adj)
print("adjusted R^2 Model 3: ", model3.rsquared_adj)

print("\n")

# Run an F test comparing model2 and model3
from statsmodels.stats.anova import anova_lm

anova_results = anova_lm(model2,model3)
print(anova_results.round(2))

print("\n")

models = [model1, model2, model3]
LLF_list = []
AIC_list = []
BIC_list = []

for m in models:
  LLF_list.append((m.llf).round(2))
  AIC_list.append((m.aic).round(2))
  BIC_list.append((m.bic).round(2))

# Print log likelihood for all models
for i in range(3):
  print(f"Metrics of model {i+1}")
  print("-----------------------")
  print(f"Log-likelihood of Model {i+1}: ", LLF_list[i])
  print(f"AIC of Model {i+1}: ", AIC_list[i])
  print(f"BIC of Model {i+1}: ", BIC_list[i])
  print("\n")

print(min(LLF_list),min(AIC_list),min(BIC_list))


# Split housing data
indices = range(len(housing))
s = int(0.8*len(indices))
train_ind = np.random.choice(indices, size = s, replace = False)
test_ind = list(set(indices) - set(train_ind))
housing_train = housing.iloc[train_ind]
housing_test = housing.iloc[test_ind]

# Fit model2 with training data
model2_train = sm.OLS.from_formula('price ~ type + sqfeet + beds + baths + comes_furnished + laundry_options + parking_options + smoking_allowed ', data=housing_train).fit()

# Fit model3 with training data
model3_train = sm.OLS.from_formula('price ~ type + sqfeet + beds + baths + comes_furnished + laundry_options + parking_options + smoking_allowed  + cats_allowed + dogs_allowed', data=housing_train).fit()


# Calculate predicted price based on model2
fitted_mod2 = model2_train.predict(housing_test)

# Calculate predicted price based on model3
fitted_mod3 = model3_train.predict(housing_test)

# Calculate PRMSE for model2
prmse2 = np.mean((housing_test.price-fitted_mod2)**2)**.5

# Calculate PRMSE for model3
prmse3 = np.mean((housing_test.price-fitted_mod3)**2)**.5

print("\n")

# Print PRMSE for both models
print("predicted root mean squared error (PRMSE) of model 2: ", prmse2)
print("predicted root mean squared error (PRMSE) of model 3: ", prmse3)
