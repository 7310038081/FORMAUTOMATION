# FORMAUTOMATION
Create a Django App that can automatically fill a Google form.
Google Form Auto-Filler using Django, Python, and Selenium
This project automates the process of filling out Google Forms using Python, Django, and Selenium. It is designed to automatically interact with a specified Google Form and submit responses based on pre-defined data.

Technologies Used:
Python: The primary programming language used for scripting the automation logic.
Django: A web framework used to manage and serve the form submission requests.
Selenium: A tool used for automating web browsers to fill out the form fields and submit them programmatically.
Git: Version control used to manage the project and collaborate with other developers.
Project Overview:
This repository contains a script that automates the completion and submission of a Google Form. The script leverages Selenium for interacting with the form fields and filling them with predefined answers. Django is used for the project structure, enabling easy deployment and scaling of the automation process.

Features:
Automates form filling using Selenium WebDriver.
Uses a Django backend to manage requests and data.
Easy configuration to adapt to other Google Forms.
Includes detailed logging for error handling and debugging.

Installation Instructions:
Clone the repository:

Copy code
git clone https://github.com/yourusername/google-form-auto-filler.git



![Screenshot (312)](https://github.com/user-attachments/assets/8bfd3815-7b6d-4be4-a829-e69f9972f244)
![Screenshot (313)](https://github.com/user-attachments/assets/92e582d0-bfd8-4861-9053-a1c53d0ae340)
![Screenshot (314)](https://github.com/user-attachments/assets/407373f5-b4cb-4a3f-89c3-95210e6f933f)
![Screenshot (315)](https://github.com/user-attachments/assets/82c0208c-e8f4-4ffa-8fe1-675e88ce683f)


How It Works:
The Python script initiates a Selenium WebDriver to open the Google Form URL.
It then locates the form elements (text inputs, radio buttons, dropdowns, etc.) using their HTML attributes (like name, id, or class).
Predefined data is fed into the form fields, and the form is submitted programmatically.
Upon successful submission, a confirmation page is captured as a screenshot and saved locally.

