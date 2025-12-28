ML Challenge 2025: Smart Product Pricing Solution

Team Name:   FireBlazer
Team Members:   Chinmay Sinha, Neha Amin, Aman Deol
Submission Date:   October 12, 2025

---

1. Executive Summary

Our solution predicts product prices by engineering a rich, multi-modal feature set from text, image, and structured data. We combine deep learning-based embeddings with high-signal handcrafted features, such as a target-encoded brand feature, to feed into a robust   ensemble of LightGBM and XGBoost models  , whose predictions are averaged for the final output.

---

  2. Methodology Overview

   2.1 Problem Analysis

Our initial Exploratory Data Analysis (EDA) revealed several key insights that guided our approach:
    Skewed Price Distribution:   The target variable, `price`, was heavily right-skewed. To handle this, we opted to predict `log(price + 1)` and inverse-transform the final predictions, which stabilizes model training.
    Semi-Structured Text:   The `catalog_content` field contained valuable structured data like `Pack_Size` and `Value`, which we parsed using regular expressions.
    Implicit Brand Signal:   Brand name, a critical driver of price, was not an explicit feature. We identified it as the most important feature to extract from the item name.
    Visual Importance:   Product images contain implicit information about brand tier, quality, and product type, making them essential for accurate prediction.

   2.2 Solution Strategy

Our high-level strategy is a multi-modal ensemble approach focused on robust feature engineering.

    Approach Type:   Ensemble Model (Averaging).
    Core Innovation:   The primary driver of performance is our feature engineering pipeline, specifically the creation of a   target-encoded brand feature  . This provides the model with a powerful, explicit signal about a brand's average price point, which is more effective than relying on the model to infer this information from embeddings alone.

---

  3. Model Architecture

   3.1 Architecture Overview

Our architecture is a parallel, two-model ensemble. Raw data is processed through three distinct feature engineering pipelines, concatenated, and then fed into both a LightGBM and an XGBoost model. The final prediction is the simple average of the outputs from these two models.



  Flow:  
`Raw Data (Text, Image, ID)` -> `[Text Pipeline, Image Pipeline, Numerical Pipeline]` -> `Concatenated Feature Vector` -> `[LightGBM, XGBoost]` -> `Average Predictions` -> `Final Price`

   3.2 Model Components

  Text Processing Pipeline:  
    Preprocessing steps:   Removed boilerplate text (e.g., "Item Name:", "Bullet Point:").
    Model type:   `SentenceTransformer ('all-MiniLM-L6-v2')` to generate 384-dimensional semantic embeddings.

  Image Processing Pipeline:  
    Preprocessing steps:   Downloaded images from URLs, resized to 224x224, and normalized.
    Model type:   `timm ('efficientnet_b0')` pre-trained on ImageNet, used as a feature extractor to generate 1280-dimensional visual embeddings.

  Final Regression Models:  
1.    XGBoost (`XGBRegressor`):   A robust gradient boosting model known for high performance.
        Key parameters:   Both models were tuned with strong regularization (`max_depth`, `subsample`, `lambda`, `alpha`) to combat the severe overfitting observed in initial experiments.

---

  4. Feature Engineering

Our approach prioritized creating explicit, high-signal features over relying solely on general-purpose embeddings.

1.    Text & Image Embeddings:   As described in the architecture section.

2.    Parsed & Transformed Features:  
      `Pack_Size`, `Value`, `Unit`: Extracted using regex.
      `Pack_Size_log`, `Value_log`: Log-transformed to handle skewed distributions.

3.    Advanced Handcrafted Features:  
      `brand_encoded`: The product brand, extracted from the item name and label-encoded.
      `item_size`: The calculated size of a single item in a pack (`Value` / `Pack_Size`).
      `desc_length`: The character length of the cleaned text content.
        `brand_mean_price` (Target Encoding):   The most impactful feature. For each brand, we calculated its average price using a safe, K-Fold encoding strategy to prevent data leakage. This directly informs the model of each brand's price tier.

---

  5. Model Performance

   5.1 Validation Results
    SMAPE Score:   Our final ensemble approach, including the advanced features, achieved a cross-validation   SMAPE score below 52%  , 
---

  6. Conclusion

Our solution successfully addresses the product pricing challenge by combining the strengths of deep learning embeddings with insightful, handcrafted features. The key to our success was overcoming severe overfitting through aggressive regularization and robust K-Fold validation. The ensemble of LightGBM and XGBoost provided a stable and highly accurate final model, demonstrating that a hybrid approach is superior to relying on a single model or feature type.

---