# Notes Application 

#### Technologies used : Django, Django Rest Framework, Docker.

------

A lightweight notes app build using django rest framework and made production ready using Docker.The Docker builds a global image of the system to run on any platform supporting docker in the form of containers.Each unit of the application has its separate container like database, web app, reverse proxy(Nginx), whose configurations and how they connect internally are managed by the docker-compose file.We havent used Nginx in the application due to lack of a domain and ssl certificates.


![image](https://user-images.githubusercontent.com/46066735/210101714-246b037f-7c44-4c68-b858-595c7cf541ce.png)
![image](https://user-images.githubusercontent.com/46066735/210101732-f808c9ca-4bc8-4682-82b5-f454775e462b.png)
![image](https://user-images.githubusercontent.com/46066735/210101759-b78a7896-0004-41d2-a047-fd69a783e974.png)
![image](https://user-images.githubusercontent.com/46066735/210101779-71251b06-0515-4399-a3d2-b180152907a7.png)
![image](https://user-images.githubusercontent.com/46066735/210101652-b59b31ef-ebfb-4d07-a479-b0112ca28c5e.png)


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

Health Check

```
sudo docker inspect --format='{{json .State.Health}}' [image_name]
```
One can use clients like **Thunder Cient** extension in Vscode or **Postman** to test these API's
