# 🌍 AI Travel Planner

**An intelligent full-stack web application that creates personalized travel itineraries using AI technology**

![AI Travel Planner](https://img.shields.io/badge/AI-Travel%20Planner-blue?style=for-the-badge&logo=airplane)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3.3-red?style=for-the-badge&logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange?style=for-the-badge&logo=mysql)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-purple?style=for-the-badge&logo=openai)

## ✨ Features

- 🗺️ **Automatic Location Detection** - Uses browser geolocation to detect your current location
- 🤖 **AI-Powered Itineraries** - Generates personalized travel plans using OpenAI GPT-3.5
- 📅 **Day-wise Planning** - Detailed morning, afternoon, and evening activities
- 🏨 **Smart Recommendations** - AI suggests hotels, restaurants, and attractions
- 💾 **Database Storage** - Saves all itineraries in MySQL for future reference
- 📱 **Responsive Design** - Modern, mobile-friendly interface with Bootstrap 5
- 📄 **PDF Export** - Download your itinerary as a PDF document
- 🌐 **Global Coverage** - Works for any city worldwide
- ⚡ **Real-time Processing** - Fast itinerary generation with loading indicators


## 🌟 Key Features of This Repository:
✅ Professional Documentation - Detailed README with screenshots placeholders
✅ Automated Setup - One-command installation
✅ Docker Support - Easy containerized deployment
✅ CI/CD Pipeline - Automated testing and deployment
✅ Development Tools - Pre-commit hooks, linting, testing
✅ Security - Environment variables, .gitignore
✅ Community Ready - Contributing guide, issue templates


## 🚀 Demo

![Demo GIF](./assets/demo.gif)

### Live Features:
- Enter your interests (museums, food, adventure, etc.)
- Select trip duration (1-7 days)
- Get AI-generated detailed itineraries
- View recommendations for hotels and restaurants
- Download as PDF for offline use

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Technologies Used](#technologies-used)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- MySQL Server 8.0+
- OpenAI API key
- Modern web browser with geolocation support

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/shreyashpatil530/ai-travel-planner.git
cd ai-travel-planner
```

2. **Create virtual environment**
```bash
python -m venv travel_planner_env

# Windows
travel_planner_env\Scripts\activate

# macOS/Linux
source travel_planner_env/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup MySQL Database**
```bash
# Start MySQL service
# Run the database setup
python database.py
```

5. **Configure API Keys**
Edit `app.py` and update your OpenAI API key:
```python
OPENAI_API_KEY = "your-openai-api-key-here"
```

6. **Run the application**
```bash
python app.py
```

7. **Open in browser**
Navigate to `http://localhost:5000`

## 📖 Usage

### Basic Usage

1. **Detect Location**: Click "Detect My Location" to get your current coordinates
2. **Set Preferences**: Select number of days (1-7) and enter your interests
3. **Generate**: Click "Generate Itinerary" to create your personalized plan
4. **Review**: Browse through day-by-day activities, hotel and restaurant recommendations
5. **Export**: Download your itinerary as a PDF for offline access

### Example Input

```
Days: 3
Interests: museums, food, architecture, history
Location: Automatically detected (e.g., New York, USA)
```

### Example Output

The AI will generate a detailed 3-day itinerary including:
- **Morning activities** (9:00 AM - 12:00 PM)
- **Afternoon activities** (1:00 PM - 5:00 PM) 
- **Evening activities** (6:00 PM - 9:00 PM)
- **Hotel recommendations** with price ranges
- **Restaurant suggestions** with cuisine types
- **Travel tips** specific to the destination

## 🔌 API Documentation

### Generate Itinerary

**POST** `/generate`

**Request Body:**
```json
{
    "lat": 40.7128,
    "lon": -74.0060,
    "days": 3,
    "interests": "museums, food, architecture"
}
```

**Response:**
```json
{
    "success": true,
    "itinerary_id": 123,
    "itinerary": {
        "city": "New York, USA",
        "total_days": 3,
        "overview": "A 3-day exploration of New York...",
        "daily_itinerary": [...],
        "recommended_hotels": [...],
        "recommended_restaurants": [...],
        "travel_tips": [...]
    }
}
```

### Get All Itineraries

**GET** `/itineraries`

Returns all saved itineraries from the database.

## 🗄️ Database Schema

### `itineraries` Table

```sql
CREATE TABLE itineraries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    days INT NOT NULL,
    interests TEXT,
    itinerary JSON,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### Sample Data Structure

```json
{
    "city": "Paris, France",
    "total_days": 4,
    "overview": "A romantic 4-day journey...",
    "daily_itinerary": [
        {
            "day": 1,
            "theme": "Classic Paris",
            "morning": {
                "time": "9:00 AM - 12:30 PM",
                "activity": "Louvre Museum",
                "description": "Explore the world's largest art museum",
                "location": "Rue de Rivoli, 75001 Paris"
            }
        }
    ],
    "recommended_hotels": [...],
    "recommended_restaurants": [...],
    "travel_tips": [...]
}
```

## 🧰 Technologies Used

### Backend
- **Flask 2.3.3** - Python web framework
- **MySQL 8.0+** - Database with JSON support
- **OpenAI API** - GPT-3.5-turbo for itinerary generation
- **OpenStreetMap Nominatim** - Geolocation to city conversion

### Frontend
- **HTML5 & CSS3** - Semantic markup and modern styling
- **JavaScript ES6+** - Interactive functionality
- **Bootstrap 5** - Responsive UI framework
- **Font Awesome** - Icon library
- **jsPDF** - Client-side PDF generation

### APIs & Services
- **OpenAI GPT-3.5-turbo** - AI-powered content generation
- **Nominatim API** - Reverse geocoding
- **Browser Geolocation API** - Location detection

## ⚙️ Configuration

### Environment Variables (Recommended)

Create a `.env` file:

```env
OPENAI_API_KEY=your-openai-api-key
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your-password
MYSQL_DATABASE=travel_planner
FLASK_ENV=development
```

### Database Configuration

Update `app.py` with your MySQL credentials:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your-password',
    'database': 'travel_planner'
}
```

## 📁 Project Structure

```
ai-travel-planner/
├── app.py                      # Main Flask application
├── database.py                 # Database operations and management
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── LICENSE                     # MIT License
├── .gitignore                 # Git ignore file
├── .env.example               # Environment variables template
├── templates/
│   └── index.html             # Main frontend template
├── static/
│   ├── css/
│   │   └── style.css         # Custom styles (optional)
│   ├── js/
│   │   └── script.js         # Custom JavaScript (optional)
│   └── images/
│       └── logo.png          # App logo
├── sql/
│   ├── schema.sql            # Database schema
│   ├── sample_data.sql       # Sample data insertion
│   └── queries.sql           # Useful SQL queries
├── docs/
│   ├── API.md               # API documentation
│   ├── SETUP.md             # Detailed setup guide
│   └── TROUBLESHOOTING.md   # Common issues and solutions
├── tests/
│   ├── test_app.py          # Application tests
│   ├── test_database.py     # Database tests
│   └── test_api.py          # API endpoint tests
└── assets/
    ├── demo.gif             # Demo animation
    └── screenshots/         # Application screenshots
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Add tests for new features**
5. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Add docstrings to all functions
- Include unit tests for new features
- Update documentation for any API changes
- Test across different browsers and devices

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_app.py

# Run with coverage
python -m pytest --cov=app
```

## 🚨 Troubleshooting

### Common Issues

1. **Location Detection Failed**
   - Enable location services in your browser
   - Use HTTPS for production deployment

2. **OpenAI API Errors**
   - Verify your API key is valid
   - Check your OpenAI account credits
   - Monitor rate limits

3. **Database Connection Issues**
   - Ensure MySQL service is running
   - Verify database credentials
   - Check firewall settings

4. **PDF Download Not Working**
   - Ensure jsPDF library loads correctly
   - Check browser compatibility

For more detailed troubleshooting, see [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for providing the GPT API
- [OpenStreetMap](https://www.openstreetmap.org/) for the Nominatim geocoding service
- [Bootstrap](https://getbootstrap.com/) for the responsive UI framework
- [Font Awesome](https://fontawesome.com/) for the beautiful icons

## 📞 Support

If you have any questions or need help:

- 📧 Email: shreyashpatil539@gmail.com.com

- 📝 Issues: [GitHub Issues](https://github.com/shreyashpatil530/ai-travel-planner/issues)

## 🗺️ Roadmap

### Version 2.0 (Coming Soon)
- [ ] User authentication and profiles
- [ ] Social itinerary sharing
- [ ] Weather integration
- [ ] Budget planning features
- [ ] Multi-language support
- [ ] Mobile app (React Native)

### Version 3.0 (Future)
- [ ] Real-time collaboration
- [ ] AI chat assistant
- [ ] Booking integration
- [ ] Offline map support
- [ ] AR navigation features

---

⭐ **Star this repository if you found it helpful!** ⭐

Made with ❤️ by shreyash patil*(https://github.com/shreyashpatil530)
