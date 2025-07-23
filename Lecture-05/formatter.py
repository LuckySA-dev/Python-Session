def format_strings(*str1:str) -> str:
    return "".join(str1).upper()

def main():
    
    result = format_strings("Hello", "world", "this", "is", "a", "test")
    print(result)
    
    result = format_strings("Python", "is", "fun")
    print(result)
    
    result = format_strings("Concatenate", "these", "strings", "please")
    print(result)
    
if __name__ == "__main__":
    main()