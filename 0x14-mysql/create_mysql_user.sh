#!/usr/bin/env bash

# MySQL credentials
MYSQL_USER="root"

# Create MySQL user and grant permissions
create_mysql_user() {
    mysql -u$MYSQL_USER -p$MYSQL_PASSWORD <<EOF
    CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
    GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
    FLUSH PRIVILEGES;
    exit
EOF
}

# Run the function to create MySQL user
create_mysql_user
