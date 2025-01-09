# **Pixify 🎨**  
Transform your images like a pro with Pixify! An interactive, cloud-powered image editing tool designed for users who want to resize, enhance, and customize their images effortlessly.

---

## **Overview**  
Pixify is a user-friendly web application built with **Streamlit** and powered by **Cloudinary** for real-time image manipulation. It offers a sleek and intuitive interface to upload images, apply effects, resize, and add text layers. The app is perfect for casual users, content creators, and developers exploring cloud-based image processing.

---

## **Features**  
- **Real-Time Resizing**: Scale, fit, crop, and customize image dimensions seamlessly.  
- **Image Effects**: Apply blur, grayscale, or pixelate portions of your image with a single click.  
- **Text Layers**: Add customizable text overlays with font, size, color, and positioning options.  
- **Live Comparisons**: Compare original and edited images side by side using a dynamic slider.  
- **Download Ready**: Instantly download your edited images in high quality.

---

## **Tech Stack**  
- **Frontend**: [Streamlit](https://streamlit.io) for building the interactive user interface.  
- **Cloud Integration**: [Cloudinary](https://cloudinary.com) for image processing and hosting.  
- **Visualization**: `streamlit-image-comparator` for side-by-side image comparisons.  
- **Programming Language**: Python.

---

## **Getting Started**

### **Prerequisites**
- Python 3.8 or higher installed on your local machine.
- A Cloudinary account. (Sign up [here](https://cloudinary.com/))
- API keys for Cloudinary.

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-github-username/Pixify.git
   cd Pixify
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up API keys:
   - Create a `.streamlit/secrets.toml` file in the project directory:
     ```toml
     [cloudinary]
     cloud_name = "your_cloudinary_cloud_name"
     api_key = "your_cloudinary_api_key"
     api_secret = "your_cloudinary_api_secret"
     ```

5. Run the application:
   ```bash
   streamlit run main.py
   ```

6. Open the app in your browser at `http://localhost:8501`.

---

## **Usage Instructions**

1. **Choose an Input Method**:
   - Upload an image from your device or take a picture using your webcam.  
2. **Select an Operation**:
   - Resize, apply effects, or add text layers.  
3. **Customize Parameters**:
   - Specify dimensions, effects, or text properties to fine-tune your image.  
4. **Preview and Download**:
   - View the output in real-time and download the edited image.  
