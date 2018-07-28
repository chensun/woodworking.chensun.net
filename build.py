#!/usr/bin/env python3

import getopt
import glob
import os
import sys

html_begin ='\
<!DOCTYPE html>\n\
<html>\n\
<head>\n\
<title>[update title]</title>\n\
<style>\n\
header {\n\
    padding: 20px;\n\
    text-align: center;\n\
}\n\
footer {\n\
    margin-top: auto; \n\
    padding-top: 20px;\n\
    text-align: center;\n\
}\n\
div.gallery {\n\
    border: 1px solid #ccc;\n\
    display: block;\n\
    width: 100%;\n\
    position: relative;\n\
    padding: 100% 0 0 0;\n\
}\n\
div.gallery:hover {\n\
    border: 1px solid #777;\n\
}\n\
div.gallery img {\n\
    position: absolute;\n\
    display: block;\n\
    max-width: 100%;\n\
    max-height: 100%;\n\
    left: 0;\n\
    right: 0;\n\
    top: 0;\n\
    bottom: 0;\n\
    margin: auto;\n\
}\n\
div.desc {\n\
    padding: 15px;\n\
    text-align: center;\n\
}\n\
* {\n\
    box-sizing: border-box;\n\
}\n\
.responsive {\n\
    padding: 6px 6px;\n\
    float: left;\n\
    width: 19.99999%;\n\
}\n\
@media only screen and (max-width: 1600px) {\n\
    .responsive {\n\
        width: 24.99999%;\n\
    }\n\
}\n\
@media only screen and (max-width: 1200px) {\n\
    .responsive {\n\
        width: 33.33333%;\n\
    }\n\
}\n\
@media only screen and (max-width: 800px) {\n\
    .responsive {\n\
        width: 49.99999%;\n\
    }\n\
}\n\
@media only screen and (max-width: 500px) {\n\
    .responsive {\n\
        width: 100%;\n\
    }\n\
}\n\
.clearfix:after {\n\
    content: "";\n\
    display: table;\n\
    clear: both;\n\
}\n\
</style>\n\
</head>\n\
<body>\n\
<header>\n\
    <h1>[update title]</h1>\n\
    <h2>[update description]</h2>\n\
</header>\n\
'

html_end = '\
<div class="clearfix"></div>\n\
<footer>[update copyright]</footer>\n\
</body>\n\
</html>\n\
'

image_div = '\
<div class="responsive">\n\
    <div class="gallery">\n\
        <a target="_self" href="{img_full}">\n\
            <img src="{img_preview}">\n\
        </a>\n\
    </div>\n\
</div>\n\
'

def main(argv):
    if len(argv) != 2:
        argv[0:] = ['-h']

    path = ''
    cwd = os.getcwd()
    try:
        opts, _ = getopt.getopt(argv,'hp:t:')
    except getopt.GetoptError:
        print('build.py -p <path>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('build.py -p <path>')
            sys.exit()
        elif opt == '-p':
            path = arg

    try:
        os.chdir(path)
        with open('index.html', 'w') as out_file:
            out_file.write(html_begin)
            for img_preview in sorted(glob.glob('images/preview_*')):
                img_full = 'images/' + img_preview[len('images/preview_'):]
                out_file.write(image_div.format(img_full=img_full, img_preview=img_preview))
            out_file.write(html_end)
    except Exception as e:
        print('Error', e)
    finally:
        os.chdir(cwd)



if __name__ == '__main__':
    main(sys.argv[1:])
    print('Done!')

