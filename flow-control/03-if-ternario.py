age = 15

message = (
    "You are an adult"
    if age > 17
    else "You are a teenager" if age > 12 else "You are a minor"
)

print(message)  # You are a teenager
