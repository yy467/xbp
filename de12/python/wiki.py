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
    url = f"https://history.muffinlabs.com/date/{date.month}/{date.day}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        events = data.get('data', {}).get('Events', [])
        return events
    else:
        return None

#サーバーに接続
smtp_server = "smtp-mail.outlook.com"
port = 587
server = smtplib.SMTP(smtp_server, port)
            #暗号化の設定
server.starttls()
            #サーバーにログイン
login_address = "r202401945pj@jindai.jp"
login_password = "6yYbqwMLSv"
server.login(login_address, login_password)
           
            

# メイン処理
def main():
    events = get_historical_events(ten_years_ago)
    
    if events:
        event_details = "\n".join([f"{event['year']}: {event['text']}" for event in events])
        subject = f"10年前の今日 ({ten_years_ago}) の出来事"
        body = f"10年前の{ten_years_ago}に起こった出来事:\n\n{event_details}"
    else:
        subject = f"10年前の今日 ({ten_years_ago}) の出来事"
        body = "10年前の今日の出来事は取得できませんでした。"
    
    # 送信先メールアドレスを指定
               #メールの送信
    to_mail="r202401945pj@jindai.jp"
    server.send_message(subject,body,to_mail)
            #サーバーの切断
    server.quit()

if __name__ == "__main__":
    main()
