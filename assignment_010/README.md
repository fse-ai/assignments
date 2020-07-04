# assignment_010: Building your own Data set from Google Images

The task is to create an image dataset through Google Images. So first form a classification problem statement of your choice. The very first step is to search for images of each class on Google. Try to be more specific you are in your Google Search for better results. Scroll down until you've seen all the images you want to download, or until you see a button that says 'Show more results'. All the images you scrolled past are now available to download. To get more, click on the button, and continue scrolling. The maximum number of images Google Images shows is 700.

Now you must run some Javascript code in your browser which will save the URLs of all the images you want for you dataset. In Google Chrome press `Ctrl` `Shift` `j` on Windows/Linux and a small window the javascript 'Console' will appear. Use `Ctrl` `Shift` `k` for Firefox browser. You have to now paste the following JavaScript commands:


    urls = Array.from(document.querySelectorAll('.rg_di .rg_meta')).map(el=>JSON.parse(el.textContent).ou);
    window.open('data:text/csv;charset=utf-8,' + escape(urls.join('\n')));

This code lets you collect the URLs of each of the images. Do not forget to disable ad blocking extensions (uBlock, AdBlockPlus etc.) in Chrome to avoid any interruption for the window.open() command.

If you find trouble in obtaining the URL’s, you can try these commands..

    var urls=Array.from(document.querySelectorAll('.rg_i')).map(el=> el.hasAttribute('data-src')?el.getAttribute('data-src'):el.getAttribute('data-iurl'));
    var hiddenElement = document.createElement('a');
    hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(urls.join('\n'));
    hiddenElement.target = '_blank';
    hiddenElement.download = 'myFile.txt';
    hiddenElement.click();

The next step is to create directory and upload the obtained URLs text file into your server. You then create folders for each class. Now you will need to download your images from their respective URLs. 

Here is a sample visualization of datasets we created for a binary classifation of "Bees" and "Ants" from Google Images

![](https://github.com/hanoonaR/fseai_image_collection/blob/master/assign10.png)
