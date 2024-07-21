
# BuzzClick

BuzzClick is a URL shortening and analytics tool built with Flask. It allows users to shorten URLs and track various statistics, including browser usage, operating system distribution, referrer sources, and more.

## Features

- Shorten long URLs
- Track clicks and viewer information
- View detailed analytics with charts
- Light and dark theme toggle

## Installation

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)
- Virtual environment tools (optional but recommended)

### Setup

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/buzz_click.git
    cd buzz_click
    ```

2. **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Create and Configure `.env` File:**
    Create a `.env` file in the root directory of the project and add the following configuration:
    ```
    DATABASE_URL=sqlite:///urls.db
    SECRET_KEY=supersecretkey
    IPINFO_API_KEY=YOUR_IPINFO_API_KEY
    ```

5. **Set Up the Database:**
    Initialize and migrate the database schema:
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

## Running the Application

1. **Start the Flask App:**
    ```bash
    python run.py
    ```

2. **Access the Application:**
    Open your web browser and go to `http://127.0.0.1:5000`.

## Project Structure

```
buzz_click/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── config.py
│   ├── models.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── stats.html
│   ├── static/
│       ├── styles.css  # If you have any static CSS files
│
├── .env
├── run.py
├── requirements.txt
```

## Usage

- Navigate to the homepage to shorten a URL.
- Once a URL is shortened, you will receive a short URL and a stats URL.
- Use the short URL to redirect to the original URL.
- Access the stats URL to view detailed analytics about the shortened URL.

## Contributing

Feel free to submit issues, fork the repository and send pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
