Title: Personalize Your Webpage
Date: 2018-05-29 12:34
Tags: article, news, first

In order to make your blog your own, you must follow these steps:

1. go to 'pelicanconf.py' in your content folder

2. Edit the following:
AUTHOR = ''yourname"  
SITE = "Your Site Name"  
LINKS = ('Text', 'link to any of your sites')  *optional*
SOCIAL = ('Text', 'Link to any of your social sites')  *optional*

3. Save the file

4. Run ``` pelican content ``` in the terminal, which will update your output folder

5. Upload your output folder to your repository

6. Your website should display your name now!