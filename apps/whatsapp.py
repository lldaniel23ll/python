import pywhatkit

try:
    phone = input('Please, insert her phone number: ')
    message = input('Please, insert her message: ')
    hour = int(input('Please, insert the hour: '))
    minutes = int(input('Please, insert the minutes: '))

    pywhatkit.sendwhatmsg('+505' + phone, message, hour, minutes, 1, True, 1)
except Exception as e:
    print(e)
