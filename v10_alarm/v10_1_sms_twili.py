from twilio.rest import Client
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
message = client.messages.create(
  from_='+12563635226',
  body='테스트 문자',
  to='+8201050759832'
)
print(message.sid)