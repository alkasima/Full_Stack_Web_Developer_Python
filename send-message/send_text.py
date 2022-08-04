from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Your twilio accouont_sid"
# Your Auth Token from twilio.com/console
auth_token  = "Your twilio auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+2348068262120", 
    from_="+15138556153",
    body="Hello Alkasima from Python!")

print(message.sid)