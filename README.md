# Salary Calculation Project

## Description
This project calculates the monthly salaries of employees based on their hourly rate, weekly hours worked, and contract hours. It also computes salary statistics (average, maximum, and minimum) for each branch of the company.

## Features
- **Calculate Monthly Salaries**: Includes overtime pay calculation at 1.5x the hourly rate for hours worked beyond contract hours.
- **Branch-wise Salary Statistics**: Computes average, maximum, and minimum salaries for each branch.
- **Output Results**: Saves the calculated salaries and statistics to a text file.

## Directory Structure
```
Salary_Calculation_Project/
├── resultat.py
├── info_salaries.json
└── README.md
```

## Files
- **resultat**: The main script that performs salary calculations and generates statistics.
- **info_salaries.txt**: The output file containing calculated salaries and statistics.
- **README.md**: This file, providing an overview of the project.

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:RaoufAddeche/Simplon-TechIA-Salary-Manager.git
   cd Salary_Calculation_Project
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```
3. Install any required dependencies (if applicable).

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. The results will be saved in the `info_salaries.json` file.

## Example Output
### Sample Employee Salaries
```
Entreprise : TechCorp
Alice                | Engineer             | Salaire mensuel: 4330.00 €
Bob                  | Manager              | Salaire mensuel: 4871.25 €
```

### Sample Statistics
```
Statistiques des salaires pour l'entreprise TechCorp:
Salaire moyen : 4600.62€
Salaire maximum : 4871.25€
Salaire minimum : 4330.00€
```

## Notes
- The script uses simulated employee data for demonstration purposes.
- Ensure that the `resultat.py` script is in the same directory as the output file.

## License
This project is licensed under the MIT License.
