# Chapter 16:
## Vocabulary
### Black box algorithms: 
One whose logic is not interpretable by humans either due to its complexity or due to its logic being represented in a convoluted manner.

•	Many algorithms (especially those within machine learning sphere) are often termed “black box” due to their opaque nature.

•	Neural networks are quintessential examples of black box models.

### White box algorithm: 
One whose logic is visible and understandable to a human.

### Explainability (in context of machine learning): 
The clarity with which we can understand and interpret a machine learning model’s decision.

•	Gauges how comprehensible an algorithm’s inner workings and decision pathways are to human cognition.

### A global explainability strategy: 
Strategy to provide the details of the formulation of a model.

### A local explainability strategy: 
Strategy to provide the rationale for a single individual prediction made by our trained model.

•	Aim is to provide transparency for each individual decision.

### Testing with Concept Activation Vectors (TCAV): 
Used to provide explainability for image classification models. 

•	Depends on calculating directional derivatives to quantify the degree of the relationship between a user-defined concept and the classification of pictures.

### Model-specific strategies:
Apply to certain types of models.

### Model-agnostic strategies: 
Can be applies to a wide variety of models.

### Local Interpretable Model-Agnostic Explanations (LIME): 
A model-agnostic approach that can explain individual predictions made by a trained model. 

•	Since it is model-agnostic, it can explain the predictions of most types of trained machine learning models.

•	Explains decisions by inducing small changes to the input for each instance.

•	Can gather the effects on the local decision boundary for that instance.

•	Iterates over the loop to provide details for each variable.


## Misc. Notes
Even the most sophisticated algorithms are based on simplification and assumptions and cannot handle surprises.

Black box and white box are definitive(?) categorizations that indicate either complete opacity or transparency, respectively. Not a gradient or spectrum where an algorithm can be somewhat black or white.