# Python Switch statement introduced in 3.10 +

# %%
def respond(language):
    match language:
        case "Java" | "JavaScript":
            return "This matches Java."
        case "Python":
            return "This matches Python."
        case "Rust":
            return "This matches Rust."
        case "Go" | "Golang":
            return "This matches Go."
        case _:
            return "This matches default"

print(respond('Java'))
print(respond('JavaScript'))
print(respond('C++'))

# %%
# %%
