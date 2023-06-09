<p align="center">
  <img src="picture\16007803099977_P8.png" alt="logo" />
</p>

## The Project

- Develop a **REST API** using the **Django REST framework**
- Use the **Django** framework.
- Using server-side rendering in **Django**.
- The application is an API that can be compatible with **Web**, **IOS** or **Android** applications
- Using **JSON Web Tokens (JWT)** to secure the API

## Context

- SoftDesk, a software development company.
- Development of an application to track technical issues (issue tracking system).
- This solution is aimed at corporate clients, in B2B

## Database

- This repository comes with a pre-populated SQLite database of some user accounts.
- we have used SQLite for this project.

## Application Vocabulary

- **User** - represents the users of the application.
- **Project** - designates a project with its characteristics.
- **Contributor** - includes all users participating in a project.
- **Issue** - represents an issue related to a project.
- **Comment** - denotes a comment related to an issue.

## Overall application architecture

- To-do lists include projects
- Each project can include issues
- Each issue can include comments
- Only project contributors can access the details of a project (contributors, issues, comments)
- Only the author of a project/issue/comment can update or delete it

## API Documentation

Detailed API documentation is available at:

[API Documentation](https://documenter.getpostman.com/view/24753025/2s93XvW4td)

You will find in this documentation all the detailed API endpoints

##  Project download

_Tested on Windows 10, Python 3.10.6. / Django 4.1.7. / djangorestframework 3.14.0_


[Technical Specifications 1 ( french )](https://github.com/alexandre-75/Create_a_secure_RESTful_API_using_Django_REST/blob/main/picture/PDF/Softdesk%20-%20Conception%20de%20la%20mise%20en%20%C5%93uvre.pdf)

[Technical Specifications 2 ( french )](https://github.com/alexandre-75/Create_a_secure_RESTful_API_using_Django_REST/blob/main/picture/PDF/Softdesk%20-%20Liste%20des%20v%C3%A9rifications%20OWASP.pdf)



####  1. project recovery

    $ git clone https://github.com/alexandre-75/Create_a_secure_RESTful_API_using_Django_REST.git

####  2. Creating a virtual environment

    python<version> -m venv nom_env_virtuel

    Activate the environment  `mon_env_virtuel\Scripts\activate` (Windows)

####  3. Installing packages

    pip<version> install -r requirements.txt
    
####  4. Start the program

- From the project root folder, go with the terminal to the ***source*** folder :
    ```sh
     cd source/
     ```
- ***Run the server*** by executing the command :
  ```sh
  python manage.py runserver
  ```

- Open your favorite browser and navigate to the ***local development server*** at :
  ```sh
  http://127.0.0.1:8000/
  ```

  ## Use of the program
  
  It is possible to navigate in the API with :

- The [Postman](https://www.postman.com/) platform
- The built-in Django REST framework interface,  see [endpoints](https://documenter.getpostman.com/view/24753025/2s93XvW4td).

- Access to the admin page is possible :

      Example on a local installation: http://127.0.0.1:8000/admin

      user: username
      password: a
      
      or 
      
      user: username2
      password: password

  This allows full access (read and write) to the database tables.
  
  
  - User list :

| *ID* | *User*          | *Password*      |
|------|---------------|----------------|
| 1    | username      |       a        |
| 9    | username2     | password       |
| 15    | username8     | password       |
| 16    | username9     | password       |
| 17    | username10     | password       |
  
  ## Generate a flake8 report
    
flake8 can identify syntax errors and non-compliance with the PEP.

#### 1. To view a flake8-html report :

- From the project root folder, go with the terminal to the *** report_flake8*** folder  :

```sh
     cd report_flake8/
```
 - next open file .HTML to view the report
 
#### 2. Screenshot of a report-HTML Flake 8 : 
  
  <p align="center"><img src="picture\145825.jpg" alt="flake8" /></p>
    
  
#### 3. A new report can be generated by running the following command in the terminal :

     $ flake8 --format=html --htmldir=flake8_rapport project_link/