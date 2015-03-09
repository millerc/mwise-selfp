#!/bin/sh

WORKON_HOME=/home/commlink/projects
PROJECT_ROOT=/home/commlink/projects/mwotb

# activate virtual environment
. $WORKON_HOME/mwotb-env/bin/activate

cd $PROJECT_ROOT
python manage.py emit_notices >> $PROJECT_ROOT/logs/cron_mail.log 2>&1
