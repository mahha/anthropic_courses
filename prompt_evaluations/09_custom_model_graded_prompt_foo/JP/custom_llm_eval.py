import anthropic
import os
import json

def llm_eval(summary, article):
    """
    Evaluate summary using an LLM (Claude).
    
    Args:
    summary (str): The summary to evaluate.
    article (str): The original text that was summarized.
    
    Returns:
    bool: True if the average score is above the threshold, False otherwise.
    """
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""以下の基準に基づいて、次の要約を評価してください：
    1. 簡潔性（1-5）- 要約は可能な限り簡潔ですか？
        - 簡潔性1：要約が不必要に長く、過度な詳細、繰り返し、または無関係な情報が含まれています。主要なポイントを効果的に要約できていません。
        - 簡潔性3：要約はほとんどの主要なポイントを捉えていますが、より焦点を絞ることができます。不必要な詳細が含まれているか、特定の概念を少し説明しすぎている可能性があります。
        - 簡潔性5：要約は主要なアイデアを簡潔で焦点を絞ったテキストに効果的に凝縮しています。すべての重要な情報を含み、余分な詳細や説明はありません。
    2. 正確性（1-5）- 元の記事に基づいて、要約は完全に正確ですか？
        - 正確性1：要約には、元の記事の意味や主要なポイントを根本的に変える重大な誤り、誤った表現、または省略が含まれています。
        - 正確性3：要約は一部の主要なポイントを正しく捉えていますが、軽微な不正確さや省略がある可能性があります。全体的なメッセージは一般的に正しいですが、一部の詳細が間違っている可能性があります。
        - 正確性5：要約は、誤りや誤解釈なく、元の記事の主要な要点を忠実に表現しています。含まれるすべての情報が正確で、元の資料と一致しています。
    4. トーン（1-5）- 要約は技術的な訓練を受けていない小学生に適切ですか？
        - トーン1：要約は、小学生の読者には複雑すぎる、技術的すぎる、または成熟しすぎた言語や概念を使用しています。専門用語、高度な専門用語、または若い読者に適さないテーマが含まれている可能性があります。
        - トーン2：要約は主に小学生に適した言語を使用していますが、時折、挑戦的な用語や概念が含まれています。完全な理解にはいくつかの説明が必要かもしれません。
        - トーン3：要約は一貫して、小学生が簡単に理解できるシンプルで明確な言語を使用しています。複雑なアイデアを、若い読者にとってアクセスしやすく魅力的な方法で説明しています。
    5. 説明 - 要約がどのように評価されるかの一般的な説明

    <examples>
    <example>
    この要約：
    <summary>
    人工ニューラルネットワークは、人間の脳の働きにインスピレーションを得たコンピューターシステムです。情報を処理する相互接続された「ニューロン」で構成されています。これらのネットワークは、人間が学習するのと同様に、多くの例を見ることでタスクを学習できます。 

    ニューラルネットワークに関する重要な点：
    - パターンを認識し、予測を行うことができる
    - より多くのデータと練習で改善する
    - 画像内のオブジェクトの識別、言語の翻訳、ゲームのプレイなどに使用される

    ニューラルネットワークは人工知能の強力なツールであり、今日私たちが使用する多くの「スマート」技術の背後にあります。驚くべきことを行うことができますが、人間の脳ほど複雑でも能力もありません。
    <summary>
    トーン5、正確性5、簡潔性5を受け取るべきです
    </example>

    <example>
    この要約：
    <summary>
    人工ニューラルネットワーク（ANN）に関する記事の主要なポイントの要約：

    1. ANNは、動物の脳内の生物学的ニューラルネットワークにインスピレーションを得た計算モデルです。信号を処理および伝送する相互接続された人工ニューロンで構成されています。

    2. 基本構造：
    - 入力層がデータを受信
    - 隠れ層が情報を処理
    - 出力層が結果を生成
    - ニューロンは重み付きエッジで接続

    3. 学習プロセス：
    - ANNは接続の重みを調整することで学習
    - バックプロパゲーションなどの技術を使用してエラーを最小化
    - 教師あり学習、教師なし学習、強化学習を実行可能

    4. 主要な発展：
    - 画像処理のための畳み込みニューラルネットワーク（CNN）
    - シーケンシャルデータのためのリカレントニューラルネットワーク（RNN）
    - 多くの隠れ層を持つ深層学習

    5. 応用：
    - パターン認識、分類、回帰
    - コンピュータビジョン、音声認識、自然言語処理
    - ゲームプレイ、ロボティクス、金融モデリング

    6. 利点：
    - 複雑な非線形関係をモデル化可能
    - データから学習し、一般化する能力
    - 多くの異なるタイプの問題に適応可能

    7. 課題：
    - 大量の訓練データが必要
    - 計算集約的になる可能性
    - 「ブラックボックス」の性質により解釈可能性が困難になる可能性

    8. 最近の進歩：
    - より深いネットワークを可能にする改良されたハードウェア（GPU）
    - 言語タスクのためのトランスフォーマーなどの新しいアーキテクチャ
    - 生成AIなどの分野での進歩

    この記事は、人工知能と機械学習のこの分野におけるANNの概念、歴史、タイプ、応用、および進行中の研究領域の包括的な概要を提供しています。
    </summary>
    トーン1、正確性5、簡潔性3を受け取るべきです
    </example>
    </examples>

    JSON形式で各基準のスコアを提供してください。常に従うべき形式は次のとおりです：

    <json>
    {{
    "conciseness": <number>,
    "accuracy": <number>,
    "tone": <number>,
    "explanation": <string>,
    }}
    </json>


    元のテキスト：<original_article>{article}</original_article>
    
    評価する要約：<summary>{summary}</summary>
    """
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": "<json>" 
            }
        ],
        stop_sequences=["</json>"]
    )
    
    evaluation = json.loads(response.content[0].text)
    # Filter out non-numeric values and calculate the average
    numeric_values = [value for key, value in evaluation.items() if isinstance(value, (int, float))]
    avg_score = sum(numeric_values) / len(numeric_values)
    # Return the average score and the overall model response
    return avg_score, response.content[0].text

def get_assert(output: str, context, threshold=4.5):
    article = context['vars']['article']
    score, evaluation = llm_eval(output, article )
    return {
        "pass": score >= threshold,
        "score": score,
        "reason": evaluation
    }
    

