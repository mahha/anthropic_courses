def basic_summarize(article):
  return f"この記事を要約してください {article}"

def better_summarize(article):
  return f"""
  小学生向けにこの記事を要約してください：{article}"""

def best_summarize(article):
  return f"""
  あなたの仕事は、長いWikipedia記事を小学生向けに要約することです。
  できるだけ簡潔に、短い要約を書いてください。 
  この要約は、技術的な背景のない小学生向けです。 
  これが記事です：{article}"""

