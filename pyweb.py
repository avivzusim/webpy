import os
import sys
pages = {}
pageamount = 0
logs = False

class page:
    
    # ! important ! - added option to change language
    # add more metadata options
    def new(page,link,title):
        f = open(str(page),"w")
        pages[str(page)] = str(link)
        f.write(f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
            <link rel="stylesheet" href="{link}">
        </head>
        <body>
            
        """)
        print(pages)
        f.close()  

        if logs == True:
            print(f"Page {page} rewritten and linked to {link} with title: {title}")     


    def write(page, text):
        with open(f"{page}","a+") as mypage:
            mypage.seek(11)
            mypage.write(f"""{text}""")
            mypage.close()

        if logs == True:
            print(f"added {text} to {page}")


# create paragraph    
    def p(page,text):
        with open(f"{page}","a+") as mypage:
            mypage.seek(11)
            mypage.write(f"""<p>{str(text)}</p>""")
            mypage.write(" ")
            mypage.close()



    def img(page,src,size):
        with open(f"{page}","a+") as mypage:
            if size == "auto":
                mypage.seek(11)
                mypage.write(f"""
            <img src={src} alt="">""")
                mypage.close()
            else:

                findx = str(size.find("x"))
                findx = int(findx)
                x = size[:findx]
                y = size[findx+1:]

                # print(x,y) # debug print for x and y
                mypage.seek(11)
                mypage.write(f"""
            <img src={src} alt="" width="{x}" height="{y}">""")
                mypage.close()

            if logs == True:
                print(f"{src} added to {page}")
        # auto to make it auto
        # web.page.img(page,src,size)
        # xy
        # 40x80
        # read
        # auto

        # web.page.img("web.html","img.png", auto)
    
#add open and close to div!
class div:        
    def open(name,page):
        with open(f"{page}","a+") as mypage:
            mypage.seek(11)
            mypage.write(f"""<div class="{name}">
            """)
            mypage.close()
        
        if logs == True:
            print(f"Div tag with class: {name} created in {page}")
    
    def close(page):
        with open(f"{page}","a+") as mypage:
            mypage.seek(11)
            mypage.write(f"""
        </div>
            """)
            mypage.close()
        if logs == True:
            print(f"div close tag added to {page}")

class text:
    def new(page,text,size):
        with open(f"{page}","a+") as mypage:
                mypage.seek(11)
                mypage.write(f"""
            <{size}>{text}</{size}>""")
                mypage.close()
        if logs == True:
            print(f"text: {text} added to {page} with size {size}")


# create the stuff noob
positions = []
class table:
    def new(page,rows,columns):
        with open(f"{page}","a+") as mypage:
            print("idk im too stupid for this shit, ill do it later if i have time lol")
            mypage.close()



class css:
    #create css style tag in html file
    def style_tag(page):
        with open(f"{page}","a+") as mypage:
            mypage.seek(11)
            mypage.write("""
        <style>
        """)
            mypage.close()
        if logs == True:
            print(f"Style tag added to {page}")


    def finish_tag(page):    
        with open(f"{page}","a+") as mypage:
            mypage.seek(11)
            mypage.write("""
        </style>""")
            mypage.close()
        if logs == True:
            print(f"Finish style tag added to {page}")
    

class finish:
    def end(page):
        with open(f"{page}","a+") as mypage:
            mypage.seek(11)
            mypage.write(f"""
            
</body>
</html>""")
        mypage.close()
        if logs == True:
            print(f"Finish html,body tags added to {page}")


    # run page
    def run(page):
        os.system(f"start {page}")
        print(f"{page} is starting up")

