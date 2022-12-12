from twilio.rest import Client 
import os

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_ACCOUNT_TOKEN')
phone_number = os.environ.get('PHONE')
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hi, DevOps Hero!',      
                              to='whatsapp:+918762049044'
                          ) 
 
print(message.sid)