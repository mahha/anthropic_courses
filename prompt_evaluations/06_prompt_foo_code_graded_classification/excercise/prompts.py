def basic_prompt(complaint):
    return f"""
    次の顧客の苦情を、以下のカテゴリの1つ以上に分類してください： 
    Software Bug、Hardware Malfunction、User Error、Feature Request、または Service Outage。
    分類のみを回答してください。

    苦情: {complaint}

    分類:
    """


def improved_prompt(complaint):
    return f"""
    あなたは顧客サポートの問題分類を専門とするAIアシスタントです。顧客の苦情を分析し、以下のカテゴリの1つ以上に分類するのがあなたの仕事です：

    1. Software Bug: ソフトウェアが意図通りに機能しない問題。
    2. Hardware Malfunction: 物理的なデバイスやコンポーネントの問題。
    3. User Error: ユーザーの誤解や誤用による困難。
    4. Feature Request: 新機能や改善の提案。
    5. Service Outage: サービスの可用性に影響を与えるシステム全体の問題。

    重要なガイドライン：
    - 苦情は複数のカテゴリに該当する場合があります。その場合は、該当するすべてをリストアップしてください。ただし、可能な限り単一のカテゴリを優先的に選択するよう努めてください。

    例：
    1. 苦情: "アプリが進捗を保存しようとするたびにクラッシュします。"
    分類: Software Bug

    2. 苦情: "コーヒーをこぼした後、キーボードが動作しなくなりました。"
    分類: Hardware Malfunction

    3. 苦情: "ウェブサイトでログインボタンが見つかりません。"
    分類: User Error

    4. 苦情: "アプリにダークモードがあると素晴らしいです。"
    分類: Feature Request

    5. 苦情: "私や同僚にとって、あなたのサービスのどれも読み込まれません。"
    分類: Service Outage

    6. 苦情: "アプリがプロフィール写真を変更しようとするたびに壊れます"
    分類: Software Bug

    7. 苦情: "アプリが私の電話でバグだらけで、ウェブサイトもダウンしているようで、完全に行き詰まっています！"
    分類: Software Bug, Service Outage

    8. 苦情: "あなたのソフトウェアが私のコンピューターを非常に遅くし、最悪です、嫌いです！"
    分類: Software Bug

    9. 苦情: "あなたのダメなアプリは、画像で何かしようとするたびに常に壊れます。"
    分類: Software Bug

    それでは、次の顧客の苦情を分類してください：

    <complaint>{complaint}</complaint>

    適切なカテゴリのみを回答し、それ以外は何も含めないでください。
    分類:
    """
