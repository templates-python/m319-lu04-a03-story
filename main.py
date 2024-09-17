def main():
    # write your code below this line
    print('I will tell you a story, but I need some information first.')
    name = input('What is the main character called?\n')
    job = input('What is their job?\n')
    print('Here is the story:')
    print(f'Once upon a time there was {name}, who was a {job}.')
    print(f'On the way to work, {name} reflected on life.')
    print(f'Perhaps {name} will not be a {job} forever.')

if __name__ == '__main__':
    main()
