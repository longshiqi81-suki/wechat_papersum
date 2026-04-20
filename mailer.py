import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

class WeeklyMailer:
    def __init__(self):
        self.smtp_server = config.SMTP_SERVER
        self.smtp_port = config.SMTP_PORT
        self.sender_email = config.SENDER_EMAIL
        self.sender_password = config.SENDER_PASSWORD
        self.receiver_email = config.RECEIVER_EMAIL

    def send_weekly_report(self, html_content):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.receiver_email
        msg['Subject'] = "微信公众号 AI 周报总结"

        msg.attach(MIMEText(html_content, 'html'))

        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            print(f"周报已成功发送至 {self.receiver_email}")
            return True
        except Exception as e:
            print(f"邮件发送失败: {e}")
            return False

if __name__ == "__main__":
    mailer = WeeklyMailer()
    test_html = "<h1>这是一封测试邮件</h1><p>微信公众号 AI 周报系统测试。</p>"
    mailer.send_weekly_report(test_html)
