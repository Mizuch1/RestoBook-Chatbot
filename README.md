# RestoBook Chatbot 🍽️

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/) [![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/) [![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org/) [![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://html.spec.whatwg.org/) [![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A sophisticated restaurant reservation chatbot system built with Python, HTML, CSS, and machine learning. This intelligent chatbot helps customers make restaurant reservations, browse menus, and get information about multiple restaurants through an interactive web interface.

---

## ✨ Features

This application provides a comprehensive restaurant reservation experience with intelligent automation and modern web design:

### 🤖 Intelligent Chatbot
- **Natural Language Processing**: Understands customer queries and responds conversationally
- **Multi-Restaurant Support**: Handles reservations for multiple restaurants
- **Menu Display**: Shows restaurant menus with descriptions and pricing
- **Reservation Management**: Complete booking system with date/time management
- **Smart Responses**: Context-aware replies based on user intent

### 🎨 User Interface
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Modern UI**: Clean, intuitive interface with restaurant-themed styling
- **Interactive Elements**: Dynamic forms and real-time responses
- **Multi-Restaurant Showcase**: Beautiful presentation of different restaurants
- **Real-time Updates**: Live chat interface with instant responses

### 🛠️ Technical Features
- **Machine Learning Model**: Trained on restaurant and reservation data
- **Flask Backend**: Robust Python web framework
- **Static File Management**: Organized CSS and image assets
- **Template System**: Dynamic HTML generation
- **Session Management**: Persistent user sessions for better UX

### 📱 Restaurant Management
- **Menu Management**: Easy menu updates and modifications
- **Reservation Tracking**: Real-time reservation status monitoring
- **Multi-location Support**: Handle multiple restaurant branches
- **Customer Database**: Store customer preferences and history

*(For detailed feature implementation status, see project documentation)*

---

## 🛠️ Tech Stack

- **Backend Framework:** Python Flask for web server and API endpoints
- **Machine Learning:** TensorFlow/Keras for natural language processing
- **Frontend:** HTML5, CSS3, and vanilla JavaScript for responsive UI
- **Data Processing:** NLTK for text processing and tokenization
- **Data Storage:** JSON for configuration, Pickle for ML model persistence
- **Web Server:** Flask development server with production deployment support
- **Development Tools:** Git & GitHub for version control

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python** (version 3.8 or later recommended)
- **pip** package manager (usually included with Python)
- **Git** for version control
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Mizuch1/RestoBook-Chatbot.git
cd RestoBook-Chatbot
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install flask tensorflow nltk numpy
```

### 3. Download Required NLTK Data

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
```

### 4. Run the Application

Start the Flask development server:

```bash
python app.py
```

### 5. Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

---

## 📁 Project Structure

```
RestoBook-Chatbot/
├── app.py                 # Main Flask application
├── Training.py           # Machine learning model training
├── data.json             # Training data for the chatbot
├── model.h5              # Trained ML model
├── labels.pkl            # Model labels
├── texts.pkl             # Tokenized texts
├── static/               # Static assets
│   ├── style.css         # Main stylesheet
│   └── [restaurant-images] # Restaurant photos
├── templates/            # HTML templates
│   ├── index.html        # Main page
│   ├── menu-la.html      # Menu display
│   └── [restaurant-pages] # Individual restaurant pages
└── README.md             # This file
```

---

## 🎯 Usage

### For Customers
1. **Start a conversation** with the chatbot on the main page
2. **Browse restaurants** and their menus by asking about available options
3. **Make reservations** by specifying:
   - Restaurant name
   - Date and time
   - Number of guests
   - Contact information

### For Restaurant Owners
- **Add new restaurants** by updating the restaurant data in the system
- **Modify menus** through the configuration files
- **Manage reservations** in real-time through the web interface
- **Customize responses** by training the model with new data

---

## 🏗️ Architecture

### Backend (Python/Flask)
- **Chat Processing**: Natural language understanding and response generation
- **Reservation Logic**: Booking validation and confirmation system
- **Data Management**: Restaurant and menu information handling
- **Session Control**: User session management for personalized experience

### Frontend (HTML/CSS/JavaScript)
- **User Interface**: Interactive chat interface with modern design
- **Responsive Design**: Mobile-first approach for all devices
- **Real-time Updates**: Dynamic content loading and live responses
- **Form Validation**: Client-side validation for better UX

### Machine Learning
- **Intent Classification**: Understanding user intentions from natural language
- **Entity Recognition**: Extracting dates, times, restaurant names, and numbers
- **Response Generation**: Contextually appropriate and helpful replies
- **Model Training**: Continuous learning from new conversation data

---

## 📊 Model Training

The chatbot uses a trained neural network model for understanding natural language:

```bash
python Training.py
```

**Training Process:**
- Process the training data in `data.json`
- Train a new neural network model
- Save the trained model as `model.h5`
- Update labels and tokenized texts for prediction
- Validate model accuracy with test data

---

## 🎨 Customization

### Adding New Restaurants
1. Add restaurant data to the system configuration
2. Include menu items with descriptions and pricing
3. Add restaurant images to the `static/` directory
4. Update HTML templates for new restaurant pages
5. Retrain the model with new restaurant data

### Styling Customization
- Modify `static/style.css` for visual customization
- Update restaurant-specific color schemes
- Customize the chat interface appearance
- Add responsive breakpoints for different devices

---

## 🔧 Configuration

Key configuration options in `app.py`:
- **Port**: Change the default port (5000)
- **Debug Mode**: Enable/disable for development
- **Secret Key**: Update for production security
- **Session Timeout**: Configure user session duration

---

## 🚀 Deployment

### Local Deployment
```bash
python app.py
```

### Production Deployment Options
- **WSGI Server**: Use Gunicorn for production deployment
- **Reverse Proxy**: Set up Nginx for load balancing
- **Environment Variables**: Configure for production settings
- **SSL/TLS**: Enable HTTPS for secure connections

### Deployment Commands
```bash
# Install production server
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Or use Waitress (Windows)
pip install waitress
waitress-serve --listen=0.0.0.0:5000 app:app
```

---

## 📸 Screenshots
soon

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Mizuch1/RestoBook-Chatbot/issues).

### How to Contribute:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📊 Architecture & Diagrams

For detailed architecture diagrams and system design documentation, refer to the project documentation.

---

## 👤 Author

**Mohamed Jbilou (Mizuchi)**

- GitHub: [@Mizuch1](https://github.com/Mizuch1)
- Email: `mohamed.jbilou.it@gmail.com`

---

## 🙏 Acknowledgments

- Built with ❤️ using Flask, TensorFlow, and modern web technologies
- Special thanks to the open-source community for amazing tools and libraries
- Restaurant images and sample data are for demonstration purposes
- Inspired by modern chatbot and reservation systems

---

```python
# project_info.py

class ProjectInfo:
    def __init__(self, project_name, author, year):
        self.project_name = project_name
        self.author = author
        self.year = year

    def display_info(self):
        return f"© {self.year} {self.author}. All rights reserved."

    def signature(self):
        return f"Built with passion by {self.author}"

# Usage
if __name__ == "__main__":
    resto_chatbot = ProjectInfo(
        project_name="RestoBook Chatbot",
        author="Mohamed Jbilou (Mizuchi)",
        year=2025
    )
    print(resto_chatbot.display_info())
    print(resto_chatbot.signature())
    print("May your reservations be smooth and your code bug-free! 🍽️")
```

---

_Made with ☕ and 💻 by Mizuchi_
