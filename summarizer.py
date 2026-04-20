import openai
import config

class ArticleSummarizer:
    def __init__(self):
        self.client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
        self.model = config.OPENAI_MODEL

    def summarize_article(self, title, content):
        try:
            prompt = f"请总结以下文章，提取主要观点和关键信息，并以中文输出。\n\n标题：{title}\n\n内容：{content}\n\n总结："
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是一个专业的文章总结助手。"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500
            )
            summary = response.choices[0].message.content.strip()
            return summary
        except Exception as e:
            print(f"AI 总结文章失败: {e}")
            return "AI 总结失败，请检查 OpenAI API 配置或重试。"

if __name__ == "__main__":
    summarizer = ArticleSummarizer()
    test_title = "人工智能的未来发展趋势"
    test_content = "近年来，人工智能技术取得了飞速发展，尤其是在深度学习、自然语言处理和计算机视觉等领域。未来，人工智能将更加深入地融入我们的日常生活，例如智能家居、自动驾驶、医疗诊断等。同时，人工智能的伦理问题和就业影响也日益受到关注。"
    summary = summarizer.summarize_article(test_title, test_content)
    print("测试文章总结：")
    print(summary)
