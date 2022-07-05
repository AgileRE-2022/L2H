# Welcome to L2H Aplication (Generate GUI Lofi-to-Hifi from SALT to HTML)
## About Aplication 
The L2H (GUI Low fidelity to high fidelity) application is a web-based application that translates the Low Fidelity GUI (wireframe) from the PlantUML SALT code into a High Fidelity GUI with two HTML code templates.
The user can input the SALT Plant UML code (without login), then the user can generate the SALT Plant UML code into HTML code by clicking the generate button, then the user can see a preview of the results generated into a GUI high fidelity. (This L2H Application Project is carried out by group 2 class I1).

## Builder System
1. HTML 
2. CSS
3. Django
4. Python
5. Javascript
6. Tailwind CSS with JIT mode enabled (Tailwind CSS which generates templates on user request instead of generating everything in advance at initial build time)
7. SALT PLant UML

## Requirements
Node JavaScript
Node Packet Manager
Python 3
Python Virtual Environment
Python's requirements (included in the requirements.txt file)

## Live Demo
You can use this application (demo) by accessing our [http://salt2html.herokuapp.com/]

## Installation Guide
1. Clone the repository
2. Open the main directory in shell
3. Run Python's virtual environemnt
```bash
  pyenv virtualenv [python3-version] [project-name]-venv
  pyenv activate [project-name]-venv
  pip3 install -r requirements.txt
```
3. Run the program through Live Server
```bash
  python manage.py migrate
  python manage.py runserver
```

## How it Works

## Input
SALT PlantUML's Basic Widgets, consisting of :
1. Button;
2. Unchecked Radio Button;
3. Checked Radio Button;
4. Unchecked Checkbox;
5. Checked Checkbox;
6. User Text;
7. Droplist.

![image](https://user-images.githubusercontent.com/95199454/177311441-6b40f756-67ef-471d-ba21-7aa1c98cfe19.png)

## Output
L2H automatically converts SALT PlantUML's code into a working HTML + Tailwind CSS Template
![image](https://user-images.githubusercontent.com/95199454/177312119-f29b6141-6ff3-4bd4-a45b-5799ba00c33d.png)
![image](https://user-images.githubusercontent.com/95199454/177312173-20c42c04-3ca7-4579-a643-29c5c3b3a24a.png)
![image](https://user-images.githubusercontent.com/95199454/177312204-a82ffe2c-0a9a-402e-a82e-220603d9192e.png)

## How to Use
1. Run the server 
![image](https://user-images.githubusercontent.com/95199454/177312736-b416b3ba-c43e-4beb-b5a8-9315852a8cc0.png)

2. Click "Try Converting" on the navigation bar or the "Try Now" button on the index page.
![try](https://user-images.githubusercontent.com/95199454/177313239-f1184efa-84f6-4737-b449-914608394fb0.png)

4. Insert your SALT PlantUML's code into the text box, and then click convert.
![image](https://user-images.githubusercontent.com/95199454/177313338-1129079c-8653-4693-a759-3fabb327dd8f.png)

6. Click the "Convert" button.
![image](https://user-images.githubusercontent.com/95199454/177313615-c4a84743-5210-4984-a48f-af66e59fc9b2.png)

7. Preview template 1 or 2, user can also changes the style before previewing the template
![image](https://user-images.githubusercontent.com/95199454/177313679-4e5442ad-fa7d-433f-8082-7b55c8d2851f.png)


## Limitations
As of now, L2H can only converts SALT PlantUML's basic widgets. 

## Our Works

### Report
UTS --> https://docs.google.com/document/d/1PHiJ_pPyprul0quqZNPtlgOl_u6YMZA6wdVSjPCg1v8/edit#

Product dan Sprint Backlog --> https://docs.google.com/document/d/1RLCnumE05cm0RvdqcIXX8KxBItOdK2GUvZvGLdyPqLU/edit

Burn Down Chart dan Progress --> 

1. https://docs.google.com/document/d/1Z0ov0M34vkLnFd25zOG8nbRQm58JKZr6kyUXHG1jhHc/edit

2. https://docs.google.com/document/d/1tesXYCFpP59lmOYRh6b4ARUAGehOuPeBAHilLgRicyI/edit

## Other information
### Project Member
Members of the L2H application project consist of 7 people, including:
1. Ajyan Brava Bietrosula
2. Daffa Kenny Nabil Fayyaadh Priadi
3. Gita Safitri
4. Intalitha Fulka Hajar Amethys (081911633074)
5. Muhamad Erza Ranandha
6. Muhamad Syafiq Herdiansa
7. Muhammad Akhdan Fauzan  

### Contact
Email :
1.
2.
3.
4. intalitha.fulka.hajar-2019@fst.unair.ac.id
5.
6.
7.
