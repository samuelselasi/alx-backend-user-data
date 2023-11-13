# 0x03. User authentication service
#### `Back-end` `Authentification`

<sub>In the industry, you should **not** implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-User](https://flask-user.readthedocs.io/en/latest/)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</sub>

## Resources
**Read or watch**:

* [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [Requests module](https://requests.kennethreitz.org/en/latest/user/quickstart/)
* [HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

## Requirements
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu `18.04` LTS using `python3` (version `3.7`)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/env python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `pycodestyle` style (version `2.5)`
* You should use `SQLAlchemy 1.3.x`
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions should be type annotated
* The flask app should only interact with `Auth` and never with `DB` directly.
* Only public methods of `Auth` and `DB` should be used outside these classes

## Setup
You will need to install `bcrypt`
```
pip3 install bcrypt
```

## Tasks

