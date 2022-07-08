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
Tailwind CSS's JIT mode, it's a just-in-time compiler, when enabled it can generate styles according to the user's request when creating templates instead of generating everything in advance at the initial build time. The system can only convert basic widgets such as buttons, unchecked radio buttons, checked radio buttons, unchecked checkbox, checked checkbox, and user text. users can create a GUI  in the form of logins, registers, simple forms, and questionnaires.
Based on JIT mode enabled, the user can create a GUI such as changing the color of the buttons,button shape, button width using space in the HTML area before previewing the template.
7. SALT PLant UML

## Requirements
1. Node JavaScript
2. Node Packet Manager
3. Python 3
4. Python Virtual Environment
5. Python's requirements (included in the requirements.txt file)

## Live Demo
You can use this application (demo) by accessing our [website](http://salt2html.herokuapp.com/)
You can try the new version by launching the program in your local server

## Installation Guide
1. Clone the repository
2. Open the main directory in shell
3. Run Python's virtual environemnt
bash
  `pyenv virtualenv [python3-version] [project-name]-venv`
  `pyenv activate [project-name]-venv`
  `pip3 install -r requirements.txt`
3. Run the program through Live Server
bash
  `python manage.py migrate`
  `python manage.py runserver`

## Getting Started

- install node
- case node version **v14.19.1**
- install npm
- case npm version **6.14.16**
- run `npm i`
- install python3
- case python3 version is **3.9.12**
- install pyenv
- install python `[*python3-version*]`
- install `pyenv-virtualenv`
- run `pyenv virtualenv [python3-version] [project-name]-venv`
- run `pyenv activate [project-name]-venv`
- run `pip3 install -r requirements.txt`

- **case without authentication**
- run `python manage.py migrate`
- run `python manage.py runserver`
- done, do something

- **case using authentication**
- run `python manage.py migrate`
- run `python manage.py createsuperuser`
- set username:[*yourname*]
- set passcode:[*yourpasscode*]
- run `python manage.py runserver`
- head to `[url]/admin`
- done, login and do something


## How it Works
![image](https://user-images.githubusercontent.com/95199454/177818104-3b3f85b1-7e49-4749-8c45-6b84d9c119c3.png)
The system procedure includes three stages: (1) input, (2) conversion process, and (3) output. The first stage input comes from one system input, namely the SALT script. The SALT script is processed with Regex to produce HTML script output in two templates.

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
7. Preview template 1 or 2, user can also changes the style before previewing the template
![image](https://user-images.githubusercontent.com/95199454/177313679-4e5442ad-fa7d-433f-8082-7b55c8d2851f.png)

## Limitations
As of now, L2H can only converts SALT PlantUML's basic widgets. 
The system can only convert basic widgets such as buttons, unchecked radio buttons, checked radio buttons, unchecked checkbox, checked checkbox, and user text. users can create a GUI  in the form of logins, registers, simple forms, and questionnaires.

## Our Works
### Report
You can see our work in [drive](https://drive.google.com/drive/folders/1H6FALCHmvB39zWxshR_dFD2nxglEoqoq?usp=sharing)

## Other information
### Project Member
Members of the L2H application project consist of 7 people, including:
1. Ajyan Brava Bietrosula             (081911633073)
2. Daffa Kenny Nabil Fayyaadh Priadi  (081911633040)
3. Gita Safitri                       (081911633032)
4. Intalitha Fulka Hajar Amethys      (081911633074)
5. Muhamad Erza Ranandha              (081911633069)
6. Muhamad Syafiq Herdiansa           (081911633036)
7. Muhammad Akhdan Fauzan             (081911633043)
### Contact
Email :
1. ajyan.brava.bietrosula-2019@fst.unair.ac.id
2. daffa.kenny.nabil-2019@fst.unair.ac.id
3. gita.safitri-2019@fst.unair.ac.id
4. intalitha.fulka.hajar-2019@fst.unair.ac.id
5. muhamad.erza.ranandha-2019@fst.unair.ac.id
6. muhamad.syafiq.herdiansa-2019@fst.unair.ac.id
7. muhammad.akhdan.fauzan-2019@fst.unair.ac.id
