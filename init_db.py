import mysql.connector
from mysql.connector import Error

def create_database_and_table():
    """Initialize the travel_planner database and itineraries table"""
    
    # Database configuration
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'shreyash7710'
    }
    
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        
        print("Connected to MySQL server successfully!")
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS travel_planner")
        print("Database 'travel_planner' created successfully!")
        
        # Use the database
        cursor.execute("USE travel_planner")
        
        # Create itineraries table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS itineraries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            city VARCHAR(255) NOT NULL,
            days INT NOT NULL,
            interests TEXT,
            itinerary JSON,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_city (city),
            INDEX idx_created_at (created_at)
        )
        """
        
        cursor.execute(create_table_query)
        print("Table 'itineraries' created successfully!")
        
        # Insert sample data for testing (optional)
        sample_data = {
            'city': 'New York, USA',
            'days': 2,
            'interests': 'museums, food, architecture',
            'itinerary': '''
            {
                "city": "New York, USA",
                "total_days": 2,
                "overview": "A 2-day exploration of New York focusing on museums, food, and architecture",
                "travel_tips": [
                    "Use public transportation - MetroCard is your best friend",
                    "Book museum tickets in advance to skip lines",
                    "Try street food - hot dogs and pretzels are iconic",
                    "Walk in Central Park early morning for best experience"
                ],
                "daily_itinerary": [
                    {
                        "day": 1,
                        "theme": "Museums and Architecture",
                        "morning": {
                            "time": "9:00 AM - 12:00 PM",
                            "activity": "Metropolitan Museum of Art",
                            "description": "Explore one of the world's largest art museums",
                            "location": "1000 5th Ave, New York, NY"
                        },
                        "afternoon": {
                            "time": "1:00 PM - 5:00 PM",
                            "activity": "Central Park and Architecture Tour",
                            "description": "Walk through Central Park and admire surrounding architecture",
                            "location": "Central Park, New York, NY"
                        },
                        "evening": {
                            "time": "6:00 PM - 9:00 PM",
                            "activity": "Times Square and Dinner",
                            "description": "Experience the bright lights and find a great restaurant",
                            "location": "Times Square, New York, NY"
                        }
                    }
                ],
                "recommended_hotels": [
                    {"name": "The Plaza Hotel", "area": "Midtown", "price_range": "$$$$"},
                    {"name": "Pod Hotels", "area": "Various Locations", "price_range": "$$"}
                ],
                "recommended_restaurants": [
                    {"name": "Katz's Delicatessen", "cuisine": "Jewish Deli", "area": "Lower East Side"},
                    {"name": "Joe's Pizza", "cuisine": "Pizza", "area": "Multiple Locations"}
                ]
            }
            '''
        }
        
        insert_query = """
        INSERT INTO itineraries (city, days, interests, itinerary, created_at)
        VALUES (%(city)s, %(days)s, %(interests)s, %(itinerary)s, NOW())
        """
        
        cursor.execute(insert_query, sample_data)
        connection.commit()
        print("Sample data inserted successfully!")
        
        # Verify table creation
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print(f"Tables in database: {tables}")
        
        cursor.execute("DESCRIBE itineraries")
        columns = cursor.fetchall()
        print("Table structure:")
        for column in columns:
            print(f"  {column}")
        
        cursor.execute("SELECT COUNT(*) FROM itineraries")
        count = cursor.fetchone()[0]
        print(f"Total records in itineraries table: {count}")
        
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    print("Initializing AI Travel Planner Database...")
    create_database_and_table()
    print("Database initialization completed!")