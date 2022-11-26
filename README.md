## Import library and create new page value
```python
import pyweb as web
main = "web.html"
```

## set log True (Print everything that happens for people who wanna look like hackers)
```python
web.logs = True
```

## print the pages dict (all program pages)
```python
print(web.pages)
```

## create simple html (warning: rewrite whole file)
```python
web.page.new(main,"something.css","title") #log: pages in the whole program
```

## name, page to edit: create new div.
```python
web.div.open("a", main)
```

## close div on file
```python
web.div.close(main)
```

## use loop for objects in pyweb!

```python
for i in range(0,1000):
    web.text.new(main,str(i),"h2")
```

## create new paragraph:

```python
web.page.p(main,"text")
```


## create image (page, source, xy size)
```python
web.page.img(main,"img.png","555x800")
```

## create text with sizes {h1","h2","h3","h4","h5","h6}
```python
web.text.new(main, "Hello World", "h1")
```

## create style tag in *html*
```python
web.css.style_tag(main)
```

## write stuff urself lol
```python
web.page.write(main,"""body{
            text-align: center;
            background-color: red;
        }""")
```


## finish style tag in *html*
```python
web.css.finish_tag(main)
```

## web finish (</html></body>)
```python
web.finish.end(main)
```

## web run (your page file)
```python
web.finish.run(main)
```
# My first website with "Pyweb"!
```python
import pyweb as web
main = "web.html"

web.logs = True
print(web.pages)
web.page.new(main,"something.css","title") #log: pages in the whole program
web.div.open("a", main)
web.div.close(main)
for i in range(0,2):
    web.text.new(main,str(i),"h2")
web.page.p(main,"text")
web.page.img(main,"img.png","555x800")
web.text.new(main, "Hello World", "h1")
web.css.style_tag(main)
web.page.write(main,"""body{
            text-align: center;
            background-color: red;
        }""")

web.css.finish_tag(main)
web.finish.end(main)
web.finish.run(main)
```
