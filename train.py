"""
Smart Crop Advisory System - Training Script

This script trains a machine learning model to predict the most suitable crop
based on environmental and soil parameters.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os


def load_data(filepath='sample_crop_data.csv'):
    """Load the crop dataset from CSV file."""
    print(f"Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    print(f"Data loaded successfully! Shape: {df.shape}")
    print(f"\nDataset preview:")
    print(df.head())
    print(f"\nCrop distribution:")
    print(df['crop'].value_counts())
    return df


def prepare_data(df):
    """Prepare features and target variables for training."""
    print("\nPreparing data for training...")
    
    # Separate features and target
    X = df.drop('crop', axis=1)
    y = df['crop']
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Testing set size: {X_test.shape[0]}")
    
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    """Train a Random Forest classifier."""
    print("\nTraining Random Forest model...")
    
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    print("Model training completed!")
    
    return model


def evaluate_model(model, X_test, y_test):
    """Evaluate the trained model."""
    print("\nEvaluating model performance...")
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nModel Accuracy: {accuracy:.2%}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    return accuracy


def save_model(model, filepath='crop_model.pkl'):
    """Save the trained model to disk."""
    print(f"\nSaving model to {filepath}...")
    joblib.dump(model, filepath)
    print("Model saved successfully!")


def main():
    """Main training pipeline."""
    print("=" * 60)
    print("Smart Crop Advisory System - Model Training")
    print("=" * 60)
    
    # Load data
    df = load_data()
    
    # Prepare data
    X_train, X_test, y_train, y_test = prepare_data(df)
    
    # Train model
    model = train_model(X_train, y_train)
    
    # Evaluate model
    accuracy = evaluate_model(model, X_test, y_test)
    
    # Save model
    save_model(model)
    
    print("\n" + "=" * 60)
    print("Training pipeline completed successfully!")
    print(f"Final Model Accuracy: {accuracy:.2%}")
    print("=" * 60)


if __name__ == '__main__':
    main()
