from jshen.jspider import send_request, bs4_local_html, download_html
url = "https://www.gov.cn/zhengce/zhengceku/2022-12/15/content_5732092.htm"
# soup = send_request()
# download_html(url, "test.html")
soup = bs4_local_html("build_dataset/test.html")
print(soup.title)
# div.b12c pages_content

soup = soup.find("div", class_="b12c pages_content")

# with open("build_dataset/test.txt", "w", encoding="utf-8") as f:
#     f.write(soup.text)

with open("build_dataset/test.txt", "r", encoding="utf-8") as f:
    with open("build_dataset/test2.txt", "w+", encoding="utf-8") as f2:
        for line in f.readlines():
            if not line.strip():
                continue
            # !。？；分割字符串
            import re
            for text in re.split(r"[!！。？；;]", line):
                text = text.strip()
                if not text:
                    continue
                f2.write(text)
                f2.write("\n")