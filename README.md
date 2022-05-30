# Sloovi API

## Description

The API manages templating. It allows users to perform CRUD operations on template.

## Getting Started

### Dependencies

The API was tested on Linux Ubuntu 20.04 and Python 3.10.1.

- Python 3.8+
- Flask
- MongoDB & Mongo Compass
- Other dependencies are in the requirements.txt and are installed during the build

### Building the app

- Check the .env-example file to create a .env file.

On Linux

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Ensure you run the command at the root of the project.

```
python manage.py run
```

### Testing the app

There is a deployed version on [Render](https://sloovi-api.onrender.com)

You can test the API locally using pytest but ensure the test db has been created before running this command.

Use the command below to test using pytest.

```

```

## Help

If you encounter any problem while building, kindly reach out through issues on [GitHub](https://github.com/joshajiniran/sloovi-task.git)

## Authors

Contributors names and contact info

Joshua Ajiniran

## Version History

This is inital release

- 0.1.1 (coming)
  - Generate API Docs
  - Use Flask-RESTful package
- 0.1.0
  - Initial Release
