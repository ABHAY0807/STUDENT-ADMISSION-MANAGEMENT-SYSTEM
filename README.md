# Student Admission Management System

A comprehensive Python-based command-line application for managing student admissions, built with object-oriented programming principles and file-based data storage.

## 🎯 Features

### Core Functionality
- **Student Management**: Add, view, update, delete, and search student records
- **Authentication System**: Secure admin login with credentials
- **Multiple Program Types**: Support for both Degree and Diploma programs
- **Branch-specific Requirements**: Different minimum marks and fees for each branch
- **SC/ST Support**: Special fee structure for reserved category students

### Program Branches
**Degree Programs:**
- Computer Science (Min: 80%, Fee: ₹50,000)
- Information Technology (Min: 75%, Fee: ₹48,000)
- AIML (Min: 85%, Fee: ₹55,000)
- Data Science (Min: 82%, Fee: ₹53,000)
- Cyber Security (Min: 78%, Fee: ₹52,000)
- Biotechnology (Min: 65%, Fee: ₹40,000)
- Chemical Engineering (Min: 60%, Fee: ₹38,000)
- Aerospace Engineering (Min: 88%, Fee: ₹60,000)
- Automobile Engineering (Min: 68%, Fee: ₹42,000)

**Diploma Programs:**
- Mechanical Engineering (Min: 70%, Fee: ₹45,000)
- Electrical Engineering (Min: 60%, Fee: ₹40,000)
- Civil Engineering (Min: 55%, Fee: ₹35,000)
- Electronics (Min: 50%, Fee: ₹30,000)

### Advanced Features
- **Data Visualization**: Graphical representation of student distribution across branches using matplotlib
- **Search & Filter**: Search by student ID, caste, branch, or program type
- **Sorting Options**: Sort students by name or branch
- **Formatted Reports**: Clean, tabular output for better readability
- **Fee Calculation**: Automatic fee calculation with special provisions for SC/ST students

## 📁 File Structure

```
Add_Man_System/
├── main.py              # Main application file
├── students.txt         # Raw student data storage (CSV format)
├── students_formatted.txt # Formatted student data for reporting
└── README.md           # Project documentation
```

## 🚀 Installation & Usage

### Prerequisites
- Python 3.6+
- matplotlib library (`pip install matplotlib`)

### Running the Application
```bash
cd Add_Man_System
python main.py
```

### Default Credentials
- Admin ID: `abc`
- Password: `123`

## 🛠️ Technical Implementation

### Object-Oriented Design
- **StudentAdmissionSystem** class with comprehensive methods
- Encapsulation of student data and business logic
- Modular design for easy maintenance and extension

### Data Persistence
- Text file-based storage system
- Two file formats: raw CSV and formatted table view
- Automatic data loading and saving

### Error Handling
- Input validation for marks and branch selection
- Authentication attempts limitation
- File operation error handling

## 📊 Sample Usage

1. **Add Student**: Collects student details, validates marks, calculates fees
2. **View Students**: Displays all students in formatted table
3. **Search Functionality**: Find students by ID, caste, or branch
4. **Statistical Analysis**: View student counts and distribution graphs
5. **Fee Management**: Automatic fee calculation based on caste and program

## 🔧 Future Enhancements

- Database integration (SQLite/MySQL)
- Web-based GUI interface
- Enhanced security with password hashing
- Email notifications
- Batch processing for multiple admissions
- Export functionality (PDF/Excel reports)
- Multi-user support with role-based access


## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📞 Support

If you have any questions or need help with the implementation, please open an issue in the repository.

---

**Built with Python 🐍 | File-based Storage | Command-line Interface | Data Visualization**
