#!/bin/sh
# Dump MySQL database

## date format ##
NOW=$(date +"%F")
NOWT=$(date +"%T")

## Backup path ##
BAK="$HOME/iva/iva_backend_backups/$NOW"


MUSER="root"
MPASS="secret"
DB="homestead"
CONTAINER="iva_backend-db-1"

FILE="$BAK/mysql-backup-$NOWT.sql.gz"
docker exec $CONTAINER /usr/bin/mysqldump -u $MUSER  --password=$MPASS $DB | gzip -9 > $FILE
