# Deploy ML models with FastAPI, Docker, and Heroku

This project demonstrates how to deploy machine learning models using FastAPI, Docker, and Heroku. The current app is deployed at : https://language-detection-app-12-3ae1e3dea495.herokuapp.com.

## 1. Develop and Save the Model with Google Colab

[Open Colab](https://colab.research.google.com/drive/1uaALcaatvxOu42IhQA4r0bahfdpw-Z7v?usp=sharing) to develop and save your machine learning model.

## 2. Create Docker Container

```bash
docker build -t app-name .

docker run -p 80:80 app-name
This will build the Docker image and run the FastAPI app inside a Docker container.
```

## 3. Set Up Git Repository
If you're starting with a new repository, follow these steps:

```bash
Copy code
git init
git add .
git commit -m "initial commit"
git branch -M main
If you've cloned this repository, skip this step or delete the existing Git repository with rm -rf .git.
```

## 4. Create Heroku Project
```bash
Copy code
heroku login
heroku create your-app-name
heroku git:remote your-app-name
heroku stack:set container
git push heroku main
This will create a new Heroku app, set it up for container deployment, and push your code to Heroku.
```

Access your deployed app on Heroku: https://your-app-name.herokuapp.com

## Usage
Develop and save your machine learning model using the provided Google Colab.

Build the Docker container and run your FastAPI app locally using the provided commands.

Set up a new Git repository or clone this repository and follow the Git setup steps.

Create a new Heroku project, set it up for container deployment, and push your code to Heroku.

Access your deployed app on Heroku and test it by entering text in the provided textbox.

## Additional Information
The app has been designed using a machine learning model built with the provided Google Colab.

The ML model has been integrated into FastAPI, encapsulated using Docker, and deployed using Heroku.

## Contributing
Feel free to contribute to this project. Submit issues or pull requests as needed.
