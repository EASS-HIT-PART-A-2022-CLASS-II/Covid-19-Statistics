import pymongo

client = pymongo.MongoClient("mongodb+srv://sahar:sahar@covid19.ahht6gg.mongodb.net/Covid19")

db = client["Covid19_database"]
collection = db["Covid19_collection"]

collection.insert_many([
    {
        "country":"USA",
        "country_image":"http://www.flags.net/images/largeflags/UNST0001.GIF"
    },
    {
        "country":"Argentina",
        "country_inage":"http://www.flags.net/images/largeflags/ARGE0001.GIF"
    },
    {
        "country":"Belgium",
        "country_inage":"http://www.flags.net/images/largeflags/BELG0003.GIF"
    },
    {
        "country":"Brazil",
        "country_inage":"http://www.flags.net/images/largeflags/BRAZ0001.GIF"
    },
    {
        "country":"China",
        "country_inage":"http://www.flags.net/images/largeflags/CHIN0001.GIF"
    },
    {
        "country":"Canada",
        "country_inage":"http://www.flags.net/images/largeflags/CANA0001.GIF"
    },
    {
        "country":"Denmark",
        "country_inage":"http://www.flags.net/images/largeflags/DENM0001.GIF"
    }
])