# American Sign Language (ASL) Alphabet Detection

This project is a full-stack deep learning application for real-time American Sign Language (ASL) alphabet recognition using your webcam. It combines computer vision, a convolutional neural network (CNN), and a Flask web interface.

## Project Overview
- **Goal:** Detect static ASL hand signs (A-Z) from webcam or uploaded images and classify them in real-time.
- **Tech Stack:** Python, TensorFlow/Keras, OpenCV, Flask, Bootstrap, Jupyter Notebooks.

## Key Features
- **Dataset:** Uses the [ASL Alphabet Dataset](https://www.kaggle.com/grassknoted/asl-alphabet) (not included in repo; see `data/README.md` for download instructions).
- **Preprocessing:** Jupyter notebook for image resizing, normalization, label encoding, and augmentation.
- **Model:** Custom CNN (or MobileNetV2/EfficientNet) for classification, with training and evaluation notebooks.
- **Webcam Inference:** Real-time hand sign detection using OpenCV and the trained model.
- **Flask Web App:** User-friendly interface for live webcam predictions and image uploads.
- **Clean Repo:** Large datasets and models are excluded from version control (see `.gitignore`).

## Project Structure

```
project-root/
├── app/                # Flask web app (HTML, CSS, JS, app.py)
├── data/               # ASL dataset (see data/README.md)
├── models/             # Trained model files (not tracked by git)
├── notebooks/          # Jupyter Notebooks (preprocessing, training, inference)
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignore data/models, envs, etc.
└── README.md           # Project documentation
```

## Quick Start
1. **Clone the repo:**
   ```bash
   git clone <your-repo-url>
   cd <project-root>
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Download the dataset:**
   - See `data/README.md` for instructions.
4. **Run the notebooks:**
   - Preprocess data, train, and evaluate the model in `notebooks/`.
5. **Start the web app:**
   ```bash
   python app/app.py
   ```
6. **Open your browser:**
   - Go to `http://127.0.0.1:5000` to use the ASL detection app.

## License
MIT License. See `LICENSE` file for details.
