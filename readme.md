# MOODLE PROJECT

## INTRODUCTION

This is a project which makes installation of necessary files from your respective courses in current semester into your remote machine automatically through terminal with a single command "moodle3it".

## INSTALLATION PROCEDURE

- `sudo add-apt-repository ppa:sriteja777/terminal`
- `sudo apt-get update`
- `sudo apt-get install moodle3it`

## Usage of command:
- Once we type the command "moodle3it" we will get a display on terminal like below and all the respective folders will be created in the path that we mentioned above.

#### Run
- `moodle3it'

Now you will be prompted for username,password and directory path for the files to download the respective courses.

-  So to avoid typing every time the username,password

### Login Requirement for "https://moodle.iiit.ac.in/" through the following commands
- `export MOODLE_USERNAME=abc.xyz@students.iiit.ac.in(or abc.xyz@research.iiit.ac.in)`
- `export MOODLE_PASSWORD=*******`

### Path of the directory where the files should download 
- `export MOODLE_FILES_PATH=.....(example- /home/abc/xyz)`



![](original.png)

- There are necessary instructions in which we can download the respective courses files.

## Contribute

Contributions are always welcome!


