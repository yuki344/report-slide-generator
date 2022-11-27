import json
import os

# you can edit retstr for creating template.
def generate_page(page_items):
    retstr = f'''
## {page_items.get("title")}
|method|mean|max|std|image|map|
|---:|:---:|:---:|:---:|:---:|:---:|
|{page_items.get("method1","")}|{page_items.get("mean1")}|{page_items.get("max1","")}|{page_items.get("std1","")}|![w:128]({page_items.get("image1","")})|![w:128]({page_items.get("map1","")})|
|{page_items.get("method2","")}|{page_items.get("mean2","")}|{page_items.get("max2","")}|{page_items.get("std2","")}|![w:128]({page_items.get("image2","")})|![w:128]({page_items.get("map2","")})|
|{page_items.get("method3","")}|{page_items.get("mean3","")}|{page_items.get("max3","")}|{page_items.get("std3","")}|![w:128]({page_items.get("image3","")})|![w:128]({page_items.get("map3","")})|

        '''
    return retstr

if __name__ == "__main__":
    path_report = os.path.join("out","report.md")
    page_items1 = {"title":"Sample1","method1":"something","mean1":2.2,"max1":10.3,"std1":1.3,"image1":"imgs/img1.png","map1":"imgs/map1.png"}
    # you can edit this template
    template_slide = '''---
marp: true
paginate: true
headingDivider: 2
header: Report example
footer: yuki344
---
# Report
yuki344
'''
    out_slide = template_slide + generate_page(page_items1)
    print("--slide start--")
    print(out_slide)
    print("-----")
    with open(path_report,"w") as f:
        f.write(out_slide)
    print(f"wrote report {path_report}")