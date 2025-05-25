from twilio.rest import Client


# Set environment variables for your Account Sid and Auth Token!
# These can be found at twilio.com/console
# +, country code, phone number for phone number field
# copy paste over twilio_account_sid, and twilio_account_token when you want to use it...

TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''
client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)

phone_number = client.lookups \
                     .v2 \
                     .phone_numbers('') \
                     .fetch(fields='line_type_intelligence')

print(phone_number.line_type_intelligence) # All of the carrier info.
print(phone_number.line_type_intelligence['carrier_name']) # Just the carrier name.