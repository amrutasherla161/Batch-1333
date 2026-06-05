movie_db = {
    "Arjun Reddy": {
        "Hero": "Vijay Deverakonda",
        "Cast": "Shalini Pandey"
    },
    "Jersey": {
        "Hero": "Nani",
        "Cast": "Shraddha Srinath"
    },
    "Mission Mangal": {
        "Hero": "Akshay Kumar",
        "Cast": "Vidya Balan"
    },
    "12th Fail": {
        "Hero": "Vikrant Massey",
        "Cast": "Medha Shankar"
    },
    "The Pursuit of Happyness": {
        "Hero": "Will Smith",
        "Cast": "Jaden Smith"
    }
}

for movie, details in movie_db.items():
    print("Movie Name :", movie)
    print("Hero       :", details["Hero"])
    print("Cast       :", details["Cast"])
    print()
