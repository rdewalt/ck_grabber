# Comic Kingdom Strip Grabber
Comics Kingdom Strip Grabber

YOU WILL NEED TO EDIT LINE 16 of the script 
https://github.com/rdewalt/ck_grabber/blob/dd89f0d515b23245004653fb4509b639b79492db/gather.py#L16 
and put in the correct cookie, or you will not be able to download any archives.  

I made a requirements.txt   You probably know how to use pip for this.  Use a search engine. Unless your go-to search engine is Bing, in which case, good luck.

How do you get this cookie?

Get a Subscription Account.  Log Into It. Extract the wordpress_logged_in..... something or other cookie from your browser.

Now, say you were on vacation and forgot to keep up with the last month of "Shoe"  Don't worry, we won't judge you.  Use this script:
python3 gather.py -s 2023-07-01 -e 2023-08-01 -c shoe

If you did it right, it'll pull that month worth of "Shoe" strips into a subdirectory. (./shoe/2023/) 

Things might not work.  I don't know. I'm powered by coffee and sarcasm.  It works for me.  I'm sticking it here because when I was looking for this script, I never found one.  So I'm making it.
