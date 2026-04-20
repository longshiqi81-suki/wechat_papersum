import asyncio
import json
import os
import datetime
from scraper import WechatScraper
from summarizer import ArticleSummarizer
from mailer import WeeklyMailer
import config

class WechatDigestSystem:
    def __init__(self):
        self.scraper = WechatScraper()
        self.summarizer = ArticleSummarizer()
        self.mailer = WeeklyMailer()
        self.articles = []

    async def run(self):
        print(f"[{datetime.datetime.now()}] 微信公众号周报系统启动...")

        # 1. 抓取文章
        print("步骤 1: 正在抓取公众号文章...")
        self.articles = await self.scraper.get_articles()

        # 2. AI 总结
        print(f"步骤 2: 正在对 {len(self.articles)} 篇文章进行 AI 总结...")
        for article in self.articles:
            print(f"  正在总结: {article['title']}")
            article['summary'] = self.summarizer.summarize_article(article['title'], article['content'])

        # 3. 更新网页数据文件 (JSON)
        print("步骤 3: 正在更新网页数据文件...")
        self.save_data()

        # 4. 生成 HTML 周报
        print("步骤 4: 正在生成 HTML 周报内容...")
        html_report = self.generate_html_report()

        # 5. 发送邮件
        print("步骤 5: 正在发送周报邮件...")
        self.mailer.send_weekly_report(html_report)

        print(f"[{datetime.datetime.now()}] 微信公众号周报系统运行完成！")

    def save_data(self):
        os.makedirs(os.path.dirname(config.DATA_FILE), exist_ok=True)
        with open(config.DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.articles, f, ensure_ascii=False, indent=4)

    def generate_html_report(self):
        today = datetime.date.today().strftime("%Y-%m-%d")
        html = f"""
        <html>
        <head>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 800px; margin: 0 auto; padding: 20px; }}
                .header {{ background-color: #f4f4f4; padding: 10px 20px; border-radius: 5px; margin-bottom: 20px; }}
                .article {{ border-bottom: 1px solid #eee; padding: 15px 0; }}
                .article-title {{ font-size: 1.2em; font-weight: bold; color: #2c3e50; margin-bottom: 5px; }}
                .article-meta {{ font-size: 0.9em; color: #7f8c8d; margin-bottom: 10px; }}
                .article-summary {{ background-color: #fdfefe; border-left: 4px solid #3498db; padding: 10px 15px; font-style: italic; }}
                .footer {{ font-size: 0.8em; color: #95a5a6; margin-top: 30px; text-align: center; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>微信公众号 AI 周报</h1>
                    <p>日期：{today} | 覆盖公众号：{', '.join(config.WECHAT_ACCOUNTS)}</p>
                </div>
        """
        
        for article in self.articles:
            html += f"""
                <div class="article">
                    <div class="article-title">{article['title']}</div>
                    <div class="article-meta">公众号: {article['account']} | 日期: {article['date']} | <a href="{article['url']}">查看原文</a></div>
                    <div class="article-summary">
                        <strong>AI 总结：</strong><br>
                        {article['summary']}
                    </div>
                </div>
            """
            
        html += """
                <div class="footer">
                    <p>本周报由 Manus AI 自动生成。如需修改订阅，请联系管理员。</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # 保存 HTML 文件供网页展示
        with open(config.HTML_REPORT, 'w', encoding='utf-8') as f:
            f.write(html)
            
        return html

if __name__ == "__main__":
    system = WechatDigestSystem()
    asyncio.run(system.run())
