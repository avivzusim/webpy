import os
import sys
pages = {}
pageamount = 0
class page:
    
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
            <img src={src}>""")
            else:

                findx = str(size.find("x"))
                findx = int(findx)
                x = size[:findx]
                y = size[findx+1:]

                # print(x,y) # debug print for x and y
                mypage.seek(11)
                mypage.write(f"""
            <img src={src} width="{x}" height="{y}">""")


        # auto to make it auto
        # web.page.img(page,src,size)
        # xy
        # 40x80
        # read
        # auto

        # web.page.img("web.html","img.png", auto)
    

#add open and close to div!
class div:        
    def new(name,page):
        with open(f"{page}","a+") as mypage:
            mypage.seek(11)
            mypage.write(f"""<div class="{name}">
            
        </div>
            """)
        mypage.close()

class finish:
    def end(page):
        with open(f"{page}","a+") as mypage:
            mypage.seek(11)
            mypage.write(f"""
            
             </body>
            </html>""")
        mypage.close()

    # run page
    def run(page):
        os.system(f"start {page}")


