branch_name="${1:-"master"}"
collectstatic=${2:-1}

cd app
git checkout $branch_name
git pull origin $branch_name
echo "Updated code from branch "$branch_name
pip3 install -r ../requirements.txt
echo "Installed Requirements"
cd billing
git checkout $branch_name
git pull origin $branch_name
echo "Updated billing code from branch "$branch_name
cd ../comp_manager
git checkout $branch_name
git pull origin $branch_name
echo "Updated comp_manager code from branch "$branch_name
cd ..
python3 manage.py migrate
echo "Migrated database completed"

if [ $collectstatic = 1 ] ; then
    python3 manage.py collectstatic --noinput
    echo "Updated static files"
fi

cd ..
if [ $branch_name = "master" ]
then
   echo "touch deployment/uwsgi.ini"
   touch deployment/uwsgi.ini
else
   echo "touch deployment/uwsgi-dev.ini"
   touch deployment/uwsgi-dev.ini
fi


echo "Reloaded the server"
