# 🌸 Fergana Flowers - AI-Powered Flower Classifier

Fergana Flowers is launching an online plant and flower store with an AI-powered assistant to help customers identify flowers from images and provide useful information like pricing, availability, and care tips. This project implements a deep learning-based flower classification system using transfer learning on the Oxford Flowers 102 dataset.

---

## 📁 Dataset

- **Name**: Oxford Flowers 102
- **Source**: [Oxford Visual Geometry Group](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html)
- **Images**: 8,189 total
  - 1020 in `trainval` (used for training/validation)
  - 6149 in `test` (used for evaluation)
- **Classes**: 102 flower species

---

## 🧠 Model Architecture

- **Base Model**: ResNet18 (pre-trained on ImageNet)
- **Technique**: Transfer Learning
  - Early layers frozen (feature extractor)
  - Final fully connected layer replaced to output 102 flower classes
- **Framework**: PyTorch

---

## 🏋️‍♂️ Training Details

- **Optimizer**: Adam
- **Loss Function**: CrossEntropyLoss
- **Learning Rate**: 0.001
- **Epochs**: 5
- **Train/Val Split**: 80/20 on `trainval` (1,020 images)

---

## 📊 Results

| Metric                  | Value                                      |
| ----------------------- | ------------------------------------------ |
| **Validation Accuracy** | 90.07% after 5 epochs                      |
| **Test Accuracy**       | 91.38% on official test set (6,149 images) |

---

## 🖥️ Tech Stack

- **Frontend**: Streamlit (image upload, prediction display)
- **Backend**: PyTorch (model training + inference)
- **Deployment-ready Metadata**: JSON catalog with
  - Flower name
  - Price
  - Availability
  - Care tips

---

## 🚀 Features

- Upload an image and identify flower type from 102 categories
- See flower name, price, availability, and care instructions
- Trained using real-world flower photos from the Oxford dataset
- Built with reproducibility and production readiness in mind

---

## 📂 Project Structure
