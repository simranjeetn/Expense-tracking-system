# Expense Tracking System

An Expense Tracking System is a web application that allows users to manage their personal or business expenses effectively. This project is built using Python and utilizes several powerful packages to ensure a robust and efficient solution.

## Features
- User-friendly interface for tracking expenses.
- Integration with a MySQL database for storing expense data.
- Streamlit-powered interactive dashboards.
- RESTful API using FastAPI for backend operations.
- Data validation and modeling with Pydantic.

## Requirements
Ensure you have the following installed on your system:
- Python 3.9+
- MySQL server

## Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/expense-tracking-system.git
cd expense-tracking-system
```

2. Set up a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the MySQL database:
   - Create a database named `expense_tracker`.
   - Update the database credentials in the `config.py` file.
   - Run the provided SQL scripts (if any) to initialize the database schema.

5. Start the backend server:
```bash
uvicorn main:app --reload
```

6. Run the Streamlit application:
```bash
streamlit run app.py
```

## Packages Used
The following Python packages are used in this project:

- **FastAPI** (`~0.115.7`): For building the RESTful API.
- **typing** (`~3.7.4.3`): For type hints and annotations.
- **Pydantic** (`~2.10.5`): For data validation and modeling.
- **mysql-connector-python** (`~9.2.0`): For connecting and interacting with the MySQL database.
- **requests** (`~2.32.3`): For making HTTP requests.
- **Streamlit** (`~1.41.1`): For building the interactive front-end dashboard.
- **Pandas** (`~2.2.3`): For data manipulation and analysis.

## Usage
1. Open your browser and navigate to the Streamlit application (default: `http://localhost:8501`).
2. Add, update, and delete expenses using the provided interface.
3. Visualize expense data using the interactive charts and graphs.



## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any inquiries or support, please contact:
**Devang Patel**  
Email: [devangpatel10505@gmail.com](mailto:your-email@example.com)

---

Happy Expense Tracking!
