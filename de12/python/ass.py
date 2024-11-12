import smtplib
import datetime
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 10年前の日付を計算
today = datetime.date.today()
ten_years_ago = today.replace(year=today.year - 10)

# 10年前の出来事を取得するためのAPI (例: 'history.muffinlabs.com' など)
def get_historical_events(date):
    # 'history.muffinlabs.com' API を使用して、10年前のその日の出来事を取得
    url = f"https://history.muffinlabs.com/date/{date.month}/{date.day}"
    response = requests.get(url)
    
    # APIからのレスポンスが成功した場合
    if response.status_code == 200:
        data = response.json()
        events = data.get('data', {}).get('Events', [])
        return events
    else:
        # APIからデータを取得できなかった場合はNoneを返す
        return None

# メール送信関数
def send_email(subject, body, to_email):
    # メールの送信元アドレスとパスワード
    from_email = "r202401945pj@jindai.jp"
    login_password = "6yYbqwMLSv"  # セキュリティのため、環境変数などで管理することを推奨します。

    # メールのヘッダーと本文を作成
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))  # 本文を追加

    # サーバーに接続してメールを送信
    smtp_server = "smtp-mail.outlook.com"
    port = 587
    try:
        # サーバーに接続
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # TLS暗号化を開始
        server.login(from_email, login_password)  # ログイン

        # メール送信
        server.sendmail(from_email, to_email, msg.as_string())
        print("メールが送信されました。")
    except Exception as e:
        print(f"メール送信エラー: {e}")
    finally:
        server.quit()  # サーバーを切断

# メイン処理
def main():
    # 10年前の出来事を取得
    events = get_historical_events(ten_years_ago)
    
    if events:
        # 出来事が取得できた場合、メール本文を作成
        event_details = "\n".join([f"{event['year']}: {event['text']}" for event in events])
        subject = f"10年前の今日 ({ten_years_ago}) の出来事"
        body = f"10年前の{ten_years_ago}に起こった出来事:\n\n{event_details}"
    else:
        # 出来事が取得できなかった場合
        subject = f"10年前の今日 ({ten_years_ago}) の出来事"
        body = "10年前の今日の出来事は取得できませんでした。"
    
    # 送信先メールアドレスを指定
    to_email = "r202401945pj@jindai.jp"  # ここで送信先を設定
    
    # メールを送信
    send_email(subject, body, to_email)

# メイン処理を実行
if __name__ == "__main__":
    main()
