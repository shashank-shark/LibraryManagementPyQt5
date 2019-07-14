# Simple Library Management System
## Tools used are :
1. python3.
2. PyQt5.
3. MySQL 8.0.
4. MySQL Workbench (for easy workflow).
5. RPA (will be updated soon)

## INDEX
| SNO  |  About |  Link |
|---|---|---|
|  1 | Installation  | [Click here](#Installtion-of-PyQT5)  |
|  2 | QtDesigner  |  [Click here](#Basic-idea-of-QtDesigner) |
|  3 | .qrc file (for icons)  |  [Click here](#The-qrc-file) |
|   |   |   |


## Installtion of PyQT5
Assuming python3 and pip3 is installed on the system.
Use the below commands. (Tested on Ubuntu 19.04)

```sh
sudo apt-get update
pip3 install pyqt5
sudo apt-get install python3-pyqt5
sudo apt-get install pyqt5-dev-tools
sudo apt-get install qttools-dev-tools
```

## Basic idea of QtDesigner

### See the snapshot below

![Qt Designer](https://firebasestorage.googleapis.com/v0/b/libraryprojectpyqt5.appspot.com/o/initial%2FQt1.png?alt=media&token=992d4155-8178-4302-be69-08fe44819d26)

## The .qrc file

The Qt Resource Collection File is stored in the QRC format and is affixed with the QRC extension, and is used by the Qt application and toolkit. These QRC files are generally classified as settings file that contain a list of application resources like image files or icons in XML format.

### The below is an example of .qrc file which I used in the project
```xml
<!DOCTYPE RCC>
<RCC version="1.0">
<qresource>
    <file>icons/books.png</file>
    <file>icons/daytoday.png</file>
    <file>icons/settings.png</file>
    <file>icons/users.png</file>
    <file>icons/theme.png</file>
</qresource>
</RCC>
```