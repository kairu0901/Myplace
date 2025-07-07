import logging

# フォーマット定義
formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')

# ルートロガー取得
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)  # 全体でDEBUGまで出す

# コンソールハンドラ
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# 二重追加を防ぐ
if not root_logger.hasHandlers():
    root_logger.addHandler(console_handler)

# ファイル出力（必要なら）
#file_handler = logging.FileHandler('app.log', mode='a', encoding='utf-8')
#file_handler.setLevel(logging.DEBUG)
#file_handler.setFormatter(formatter)
#root_logger.addHandler(file_handler)

# ロガーの生成関数（使いやすくするため）
def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
