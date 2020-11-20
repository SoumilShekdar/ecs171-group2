# ECS Group 2 Project Proposal: COVID 19 Test Result Prediction  

In the early days of the COVID 19 pandemic, there was a lack of testing in the United States, which is one of the reasons we could not contain the Pandemic. Today even though COVID 19 tests are available, most of them are still slow requiring multiple days. In addition to this COVID 19 testing might still be an issue in other countries as the pandemic spreads across the world.  
To address this problem we will be developing a Machine Learning model to predict if a COVID 19 test will be positive or not. If successful in its purpose this model could help guide decisions as a person awaits their COVID 19 test results, and in situations where tests are not available at all this model could be used in its place until availability.  
Our project is inspired by the [EHR Dream Challenge](https://www.synapse.org/#!Synapse:syn21849255/wiki/601865) on Synapse.  

### Primary Goal  
Classify the outcome of COVID 19 tests.  

### Secondary Goal  
For positive tests classify outcomes as Hospitalization, ICU, etc.  

### Team  
We will be determining final roles once the project proposal has been approved, and we are confident that we have all the requisite skill sets. Members: Ankit Agarwal, Omar Alsabbagh, Ryan Bui, Lijing Chen, Claude Guo, Eric Hoang, Arhan Khalid, Roberto Lozano, Qingyao Meng, Soumil Shekdar, Alick Sun, and Tony Wu.  

### Dataset  
As of now we plan to only use data provided through the challenge, but this might be subject to change as we start evaluating results from our models and determine feature importance. As a part of the challenge, we will be using EHR data along with biometric data collected before the test. Due to privacy reasons, the data available to us is synthetic data based on the real data in the UW EHR OMOP Repository. We have multiple datasets available to us through the challenge database containing features like medications prescribed, conditions of patients, observations such as blood pressure and heart rate, demographic information, procedures, and laboratory measurements.  

### Data Pre-Processing  
- Feature Selection through p-value, chi score, correlation matrix, and model-based importance.  
- Data preparation including encoding categorical data, normalization, and addressing biases.  

## Machine Learning  
- Train multiple Classification models; Logistic Classification, Lasso Classification, Ridge Classification, Decision Tree Classification, Random Forest Classification, Neural Net Classification, etc.; through libraries (sci-kit learn).  
- For Neural Network-based classifiers we will be implementing multiple Architectures including Dense, CNN, and LSTM through Keras and Tensorflow.
- Develop own implementations of basic Machine Learning Algorithms like Logistic Classification to compare our results with library-based implementations.
- Develop an ensemble model that uses predictions of previous models as inputs.

### Web Application and Visualization  
- Graphs to convey the distribution of predictions as compared to known outcomes, and the relative importance of features in making these predictions.
- Endpoint for inputting data available to you, in order to get a prediction regarding the result of your COVID 19 test if you were to be tested.

