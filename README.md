# IOE CGPA Calculator

## Overview

The CGPA Calculator is a Python-based application designed to help students calculate their Cumulative Grade Point Average (CGPA) based on their semester marks. This tool provides a user-friendly interface where students can input their marks and credits for different subjects across multiple semesters. It allows calculation up to a specified semester and displays results in a tabular format.

*Note: Currently Supports BCT and BEI programmes*

## Features

- **Dynamic Semester Selection**: Choose the number of semesters for which you want to calculate the CGPA.
- **Interactive Data Entry**: Enter marks and credits in a tabular format.
- **Error Handling**: The application handles empty fields gracefully and ensures data integrity.
- **Flexible Calculation**: Computes CGPA up to the selected semester and provides detailed results.

## Data Format

The data is structured by semesters, with the following information for each subject:

- **Code**: Subject code
- **Title**: Subject title
- **Exam Type**: Theory (T), Practical (P), or Both (B)
- **Theory Assessment**: Marks for assessment
- **Theory Final**: Final exam marks for theory
- **Practical Assessment**: Marks for assessment in practical
- **Practical Final**: Final exam marks for practical
- **Credits**: Credits assigned to the subject

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Rishikesh0523/IOE-BCT-CGPA-Calculator.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd IOE-BCT-CGPA-Calculator
   ```

3. **Install Dependencies**

   The project uses standard Python libraries. Ensure you have Python 3.x installed.

4. **Run the Application**

   ```bash
   python -m venv env

   ./env/Scripts/activate

   pip install requirements.txt

   streamlit run main.py
   ```

## Usage

1. **Launch the Application**: Run the application and select the number of semesters.
2. **Enter Marks**: Fill in the marks and credits for each subject as required. Only fields with data are displayed.
3. **Calculate CGPA**: After entering the data, calculate the CGPA for the selected number of semesters.
4. **View Results**: The results will be displayed in a clear and organized format.

## Example

### Semester I/I

| Subject                          | Theory Ass | Theory Final | Practical Ass | Practical Final | Total |
|----------------------------------|------------|--------------|---------------|-----------------|-------|
| SH401 - Engineering Mathematics I | 20         | 80           | -             | -               | 100   |
| CT401 - Computer Programming      | 20         | 80           | 50            | -               | 150   |
| ME401 - Engineering Drawing I     | -          | -            | 60            | 40              | 100   |
| SH402 - Engineering Physics       | 20         | 80           | 20            | 30              | 150   |
| CE401 - Applied Mechanics         | 20         | 80           | -             | -               | 100   |
| EE401 - Basic Electrical Engineering | 20       | 80           | 25            | -               | 125   |

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code adheres to the project's coding standards.
