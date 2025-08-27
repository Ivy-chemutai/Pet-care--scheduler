# Pet Care Scheduler CLI

A Python command-line application for managing pets and tracking their daily care activities. 
Built with SQLAlchemy ORM and designed following best practices for CLI applications.

## Overview

Pet Care Scheduler helps pet owners organize and track their pets' care routines, including feeding, walking, grooming, veterinary visits, and medication schedules.
The application provides comprehensive pet management with statistics, reminders, and search functionality.

## Features

### Core Functionality
- **Owner Management**: Register and manage pet owners with contact information
- **Pet Registration**: Add pets with detailed information (species, breed, age)
- **Care Activity Logging**: Track daily activities with timestamps and notes
- **Relationship Management**: View pets organized by their owners

### Enhanced Features
- **Pet Statistics**: Species breakdown, average age calculations, and activity analysis
- **Care Reminders**: Time-based alerts for overdue feeding and walking schedules
- **Search Functionality**: Find pets by name across the entire database
- **Input Validation**: Comprehensive validation with user-friendly error messages

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Pipenv for virtual environment management

### Installation Steps

1. **Clone the repository**
     git clone <repository-url>
     cd pet-care-scheduler
2. **Install dependencies**   
    pipenv install
    pipenv shell
   
3.**Run**
  cd lib
  python cli.py
      
## Pet Care Scheduler
1. Owner Management     - Create, view, find, and delete pet owners
2. Pet Management       - Create, view, find, and delete pets
3. Care Log Management  - Log activities, view history, manage records
4. View Relationships   - See owners with their pets and recent activities
5. Pet Statistics       - View species breakdown and care analytics
6. Care Reminders       - Check for overdue feeding and walking schedules
7. Search Pets          - Find pets by name
q. Quit                 - Exit the application

## File structure

   pet-care-scheduler/
─ Pipfile                 # Project dependencies and Python version
─ README.md              # Project documentation (this file)
 ─ lib/
      *cli.py             # Main CLI interface and navigation logic
      *helpers.py         # CLI helper functions and menu operations
 ─db/
      *models.py      # SQLAlchemy models and ORM methods

## Author,
IVVY.
## License MIT.

HAPPY CODING!

