from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC04427fc02482be3cc19ec5edbf17c399'
auth_token = 'a8939d45c9e76e3f55abe8707cd7c3b6'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+12705128509',
         to='+917988192404'
     )

print(message)
    # (361) 470-7578
