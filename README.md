# CloudComputing-CS351-Project
Use Docker and Kubernetes to make an easily deployable and portable blogging web-app using Flask and MongoDB.

The following is the layount of our application

## INITIAL LAYOUT

![image](https://user-images.githubusercontent.com/79107280/233130142-414eaa5e-e98a-4f71-8fd3-9dd6771bdce2.png)

## CREATING POSTS

![image](https://user-images.githubusercontent.com/79107280/233130342-304a742e-21c1-48e5-b6b8-026d7c49255b.png)

## EDITING POSTS

![image](https://user-images.githubusercontent.com/79107280/233130408-4d88fc8b-ae29-4801-8e59-48754b874fdf.png)

## DELETING POSTS

![image](https://user-images.githubusercontent.com/79107280/233130486-5128749d-dbce-45d8-8049-32e878c3700f.png)

## STEPS TO RUN THE PROGRAM 

1. Run 'pull_images.bat' to pull required images
2. Run 'cleanup.bat' to delete all existing pods and deployments
3. Run 'create_cluster.bat' batch file to create Kubernetes cluster.\
    It will redirect you to "http://localhost:5001"
4. Finally run 'cleanup.bat' again to remove all your clusters (if required)
