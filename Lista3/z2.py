import string
import random

# Real english dictionary - online compilers doesn't support urllib.requests module
def create_real_english_words_dictionary():
    import urllib.request
    dictionary_url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
    content = urllib.request.urlopen(dictionary_url).read()
    return frozenset(content.decode('utf-8').split('\n'))

def create_simple_dictionary():
    return frozenset(['cat', 'mouse', 'and', 'another', 'animals'])

def create_strong_password(create_dictionary):
    dictionary = create_dictionary()
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    all_ascii_chars = lowercase_letters + uppercase_letters + digits + special_characters
    
    def is_password_ok(candidate_pwd):
        def is_forbidden_word_inside():
            for i in range(0, pwd_length):
                for j in range(i + 1, pwd_length + 1):
                    substr = candidate_pwd[i:j]
                    if substr in dictionary:
                        return True
            return False
        def is_character_inside(template_seq):
            for c in candidate_pwd:
                if c in template_seq:
                    return True
            return False
            
        pwd_length = len(candidate_pwd)
        return pwd_length >=8 \
               and not is_forbidden_word_inside()         \
               and is_character_inside(lowercase_letters) \
               and is_character_inside(uppercase_letters) \
               and is_character_inside(digits)            \
               and is_character_inside(special_characters)           
    
    def generate_password():
        min_length = 8
        max_length = 64
        pwd_length = random.randint(min_length, max_length)
        password = [random.choice(all_ascii_chars) for _ in range(pwd_length)]
        return "".join(password)
    
    password = "zle_haslo"
    while not is_password_ok(password):
        password = generate_password()
    return password
    

if __name__ == "__main__":
    print(create_strong_password(create_simple_dictionary))
    # Uncomment line below to use real dictionary
    # print(create_strong_password(create_real_english_words_dictionary))
    