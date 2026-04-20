import os

# 微信公众号列表
WECHAT_ACCOUNTS = [
    "AI闹",
    "数字生命卡兹克",
    "AIGC胶囊",
    "李继刚",
    "TRAE.ai",
    "智能涌现"
]

# 邮箱配置
SMTP_SERVER = "smtp.163.com"
SMTP_PORT = 465
SENDER_EMAIL = "18785649879@163.com"
SENDER_PASSWORD = "QMSrr33xr6jRHr9g"  # 授权码
RECEIVER_EMAIL = "18785649879@163.com"

# OpenAI 配置 (使用预设环境变量)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4.1-mini"

# 路径配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
DATA_FILE = os.path.join(BASE_DIR, "data/articles.json")
HTML_REPORT = os.path.join(BASE_DIR, "data/weekly_report.html")
