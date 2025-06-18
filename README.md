# American Sign Language (ASL) Alphabet Detection

Welcome to my ASL Alphabet Detection project. This is something I poured a lot of effort into, and I’m excited to share it with you. It’s a full-stack deep learning application designed to recognize static American Sign Language (ASL) hand signs (A-Z) in real-time using your webcam. Whether you’re a developer, a student, or just curious about how AI can interpret sign language, I hope you’ll find this project as fascinating as I do.

## What Does This Project Do?

This project uses a trained Convolutional Neural Network (CNN) to classify ASL hand signs. Here’s what it can do:

- Detect and classify static ASL hand signs in real-time using your webcam.
- Provide a user-friendly web interface for live predictions and image uploads.
- Help you explore the amazing intersection of computer vision and sign language.

## How Does It Work?

1. **Dataset**: I used the [ASL Alphabet Dataset](https://www.kaggle.com/grassknoted/asl-alphabet), which contains thousands of labeled images for each ASL letter.
2. **Preprocessing**: The images are resized, normalized, and augmented to prepare them for training.
3. **Model**: A custom CNN is trained to classify the ASL signs. It achieves high accuracy and is optimized for real-time inference.
4. **Webcam Inference**: OpenCV captures video frames, preprocesses them, and feeds them into the trained model for predictions.
5. **Web App**: A Flask-based web app provides an intuitive interface for you to interact with the model.

## Key Features

- **Real-Time Detection**: The model can track your hand movements and display the letter you’re signing.
- **Interactive Web App**: Use the web app to test the model with your webcam or uploaded images.
- **Extensive Documentation**: Jupyter notebooks guide you through preprocessing, training, and evaluation.
- **Customizable**: The codebase is modular, making it easy to adapt for other sign language datasets or tasks.

## Project Structure

```plaintext
project-root/
├── app/                # Flask web app (HTML, CSS, JS, app.py)
├── data/               # ASL dataset (see data/README.md)
├── models/             # Trained model files (not tracked by git)
├── notebooks/          # Jupyter Notebooks (preprocessing, training, inference)
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignore data/models, envs, etc.
└── README.md           # Project documentation
```

## How to Get Started

1. **Clone the Repository**:

   ```bash
   git clone <your-repo-url>
   cd <project-root>
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Dataset**:
   - Follow the instructions in `data/README.md` to download and set up the ASL Alphabet Dataset.

4. **Run the Notebooks**:
   - Use the Jupyter notebooks in the `notebooks/` folder to preprocess the data, train the model, and evaluate its performance.

5. **Start the Web App**:

   ```bash
   python app/app.py
   ```

6. **Open Your Browser**:
   - Navigate to `http://127.0.0.1:5000` to start using the ASL detection app.

## Why This Project Matters

Sign language is a vital form of communication for millions of people worldwide. By leveraging AI and computer vision, I hope this project can help bridge the gap between sign language users and technology, making communication more accessible and inclusive.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Thank you for checking out my project! If you have any questions, suggestions, or feedback, I’d love to hear from you.
