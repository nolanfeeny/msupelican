Title: Personalize Your Website 
Date: 2018-06-01 

Now tha that you have a website it is time to make it your own.  First thing you can do is edit the ```pelican.conf``` file.  This file is used to set some variables related to your website.  Read through the file and change what you think is approprite Specifically change the following lines of code:

```
AUTHOR = 'authorname'
SITENAME = "CMSE Pelican/Github.io tutorial"
```

Use your name and your website.  Now just remake your repository using the make or pelican commands and view your changes on the local machine:

```
make html
make serve
```

Once you are happy with the changes copy the contents of output to your user.github.io repository and push your changes to github.
