import pyweb as web

main = "web.html"

#set log True (Print everything that happens for people who wanna look like hackers)
web.logs = True

# print the pages dict (all program pages)
print(web.pages)

# create simple html (warning: rewrite whole file)
web.page.new(main,"something.css","title") #log: pages in the whole program

# name, page to edit: create new div.
web.div.open("a", main)
# close div on file
web.div.close(main)


# loop for objects!   
for i in range(0,2):
    web.text.new(main,str(i),"h2")

# create new paragraph:
web.page.p(main,"text")

# create image (page, source, xy size)
web.page.img(main,"img.png","555x800")

# create text with sizes {h1","h2","h3","h4","h5","h6}
web.text.new(main, "Hello World", "h1")

            #create table later -- stupid lol - for aviv () --


# create style tag in *html*
web.css.style_tag(main)

#write stuff urself lol
web.page.write(main,"""body{
            text-align: center;
            background-color: red;
        }""")

# finish style tag in *html*
web.css.finish_tag(main)


# web finish (</html></body>)
web.finish.end(main)

# web run (your page file)
web.finish.run(main)

