Title: Adding Google Analytics to your site 
Date: 2017-07-02

Google Analytics allows you to track the traffic on your website.  

1 . First, create a Disqus account [here](//disqus.com/admin/create/)
2. Once you have a Disqus account create a "new site" and point it to your github.io website.  Remember the site name you used.
3. Open up the pelican.conf file and uncomment the following line and add your site name to the script.

DISQUS_SITENAME = "YOUR SITE NAME"

That should be it. Run Pelican and push your changes to your github.io repository and you should now see comments  
