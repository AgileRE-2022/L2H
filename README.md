# salt-to-html

Salt PlantUML to HTML Converter Using Django Python

## getting started

- install node
- case node version **v14.19.1**
- install npm
- case npm version **6.14.16**
- run `npm i`
- install python3
- case python3 version is **3.9.12**
- install pyenv
- install python [*python3-version*]
- install pyenv-virtualenv
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

## [dev] setup tailwind css

- run *npm i tailwindcss@latest postcss@latest autoprefixer@latest*
- head to `static/css`
- create file called *tailwind.css*
- fill with these
  `@tailwind base;`
  `@tailwind components;`
  `@tailwind utilities;`
- create package.json *npm init -y*
- npm i tailwindcss autoprefixer
- make scripts in package.json
  `"scripts": {`
    `"build:css": "tailwind build static/css/tailwind.css -o static/css/tailwind-output.css"`
  `}`

## [dev] build tailwind css

- run *npm run build:css*

## [dev] using tailwind css

- head to [projectname]/template/index.html
- insert link into head tag
  `<link rel="stylesheet" href="{% static 'css/tailwind-output.css' %}">`

## [dev] setup alpine js

- run *npm i alpinejs*
- head to *static/js*
- create file called *alpine.js*
- fill with these
  `import Alpine from 'alpinejs';`

  `Alpine.data('app', () => ({`
    `open: false,`
  `}));`

  `window.Alpine = Alpine;`
  `Alpine.start();`

## [dev] using alpine js

- head to [projectname]/template/index.html
- insert script into body tag
  `<script src="{% static 'js/alpine.js' %}"></script>`
