### Data cleaning
All columns not in english has been translated to EN.  
Unnecessary columns are removed.  


### RFM value calculation
RFM(Recency, Frequency, Monetary) values are calculated based on purchase history in fc membership, merchandise, and tickets.    
Season-based R: min 0, max 8. 8 means no transaction history  
Season-based F, M: min 0. 0 means no transaction history  

Monthly-based R: min 0, max 61. 61 means no transaction history  
Monthly-based F, M: min 0. 0 means no transaction history  

Scaling: minmax or logarithm(for better visualization)  

### Clustering
K-means is used for clustering.  

### Classification
Multilabel-multiclass classification with logistic regression, random forest, SVM, and KNN.  

### Evaluation  
K-means: The elbow method; silouhette score  
Classification: Subset accuracy; accuracy ,precision, recall, f1 for each of fc membership, merchandise, and tickets  

### Written paper
The full paper can be found [here](). 