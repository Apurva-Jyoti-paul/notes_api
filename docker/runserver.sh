NAME="notes_api"  #Django application name
DIR=/home/app/notes_api   #Directory where project is located
USER=root  #User to run this script as
GROUP=root  #Group to run this script as
WORKERS=3     #Number of workers that Gunicorn should spawn
SOCKFILE=unix:/home/app/notes_api/gunicorn.sock   #This socket file will communicate with Nginx 
DJANGO_SETTINGS_MODULE=notes_api.settings   #Which Django setting file should use
DJANGO_WSGI_MODULE=notes_api.wsgi           #Which WSGI file should use
LOG_LEVEL=debug
cd $DIR

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DIR:$PYTHONPATH


#Command to run the progam under supervisor
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $WORKERS \
--user=$USER \
--group=$GROUP \
--bind=$SOCKFILE \
--log-level=$LOG_LEVEL \
--log-file=-
