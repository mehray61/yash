# 
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

sel = Selector(text=data)
company_name = sel.xpath('//div/div[text()="Project Name :"]/following-sibling::div[1]/label/text()').extract_first()


engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}?charset=utf8"
                       .format(user="root",
                               pw="admin",
                               db="rera_up"))