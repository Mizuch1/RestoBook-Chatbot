# RestoBook Chatbot 🍽️

A sophisticated restaurant reservation chatbot system built with Python, HTML, CSS, and machine learning. This intelligent chatbot helps customers make restaurant reservations, browse menus, and get information about multiple restaurants through an interactive web interface.

## 🌟 Features

### 🤖 Intelligent Chatbot
- **Natural Language Processing**: Understands customer queries and responds conversationally
- **Multi-Restaurant Support**: Handles reservations for multiple restaurants
- **Menu Display**: Shows restaurant menus with descriptions and pricing
- **Reservation Management**: Complete booking system with date/time management

### 🎨 User Interface
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Modern UI**: Clean, intuitive interface with restaurant-themed styling
- **Interactive Elements**: Dynamic forms and real-time responses
- **Multi-Restaurant Showcase**: Beautiful presentation of different restaurants

### 🛠️ Technical Features
- **Machine Learning Model**: Trained on restaurant and reservation data
- **Flask Backend**: Robust Python web framework
- **Static File Management**: Organized CSS and image assets
- **Template System**: Dynamic HTML generation

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

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Flask
- TensorFlow/Keras
- NLTK
- Pickle

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mizuch1/RestoBook-Chatbot.git
   cd RestoBook-Chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install flask tensorflow nltk
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 🎯 Usage

### For Customers
1. **Start a conversation** with the chatbot
2. **Browse restaurants** and their menus
3. **Make reservations** by specifying:
   - Restaurant name
   - Date and time
   - Number of guests
   - Contact information

### For Restaurant Owners
- **Add new restaurants** by updating the restaurant data
- **Modify menus** through the admin interface
- **Manage reservations** in real-time

## 🏗️ Architecture

### Backend (Python/Flask)
- **Chat Processing**: Natural language understanding and response generation
- **Reservation Logic**: Booking validation and confirmation
- **Data Management**: Restaurant and menu information handling

### Frontend (HTML/CSS/JavaScript)
- **User Interface**: Interactive chat interface
- **Responsive Design**: Mobile-first approach
- **Real-time Updates**: Dynamic content loading

### Machine Learning
- **Intent Classification**: Understanding user intentions
- **Entity Recognition**: Extracting dates, times, and restaurant names
- **Response Generation**: Contextually appropriate replies

## 📊 Model Training

The chatbot uses a trained neural network model for understanding natural language. To retrain the model:

```bash
python Training.py
```

This will:
- Process the training data in `data.json`
- Train a new model and save it as `model.h5`
- Update the labels and texts for prediction

## 🎨 Customization

### Adding New Restaurants
1. Add restaurant data to the system
2. Include menu items and descriptions
3. Add restaurant images to the `static/` directory
4. Update the HTML templates as needed

### Styling
- Modify `static/style.css` for visual customization
- Update restaurant-specific styling
- Customize the chat interface appearance

## 🔧 Configuration

Key configuration options in `app.py`:
- **Port**: Change the default port (5000)
- **Debug Mode**: Enable/disable for development
- **Secret Key**: Update for production security

## 🚀 Deployment

### Local Deployment
```bash
python app.py
```

### Production Deployment
- Use a WSGI server like Gunicorn
- Set up a reverse proxy with Nginx
- Configure environment variables for production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with Flask, TensorFlow, and NLTK
- Restaurant images and data are for demonstration purposes
- Inspired by modern chatbot and reservation systems

## 📞 Support

For support and questions:
- Create an issue in the GitHub repository
- Contact the development team

---

**Made with ❤️ for food lovers and restaurant owners**
