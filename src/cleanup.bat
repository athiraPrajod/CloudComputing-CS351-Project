@ECHO OFF
ECHO ===========================Arushi Pandey - PES1UG20CS077===========================
ECHO ===========================Anushka Jalori - PES1UG20CS071===========================
ECHO ===========================Athira Prajod - PES1UG20CS089===========================

@ECHO OFF
ECHO Removing images,pods and deployments...
kubectl delete pod --all
kubectl delete deploy --all
docker rmi -f blogapp:1.0

@ECHO OFF
ECHO --------Cleaned up Successfully-----------

pause
