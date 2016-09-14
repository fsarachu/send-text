from twilio.rest import TwilioRestClient

account_sid = "ACCOUNT_SID"  # Your Account SID from www.twilio.com/console
auth_token = "AUTH_TOKEN"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Alo alo! Franco is messing up with Twilio!",
                                 to="+59812345678",  # Replace with your phone number
                                 from_="+19012345678")  # Replace with your Twilio number

print(message.sid)
