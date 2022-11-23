import pyweb as web

main = "web.html"

# print the pages dict (all program pages)
print(web.pages)

# create simple html (warning: rewrite whole file)
web.page.new(main,"something.css","title") #log: pages in the whole program

# name, page to edit: create new div.
web.div.new("a", main)

# create new paragraph:
web.page.p(main,"text")

# create image (page, source, xy size)
web.page.img(main,"img.png","555x800")




# web finish (</html></body>)
web.finish.end(main)

# web run (your page file)
web.finish.run(main)

