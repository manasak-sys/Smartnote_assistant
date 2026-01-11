# Smartnote_assistant
A Django REST API project that generates text summaries with different tones using token-based authentication.

# SmartNote Assistant

## Description
SmartNote Assistant is a backend-based application developed using Django REST Framework. It allows users to generate summaries with different tones using a secured API. Authentication is handled using token-based authentication, and API testing is performed using Postman.

## Technologies Used
- Python
- Django
- Django REST Framework
- Token Authentication
- SQLite
- Postman

## Features
- Token-based authentication
- Secure API access using tokens
- Generate text summaries
- Support for multiple summary tones
- Admin panel to manage original text and summaries
- RESTful API endpoints

## Workflow
1. Admin adds original text and tone options in the Django admin panel.
2. User generates an authentication token.
3. Token is passed in Postman headers.
4. API URL is used to fetch summaries with selected tones.
5. Summary output is returned in JSON format.

## API Usage
- Generate token using authentication endpoint
- Pass token in Postman using:
  Authorization: Token your_token_here
- Access summary endpoint using provided URL
- Receive summary response with tone applied

## Project Structure
- Django REST API architecture
- Models for text and summaries
- Token authentication system
- Admin-based data management

## How to Run the Project
1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Run migrations using `python manage.py migrate`
4. Create superuser using `python manage.py createsuperuser`
5. Start the server using `python manage.py runserver`
6. Use Postman to test APIs with token authentication

## Future Enhancements
- Frontend integration
- User registration API
- More tone options
- Improved response formatting

## Author
Manasa K
