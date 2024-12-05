import emoji

def main():
    user_input = input("Input: ").strip()
    output_emoji = emoji.emojize(user_input, language = 'alias' )
    print("Output: " + output_emoji)

if __name__ == "__main__":
    main()