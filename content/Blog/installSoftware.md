Title: Installing the Software 
Date: 2018-07-02 

Before you start you will need to download some software. Pelican is based on python and github.io uses git.  

We recommend using the Anaconda install for python.  You can download the installer [here]().

Once Anaconda is installed you can use the installers to install the rest of what you need:

``` conda install git ```

``` pip install pelican ```

``` pip install markdown ``` 

Now you should be able to clone this repository using the following commands:

``` git clone https://xxx.xxxxx.github.com// ```

You should be able to now get this site running on your local machine. First change to the msupelican directory and run the following commands:

```make html```

```make serve```

If the above dosn't work it probably means you don't have make installed.  You can use the following commands instead:

``` pelican content ```

``` cd output && python -m pelican.server ```

To connect to the local site you can use the following URL:

[http://localhost:8000](http://localhost:8000)

You are ready to start editing... 
