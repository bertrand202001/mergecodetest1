#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 18:20:26 2019

@author: yujzhang
"""

from lxml import etree

html = """<div class="cNav2" id="blk_cNav2_01">
    	<div class="cNavLinks" data-sudaclick="newsnav">
            <a href="http://news.sina.com.cn/roll/" style="margin-left:8px;"><span class=" ptn_19">滚动</span></a>
            <!--<a href="http://news.sina.com.cn/live/"><span class=" ptn_17">直播</span></a>-->
            <!--<a href="http://survey.news.sina.com.cn/"><span class=" ptn_160">调查</span></a>-->
            <a href="http://news.sina.com.cn/hotnews/"><span class=" ptn_18">排行</span></a>
            <a href="http://news.sina.com.cn/gov/"><span class=" ptn_08">政务</span></a>
			<a href="http://news.sina.com.cn/zt_nys/nxw0312/#282402036"><span class=" ptn_17">暖闻</span></a>
			<span class="sp_v01"></span>
            <a href="http://news.sina.com.cn/china/"><span class=" ptn_02">国内</span></a>
            <a href="http://news.sina.com.cn/world/"><span class=" ptn_03">国际</span></a>
            <!-- <a href="http://news.sina.com.cn/society/"><span class=" ptn_04">社会</span></a> -->
            <a href="http://mil.news.sina.com.cn/"><span class=" ptn_05">军事</span></a>
			<a href="http://piyao.sina.cn"><span class="ptn_04">辟谣</span></a>
            <a href="http://news.sina.cn/zt_d/sz2019"><span class=" ptn_15">知事</span></a>

          <span class="sp_v01"></span>
			<a class="ptn_50_wap" href="http://cul.news.sina.com.cn/"><span class=" ptn_50" style='margin-left: 3px;margin-top: 15px;'>文化</span></a>
			<a href="http://sifa.sina.com.cn/"><span class="">司法</span></a>
			<a href="http://tousu.sina.com.cn/" class="cNavlinks2"><span class=" ptn_51" style='margin-top: 15px;'>黑猫投诉</span></a>
            <a href="http://photo.sina.com.cn/"><span class=" ptn_16" style='margin-right: 3px;'>图片</span></a>
            <a href="http://video.sina.com.cn/news/"><span class=" ptn_14">视频</span></a>
            <!-- <a href="http://weather.sina.com.cn/"><span class="titName ptn_09">天气</span></a> -->

            <span class="sp_v01"></span>

            <a href="http://sports.sina.com.cn/"><span class=" ptn_10">体育</span></a>
            <a href="http://ent.sina.com.cn/"><span class=" ptn_11">娱乐</span></a>
            <a href="http://finance.sina.com.cn/"><span class=" ptn_12">财经</span></a>
            <a href="http://tech.sina.com.cn/"><span class=" ptn_13">科技</span></a>
            <a href="http://news.sina.com.cn/zt/"><span class=" ptn_20">专题</span></a>
        </div>

   </div>
	"""
  #构造解析对象  
parseHtml = etree.HTML(html)
#
r1 = parseHtml.xpath('//a/@href')
print(r1)
r2 = parseHtml.xpath('//a[@class="ptn_50_wap"]/@href')
print(r2)

r3 = parseHtml.xpath('//span/text()')

print(r3)

r4 = parseHtml.xpath('//span')
for i in r4:
    print(i.text)