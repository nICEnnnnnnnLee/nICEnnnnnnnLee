import requests,re
import globals



@globals.task(type = "my_task_list_latest_posts", description =\
    "输出最近的博客")
def get_latest_posts(*kargs, **kwargs):
    xml = requests.get("https://nicelee.top/feed.xml").text
    it = re.finditer("<item>.*?<title>(.*?)</title>.*?<link>(.*?)</link>.*?</item>" , xml, flags = re.DOTALL)
    posts = [ (match.group(1), match.group(2)) for match in it]
    posts = posts[:4]
    globals.template_inputs["latest_posts"] = posts
    
