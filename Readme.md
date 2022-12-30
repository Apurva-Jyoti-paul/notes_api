# Notes Application 

#### Technologies used : Django, Django Rest Framework, Docker.

------

A lightweight notes app build using django rest framework and made production ready using Docker.The Docker builds a global image of the system to run on any platform supporting docker in the form of containers.Each unit of the application has its separate container like database, web app, reverse proxy(Nginx), whose configurations and how they connect internally are managed by the docker-compose file.We havent used Nginx in the application due to lack of a domain and ssl certificates.



[!alt txt](https://raw.githubusercontent.com/Apurva-Jyoti-paul/notes_api/master/Screenshots/Screenshot%20from%202022-12-30%2023-41-36.png)

[!alt txt](https://raw.githubusercontent.com/Apurva-Jyoti-paul/notes_api/master/Screenshots/Screenshot%20from%202022-12-30%2023-46-58.png)

[!alt](https://raw.githubusercontent.com/Apurva-Jyoti-paul/notes_api/master/Screenshots/Screenshot%20from%202022-12-30%2023-48-42.png)

[!alt](https://raw.githubusercontent.com/Apurva-Jyoti-paul/notes_api/master/Screenshots/Screenshot%20from%202022-12-30%2023-49-19.png)

[!alt](https://raw.githubusercontent.com/Apurva-Jyoti-paul/notes_api/master/Screenshots/Screenshot%20from%202022-12-30%2023-49-50.png)



### Setup

------

Clone the git repository locally:

```
git clone https://github.com/Apurva-Jyoti-paul/notes_api.git
```

**Build and run the docker container[1]:**

```
sudo sudo docker-compose up -d --build
```

**Stopping a running container:**

```
sudo docker-compose stop
```

**Removing the volumes and containers:**

```
sudo docker-compose down -v
```



[^1]: Make sure you are at the directory in which the dockerfile is present before running the build command



### API

------

After successfull deployment of the image containers our backend is up and running on : http://127.0.0.1:8000/

The application generally supports all type of crud operations for an app:

- View all existing notes[GET]:

  ​	http://127.0.0.1:8000/api/notes/

- View a particular note[GET]:

  http://127.0.0.1:8000/api/note/<note_id>/

- Create a note[POST]:

  http://127.0.0.1:8000/api/create-note/

- Modify a note[PUT]:

  http://127.0.0.1:8000/api/update-note/<note_id>/

- Delete a particular note[DELETE]:

  http://127.0.0.1:8000/api/delete-note/<note_id>/

Here each  note has an unique note id associated with it,you can view them using the get-notes functionality like http://127.0.0.1:8000/api/notes/

For more information on the notes-id feature checkout : [note model](https://github.com/Apurva-Jyoti-paul/notes_api/blob/master/api/models.py)



### Debugging

------

**To check running docker containers:**

```
sudo docker container ls
```

**To see all docker containers :**

```
sudo docker container ls -a
```

**To view logs of a particular container while facing some issue:**

```
sudo docker logs [container_id]
```



### Testing

------

One can use clients like **Thunder Cient** extension in Vscode or **Postman** to test these API's