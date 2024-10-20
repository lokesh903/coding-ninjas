## Error 
An error ia an abnormal condition encountered in a code which can leads to the termination of the code and needs to be fic=xes for the succesfull execution 

## Exceptions

Exception, also called as runtime error, is a abnormal condition in the code which occrs due to a logical mistake and can be handled ,if not handel it would lead to a diffrent flow than excepted flow

## Summery -
### exceptions 
are error in Logic 
### example 
1. passing a 3 attributes in a function which only accepts 2 arguments 
2. dividing by zero 

## error
where as error are occur due to incorrect syntax like ending a function with :,instead of :

## Note :
Errors can not be handled, only exceptions can be handeled 

# Handling Execptions 

```
a = [1,2,3]
try:
    print ("second element of array:: %d" %(a[1]))

    print ("fourth element of array:: %d" %(a[3]))

except:
    print("An Error Occured")

print("executed successfully")
```

## multiple exceptions with else and finally

```
try:
    num1 = int(input("Enter a numerator: "))
    num2 = int(input("Enter a denominator: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter integers.")
except  ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Division performed successfully.")
finally:
    print("always exectue wether exceptions occur or not")

```


### raise Keyword

it is used to raise exceptions or errors , it is used to raise a an error and stops the control flow of the progrram it is used to bring up the current exceptions in an exception handler so that it can be handeled further up the call stack 

```
a=5
if a%2 == 0:
    raise Exception("The number shoudn't be an odd integer")
```

## Custom Exceptions

```
class CustomException(Exception):
    pass

def validate_input(value):
    if not isinstance(value, int):
        raise CustomException("Invalid input. Expected an
integer.")
try:
    validate_input("abc")
except CustomException as e:
    print("Error:", str(e))

```

### case 1

```
try:
    <!-- some thing -->
except (URLError, ValueError, SocketTimeout):

```

a tuple can be used if there is same action to perform different exception
