dogs = [
    {
        "name" : "Melba",
        "handle" : "melba",
        "bio" : "Hi, I'm Melba! I'm a mini-goldendoodle and I love to play.",
        "age" : 3
    },
    {
        "name" : "Charlie",
        "handle" : "chucky",
        "bio" : "Hi I'm Charlie! I'm a big white standard poodle.",
        "age" : 7
    },
    {
        "name" : "Rosie",
        "handle" : "rose",
        "bio" : "Hi I'm Rosie! I'm from the hard streets of LA, don't mess with me.",
        "age" : 9
    }
]

# def get_dog_by_handle(handle):
#     for dog in dogs:
#         if dog['handle'] == handle:
#             return dog
#     return None

# posts = [
#     {
#         "text" : "I'm so excited to move to California!",
#         "handle" : "melba",
#         "likes" : ["rose", "chucky"],
#         "id" : "1"
#     },
#     {
#         "text" : "Hung out with @melba!",
#         "handle" : "rose",
#         "likes" : ["melba","chucky"],
#         "id" : "6"
#     },
#     {
#         "text" : "Great game of fetch today with my Dad, Paul",
#         "handle" : "melba",
#         "likes" : ["rose"],
#         "id" : "2"
#     },
    
#     {
#         "text" : "Took a great 8 hour nap today, then guarded the household",
#         "handle" : "chucky",
#         "likes" : ["rose"],
#         "id" : "3"
#     },
#     {
#         "text" : "Peanut butter is my favorite snack!",
#         "handle" : "melba",
#         "likes" : ["chucky"],
#         "id" : "4"
#     },
#     {
#         "text" : "Today I stole food from a blind dog.",
#         "handle" : "rose",
#         "likes" : ["melba","chucky"],
#         "id" : "5"
#     }
   
# ]

def add_post_url():
    results = []
    for post in posts:
        for dog in dogs:
            sub = "@" + dog['Handle']
            print(sub)
            if sub in post['Text']:
                link = '<a href="/dog/' +dog['Handle'] + '">' + sub + '</a>'
                post['Text'] = post['Text'].replace(sub, link)     
        results.append(post)
    return results

# def get_posts_by_handle(handle):
#     results = []
#     url_posts = add_post_url()
#     for post in url_posts:
#         if post['handle'] == handle:
#             results.append(post)
#     return results

def get_post_by_id(id):
    for post in posts:
        if post['id'] == id:
            return post
    return None