# INSTALLATION instructions

Follow these directions to create your own website or blog using github pages and the software called pelican, which allows processes markdown and jupyter notebook files into HTML for you. Very easy to update content on your website without dealing with HTML syntax.

### 1) Ensure that both python and pelican are installed on your computer
~~~~
pip install pelican markdown
~~~~

### 2) Create your own blog folder name:{yourblog} on your computer
All contents should be inside of this folder. When you run a pelican command later on in these instructions, it should be run in this folder using the terminal.

### 3) Download this repository into your blog folder
Using either git pull or downloading the zip file

### 4) Open yourblog/output/index.html
This allows you to see the default webpage I've set, with an MSU theme

### 5) Make changes to files within yourblog/content
This allows you to customize your website

### 6) Test changes
Do this by running the following code in your Terminal, located in your blog folder
~~~~
pelican content
~~~~
This runs the pelican software on everything inside yourblog/content folder, converting markdown files into html. This makes updating your pages much quicker and easier than rewriting HTML code.

Open your index.html in the blog's output folder to see the new changes

### 7) Upload to your github.io site
Follow the directions on creating your own github.io site at [Github Pages](https://pages.github.com/), which should be very quick and easy. Once you commit everything in your blog's output folder to your new GitHub repository (which can be done with the a git push or simply by dragging the files), your new website should be up and running online within the minute!
