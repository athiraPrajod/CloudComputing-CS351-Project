db = db.getSiblingDB("cc-project");
//db.blogs.drop();

db.blogs.insert([
    {
        "name": "John", 
        "blog_id": 1, 
        "blog_name":"test blog"
    }
]);