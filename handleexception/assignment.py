class InvalidPasswordException(Exception):
    pass
try:
    psw=input("Enter Password:")
    
    if len(psw)<8:
        raise InvalidPasswordException

except InvalidPasswordException:
    print("Password must contain at least 8 characters.")

else:
    print("You entered Password successfully")